from django.urls import path, include
from login.views import *


urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'), #metodo por LogoutView
    path('logout/', LogoutRedirectView.as_view(), name='logout'), #metodo RedirectView

]