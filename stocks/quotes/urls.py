from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name ="home"),
	path('about.html', views.about, name="about"),
	path('add_stock.html', views.add_stock, name="add_stock"),
	path('delete/<stock_id>', views.delete, name="delete"),
	path('eight_pillars.html', views.eight_pillars, name="eight_pillars"),
	path('index.html', views.index, name="index"),
	path('<str:tid>', views.ticker, name="ticker"),
	
]