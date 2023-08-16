from django.urls import path
from apps.usuarios.views import logout,login,cadastro


urlpatterns=[
    path('login',login,name='login'),
    path('cadastro',cadastro,name='cadastro'),
    path('logout',logout,name='logout')
]