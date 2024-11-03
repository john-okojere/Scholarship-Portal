from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import PersonalInfoForm, AcademicInfoForm, ScholarshipDetailsForm, GuardianInfoForm, DeclarationForm
from .models import PersonalInfo

# Dictionary to keep track of form stages
STAGES = {
    1: ("Personal Information", PersonalInfoForm),
    2: ("Academic Information", AcademicInfoForm),
    3: ("Scholarship Details", ScholarshipDetailsForm),
    4: ("Parent/Guardian Information", GuardianInfoForm),
    5: ("Applicant's Declaration", DeclarationForm)
}

def home(request):
    return render(request, 'scholarship/home.html')

def apply(request):
    return render(request, 'scholarship/apply.html')

def about(request):
    return render(request, 'scholarship/about.html')

def contact(request):
    return render(request, 'scholarship/contact.html')

def donate(request):
    return render(request, 'scholarship/donate.html')


# Scholarship Application Views for each Stage
def scholarship_application1(request, stage=1):
    # Ensure the stage is valid
    if stage not in STAGES:
        return redirect("apply", stage=1)
    stage_name, form_class = STAGES[stage]
    
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            personal_info = form.save()
            return redirect('apply2', stage=2, p_id=personal_info.id)
    else:
        form = form_class()

    return render(request, "scholarship_form.html", {
        "form": form,
        "stage": stage,
        "stage_name": stage_name
    })

def scholarship_application2(request, stage=2, p_id=None):
    personal_detail = PersonalInfo.objects.get(pk=p_id)
    if stage not in STAGES:
        return redirect("apply", stage=2, p_id=personal_detail.id)
    stage_name, form_class = STAGES[stage]

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            application_info = form.save(commit=False)
            application_info.personal_info = personal_detail
            application_info.save()
            return redirect('apply3', stage=3, p_id=personal_detail.id)
    else:
        form = form_class()

    return render(request, "scholarship_form.html", {
        "form": form,
        "stage": stage,
        "stage_name": stage_name
    })

def scholarship_application3(request, stage=3, p_id=None):
    personal_detail = PersonalInfo.objects.get(pk=p_id)
    if stage not in STAGES:
        return redirect("apply", stage=3, p_id=personal_detail.id)
    stage_name, form_class = STAGES[stage]

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            academic_info = form.save(commit=False)
            academic_info.personal_info = personal_detail
            academic_info.save()
            return redirect('apply4', stage=4, p_id=personal_detail.id)
    else:
        form = form_class()

    return render(request, "scholarship_form.html", {
        "form": form,
        "stage": stage,
        "stage_name": stage_name
    })

def scholarship_application4(request, stage=4, p_id=None):
    personal_detail = PersonalInfo.objects.get(pk=p_id)
    if stage not in STAGES:
        return redirect("apply", stage=4, p_id=personal_detail.id)
    stage_name, form_class = STAGES[stage]

    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            guardian_info = form.save(commit=False)
            guardian_info.personal_info = personal_detail
            guardian_info.save()
            return redirect('apply5', stage=5, p_id=personal_detail.id)
    else:
        form = form_class()

    return render(request, "scholarship_form.html", {
        "form": form,
        "stage": stage,
        "stage_name": stage_name
    })


from django.urls import reverse

def scholarship_application5(request, stage=5, p_id=None):
    personal_detail = PersonalInfo.objects.get(pk=p_id)
    if stage not in STAGES:
        return redirect("apply", stage=5, p_id=personal_detail.id)
    stage_name, form_class = STAGES[stage]

    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            declaration = form.save(commit=False)
            declaration.personal_info = personal_detail
            declaration.save()
            return redirect(reverse('application_success', args=[personal_detail.id]))
    else:
        form = form_class()

    return render(request, "scholarship_form.html", {
        "form": form,
        "stage": stage,
        "stage_name": stage_name
    })


from django.shortcuts import render, get_object_or_404
from .models import PersonalInfo, AcademicInfo, ScholarshipDetails, GuardianInfo, Declaration

def application_success(request, applicant_id):
    # Retrieve all information associated with the applicant's ID
    personal_info = get_object_or_404(PersonalInfo, pk=applicant_id)
    academic_info = get_object_or_404(AcademicInfo, personal_info=personal_info)
    scholarship_details = get_object_or_404(ScholarshipDetails, personal_info=personal_info)
    guardian_info = get_object_or_404(GuardianInfo, personal_info=personal_info)
    declaration = get_object_or_404(Declaration, personal_info=personal_info)

    # Pass the data to the template
    return render(request, "scholarship_success.html", {
        "personal_info": personal_info,
        "academic_info": academic_info,
        "scholarship_details": scholarship_details,
        "guardian_info": guardian_info,
        "declaration": declaration
    })


from django.views.generic.edit import UpdateView
from .models import PersonalInfo, AcademicInfo, ScholarshipDetails, GuardianInfo, Declaration

class EditPersonalInfoView(UpdateView):
    model = PersonalInfo
    fields = '__all__'
    template_name = 'edit_form.html'

    def get_success_url(self):
        applicant_id = self.object.pk  # Primary key of PersonalInfo
        return reverse('application_success', kwargs={'applicant_id': applicant_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        return context

class EditAcademicInfoView(UpdateView):
    model = AcademicInfo
    fields = '__all__'
    template_name = 'edit_form.html'
    
    def get_success_url(self):
        applicant_id = self.object.personal_info.pk  # Primary key of related PersonalInfo
        return reverse('application_success', kwargs={'applicant_id': applicant_id})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        return context

class EditScholarshipDetailsView(UpdateView):
    model = ScholarshipDetails
    fields = '__all__'
    template_name = 'edit_form.html'

    def get_success_url(self):
        applicant_id = self.object.personal_info.pk  # Primary key of related PersonalInfo
        return reverse('application_success', kwargs={'applicant_id': applicant_id})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        return context

class EditGuardianInfoView(UpdateView):
    model = GuardianInfo
    fields = '__all__'
    template_name = 'edit_form.html'

    def get_success_url(self):
        applicant_id = self.object.personal_info.pk  # Primary key of related PersonalInfo
        return reverse('application_success', kwargs={'applicant_id': applicant_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        return context

class EditDeclarationView(UpdateView):
    model = Declaration
    fields = '__all__'
    template_name = 'edit_form.html'

    def get_success_url(self):
        applicant_id = self.object.personal_info.pk  # Primary key of related PersonalInfo
        return reverse('application_success', kwargs={'applicant_id': applicant_id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        return context


from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils import timezone
from django.conf import settings

def complete_registration(request, applicant_id):
    applicant = get_object_or_404(PersonalInfo, id=applicant_id)

    if request.method == "POST":
        # Prepare context
        context = {
            'applicant_name': f"{applicant.first_name} {applicant.last_name}",
            'guardian_name': applicant.guardianinfo.guardian_name,
            'current_year': timezone.now().year
        }

        # Applicant email
        applicant_subject = "Application Submitted - LOT Scholarship"
        applicant_message = render_to_string('email/applicant_email.html', context)
        applicant_email = EmailMessage(
            applicant_subject,
            applicant_message,
            settings.DEFAULT_FROM_EMAIL,
            [applicant.email]
        )
        applicant_email.content_subtype = "html"  # Set email to HTML
        applicant_email.send()

        # Guardian email
        guardian_subject = "Scholarship Application Notification for Your Child"
        guardian_message = render_to_string('email/guardian_email.html', context)
        guardian_email = EmailMessage(
            guardian_subject,
            guardian_message,
            settings.DEFAULT_FROM_EMAIL,
            [applicant.guardianinfo.guardian_email]
        )
        guardian_email.content_subtype = "html"
        guardian_email.send()

        # Internal email to us
        internal_subject = "New Scholarship Applicant Submission"
        internal_message = render_to_string('email/internal_email.html', context)
        internal_email = EmailMessage(
            internal_subject,
            internal_message,
            settings.DEFAULT_FROM_EMAIL,
            ['your_email@example.com']  # Replace with your email
        )
        internal_email.content_subtype = "html"
        internal_email.send()

        return redirect(reverse('application_success', args=[applicant_id]))

     # Retrieve all information associated with the applicant's ID
    
    personal_info = get_object_or_404(PersonalInfo, pk=applicant_id)
    academic_info = get_object_or_404(AcademicInfo, personal_info=personal_info)
    scholarship_details = get_object_or_404(ScholarshipDetails, personal_info=personal_info)
    guardian_info = get_object_or_404(GuardianInfo, personal_info=personal_info)
    declaration = get_object_or_404(Declaration, personal_info=personal_info)

    # Pass the data to the template
    return render(request, "scholarship_success.html", {
        "personal_info": personal_info,
        "academic_info": academic_info,
        "scholarship_details": scholarship_details,
        "guardian_info": guardian_info,
        "declaration": declaration
    })