from django.shortcuts import render

# Create your views here.
def appointpage(request):
    return render(request,"appointment/appointment.html")

def doctor_detail(request,name):
    return render(request,f'appointment/doctors/{name}.html')