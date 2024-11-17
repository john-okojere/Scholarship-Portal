from django.urls import path
from . import views
from .views import applicants

urlpatterns = [
    # Regular URLs
    path('', views.home, name='home'),
    path('apply/', views.apply, name='appley'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
    path("scholarship/form1/<int:stage>/", views.scholarship_application1, name="apply1"),
    path("scholarship/form2/<int:stage>/<int:p_id>/", views.scholarship_application2, name="apply2"),
    path("scholarship/form3/<int:stage>/<int:p_id>/", views.scholarship_application3, name="apply3"),
    path("scholarship/form4/<int:stage>/<int:p_id>/", views.scholarship_application4, name="apply4"),
    path("scholarship/form5/<int:stage>/<int:p_id>/", views.scholarship_application5, name="apply5"),
    path('apply/success/<int:applicant_id>/', views.application_success, name='application_success'),
    path('edit/personal-info/<int:pk>/', views.EditPersonalInfoView.as_view(), name='edit_personal_info'),
    path('edit/academic-info/<int:pk>/', views.EditAcademicInfoView.as_view(), name='edit_academic_info'),
    path('edit/scholarship-details/<int:pk>/', views.EditScholarshipDetailsView.as_view(), name='edit_scholarship_details'),
    path('edit/guardian-info/<int:pk>/', views.EditGuardianInfoView.as_view(), name='edit_guardian_info'),
    path('edit/declaration/<int:pk>/', views.EditDeclarationView.as_view(), name='edit_declaration'),
    path('apply/complete/<int:applicant_id>/', views.complete_registration, name='complete_registration'),

    # URL for applicants list
    path('applicants/', views.applicants, name="applicants"),
]
