from django.http import HttpResponse
from django.template import loader
import pandas as pd
import statsmodels.formula.api as sm
import statsmodels.api as smg
import matplotlib.pyplot as plt, mpld3


def regresja(request):
	testcsv = pd.read_csv('D:/R/Regresja/hardware.csv')
	testdivide = testcsv.iloc[:,2:10].copy()
	regetest = sm.ols(formula="PRP ~ MMAX", data=testdivide).fit()
	testcorr = testdivide.corr()
	regsummary = regetest.summary();
	
	figure = smg.graphics.abline_plot(model_results=regetest)
	
	temp = loader.get_template('regresja.html')
	context = {}
	context['regcsv'] = testcsv.to_html
	context['regcorr'] = testcorr.to_html
	context['regsummary'] = regsummary
	context['fig'] = mpld3.fig_to_html(figure, None, None, True,"simple")
	html = temp.render(context)
	return HttpResponse(html)
