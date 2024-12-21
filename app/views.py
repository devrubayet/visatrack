from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Information
from .models import CheckStatus
from .models import Slider
from .models import VisaList
from .models import PackageList
from .forms import ReferenceForm
# Create your views here.
def index(request):
    info = Information.objects.all()[Information.objects.count() - 1]
    visa_list = VisaList.objects.all()
    package_list = PackageList.objects.all()



    images = Slider.objects.filter(is_active=True).order_by('-created_at')
    context={
        'info':info,
        'images':images,
        'visa_list':visa_list,
        'package_list':package_list
        # 'error_message':error_message
    }
    return render(request, 'index.html',  context)





@csrf_exempt  # You can keep csrf_exempt or use csrf token as shown in JavaScript
def track_application(request):
    if request.method == "POST":
        data = json.loads(request.body)  # Get the incoming data
        reference_number = data.get('reference_number')
        details = None
        error_message = None
        
        if reference_number:
            # Convert reference number to lowercase to make the search case-insensitive
            reference_number = reference_number.lower()

            try:
                # Use case-insensitive lookup to fetch the record matching the reference number
                details = CheckStatus.objects.filter(reference_number__iexact=reference_number).first()
                if not details:
                    error_message = "No application found with this reference number."
            except CheckStatus.DoesNotExist:
                # Handle case when no record is found
                error_message = "No application found with this reference number."
        
        # Prepare the response data to be returned as JSON
        response_data = {
            'details': {
                'reference_number': details.reference_number if details else '',
                'visa_name': details.visa_name if details else '',
                'visa_status': details.visa_status if details else '',
                'applicant_name': details.applicant_name if details else '',
                'submission_date': details.submission_date.strftime('%Y-%m-%d') if details else ''
            } if details else None,
            'error_message': error_message
        }

        return JsonResponse(response_data)


def visa_details(request, visa_name):
    info = Information.objects.all()[Information.objects.count() - 1]
    visa_list = VisaList.objects.all()
    package_list = PackageList.objects.all()
    visa_details= get_object_or_404(VisaList, visa_name=visa_name)

    images = Slider.objects.filter(is_active=True).order_by('-created_at')
    context={
        'info':info,
        'images':images,
        'visa_list':visa_list,
        'visa_details':visa_details,
        'package_list':package_list
        # 'error_message':error_message
    }
    return render(request, 'visa-details.html',context)


def package_details(request, package_name):
    info = Information.objects.all()[Information.objects.count() - 1]
    package_list = PackageList.objects.all()

    package_details= get_object_or_404(PackageList, package_name=package_name)
    images = Slider.objects.filter(is_active=True).order_by('-created_at')
    context={
        'info':info,
        'images':images,        
        'package_list':package_list,
        'package_details':package_details

        # 'error_message':error_message    
    }
    return render(request, 'package.html',context)




def contact_us(request):

    info = Information.objects.all()[Information.objects.count() - 1]
    visa_list = VisaList.objects.all()
    package_list = PackageList.objects.all()



    images = Slider.objects.filter(is_active=True).order_by('-created_at')
    context={
        'info':info,
        'images':images,
        'visa_list':visa_list,
        'package_list':package_list
        # 'error_message':error_message
    }
    
    return render(request, 'contact_us.html',  context)