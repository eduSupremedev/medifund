from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     full_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     mobile_number = models.CharField(max_length=15, unique=True)
#     pan_details = models.CharField(max_length=10, unique=True)
#     gender = models.CharField(max_length=1,blank=True)
#     date_of_birth = models.DateField()
#     education = models.CharField(max_length=5, blank=True)
#     occupation = models.CharField(max_length=255)
#     address = models.TextField()
    
#     # Additional attributes
#     attribute1 = models.TextField(null=True, blank=True)
#     attribute2 = models.TextField(null=True, blank=True)
#     attribute3 = models.TextField(null=True, blank=True)
#     attribute4 = models.TextField(null=True, blank=True)

#     # Metadata fields
#     cb = models.CharField(max_length=255)  # Created By (Timestamp)
#     cd = models.DateTimeField(auto_now_add=True)  # Created Date
#     lub =models.CharField(max_length=255)     # Last Updated By (Timestamp)
#     lud = models.DateTimeField(auto_now=True)     # Last Updated Date

class MedicalLead(models.Model):
    lead_generate_by = models.CharField(max_length=255)
    lead_purpose = models.TextField()
    patient_name = models.CharField(max_length=255)
    patient_address = models.TextField()
    guardian_name = models.CharField(max_length=255)
    guardian_number = models.CharField(max_length=15)
    patient_age = models.IntegerField(default=0)
    patient_case = models.TextField()
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    estimate_amount = models.DecimalField(max_digits=10, decimal_places=2)
    estimate_date = models.DateField()
    patient_education = models.CharField(max_length=255)
    patient_occupation = models.CharField(max_length=255)
    doctor_detail = models.TextField()
    prescription_documents = models.FileField(upload_to="documents/", null=True, blank=True)
    hospital_name = models.CharField(max_length=255)
    doctor_number = models.CharField(max_length=15)
    patient_pic_2 = models.ImageField(upload_to="patients/", null=True, blank=True)
    patient_id_or_medical_proof = models.FileField(upload_to="medical_proofs/", null=True, blank=True)
    admit_date = models.DateField()
    remarks_description = models.TextField()
    case_type = models.CharField(max_length=20, blank=True)
    lead_source = models.CharField(max_length=20, blank=True)

    # Additional attributes
    attributes1 = models.TextField(null=True, blank=True)
    attributes2 = models.TextField(null=True, blank=True)
    attributes3 = models.TextField(null=True, blank=True)
    attributes4 = models.TextField(null=True, blank=True)
    attributes5 = models.TextField(null=True, blank=True)

    # Metadata fields
    cb = models.CharField(max_length=255)  # Created By (Timestamp)
    cd = models.DateTimeField(auto_now_add=True)  # Created Date
    lub = models.CharField(max_length=255)     # Last Updated By (Timestamp)
    lud = models.DateTimeField(auto_now=True)     # Last Updated Date


class Case(models.Model):
    case_id = models.CharField(max_length=50, unique=True)  # Unique case identifier
    case_type = models.CharField(max_length=20,blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Optional
    parties_detail = models.TextField()
    published_source = models.CharField(max_length=255, null=True, blank=True)
    case_details = models.TextField()

    # Additional attributes
    attributes1 = models.TextField(null=True, blank=True)
    attributes2 = models.TextField(null=True, blank=True)
    attributes3 = models.TextField(null=True, blank=True)
    attributes4 = models.TextField(null=True, blank=True)
    attributes5 = models.TextField(null=True, blank=True)

    # Metadata fields
    cb = models.CharField(max_length=255)  # Created By (Timestamp)
    cd = models.DateTimeField(auto_now_add=True)  # Created Date
    lub = models.CharField(max_length=255)    # Last Updated By (Timestamp)
    lud = models.DateTimeField(auto_now=True)     # Last Updated Date

class Compaign(models.Model):
    case_id = models.CharField(max_length=50)  # Case reference ID
    stage = models.CharField(max_length=100)  # Stage of the case process
    status = models.CharField(max_length=20, blank=True)
    version = models.IntegerField(default=1)  # Version tracking
    source = models.CharField(max_length=255, null=True, blank=True)  # Source of case update

    # Additional attributes
    attributes1 = models.TextField(null=True, blank=True)
    attributes2 = models.TextField(null=True, blank=True)
    attributes3 = models.TextField(null=True, blank=True)
    attributes4 = models.TextField(null=True, blank=True)
    attributes5 = models.TextField(null=True, blank=True)

    # Metadata fields
    cb = models.CharField(max_length=255)  # Created By (Timestamp)
    cd = models.DateTimeField(auto_now_add=True)  # Created Date
    lub = models.CharField(max_length=255)    # Last Updated By (Timestamp)
    lud = models.DateTimeField(auto_now=True)     # Last Updated Date



class Contribution(models.Model):
    transaction_id = models.CharField(max_length=50, unique=True)
    case_id = models.CharField(max_length=50, null=True, blank=True)
    user_id = models.BigIntegerField()
    contributor_name = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50, blank=True)
    transaction_status = models.CharField(max_length=20, blank=True, null=True)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, default='INR')
    gateway_response = models.TextField(null=True, blank=True)
    transaction_time = models.DateTimeField(auto_now_add=True)

    # Additional attributes
    attributes1 = models.TextField(null=True, blank=True)
    attributes2 = models.TextField(null=True, blank=True)
    attributes3 = models.TextField(null=True, blank=True)
    attributes4 = models.TextField(null=True, blank=True)
    attributes5 = models.TextField(null=True, blank=True)

    cb = models.CharField(max_length=255)  # Created Timestamp
    cd = models.DateTimeField(auto_now_add=True)  # Created Date
    lub = models.CharField(max_length=255)  # Last Updated Timestamp
    lud = models.DateTimeField(auto_now=True)  # Last Updated Date

class Party(models.Model):
    parties_name = models.CharField(max_length=255)
    parties_email = models.EmailField(unique=True)
    parties_number = models.CharField(max_length=15)
    parties_social_media_link = models.URLField(null=True, blank=True)
    
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=255)

    attributes1 = models.TextField(null=True, blank=True)
    attributes2 = models.TextField(null=True, blank=True)
    attributes3 = models.TextField(null=True, blank=True)
    attributes4 = models.TextField(null=True, blank=True)
    attributes5 = models.TextField(null=True, blank=True)

    cb = models.CharField(max_length=255)  # Created Timestamp
    cd = models.DateTimeField(auto_now_add=True)  # Created Date
    lub = models.CharField(max_length=255)  # Last Updated Timestamp
    lud = models.DateTimeField(auto_now=True)  # Last Updated Date



class Donation_tip(models.Model):
    transaction_id = models.CharField(max_length=50, unique=True)
    
    gst_percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text="GST percentage applied to the transaction")
    platform_fee = models.DecimalField(max_digits=12, decimal_places=2, help_text="Fee charged by the platform")
    tips = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, help_text="Optional tip amount")

    attributes1 = models.TextField(null=True, blank=True)
    attributes2 = models.TextField(null=True, blank=True)
    attributes3 = models.TextField(null=True, blank=True)
    attributes4 = models.TextField(null=True, blank=True)
    attributes5 = models.TextField(null=True, blank=True)

    cb = models.CharField(max_length=255)  # Created Timestamp
    cd = models.DateTimeField(auto_now_add=True)  # Created Date
    lud = models.DateTimeField(auto_now=True)  # Last Updated Date
    lub = models.CharField(max_length=255) 


class Role(models.Model):
    role_name = models.CharField(max_length=255, unique=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    attributes1 = models.TextField(null=True, blank=True)
    attributes2 = models.TextField(null=True, blank=True)
    attributes3 = models.TextField(null=True, blank=True)
    attributes4 = models.TextField(null=True, blank=True)
    attributes5 = models.TextField(null=True, blank=True)

    cb = models.CharField(max_length=255)  # Created Timestamp
    cd = models.DateTimeField(auto_now_add=True)  # Created Date
    lud = models.DateTimeField(auto_now=True)  # Last Updated Date
    lub = models.CharField(max_length=255) # Last Updated Timestamp

class UserRole(models.Model):
    role_id = models.BigIntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to Django User Model
    role_name = models.CharField(max_length=255)

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    attributes1 = models.TextField(null=True, blank=True)
    attributes2 = models.TextField(null=True, blank=True)
    attributes3 = models.TextField(null=True, blank=True)
    attributes4 = models.TextField(null=True, blank=True)
    attributes5 = models.TextField(null=True, blank=True)

    cb = models.DateTimeField(auto_now_add=True)  # Created Timestamp
    cd = models.DateTimeField(auto_now_add=True)  # Created Date
    lub = models.DateTimeField(auto_now=True)  # Last Updated Timestamp
    lud = models.DateTimeField(auto_now=True)  # Last Updated Date


class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    pan_details = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=1,blank=True)

class Signup(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=False)
    password = models.TextField(max_length=35)
    mobile_number = models.BigIntegerField(unique=False)
    creation_purpose = models.CharField(max_length=255)

class raising_fund_info(models.Model):
    fund_purpose = models.CharField(null=False, max_length=255)
    fund_raising_amount = models.IntegerField(null=False)
    fund_title = models.CharField(null=False, unique=True)
    fund_for = models.CharField(null=False, max_length=35, unique=True)
    user_qualification = models.CharField(null=False, max_length=35, unique=True)
    user_emp_status = models.CharField(null=False, max_length=255)
    how_to_know = models.CharField(null=False, max_length=255)
    attachments = models.TextField(null=False)

class patient_page_info(models.Model):
    patient_full_name = models.CharField(null=False, max_length=255)
    patient_age = models.IntegerField(default=0)
    hospitalisation_status = models.CharField(null=False, unique=True)
    hospital = models.CharField(null=False, max_length=35, unique=True)
    enter_city = models.CharField(null=False, max_length=35, unique=True)
    user_emp_status = models.CharField(null=False, max_length=255)
    how_to_know = models.CharField(null=False, max_length=255)

class patient_story_info(models.Model):
    patienet_story = models.TextField(null=False)
    attachments = models.TextField(null=False, default='zxcvbnm')


class fund_raising_form(models.Model):
    user_info = models.CharField(max_length=255, blank=True)
    user_id = models.IntegerField()
    user_qualification = models.CharField(max_length=255, blank=True)
    user_employed_status = models.CharField(max_length=255, blank=True)
    how_to_know = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=50)
    fund_title = models.CharField(max_length=255, blank=True)
    fund_purpose = models.TextField(blank=True)
    fund_for = models.CharField(max_length=255, blank=True)
    fund_raising_amount = models.IntegerField()
    amount_raised = models.IntegerField(default=0)
    status = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=255, blank=True)
    ngo_name = models.CharField(max_length=255, blank=True)
    ngo_registration_number = models.CharField(max_length=255, blank=True)
    ngo_website_url = models.URLField(blank=True)
    patienet_full_name = models.CharField(max_length=255, blank=True)
    patienet_age = models.IntegerField(blank=True, null=True)
    hospitalization_status = models.CharField(max_length=255, blank=True)
    hospital_name = models.CharField(max_length=255, blank=True)
    hospital_location = models.CharField(max_length=255, blank=True)
    animal_type = models.CharField(max_length=255, blank=True)
    animal_name = models.CharField(max_length=255, blank=True)
    animal_age = models.IntegerField(blank=True, null=True)
    treatment_reason = models.TextField(blank=True)
    vetnairy_name = models.CharField(max_length=255, blank=True)
    vetnairy_clinic_name = models.CharField(max_length=255, blank=True)
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)
    medical_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    patienet_image = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_date = models.DateField()
    created_by = models.CharField(max_length=255)
    last_created_date = models.DateField( null=True )
    last_created_by = models.CharField(max_length=255)


class MedicalLead(models.Model):
      #patient info
    lead_generate_by = models.CharField(max_length=255)
    lead_purpose = models.TextField()
    patient_name = models.CharField(max_length=255)
    patient_address = models.TextField()
    patient_age = models.IntegerField()
    patient_case = models.TextField()
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    estimate_amount = models.DecimalField(max_digits=10, decimal_places=2)
    estimate_date = models.DateField()
    patient_education = models.CharField(max_length=255)
    patient_occupation = models.CharField(max_length=255)
    patient_pic_2 = models.ImageField(upload_to='patients/', null=True, blank=True)
    patient_id = models.FileField(upload_to='proofs/', null=True, blank=True)
    
    # Guardian Info
    
    guardian_name = models.CharField(max_length=255)
    guardian_number = models.CharField(max_length=15)
    
    # Doctor info
    hospital_name = models.CharField(max_length=255)
    doctor_number = models.CharField(max_length=15)
    prescription_documents = models.FileField(upload_to='prescriptions/', null=True, blank=True)
    description_documents = models.FileField(upload_to='descriptions/', null=True, blank=True)
    case_type = models.CharField(max_length=100)
    lead_source = models.CharField(max_length=101)
    
from django.db import models

class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.email


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    roll_number = models.IntegerField()
