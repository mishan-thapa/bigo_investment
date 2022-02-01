from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')


def market(request):
    return render(request,'market.html')

def technical_screener(request):
    return render(request,'technical_screener.html')


def fundamental_screener(request):
    return render(request,'fundamental_screener.html')

# search bar ma searcha huda
def search(request):
    if request.method == "POST":
        a= request.POST.get('searched')
        if a == "PCBL":
            return render(request,'pcbl.html')
    # if request.GET['searched']=="PCBL" :
    #         return render(request,'pcbl.html')
    # elif request.GET['searched']=="AA":
    #     return render(request,'AA.html')