from django import forms



class Contactform(forms.Form):
	amount = forms.IntegerField()
	category1 = forms.ChoiceField(choices=[('INR','INR || INDIA'),('USD','USD || USA'),('EUR','EUR || EURO'),('JPY','JPY || JAPANESE'),('GBP','GBP || BRITISH POUND'),('AUD','AUD || AUSTRALIAN DOLLAR'),('CAD','CAD || CANADIAN DOLLAR'),('SGD','SGD || SINGAPORE DOLLAR'),('CHF','CHF || SWISS FRANC'),('CNY','CNY || CHINESE YUAN RENMINBI ')])
	category2 = forms.ChoiceField(choices=[('INR','INR || INDIA'),('USD','USD || USA'),('EUR','EUR || EURO'),('JPY','JPY || JAPANESE'),('GBP','GBP || BRITISH POUND'),('AUD','AUD || AUSTRALIAN DOLLAR'),('CAD','CAD || CANADIAN DOLLAR'),('SGD','SGD || SINGAPORE DOLLAR'),('CHF','CHF || SWISS FRANC'),('CNY','CNY || CHINESE YUAN RENMINBI ')])

	
	# widgets = {

	# 	amount : forms.TextInput(attrs={'class':'form-control'}),
	# 	category1 : forms.Select(attrs={'class':'form-control'}),
	# 	category2 : forms.Select(attrs={'class':'form-control'}),

	# }