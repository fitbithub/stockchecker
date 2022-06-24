from django.shortcuts import render
from .forms import TickerForm
from django.http import HttpResponseRedirect
from .tiingo import get_meta_data

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            stock_name = request.POST['stock_search']
            return HttpResponseRedirect(stock_name)
    else:
        form = TickerForm()

    context = {
        'form':form
    }
    return render(request, 'index.html', context)

def ticker(request,tid):
    context = {}
    context['ticker'] = tid
    context['meta'] = get_meta_data(tid)
    return render(request,'stock.html', context)
