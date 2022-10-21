from django.shortcuts import render

# Create your views here.
def indexc(request):
    return render(request, 'index_c.html')