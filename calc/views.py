from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Display(request):
    return render(request,'home.html')
def Details(request):
    if request.method=='POST' :
      hi = request.POST.get("ara")
      return render(request,'submit.html')
    