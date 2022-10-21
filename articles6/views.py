from django.shortcuts import render

# Create your views here.
def indexp(request):
    return render(request, 'index_p.html')