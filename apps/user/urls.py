
from django.urls import path
from .views import init_hs_oauth,handle_callback, owners

urlpatterns = [    
    path('init_hs_oauth/', init_hs_oauth, name='init_hs_oauth'),
    path('callback/', handle_callback, name='callback'),
    path('owners/', owners, name='owners'),
]
