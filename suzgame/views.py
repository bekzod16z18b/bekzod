from django.shortcuts import render
from django.http import HttpResponse
import random
words =[
    "int",
    "float",
    "char",
    "bool",
    "for",
    "while",
    "break",
    "case",
]
def rword():
    global jword 
    global word
    word=random.choice(words)
    jum=random.sample(word, len(word))
    jword="".join(jum)

msg=""

def homepagee(request):
    rword()
    global jword,msg
    return render(request, 'suzgame.html',
    {'jum_word':jword,'msg':msg})

def checkans(request):
    global word, msg, jword
    user_answer=request.GET['answer']
    if user_answer==word:
        msg = "Siz so`zni a`lo darajada topdingiz!!!!"
        homepagee(request)
    else:
        msg = "Siz so`zni topo olmadingiz!!!!"
    return render(request, 'suzgame.html',
    {'jum_word':jword,'msg':msg})
# Create your views here.
