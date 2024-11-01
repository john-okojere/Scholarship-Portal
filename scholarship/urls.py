from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply, name='appley'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path("scholarship/form1/<int:stage>/", views.scholarship_application1, name="apply1"),
    path("scholarship/form2/<int:stage>/", views.scholarship_application2, name="apply2"),
    path("scholarship/form3/<int:stage>/", views.scholarship_application3, name="apply3"),
    path("scholarship/form4/<int:stage>/", views.scholarship_application4, name="apply4"),
    path("scholarship/form5/<int:stage>/", views.scholarship_application5, name="apply5"),
]
