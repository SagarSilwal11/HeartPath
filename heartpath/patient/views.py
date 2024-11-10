from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView  # Use Django's built-in LoginView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login

from patient.forms import PatientForm
from patient.prediction_model import predict_heart_disease
from django.views.generic import View
from .models import PatientDetails
# Prediction page view - protected by LoginRequiredMixin
class PredictionPageView(FormView):
    template_name = 'patient/predict_page.html'
    form_class=PatientForm

    def form_valid(self, form):
        # Save patient form data
        patient = form.save()

        # Prepare patient data for prediction
        patient_data = {
            'age': patient.age,
            'sex': patient.sex,
            'chestpain': patient.chest_pain,  # Use chest_pain as per the model
            'restingbp': patient.resting_bp,  # Use resting_bp as per the model
            'cholesterol': patient.cholesterol,
            'fastingbs': patient.fasting_bs,  # Use fasting_bs as per the model
            'restingecg': patient.resting_ecg,  # Use resting_ecg as per the model
            'maxhr': patient.max_heart_rate,  # Use max_heart_rate as per the model
            'exerciseangina': patient.exercise_angina,  # Use exercise_angina as per the model
            'oldpeak': patient.old_peak,  # Use old_peak as per the model
            'st_slope': patient.st_slope  # Use st_slope as per the model
        }
        
        # Make the prediction
        prediction_result = predict_heart_disease(patient_data)

        # Redirect to the result page with prediction and patient ID as query parameters
        return redirect(reverse('resultpage') + f'?prediction={prediction_result}&patient_id={patient.id}')
# Alternatively, you can pass the prediction and patient_id via the context if you don't want to use query params in the URL.

from django.views.generic import TemplateView

class ResultPageView(TemplateView):
    template_name = 'patient/result_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prediction'] = self.request.GET.get('prediction')
        context['patient_id'] = self.request.GET.get('patient_id')
        return context


# Signup view using the UserCreationForm
class SignupView(FormView):
    template_name = "patient/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('loginpage')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account created successfully! You can now log in.')
        return super().form_valid(form)

# Login view using Django's built-in LoginView
class LoginupView(LoginView):
    template_name = "patient/login.html"
    success_url = reverse_lazy('home')  # Redirect to prediction page after successful login

    def get_success_url(self):
        # Check if there's a 'next' parameter in the URL and use that to redirect
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url  # Redirect to the page user wanted to visit
        return self.success_url  # Default redirect after login (in case 'next' is not available)
    
