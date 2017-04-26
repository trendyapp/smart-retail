from django.shortcuts import render, get_object_or_404
from .models import Report
from django.utils import timezone

# Create your views here.

def report_list(request):
	reports = Report.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'reports/report_list.html', {'reports':reports})


def report_detail(request, pk):
	report = get_object_or_404(Report, pk=pk)
	return render(request, 'reports/report_detail.html', {'report': report})
