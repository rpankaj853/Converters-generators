import requests
from django.shortcuts import render
from .forms import Contactform
from .models import typemodel

# Create your views here.
def index(request):
	return render(request,'convertors/index.html');


def convert(request):
	typemodels = typemodel.objects.all()
	return render(request,'convertors/convert.html',{'typemodels':typemodels});

def textcon(request):
	return render(request,'convertors/text_convert.html');



def currencycon(request):
	am1 = 1
	cat1 = 'USD'
	cat2 = 'INR'
	form = Contactform(request.POST)
	if form.is_valid():

		am1 = form.cleaned_data['amount']
		cat1  = form.cleaned_data['category1']  
		cat2 = form.cleaned_data['category2']

		print(am1)





	#forms end part------------------------------------------------
	from_cur = cat1
	to_cur = cat2
	amount = am1
	url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+ from_cur + '&to_currency='+to_cur +'&apikey=NNTGP21FPMMO0LMH'
	r = requests.get(url)
	r1 = r.json()
	
	cur = r1['Realtime Currency Exchange Rate']
	error_msg = ''
	if request.method == 'POST':
		error_msg = 'Default Value is shown beacuse your amount is 1 or less then 1'
		
	if amount <= 1:
		cur_rates = {
		'f_cur_name' : cur['2. From_Currency Name'],
		'f_cur_code':cur['1. From_Currency Code'],
		
		't_cur_name':cur['4. To_Currency Name'],
		't_cur_code':cur['3. To_Currency Code'],
		't_cur_rate':cur['5. Exchange Rate'],
		'time_zone':cur['7. Time Zone'],
		'bid_price':cur['8. Bid Price'],
		'ask_price':cur['9. Ask Price'],
		'f_cur_rate':amount,
		'error_msg':error_msg,

		}
		print(amount,from_cur,to_cur)
	elif amount > 1 :
		rate = cur['5. Exchange Rate']
		res = float(rate) * amount 
		cur_rates = {
		'f_cur_name' : cur['2. From_Currency Name'],
		'f_cur_code':cur['1. From_Currency Code'],
		'f_cur_rate':cur['2. From_Currency Name'],
		't_cur_name':cur['4. To_Currency Name'],
		't_cur_code':cur['3. To_Currency Code'],
		't_cur_rate':res,
		'f_cur_rate':amount,
		'time_zone':cur['7. Time Zone'],
		'bid_price':cur['8. Bid Price'],
		'ask_price':cur['9. Ask Price'],

		}
		print(res,amount,from_cur,to_cur)
	


	
	#content = typemodel.objects.all()
	cur_context = {'cur_rates':cur_rates,'form':form}
	
	
	return render(request,'convertors/currencyconvert.html',cur_context);




def markscon(request):
	
	return render(request,'convertors/marksconvert.html');


def fileconvert(request):

	return render(request,'convertors/fileconvert.html');


def thermocon(request):

	return render(request,'convertors/thermo.html');

def cryptocon(request):

	return render(request,'convertors/cryptocon.html');