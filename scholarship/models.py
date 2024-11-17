from django.db import models

gender = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

# Model for storing personal information
class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.last_name}"

# Model for storing academic information
class AcademicInfo(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=200)
    course_of_study = models.CharField(max_length=200)
    Matric_Number = models.CharField(max_length=200)
    current_year = models.CharField(max_length=20)  # Example: "Second Year", "Final Year"
    cgpa = models.CharField(max_length=20)  # Cumulative Grade Point Average
    tution_fee = models.IntegerField()

    def __str__(self):
        return f"{self.personal_info.first_name}'s Academic Info"

# Model for storing scholarship details
class ScholarshipDetails(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    scholarship_type = models.CharField(max_length=100)  # Example: "Merit-Based", "Need-Based"
    reason_for_applying = models.TextField()

    def __str__(self):
        return f"{self.personal_info.first_name}'s Scholarship Details"

# Model for storing parent/guardian information
class GuardianInfo(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    guardian_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)  # Example: "Mother", "Uncle"
    guardian_phone = models.CharField(max_length=15)
    guardian_email = models.EmailField()
    guardian_address = models.TextField()

    def __str__(self):
        return f"{self.personal_info.first_name}'s Guardian Info"

# Model for storing applicant's declaration
class Declaration(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    consent_statement = models.BooleanField()  # Text of the declaration that applicant agrees to
    applicant_declaration = models.BooleanField()  # Text of the declaration that applicant agrees to
    applicant_signature = models.CharField(max_length=100)  # Applicant's full name as signature
    date_of_application = models.DateField(auto_now_add=True)

    identification_document = models.FileField( upload_to = "identification_document/")
    passport_photo = models.ImageField( upload_to = "passport_photo/")

    def __str__(self):
        return f"{self.personal_info.first_name}'s Declaration"
