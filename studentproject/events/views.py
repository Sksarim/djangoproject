

# Create your views here.
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(req):
    home=f"<a href='/app/'>Home</a>"
    library=f"<a href='/library/'>Library</a>"
    exam=f"<a href='/exam/'>Exam</a>"
    events=f"<a href='/'>Events</a>"
    return HttpResponse(f"<center><h1>Welcome to my Events app<hr>{home}\t{library}\t{exam}\t{events}</h1></center>")