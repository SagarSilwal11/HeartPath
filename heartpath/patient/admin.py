from django.contrib import admin
from patient.models import PatientDetails
# Register your models here.
@admin.register(PatientDetails)
class PatientModelAdmin(admin.ModelAdmin):
    list_display=['id','name','sex','chest_pain','resting_bp','cholesterol','fasting_bs','resting_ecg','max_heart_rate','exercise_angina','old_peak','st_slope','created_at']