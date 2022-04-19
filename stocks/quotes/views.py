from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm
from .forms import TickerForm
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = TickerForm(request.POST)
		if form.is_valid():
			ticker = request.POST['ticker']
			return HttpResponseRedirect(ticker)
	else:
		form = TickerForm()
	return render(request, 'index.html', {'form': form})

def ticker(request, tid):
	context = {}
	context['ticker'] = tid 
	return render(request, 'ticker.html', context)


def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		return render(request, 'home.html', {'api' : api})


	else:
		return render(request, 'home.html', {})


	#pk_547bbadc4d1f4d99b4d9d35d195f24b0	
	

def about(request):
	return render(request, 'about.html', {})

def add_stock(request):
	import requests
	import json

	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added"))
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()

		output = []

		for ticker_item in ticker:
			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=")



			try:
				api = json.loads(api_request.content)				
				output.append(api)
				for item in output:
					for key, value in item.itertime():
						try:
							item[key] = float(value)
							
						except ValueError:
							item[key] = str(value)

			except Exception as e:
				api = "Error..."

		return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock deleted"))
	return redirect(add_stock)

def eight_pillars(request):
	return render(request, 'eight_pillars.html', {})