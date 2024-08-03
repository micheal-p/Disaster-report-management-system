from django.shortcuts import render, redirect
from .forms import ReportForm  # Import ReportForm from forms.py
from .models import Report
from django.utils import timezone


def home(request):
    return render(request, 'reports/index.html')


def emergency_hotlines(request):
    return render(request, 'reports/emergency.html')

    


# Define the index view
def index(request):
    reports = Report.objects.all()
    return render(request, 'reports/index.html', {'reports': reports})

# Define the report view
def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.date_reported = timezone.now()  # Set the current date and time
            report.save()
            return redirect('index')
    else:
        form = ReportForm()
    return render(request, 'reports/report.html', {'form': form})

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})


