from xml.dom.minidom import Attr
from django import forms

class TickerForm(forms.Form):
    stock_search = forms.CharField(label='Ticker', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    stock_search.widget.attrs['placeholder'] = 'Enter Stock'