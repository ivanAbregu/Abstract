import os
import requests

class HubspotClient(object):
    def __init__(self):
        self.client_id = os.environ.get("CLIENT_ID")
        self.client_secret = os.environ.get("CLIENT_SECRET")
        self.redirect_uri = os.environ.get("REDIRECT_URI")
        self.scope = os.environ.get("SCOPE")

    def get_authorization_url(self):
        url = "https://app.hubspot.com/oauth/authorize"
        return f"{url}?client_id={self.client_id}&redirect_uri={self.redirect_uri}&scope={self.scope}"
    
    def get_tokens(self, code):
        url = "https://api.hubapi.com/oauth/v1/token"
        data = {
            'code': code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code'
        }

        response = requests.post(url,data=data)
        return response.json()
    
    def get_email(self, access_token):
        url = f"https://api.hubapi.com/oauth/v1/access-tokens/{access_token}"
        response = requests.get(url)
        data = response.json()
        return data.get('user')
    
    def get_owners(self, access_token):
        url = "https://api.hubapi.com/crm/v3/owners/?limit=100&archived=false"
        headers = {
            "Authorization": f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        response = requests.get(url,headers=headers)
        return response.json()