import sys

from django.shortcuts import render
# Create your views here.
def index(request):
    if request.method == "POST":
      #  code = request.POST['code']
      codeareadata = request.POST['code']
      try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(codeareadata)
            sys.stdout.close()
            sys.stdout = original_stdout
            output = open('file.txt', 'r').read()
            return render(request, 'compiler_new.html', {'code': codeareadata, 'output': output})
      except Exception as e:
            sys.stdout = original_stdout
            output = e
            return render(request, 'compiler_new.html', {'code': codeareadata, 'output': output})
    return render(request, 'compiler_new.html')