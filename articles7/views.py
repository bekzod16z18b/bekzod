from django.shortcuts import render

# Create your views here.
def indexdj(request):
    return render(request, 'index_dj.html')