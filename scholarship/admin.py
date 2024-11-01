from django.contrib import admin
from .models import PersonalInfo, AcademicInfo, ScholarshipDetails, GuardianInfo, Declaration

# Register PersonalInfo model with appropriate fields
@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'email')  # Ensure these fields exist in PersonalInfo

# Register AcademicInfo model with appropriate fields
@admin.register(AcademicInfo)
class AcademicInfoAdmin(admin.ModelAdmin):
    list_display = ('personal_info', 'institution_name', 'course_of_study', 'current_year', 'cgpa')  # Adjusted field names

# Register ScholarshipDetails model with appropriate fields
@admin.register(ScholarshipDetails)
class ScholarshipDetailsAdmin(admin.ModelAdmin):
    list_display = ('personal_info', 'scholarship_type')  # Adjusted field names

# Register GuardianInfo model with appropriate fields
@admin.register(GuardianInfo)
class GuardianInfoAdmin(admin.ModelAdmin):
    list_display = ('personal_info', 'guardian_name', 'relationship', 'guardian_phone', 'guardian_email')  # Adjusted field names

# Register Declaration model with appropriate fields
@admin.register(Declaration)
class DeclarationAdmin(admin.ModelAdmin):
    list_display = ('personal_info', 'consent_statement', 'applicant_declaration', 'date_of_application')  # Adjusted field names
