from django.shortcuts import render
from .models import Report
from django.utils import timezone

# Create your views here.

def report_list(request):
	reports = Report.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'reports/report_list.html', {'reports':reports})



