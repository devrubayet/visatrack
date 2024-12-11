from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Information
from .models import CheckStatus
from .models import Slider
from .forms import ReferenceForm
# Create your views here.
def index(request):
    info = Information.objects.all()[Information.objects.count() - 1]

    # details = None  # Initialize to None for first-time page load
    # error_message = None  # Default value for error message

    # if request.method == "POST":
    #     reference_number = request.POST.get('reference_number')  # Match this with the form's name attribute
    #     print("Submitted Reference Number:", reference_number)  # Debugging log
    #     if reference_number:
    #         try:
    #             # Fetch the record matching the reference number
    #             details = CheckStatus.objects.get(reference_number=reference_number)
    #         except CheckStatus.DoesNotExist:
    #             # If no record is found, set an error message
    #             error_message = "No application found with this reference number."
    

    images = Slider.objects.filter(is_active=True).order_by('-created_at')
    context={
        'info':info,
        'images':images,
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
