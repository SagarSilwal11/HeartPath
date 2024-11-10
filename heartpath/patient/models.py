from django.db import models

class PatientDetails(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    chest_pain = models.CharField(
        max_length=3,
        choices=[
            ('ATA', 'Atypical Angina'),
            ('NAP', 'Non-Anginal Pain'),
            ('ASY', 'Asymptomatic Pain'),
            ('TA', 'Typical Angina')
        ]
    )
    resting_bp = models.IntegerField()
    cholesterol = models.IntegerField()
    fasting_bs = models.IntegerField(choices=[(0, '0'), (1, '1')])
    resting_ecg = models.CharField(max_length=10, choices=[('Normal', 'Normal'), ('ST', 'ST'), ('LVH', 'LVH')])
    max_heart_rate = models.IntegerField()
    exercise_angina = models.CharField(max_length=1, choices=[('N', 'No'), ('Y', 'Yes')])
    old_peak = models.DecimalField(max_digits=3, decimal_places=1)
    st_slope = models.CharField(max_length=5, choices=[('Up', 'Up'), ('Flat', 'Flat'), ('Down', 'Down')])
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically sets the current timestamp

    def __str__(self):
        return f'{self.name}'
