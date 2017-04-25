from django.shortcuts import render

# Create your views here.

def report_list(request):
	return render(request, 'reports/report_list.html', {})
	