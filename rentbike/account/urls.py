from django.urls import path
from.views import signuppage
urlpatterns = [
    path('signup/',signuppage.as_view(),name='signup')
    
]
