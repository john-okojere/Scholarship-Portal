from django import forms
from .models import *
# Step 1: Personal Information Form
class PersonalInfoForm(forms.ModelForm):
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.TextInput(attrs={"type": "date"}))
    gender = forms.ChoiceField(label="Gender", choices=[("male", "Male"), ("female", "Female")])
    nationality = forms.CharField(label="Nationality", max_length=50, required=True)
    state = forms.CharField(label="State", max_length=50, required=True)
    address = forms.CharField(label="Address", widget=forms.Textarea(attrs={"rows": 2}), required=True)
    phone_number = forms.CharField(label="Phone Number", max_length=15, required=True)
    email = forms.EmailField(label="Email", required=True)
    class Meta:
        model = PersonalInfo
        fields = [
        'first_name','last_name','date_of_birth','gender','nationality','state','address','phone_number','email',
        ]


# Step 2: Academic Information Form
class AcademicInfoForm(forms.ModelForm):
    institution_name = forms.CharField(label="Current School/Institution", max_length=100, required=True)
    current_year = forms.CharField(label="Grade/Year of Study", max_length=50, required=True)
    course_of_study = forms.CharField(label="Intended Field of Study", max_length=100, required=False)
    class Meta:
        model = AcademicInfo
        fields = ['institution_name','course_of_study','current_year','cgpa','Matric_Number','tution_fee']

# Step 3: Scholarship Details Form
class ScholarshipDetailsForm(forms.ModelForm):
    scholarship_type = forms.ChoiceField(label="Scholarship Type", choices=[("merit", "Merit-based"), ("need", "Need-based")], required=True)
    application_reason = forms.CharField(label="Reason for Application", widget=forms.Textarea(attrs={"rows": 4}), required=True)
    class Meta:
        model = ScholarshipDetails
        fields = ['scholarship_type','application_reason']

# Step 4: Parent/Guardian Information Form
class GuardianInfoForm(forms.ModelForm):

    guardian_name = forms.CharField(label="Parent/Guardian Full Name", max_length=100, required=True)
    relationship = forms.CharField(label="Relationship to Applicant", max_length=50, required=True)
    guardian_phone = forms.CharField(label="Guardian Phone Number", max_length=15, required=True)
    guardian_email = forms.EmailField(label="Guardian Email", required=True)
    guardian_address = forms.CharField(label="Guardian Address", widget=forms.Textarea(attrs={"rows": 2}), required=False)

    class Meta:
        model = GuardianInfo
        fields = [
            'guardian_name','relationship','guardian_phone','guardian_email','guardian_address',
        ]

# Step 5: Declaration Form (Final Stage)
class DeclarationForm(forms.ModelForm):
    consent_statement = forms.BooleanField(
        label="I, [Parent/Guardian Name], hereby give my consent for [Applicant's Name] to apply for and, if selected, participate in this scholarship program.",
        required=True
    )
    applicant_declaration = forms.BooleanField(
        label="I, [Applicant's Name], certify that the information provided in this application is true and accurate to the best of my knowledge.",
        required=True
    )
    applicant_signature = forms.CharField(label="Applicant’s Signature", max_length=100, required=True)
    
    # Optional: Attachments
    identification_document = forms.FileField(label="Identification Document (Photo of NIN)", required=True)
    passport_photo = forms.FileField(label="Passport Photograph", required=True)

    class Meta:
        model = Declaration
        fields = [
        'consent_statement','applicant_declaration','applicant_signature','identification_document','passport_photo',
        ]