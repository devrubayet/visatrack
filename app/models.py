from django.db import models

# Create your models here.


class Information(models.Model):
    sitename = models.CharField(max_length=50,blank=True, null=True)
    site_slogan = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    logo = models.ImageField(upload_to='img/logos/')

    office_address = models.TextField(blank=True, null=True)
    office_email = models.EmailField(blank=True, null=True)
    office_phone = models.CharField(max_length=20 , blank=True, null=True)

    about_us = models.TextField(blank=True, null=True)




    def __str__(self):
        return self.sitename
    



class SocialLink(models.Model):
    information = models.ForeignKey(
        'Information', related_name='social_links', on_delete=models.CASCADE
    )
    platform_name = models.CharField(max_length=50,blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return f"{self.platform_name} "
    






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



class VisaList(models.Model):
    visa_name = models.CharField(max_length=100,blank=True, null=True,unique=True)
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.visa_name

class VisaSilderImage(models.Model):
    visa = models.ForeignKey(VisaList, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='visa_images/')  # Directory for storing images

    def __str__(self):
        return f"Image for {self.visa.visa_name}"
    


class PackageList(models.Model):
    package_name = models.CharField(max_length=100,blank=True, null=True,unique=True)
    description = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return self.package_name

class PackageSilderImage(models.Model):
    package = models.ForeignKey(PackageList, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='package_images/')  # Directory for storing images

    def __str__(self):
        return f"Image for {self.package.package_name}"