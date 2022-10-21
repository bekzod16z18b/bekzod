from django.shortcuts import render
from django.http import HttpResponse
import random
words =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
words1 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
def rword():
    global jword1,jword2 
    global koda1,koda2
    koda1=int(random.choice(words))
    koda2=int(random.choice(words1))
    jword1=koda1
    jword2=koda2
msg=""

def homepagson(request):
    rword()
    global jword1,jword2
    return render(request, 'songame.html',
    {'jum_word1':jword1,'jum_word2':jword2,'msg':msg})

def checkanson(request):
    global koda1,koda2, msg, jword1,jword2
    user_answer=int(request.GET['sonanswer'])
    if user_answer==(jword1+jword2):
        msg = "Siz natijani a`lo darajada topdingiz!!!!"
        homepagson(request)
    else:
        msg = "Siz natijani topo olmadingiz!!!!"
    return render(request, 'songame.html',
    {'jum_word1':jword1,'jum_word2':jword2,'msg':msg})
# Create your views here.
