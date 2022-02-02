from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse
#from calc.models import TSLA
from calc.models import fundamental
from calc.models import a
import pandas as pd


# Create your views here.
def home(request):
    return render(request,'home.html')


def market(request):
    return render(request,'market.html')

def forecast(request):
    forecast_query= fundamental.objects.all()
    return render(request,'forecast.html',{'forecast_query':forecast_query})

def technical_screener(request):
    return render(request,'technical_screener.html')


def fundamental_screener(request):
    return render(request,'fundamental_screener.html')

def comparator(request):
    return render(request,'comparator.html')

def forecast_search(request):
    forecast_query= fundamental.objects.all()
    if request.method == "POST":
        fs= request.POST.get('forecast_close_search')
        print(fs)
        fsq= a.objects.all() 
        df = pd.DataFrame(list(a.objects.all().values())) 
        print(df) 
        return render(request,'forecast.html',{'fsq':fsq,'forecast_query':forecast_query})
        
        
        


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


def fundamental_screener_search(request):
    if request.method == "POST":
        # putting all the inputed datas in vaiable
        bv_min =request.POST.get('bv_min_search')
        bv_max =request.POST.get('bv_max_search')
        eps_min =request.POST.get('eps_min_search')
        eps_max =request.POST.get('eps_max_search')
        mc_min =request.POST.get('mc_min_search')
        mc_max =request.POST.get('mc_max_search')
        por_min =request.POST.get('por_min_search')
        por_max =request.POST.get('por_max_search')
        pb_min =request.POST.get('pb_min_search')
        pb_max =request.POST.get('pb_max_search')
        pe_min =request.POST.get('pr_min_search')
        pe_max =request.POST.get('pe_max_search')
        pgr_min =request.POST.get('pgr_min_search')
        pgr_max =request.POST.get('pgr_max_search')
        roa_min =request.POST.get('roa_min_search')
        roa_max =request.POST.get('roa_max_search')
        roe_min =request.POST.get('roe_min_search')
        roe_max =request.POST.get('roe_max_search')
        # defined value start
        bv_def =request.POST.get('bv_defined_search')
        eps_def =request.POST.get('eps_defined_search')
        mc_defined =request.POST.get('mc_defined_search')
        por_defined =request.POST.get('por_defined_search')
        pb_defined =request.POST.get('pb_defined_search')
        pe_defined =request.POST.get('pr_defined_search')
        pgr_defined =request.POST.get('pgr_defined_search')
        roa_defined =request.POST.get('roa_defined_search')
        roe_defined =request.POST.get('roe_defined_search')
        
        #defined value end
        fundamental_query= fundamental.objects.all()
        if bv_def !='' and bv_def is not None:
            fundamental_query= fundamental_query.filter(book_value__gte= bv_def)
        if eps_def !='' and eps_def is not None:
            fundamental_query= fundamental_query.filter(trailing_EPS__gte= eps_def)
        if mc_defined !='' and mc_defined is not None:
            fundamental_query= fundamental_query.filter(market_cap__gte= mc_defined)
        if por_defined !='' and por_defined is not None:
            fundamental_query= fundamental_query.filter(payout_ratio__gte= por_defined)
        if pb_defined !='' and pb_defined is not None:
            fundamental_query= fundamental_query.filter(price_to_book__gte= pb_defined)
        if pe_defined !='' and pe_defined is not None:
            fundamental_query= fundamental_query.filter(trailing_PE__gte= pe_defined)
        if pgr_defined !='' and pgr_defined is not None:
            fundamental_query= fundamental_query.filter(trailing_peg_ratio__gte= pgr_defined)
        if roa_defined !='' and roa_defined is not None:
            fundamental_query= fundamental_query.filter(return_on_assets__lte= roa_defined)
        if roe_defined !='' and roe_defined is not None:
            fundamental_query= fundamental_query.filter(return_on_equity__lte= roe_defined)
        if bv_min !='' and bv_min is not None:
            fundamental_query= fundamental_query.filter(book_value__gte= bv_min)
        if bv_max !='' and bv_max is not None:
            fundamental_query= fundamental_query.filter(book_value__lte= bv_max)
        if eps_min !='' and eps_min is not None:
            fundamental_query= fundamental_query.filter(trailing_EPS__gte= eps_min)
        if eps_max !='' and eps_max is not None:
            fundamental_query= fundamental_query.filter(trailing_EPS__lte= eps_max)
        if mc_min !='' and mc_min is not None:
            fundamental_query= fundamental_query.filter(market_cap__gte= mc_min)
        if mc_max !='' and mc_max is not None:
            fundamental_query= fundamental_query.filter(market_cap__lte= mc_max)
        if por_min !='' and por_min is not None:
            fundamental_query= fundamental_query.filter(payout_ratio__gte= por_min)
        if por_max !='' and por_max is not None:
            fundamental_query= fundamental_query.filter(payout_ratio__lte= por_max)
        if pb_min !='' and pb_min is not None:
            fundamental_query= fundamental_query.filter(price_to_book__gte= pb_min)
        if pb_max !='' and pb_max is not None:
            fundamental_query= fundamental_query.filter(price_to_book__lte= pb_max)
        if pe_min !='' and pe_min is not None:
            fundamental_query= fundamental_query.filter(trailing_PE__gte= pe_min)
        if pe_max !='' and pe_max is not None:
            fundamental_query= fundamental_query.filter(trailing_PE__lte= pe_max)
        if pgr_min !='' and pgr_min is not None:
            fundamental_query= fundamental_query.filter(trailing_peg_ratio__gte= pgr_min)
        if pgr_max !='' and pgr_max is not None:
            fundamental_query= fundamental_query.filter(trailing_peg_ratio__lte= pgr_max)
        if roa_min !='' and roa_min is not None:
            fundamental_query= fundamental_query.filter(return_on_assets__gte= roa_min)
        if roa_max !='' and roa_max is not None:
            fundamental_query= fundamental_query.filter(return_on_assets__lte= roa_max)
        if roe_min !='' and roe_min is not None:
            fundamental_query= fundamental_query.filter(return_on_equity__gte= roe_min)
        if roe_max !='' and roe_max is not None:
            fundamental_query= fundamental_query.filter(return_on_equity__lte= roe_max)
        print(fundamental_query)
        return render(request,'fundamental_screener.html',{'fq':fundamental_query})