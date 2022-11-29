from django import forms

class InvestmentForm(forms.Form):
	starting_amount = forms.FloatField()
	number_of_years = forms.FloatField()
	return_rate = forms.FloatField()
	annual_additional_contribution = forms.FloatField()