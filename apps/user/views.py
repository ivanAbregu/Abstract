import os
from django.shortcuts import redirect, render
import requests
import urllib.parse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import User, Hubspot
from .hubspotClient import HubspotClient

frontend_url = os.environ.get("REACT_APP_API_BASE_URL")

@api_view(['GET'])
@permission_classes([AllowAny])
def init_hs_oauth(request):
    hs = HubspotClient()
    return redirect(hs.get_authorization_url())

@api_view(['GET'])
@permission_classes([AllowAny])
def handle_callback(request):
    if request.method == 'GET':
        code = urllib.parse.unquote(request.query_params['code'])
        hs = HubspotClient()
        tokens = hs.get_tokens(code)
        access_token = tokens.get('access_token')
        email = hs.get_email(access_token)
        user,_ = User.objects.get_or_create(email=email)
        Hubspot.objects.update_or_create(user=user,defaults=tokens)
        token,_ = Token.objects.get_or_create(user=user)
        response = redirect(frontend_url)
        response.set_cookie('dj_token', token.key)
        return response

@api_view(['GET'])
def owners(request):
    access_token = request.user.hubspot.access_token
    hs = HubspotClient()
    owners = hs.get_owners(access_token)
    return Response(owners)