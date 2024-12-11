from django.db import models

# Create your models here.
class Information(models.Model):
    sitename = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    sociallink = models.TextField()
    logo = models.ImageField(upload_to='img/logos/')


    def __str__(self):
        return self.sitename


class CheckStatus(models.Model):
    reference_number = models.CharField(max_length=100, unique=True)  # Unique reference
    visa_name = models.CharField(max_length=100)
    visa_status = models.CharField(max_length=100)
    applicant_name = models.CharField(max_length=100, null=True, blank=True)
    submission_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.reference_number
   
class Slider(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    is_active = models.BooleanField(default=True)  # For enabling/disabling images
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"