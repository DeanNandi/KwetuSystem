from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('donors-form', views.my_form, name='donors-form'),
    path('login', views.loginPage, name="login"),
    path('register', views.registerPage, name="register"),
    path('logout', views.logoutUser, name="logout"),
    path('edit-donors/(?P<pk>\d+)', views.edit_donors, name='edit-donors/(?P<pk>\d+)'),
    path('delete-donors/(?P<pk>\d+)', views.delete_donors, name='delete-donors/(?P<pk>\d+)'),
]
