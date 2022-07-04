from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ["ticker"]

class TickerForm(forms.Form):
	ticker = forms.CharField(label='Ticker', max_length=5)

class QuoteForm(forms.Form):
	ticker = forms.CharField(label='Quote', max_length=5)