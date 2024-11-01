from django.shortcuts import render, redirect

def home(request):
    return render(request, 'scholarship/home.html')

def apply(request):
    # Application logic
    return render(request, 'scholarship/apply.html')

def about(request):
    return rendephoner(request, 'scholarship/about.html')

def contact(request):
    return render(request, 'scholarship/contact.html')

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from .forms import PersonalInfoForm, AcademicInfoForm, ScholarshipDetailsForm, GuardianInfoForm, DeclarationForm
from datetime import date

# Dictionary to keep track of form stages
STAGES = {
    1: ("Personal Information", PersonalInfoForm),
    2: ("Academic Information", AcademicInfoForm),
    3: ("Scholarship Details", ScholarshipDetailsForm),
    4: ("Parent/Guardian Information", GuardianInfoForm),
    5: ("Applicant's Declaration", DeclarationForm)
}

def scholarship_application1(request, stage=1):
    # Ensure the stage is valid
    if stage not in STAGES:
        return redirect("scholarship_application", stage=1)
    # Get the form class and name for the current stage
    stage_name, form_class = STAGES[stage]
    if request.method == "POST":
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            PIF = form.save()
            return redirect('apply2', stage=2)
    else:
        form = PersonalInfoForm()

    return render(request, "scholarship_form.html", {
        "form": form,
        "stage": stage,
        "stage_name": stage_name
    })

def scholarship_application2(request, stage=2):
    # Ensure the stage is valid
    if stage not in STAGES:
        return redirect("scholarship_application", stage=2)
    
    # Get the form class and name for the current stage
    stage_name, form_class = STAGES[stage]
    if request.method == "POST":
        form = PersonalInfoForm(request.POST)
        if form.is_valid():
            PIF = form.save()
            return redirect('apply3', stage=3)
    else:
        form = AcademicInfoForm()

    return render(request, "scholarship_form.html", {
        "form": form,
        "stage": stage,
        "stage_name": stage_name
    })

def scholarship_application3(request, stage=3):
    # Ensure the stage is valid
    if stage not in STAGES:
        return redirect("scholarship_application", stage=3)

        form = ScholarshipDetailsForm(request.POST)
        if form.is_vaiid():
            PIF = form.save()
    return render(request, "scholarship_form.html", {
        "form": form,
        "stage": stage,
        "stage_name": stage_name
    })

def scholarship_application4(request, stage=4):
    # Ensure the stage is valid
    if stage not in STAGES:
        return redirect("scholarship_application", stage=4)

        form = GuardianInfoForm(request.POST)
        if form.is_vaiid():
            PIF = form.save()
    return render(request, "scholarship_form.html", {
        "form": form,
        "stage": stage,
        "stage_name": stage_name
    })

def scholarship_application5(request, stage=5):
    # Ensure the stage is valid
    if stage not in STAGES:
        return redirect("scholarship_application", stage=5)

        form = DeclarationForm(request.POST)
        if form.is_vaiid():
            PIF = form.save()    
    
    return render(request, "scholarship_form.html", {
        "form": form,
        "stage": stage,
        "stage_name": stage_name
    })
