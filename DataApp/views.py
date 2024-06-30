from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from DataApp import models
from DataApp.models import faq
from DataApp.models import contactus
from DataApp.models import helpnsupport
from DataApp.models import userregister
from DataApp.models import review
from DataApp.models import article
from DataApp.models import jobsearch
from DataApp.models import video
from DataApp.models import initiative
from DataApp.models import ChatMessage
from DataApp.models import category,structure
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
from django.http import JsonResponse
import random
from django.db.models import Q

# Create your views here.
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def md1(request):
	if request.method=="POST":
		df=pd.read_csv(r"cumulative-numberof A.I bills-passed.csv")
		c1=request.POST.get('country')
		df1=df[df["Entity"]==c1]
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df1["Year"],y=df1["number_ai_bills_cumulative"], mode="lines+markers",name=c1,marker=dict(symbol="star",size=10,line=dict(width=2,
                                        color='white'))))
		fig.update_layout(
      			xaxis_type="category",
      			yaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Number of AI Bills Total",
      			title="Country with Cumulative-Bills passed over the mentioned Years",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
      			)
		graph=fig.to_html
		return render(request,"md1result.html",{"graph":graph})
	else:
  		data=pd.read_csv("cumulative-numberof A.I bills-passed.csv")
  		column=data["Entity"].drop_duplicates().tolist()
  		return render(request,"md1.html",{"data":column})

def md2(request):
	df=pd.read_csv(r"cumulative-numberof A.I bills-passed.csv")
	fig=px.bar(df,x="Year",y="number_ai_bills_cumulative",color="Entity",
		labels={"Entity":"Country","number_ai_bills_cumulative":"Number of AI bills"})
	fig.update_layout(
      			xaxis_type="category",
      			yaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Number of AI Bills Total",
      			title="All Countries' Cumulative-Bills passed over the mentioned Years",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=20,color="#649568"),
      			barmode="group"

   )
	
	graph=fig.to_html
	return render(request,"md2.html",{"graph":graph})

def md3(request):
	if request.method=="POST":
		df=pd.read_csv(r"cumulative-numberof A.I bills-passed.csv")
		c1=request.POST.get('country')
		c2=request.POST.get('country1')
		df1=df[df["Entity"]==c1]
		df2=df[df["Entity"]==c2]
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df1["Year"],y=df1["number_ai_bills_cumulative"], mode="lines+markers",name=c1,marker=dict(symbol="star",size=10,line=dict(width=2,
                                        color='white'))))
		fig.add_traces(go.Scatter(x=df2["Year"],y=df2["number_ai_bills_cumulative"], mode="lines+markers",name=c2,marker=dict(symbol="circle",size=10,line=dict(width=2,
                                        color='white'))))
		fig.update_layout(
      			xaxis_type="category",
      			yaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Number of AI Bills Total",
      			title="Two Countries with Cumulative-Bills passed all over the Years",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
   )
		graph=fig.to_html
		return render(request,"md3result.html",{"graph":graph})
	else:
  		data=pd.read_csv(r"cumulative-numberof A.I bills-passed.csv")
  		column=data["Entity"].drop_duplicates().tolist()
  		return render(request,"md3.html",{"data":column})

def md4(request):
	if request.method=="POST":
		df=pd.read_csv(r"cumulative-numberof A.I bills-passed.csv")
		c1=request.POST.get('country')
		c2=request.POST.get('country1')
		sy=int(request.POST.get('syear'))
		ey=int(request.POST.get('eyear'))
		df1=df[df["Entity"]==c1]
		df2=df[df["Entity"]==c2]
		df1=df1[(df1["Year"]>=sy) & (df1["Year"]<=ey)]
		df2=df2[(df2["Year"]>=sy) & (df2["Year"]<=ey)]
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df1["Year"],y=df1["number_ai_bills_cumulative"], mode="lines+markers",name=c1,marker=dict(symbol="star",size=10,line=dict(width=2,
                                        color='white'))))
		fig.add_traces(go.Scatter(x=df2["Year"],y=df2["number_ai_bills_cumulative"], mode="lines+markers",name=c2,marker=dict(symbol="circle",size=10,line=dict(width=2,
                                        color='white'))))
		fig.update_layout(
      			xaxis_type="category",
      			yaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Number of AI Bills Total",
      			title="Two Countries with Cumulative-Bills passed over the mentioned Years",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
      			)
		graph=fig.to_html
		return render(request,"md4result.html",{"graph":graph})
	else:
		data=pd.read_csv(r"cumulative-numberof A.I bills-passed.csv")
		column=data["Entity"].drop_duplicates().tolist()
		column1=data["Entity"].drop_duplicates().tolist()
		column2=data["Year"].drop_duplicates().tolist()
		column3=data["Year"].drop_duplicates().tolist()
		return render(request,"md4.html",{"data":column,"data1":column1,"data2":column2,"data3":column3})
	

def md5(request):
	if request.method=="POST":
		df=pd.read_csv(r"cumulative-numberof A.I bills-passed.csv")
		c1=request.POST.get('country')
		c2=request.POST.get('country1')
		c3=request.POST.get('country2')
		df1=df[df["Entity"]==c1]
		df2=df[df["Entity"]==c2]
		df3=df[df["Entity"]==c3]
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df1["Year"],y=df1["number_ai_bills_cumulative"], mode="lines+markers",name=c1,marker=dict(symbol="star",size=10,line=dict(width=2,
                                        color='white'))))
		fig.add_traces(go.Scatter(x=df2["Year"],y=df2["number_ai_bills_cumulative"], mode="lines+markers",name=c2,marker=dict(symbol="square",size=10,line=dict(width=2,
                                        color='white'))))
		fig.add_traces(go.Scatter(x=df3["Year"],y=df3["number_ai_bills_cumulative"], mode="lines+markers",name=c3,marker=dict(symbol="circle",size=10,line=dict(width=2,
                                        color='white'))))
		fig.update_layout(
      			xaxis_type="category",
      			yaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Number of AI Bills Total",
      			title="Three Countries with their 'per annum' Cumulative-Bills passed",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
      			)
		graph=fig.to_html
		return render(request,"md5result.html",{"graph":graph})
	else:
		data=pd.read_csv(r"cumulative-numberof A.I bills-passed.csv")
		column=data["Entity"].drop_duplicates().tolist()
		column1=data["Entity"].drop_duplicates().tolist()
		return render(request,"md5.html",{"data":column,"data1":column1,"data2":column1})

def md6(request):
	import country_converter as coco
	import pandas as pd
	import plotly.express as px
	df=pd.read_csv(r"cumulative-numberof A.I bills-passed.csv")
	cc=coco.CountryConverter()
	df["Entity_codes"]=cc.convert(names=df["Code"],to="ISO3")
	fig=px.scatter_geo(df,locations="Entity_codes"
		,color="Entity",hover_name="Entity",size="number_ai_bills_cumulative",size_max=50,animation_frame="Year",projection="natural earth")
	fig.show()
	graph=fig.to_html
	return render(request,"md6result.html",{"graph":graph})


def heading1(request):
	return render(request,"heading1.html")

def md11(request):
	if request.method=="POST":
		df=pd.read_csv(r"Annual Number of newly funded A.I companies.csv")
		c1=request.POST.get('country')
		df1=df[df["Entity"]==c1]
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df1["Year"],y=df1["newly_funded_ai_companies"], mode="lines+markers",name=c1,marker=dict(symbol="circle",size=12,line=dict(width=2,
                                        color='black'))))
		fig.update_layout(
      			xaxis_type="category",
      			yaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Number of newly funded AI Companies",
      			title="Country with no of newly funded AI Companies",
      			title_font=dict(family="Algerian",size=35,color="#800080"),
      			paper_bgcolor="#ccc",
      			title_x=0.5,
      			height=700,
      			width=1200,
      			font=dict(family="Comic Sans MS",size=18,color="#800080")
      			)
		graph=fig.to_html
		return render(request,"md11result.html",{"graph":graph})
	else:
  		data=pd.read_csv("Annual Number of newly funded A.I companies.csv")
  		column=data["Entity"].drop_duplicates().tolist()
  		return render(request,"md11.html",{"data":column})

def md12(request):
	df=pd.read_csv(r"Annual Number of newly funded A.I companies.csv")
	fig=px.scatter(df,x="Year",y="newly_funded_ai_companies",color="Entity",
		size="newly_funded_ai_companies",
		labels={"Entity":"Country","newly_funded_ai_companies":"Number of AI bills"})
	fig.update_layout(
      			xaxis_type="category",
      			yaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Number of newly funded AI Companies",
      			title="No of newly funded companies in all countries",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568"),
      			barmode="group",
      			#xaxis=dict(showgrid="F")
	)
	graph=fig.to_html
	return render(request,"md12.html",{"graph":graph})
def md13(request):
	if request.method=="POST":
		df=pd.read_csv(r"Annual Number of newly funded A.I companies.csv")
		c1=request.POST.get('country')
		c2=request.POST.get('country1')
		df1=df[df["Entity"]==c1]
		df2=df[df["Entity"]==c2]
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df1["Year"],y=df1["newly_funded_ai_companies"], mode="lines+markers",name=c1,marker=dict(symbol="square")))
		fig.add_traces(go.Scatter(x=df2["Year"],y=df2["newly_funded_ai_companies"], mode="lines+markers",name=c2,marker=dict(symbol="star")))
		fig.update_layout(
      			xaxis_type="category",
      			yaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Number of newly funded AI Companies",
      			title="Two Countries with no of newly aided companies in them",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
   )
		graph=fig.to_html
		return render(request,"md13result.html",{"graph":graph})
	else:
  		data=pd.read_csv(r"Annual Number of newly funded A.I companies.csv")
  		column=data["Entity"].drop_duplicates().tolist()
  		return render(request,"md13.html",{"data":column})

def md14(request):
	if request.method=="POST":
		df=pd.read_csv(r"Annual Number of newly funded A.I companies.csv")
		c1=request.POST.get('country')
		c2=request.POST.get('country1')
		sy=int(request.POST.get('syear'))
		ey=int(request.POST.get('eyear'))
		df1=df[df["Entity"]==c1]
		df2=df[df["Entity"]==c2]
		df1=df1[(df1["Year"]>=sy) & (df1["Year"]<=ey)]
		df2=df2[(df2["Year"]>=sy) & (df2["Year"]<=ey)]
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df1["Year"],y=df1["newly_funded_ai_companies"], mode="lines+markers",name=c1,marker=dict(symbol="circle",size=12,line=dict(width=2,
                                        color='black'))))
		fig.add_traces(go.Scatter(x=df2["Year"],y=df2["newly_funded_ai_companies"], mode="lines+markers",name=c2,marker=dict(symbol="square",size=12,line=dict(width=2,
                                        color='black'))))
		fig.update_layout(
	      		xaxis_type="category",
	      		yaxis_type="category",
	      		xaxis_title="Year",
	      		yaxis_title="Number of newly funded AI Companies",
	      		title="Two Countries with no of newly aided Companies with given start year and end year",
	      		title_font=dict(family="Algerian",size=35,color="#149414"),
	      		paper_bgcolor="#181818",
	      		plot_bgcolor="#202020",
	      		title_x=0.45,
	      		height=700,
	      		width=1500,
	      		font=dict(family="Comic Sans MS",size=18,color="#649568")
	      		)
		graph=fig.to_html
		return render(request,"md14result.html",{"graph":graph})
	else:
		data=pd.read_csv(r"Annual Number of newly funded A.I companies.csv")
		column=data["Entity"].drop_duplicates().tolist()
		column1=data["Entity"].drop_duplicates().tolist()
		column2=data["Year"].drop_duplicates().tolist()
		column3=data["Year"].drop_duplicates().tolist()
		return render(request,"md14.html",{"data":column,"data1":column1,"data2":column2,"data3":column3})

def md15(request):
	if request.method=="POST":
		df=pd.read_csv(r"Annual Number of newly funded A.I companies.csv")
		c1=request.POST.get('country')
		c2=request.POST.get('country1')
		c3=request.POST.get('country2')
		df1=df[df["Entity"]==c1]
		df2=df[df["Entity"]==c2]
		df3=df[df["Entity"]==c3]
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df1["Year"],y=df1["newly_funded_ai_companies"], mode="lines+markers",name=c1,marker=dict(symbol="square")))
		fig.add_traces(go.Scatter(x=df2["Year"],y=df2["newly_funded_ai_companies"], mode="lines+markers",name=c2,marker=dict(symbol="circle")))
		fig.add_traces(go.Scatter(x=df3["Year"],y=df3["newly_funded_ai_companies"], mode="lines+markers",name=c3,marker=dict(symbol="star")))
		fig.update_layout(
      			xaxis_type="category",
      			yaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Number of newly funded AI companies",
      			title="Three Countries with no of newly aided countries in all years",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
      			)
		graph=fig.to_html
		return render(request,"md15result.html",{"graph":graph})
	else:
		data=pd.read_csv(r"Annual Number of newly funded A.I companies.csv")
		column=data["Entity"].drop_duplicates().tolist()
		column1=data["Entity"].drop_duplicates().tolist()
		return render(request,"md15.html",{"data":column,"data1":column1,"data2":column1})

def md16(request):
	import country_converter as coco
	import pandas as pd
	import plotly.express as px
	cc=coco.CountryConverter()
	df=pd.read_csv(r"Annual Number of newly funded A.I companies.csv")
	df["Entity_codes"]=cc.convert(names=df["Code"],to="ISO3")
	fig=px.scatter_geo(df,locations="Entity_codes"
		,color="Entity",hover_name="Entity",size="newly_funded_ai_companies",size_max=100,animation_frame="Year",projection="natural earth")
	fig.show()
	graph=fig.to_html
	return render(request,"md16.html",{"graph":graph})

def md17(request):
	if request.method=="POST":
		df=pd.read_csv("Annual Number of newly funded A.I companies.csv")
		y1=int(request.POST.get('Year'))
		num=int(request.POST.get('count'))
		df1=df[df["Year"]==y1]
		df1=df1.dropna()
		df1=df1.sort_values(by='newly_funded_ai_companies')
		dfmax=df1.tail(num)
		fig=px.bar(dfmax,x="Entity",y="newly_funded_ai_companies",color="Entity",
			
			labels={"Entity":"Country","newly_funded_ai_companies":"Number of AI bills"})
		fig.update_layout(
      		xaxis_type="category",
      		xaxis_title="Year",
      		yaxis_title="Number of newly funded AI Companies",
      		title="No of newly funded companies in all countries",
      		title_font=dict(family="Algerian",size=35,color="#149414"),
      		paper_bgcolor="#181818",
      		plot_bgcolor="#202020",
      		title_x=0.45,
      		height=700,
      		width=1500,
      		font=dict(family="Comic Sans MS",size=18,color="#649568"),
      		
      		)
		graph=fig.to_html
		return render(request,"md17result.html",{"graph":graph})
	else:
  		data=pd.read_csv("Annual Number of newly funded A.I companies.csv")
  		column=data["Year"].drop_duplicates().tolist()
  		number={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
  		return render(request,"md17.html",{"data":column,"data1":number})

def heading2(request):
	return render(request,"heading2.html")

def md21(request):
	if request.method=="POST":
		df=pd.read_csv(r"share A.I job-postings (1).csv")
		c1=request.POST.get('country')
		df1=df[df["Entity"]==c1]
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df1["Year"],y=df1["ai_job_postings"], mode="lines+markers",name=c1,marker=dict(symbol="square",size=15)))
		fig.update_layout(
      		yaxis_type="category",
      		xaxis_title="Year",
      		yaxis_title="Shares in AI Job-postings",
      		title="Country with no of newly funded AI Companies",
      		title_font=dict(family="Algerian",size=35,color="#149414"),
      		paper_bgcolor="#181818",
      		plot_bgcolor="#202020",
      		title_x=0.45,
      		height=700,
      		width=1500,
      		font=dict(family="Comic Sans MS",size=18,color="#649568")
      		)
		graph=fig.to_html
		return render(request,"md21result.html",{"graph":graph})
	else:
  		data=pd.read_csv("share A.I job-postings (1).csv")
  		column=data["Entity"].drop_duplicates().tolist()
  		return render(request,"md21.html",{"data":column})

def md22(request):
	df=pd.read_csv(r"share A.I job-postings (1).csv")
	fig=px.scatter(df,x="Year",y="ai_job_postings",color="Entity",
		size="ai_job_postings",
		labels={"Entity":"Country","ai_job_postings":"Shares in AI Job-postings"})
	fig.update_layout(
      	yaxis_type="category",
      	xaxis_title="Year",
      	yaxis_title="Shares in AI Job-postings",
      	title="No of newly funded companies in all countries",
      	title_font=dict(family="Algerian",size=35,color="#149414"),
      	paper_bgcolor="#181818",
      	plot_bgcolor="#202020",
      	title_x=0.45,
      	height=700,
      	width=1500,
      	font=dict(family="Comic Sans MS",size=18,color="#649568"),
      	barmode="group",
      			#xaxis=dict(showgrid="F")
      			)
	graph=fig.to_html
	return render(request,"md22.html",{"graph":graph})

def md23(request):
	if request.method=="POST":
		df=pd.read_csv(r"share A.I job-postings (1).csv")
		c1=request.POST.get('country')
		c2=request.POST.get('country2')
		df1=df[df["Entity"]==c1]
		df2=df[df["Entity"]==c2]
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df1["Year"],y=df1["ai_job_postings"], mode="lines+markers",name=c1,marker=dict(symbol="square")))
		fig.add_traces(go.Scatter(x=df2["Year"],y=df2["ai_job_postings"], mode="lines+markers",name=c2,marker=dict(symbol="star")))
		fig.update_layout(
      			xaxis_type="category",
      			yaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Shares in AI Job-postings",
      			title="Two Countries with Shares in AI Job-postings",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
   )
		graph=fig.to_html
		return render(request,"md23result.html",{"graph":graph})
	else:
  		data=pd.read_csv(r"share A.I job-postings (1).csv")
  		column=data["Entity"].drop_duplicates().tolist()
  		return render(request,"md23.html",{"data":column})

def md24(request):
	if request.method=="POST":
		df=pd.read_csv(r"share A.I job-postings (1).csv")
		c1=request.POST.get('country')
		c2=request.POST.get('country1')
		sy=int(request.POST.get('syear'))
		ey=int(request.POST.get('eyear'))
		df1=df[df["Entity"]==c1]
		df2=df[df["Entity"]==c2]
		df1=df1[(df1["Year"]>=sy) & (df1["Year"]<=ey)]
		df2=df2[(df2["Year"]>=sy) & (df2["Year"]<=ey)]
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df1["Year"],y=df1["ai_job_postings"], mode="lines+markers",name=c1,marker=dict(symbol="square")))
		fig.add_traces(go.Scatter(x=df2["Year"],y=df2["ai_job_postings"], mode="lines+markers",name=c2,marker=dict(symbol="star")))
		fig.update_layout(
	      		xaxis_type="category",
	      		yaxis_type="category",
	      		xaxis_title="Year",
	      		yaxis_title="Shares in AI Job-postings",
	      		title="Two Countries with Shares in AI Job-postings with given start year and end year",
	      		title_font=dict(family="Algerian",size=35,color="#149414"),
	      		paper_bgcolor="#181818",
	      		plot_bgcolor="#202020",
	      		title_x=0.45,
	      		height=700,
	      		width=1500,
	      		font=dict(family="Comic Sans MS",size=18,color="#649568")
	      		)
		graph=fig.to_html
		return render(request,"md24result.html",{"graph":graph})
	else:
		data=pd.read_csv(r"share A.I job-postings (1).csv")
		column=data["Entity"].drop_duplicates().tolist()
		column1=data["Entity"].drop_duplicates().tolist()
		column2=data["Year"].drop_duplicates().tolist()
		column3=data["Year"].drop_duplicates().tolist()
		return render(request,"md24.html",{"data":column,"data1":column1,"data2":column2,"data3":column3})

def md25(request):
	if request.method=="POST":
		df=pd.read_csv(r"share A.I job-postings (1).csv")
		c1=request.POST.get('country')
		c2=request.POST.get('country1')
		c3=request.POST.get('country2')
		df1=df[df["Entity"]==c1]
		df2=df[df["Entity"]==c2]
		df3=df[df["Entity"]==c3]
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df1["Year"],y=df1["ai_job_postings"], mode="lines+markers",name=c1,marker=dict(symbol="square",size=10,line=dict(width=2,
                                        color='white'))))
		fig.add_traces(go.Scatter(x=df2["Year"],y=df2["ai_job_postings"], mode="lines+markers",name=c2,marker=dict(symbol="circle",size=10,line=dict(width=2,
                                        color='white'))))
		fig.add_traces(go.Scatter(x=df3["Year"],y=df3["ai_job_postings"], mode="lines+markers",name=c3,marker=dict(symbol="star",size=10,line=dict(width=2,
                                        color='white'))))
		fig.update_layout(
      			xaxis_type="category",
      			yaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Shares in AI Job-postings",
      			title="Three Countries with Shares in AI Job-postings in all years",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
      			)
		graph=fig.to_html
		return render(request,"md25result.html",{"graph":graph})
	else:
		data=pd.read_csv(r"share A.I job-postings (1).csv")
		column=data["Entity"].drop_duplicates().tolist()
		column1=data["Entity"].drop_duplicates().tolist()
		return render(request,"md25.html",{"data":column,"data1":column1,"data2":column1})

def md26(request):
	import country_converter as coco
	import pandas as pd
	import plotly.express as px
	cc=coco.CountryConverter()
	df=pd.read_csv(r"share A.I job-postings (1).csv")
	df["Entity_codes"]=cc.convert(names=df["Code"],to="ISO3")
	fig=px.scatter_geo(df,locations="Entity_codes"
		,color="Entity",hover_name="Entity",size="ai_job_postings",size_max=100,animation_frame="Year",projection="natural earth")
	fig.show()
	graph=fig.to_html
	return render(request,"md26.html",{"graph":graph})



def heading3(request):
	return render(request,"heading3.html")

#transpose and select Country then all their yearly expenses shown//////////
def md31(request):
	if request.method=="POST":
		c1=request.POST.get('country')
		df=pd.read_csv(r"World developement index.csv")
		df=df.transpose()
		df.columns= df.iloc[0,:]
		df = df.iloc[4:,:]
		df=df.astype(float)
		df=df.reset_index()
		df.rename(columns={'index':'Year'}, inplace=True)
		df['Year']=df['Year'].astype(int)
		df1=df.loc[:,['Year',c1]]
		df1=df1.dropna()
		fig=px.scatter(df1,x="Year",y=c1,size=c1,size_max=60,color="Year",log_x=True)
		fig.update_layout(
			xaxis_title="Year",
      		yaxis_title="Expenses(LCU)",
      		title="World development index of " +" "	+c1,
      		title_font=dict(family="Algerian",size=35,color="#149414"),
      		paper_bgcolor="#181818",
      		plot_bgcolor="#202020",
      		title_x=0.45,
      		height=700,
      		width=1500,
      		font=dict(family="Comic Sans MS",size=18,color="#649568")
      		)
		graph=fig.to_html
		return render(request,"md31result.html",{"graph":graph})
	else:
		data=pd.read_csv("World developement index.csv")
		column=data["Country Name"].drop_duplicates().tolist()
		return render(request,"md31.html",{"data":column})

#Select year and then all countries expenses will be shown////////////////
def md32(request):
	if request.method=="POST":
		y1=request.POST.get('Year')
		df=pd.read_csv(r"World developement index.csv")
		df1= df.loc[:,['Country Name', y1]]
		df1=df1.dropna()
		fig=px.bar(df1,x='Country Name',y=y1,color="Country Name")
		fig.update_layout(
			xaxis_title="Year",
      		yaxis_title="Expenses(LCU)",
      		title="World development index of "+" "+y1,
      		title_font=dict(family="Algerian",size=35,color="#149414"),
      		paper_bgcolor="#181818",
      		plot_bgcolor="#202020",
      		title_x=0.45,
      		height=700,
      		width=1500,
      		font=dict(family="Comic Sans MS",size=18,color="#649568")
      		)
		graph=fig.to_html
		return render(request,"md32result.html",{"graph":graph})
	else:
		data=pd.read_csv("World developement index.csv")
		return render(request,"md32.html")

#select particular year and value to show expenses of minimum first n countries 

def md33(request):
	if request.method=="POST":
		y1=request.POST.get('Year')
		n=int(request.POST.get('num'))
		n1=request.POST.get('num')
		df=pd.read_csv(r"World developement index.csv")
		df1= df.loc[:,['Country Name', y1]]
		df1=df1.dropna()
		df1=df1.sort_values(by=y1)
		dfmin=df1.head(n)
		fig=px.bar(dfmin,x='Country Name',y=y1,color="Country Name")
		fig.update_layout(
			xaxis_title="Year",
      		yaxis_title="Expenses(LCU)",
      		title="World development index of first "+n1+" Countries with least Expenses(LCU) in "+y1,
      		title_font=dict(family="Algerian",size=35,color="#149414"),
      		paper_bgcolor="#181818",
      		plot_bgcolor="#202020",
      		title_x=0.45,
      		height=700,
      		width=1500,
      		font=dict(family="Comic Sans MS",size=18,color="#649568")
      		)
		graph=fig.to_html
		return render(request,"md33result.html",{"graph":graph})
	else:
		data=pd.read_csv("World developement index.csv")
		number={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
		return render(request,"md33.html",{"data":number})

def md34(request):
	if request.method=="POST":
		y1=request.POST.get('Year')
		n=int(request.POST.get('num'))
		n1=request.POST.get('num')
		df=pd.read_csv(r"World developement index.csv")
		df1= df.loc[:,['Country Name', y1]]
		df1=df1.dropna()
		df1=df1.sort_values(by=y1,ascending=False)
		dfmax=df1.head(n)
		fig=px.bar(dfmax,x='Country Name',y=y1,color="Country Name")
		fig.update_layout(
			xaxis_title="Year",
      		yaxis_title="Expenses(LCU)",
      		title="World development index of first "+n1+" Countries with maximum Expenses(LCU) in "+y1,
      		title_font=dict(family="Algerian",size=35,color="#149414"),
      		paper_bgcolor="#181818",
      		plot_bgcolor="#202020",
      		title_x=0.45,
      		height=700,
      		width=1500,
      		font=dict(family="Comic Sans MS",size=18,color="#649568")
      		)
		graph=fig.to_html
		return render(request,"md34result.html",{"graph":graph})
	else:
		data=pd.read_csv("World developement index.csv")
		number={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
		return render(request,"md34.html",{"data":number})

#Three Countries with given Year Range

def md35(request):
	if request.method=="POST":
		c1=request.POST.get('country')
		sy=int(request.POST.get('syear'))
		print(sy)
		ey=int(request.POST.get('eyear'))
		print(ey)
		df=pd.read_csv(r"World developement index.csv")
		df=df.transpose()
		df.columns= df.iloc[0,:]
		df = df.iloc[4:,:]
		df=df.astype(float)
		df=df.reset_index()
		print(df)
		df.rename(columns={'index':'Year'}, inplace=True)
		print(df)
		df['Year']=df['Year'].astype(int)
		df1=df[(df["Year"]>sy) & (df["Year"]<ey)]
		df1=df1.loc[:,['Year',c1]]
		print(df1)
		df1=df1.dropna()
		fig=px.scatter(df1,x="Year",y=c1,size=c1,size_max=50,color=c1)
		fig.update_layout(
			xaxis_type="category",
			xaxis_title="Year",
      		yaxis_title="Expenses(LCU)",
      		title="World development index of " +" "	+c1,
      		title_font=dict(family="Algerian",size=35,color="#149414"),
      		paper_bgcolor="#181818",
      		plot_bgcolor="#202020",
      		title_x=0.45,
      		height=700,
      		width=1500,
      		font=dict(family="Comic Sans MS",size=18,color="#649568")
      		)
		graph=fig.to_html
		return render(request,"md35result.html",{"graph":graph})
	else:
		df=pd.read_csv("World developement index.csv")
		column=df["Country Name"].drop_duplicates().tolist()
		return render(request,"md35.html",{"data":column})

def md36(request):
	if request.method=="POST":
		c1=request.POST.get('country')
		c2=request.POST.get('country1')
		c3=request.POST.get('country2')
		sy=int(request.POST.get('syear'))
		ey=int(request.POST.get('eyear'))
		df=pd.read_csv(r"World developement index.csv")
		df=df.transpose()
		df.columns= df.iloc[0,:]
		df = df.iloc[4:,:]
		df=df.astype(float)
		df=df.reset_index()
		df.rename(columns={'index':'Year'}, inplace=True)
		df['Year']=df['Year'].astype(int)
		df1=df[(df["Year"]>sy) & (df["Year"]<ey)]
		df11=df1.loc[:,['Year',c1]]
		df2=df1.loc[:,['Year',c2]]
		df3=df1.loc[:,['Year',c3]]
		df11=df1.dropna()
		df2=df2.dropna()
		df3=df3.dropna()
		fig=go.Figure()
		fig.add_traces(go.Scatter(x=df11["Year"],y=df11[c1], mode="lines+markers",name=c1,marker=dict(symbol="square",size=10,line=dict(width=2,
                                        color='white'))))
		fig.add_traces(go.Scatter(x=df2["Year"],y=df2[c2], mode="lines+markers",name=c2,marker=dict(symbol="circle",size=10,line=dict(width=2,
                                        color='white'))))
		fig.add_traces(go.Scatter(x=df3["Year"],y=df3[c3], mode="lines+markers",name=c3,marker=dict(symbol="star",size=10,line=dict(width=2,
                                        color='white'))))
		fig.update_layout(
				xaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Expenses(LCU)",
      			title="World development index of" +" "	+c1+", "+c2+", "+c3,
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",	
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
      			)
		graph=fig.to_html
		return render(request,"md36result.html",{"graph":graph})
	else:
		df=pd.read_csv("World developement index.csv")
		column=df["Country Name"].drop_duplicates().tolist()
		return render(request,"md36.html",{"data":column})

def heading4(request):
	return render(request,"heading4.html")

#Prediction works begins here //////////

def jobprediction(request):
	if request.method=="POST":
		
		df = pd.read_csv('share A.I job-postings (1).csv',parse_dates=['Year'])
		country=request.POST.get('entity')
		ai_job_postings = df.loc[df['Entity']==country]

		ai_job_postings=ai_job_postings.loc[:,['Year','ai_job_postings']]
		ai_job_postings['Year']= pd.to_datetime(ai_job_postings['Year'])
		ai_job_postings = ai_job_postings.sort_values('Year')
		ai_job_postings.isnull().sum()

		ai_job_postings = ai_job_postings.set_index('Year')
		ai_job_postings.index
# Split data into train and test sets
		train_data = ai_job_postings.iloc[:7]
		test_data = ai_job_postings.iloc[7:]

# Use auto_arima to find best p,d,q values
		auto_model = auto_arima(train_data, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True)
		print(auto_model.summary())

# Define ARIMA model with best p,d,q values
		model = ARIMA(ai_job_postings, order=auto_model.order)

# Fit model to training data
		model_fit = model.fit()
		steps = int(request.POST.get('n'))
		predictions = model_fit.forecast(steps=steps)


# Create traces
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=train_data.index, y=train_data['ai_job_postings'],mode='lines+markers',name='Actual',marker=dict(symbol="circle",size=10,line=dict(width=3,
                                        color='white'))))
		fig.add_trace(go.Scatter(x=predictions.index, y=predictions,mode='lines+markers',name='Predicted',marker=dict(symbol="star",size=10,line=dict(width=2,
                                        color='white'))))
		fig.update_layout(
				xaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Expenses(LCU)",
      			title="forecast of NO. of AI jobs over the coming years",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",	
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
      			)
		graph=fig.to_html()
		return render(request, 'jobprediction_result.html',{'graph':graph})
	else:
		data=pd.read_csv(r"share A.I job-postings (1).csv")
		column3=data["Entity"].drop_duplicates().tolist()
		return render(request, 'jobprediction.html',{"data":column3})

def cumulatativebillsprediction(request):
	if request.method=="POST":
		df = pd.read_csv('cumulative-numberof A.I bills-passed.csv',parse_dates=['Year'])
		country=request.POST.get('entity')
		df1 = df.loc[df['Entity']==country]

		df1=df1.loc[:,['Year','number_ai_bills_cumulative']]
		df1['Year']= pd.to_datetime(df1['Year'])
		df1=df1.sort_values('Year')
		df1.isnull().sum()

		df1 = df1.set_index('Year')
		df1.index
# Split data into train and test sets
		train_data = df1.iloc[:7]
		test_data = df1.iloc[7:]

# Use auto_arima to find best p,d,q values
		auto_model = auto_arima(train_data, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True)
		print(auto_model.summary())

# Define ARIMA model with best p,d,q values
		model = ARIMA(df1, order=auto_model.order)

# Fit model to training data
		model_fit = model.fit()
		steps = int(request.POST.get('n'))
		predictions = model_fit.forecast(steps=steps)


# Create traces
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=train_data.index, y=train_data['number_ai_bills_cumulative'],mode='lines',name='Actual',marker=dict(symbol="circle",size=10,line=dict(width=2,
                                        color='white'))))
		fig.add_trace(go.Scatter(x=predictions.index, y=predictions,mode='lines+markers',name='Predicted',marker=dict(symbol="star",size=10,line=dict(width=2,
                                        color='white'))))
		fig.update_layout(
				xaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Expenses(LCU)",
      			title="forecast of NO. of AI bills passed over the coming years",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",	
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
      			)
		graph=fig.to_html()
		return render(request, 'cumulatativebillsprediction_result.html',{'graph':graph})
	else:
		data=pd.read_csv(r"cumulative-numberof A.I bills-passed.csv")
		column3=data["Entity"].drop_duplicates().tolist()
		return render(request, 'cumulatativebillsprediction.html',{"data":column3})

def newlyfundedAIcompanies(request):
	if request.method=="POST":
		df = pd.read_csv('Annual Number of newly funded A.I companies.csv',parse_dates=['Year'])
		country=request.POST.get('entity')
		df1 = df.loc[df['Entity']==country]

		df1=df1.loc[:,['Year','newly_funded_ai_companies']]
		df1['Year']= pd.to_datetime(df1['Year'])
		df1=df1.sort_values('Year')
		df1.isnull().sum()

		df1 = df1.set_index('Year')
		df1.index
# Split data into train and test sets
		train_data = df1.iloc[:7]
		test_data = df1.iloc[7:]

# Use auto_arima to find best p,d,q values
		auto_model = auto_arima(train_data, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True)
		print(auto_model.summary())

# Define ARIMA model with best p,d,q values
		model = ARIMA(df1, order=auto_model.order)

# Fit model to training data
		model_fit = model.fit()
		steps = int(request.POST.get('n'))
		predictions = model_fit.forecast(steps=steps)


# Create traces
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=train_data.index, y=train_data['newly_funded_ai_companies'],mode='lines+markers',name='Actual',marker=dict(symbol="circle",size=10,line=dict(width=3,
                                        color='white'))))
		fig.add_trace(go.Scatter(x=predictions.index, y=predictions,mode='lines+markers',name='Predicted',marker=dict(symbol="star",size=10,line=dict(width=2,
                                        color='white'))))
		fig.update_layout(
				xaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Expenses(LCU)",
      			title="forecast of NO. of newly funded AI company over the coming years",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",	
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
      			)
		graph=fig.to_html()
		return render(request, 'newlyfundedAIcompanies_result.html',{'graph':graph})
	else:
		data=pd.read_csv(r"Annual Number of newly funded A.I companies.csv")
		column3=data["Entity"].drop_duplicates().tolist()
		return render(request, 'newlyfundedAIcompanies.html',{"data":column3})

def expenseprediction(request):
	if request.method=="POST":
		df= pd.read_csv('World developement index.csv')
		df=df.transpose()
		print(df)
		df.columns=df.iloc[0,:]
		df.columns
		df=df.iloc[4:,:]
		print("after filtering",df)
		c=dict.fromkeys(df.columns,float)
		print(c)
		df=df.astype(c)
		print("df before reset index",df)
		df=df.reset_index()
		print("after reset index",df)
		df.columns
		df.rename(columns={"index":"Year"},inplace=True)
		print(df)
		country=request.POST.get('country')
		print("country",country)
		CountryName=df.loc[:,['Year', country]]
		CountryName['Year']= pd.to_datetime(CountryName['Year'])
		CountryName = CountryName.sort_values('Year')
		CountryName.isnull().sum()
		CountryName= CountryName.set_index('Year')
		CountryName.index
		# Split data into train and test sets
		train_data = CountryName.iloc[:7]
		test_data = CountryName.iloc[7:]

		# Use auto_arima to find best p,d,q values
		auto_model = auto_arima(train_data, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True)
		print(auto_model.summary())

		# Define ARIMA model with best p,d,q values
		model = ARIMA(CountryName, order=auto_model.order)

		# Fit model to training data
		model_fit = model.fit()
		steps = int(request.POST.get('n'))
		predictions = model_fit.forecast(steps=steps)
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=CountryName.index, y=CountryName[country],
		mode='lines+markers',name='Actual values',marker=dict(symbol="circle",size=10,line=dict(width=2,
                                        color='white'))))

		fig.add_trace(go.Scatter(x=predictions.index, y=predictions,
		mode='lines+markers',name='Predicted',marker=dict(symbol="star",size=10,line=dict(width=2,
                                        color='white'))))

		fig.update_layout(
				xaxis_type="category",
      			xaxis_title="Year",
      			yaxis_title="Expenses(LCU)",
      			title="forecast of world developement index over the coming years",
      			title_font=dict(family="Algerian",size=35,color="#149414"),
      			paper_bgcolor="#181818",
      			plot_bgcolor="#202020",	
      			title_x=0.45,
      			height=700,
      			width=1500,
      			font=dict(family="Comic Sans MS",size=18,color="#649568")
      			)
		graph=fig.to_html()
		return render(request, 'expenseprediction_result.html',{'graph':graph})
	else:
		data=pd.read_csv(r"World developement index.csv")
		column3=data["Country Name"].drop_duplicates().tolist()
		return render(request, 'expenseprediction.html',{"data":column3})



#Normal web pages work begins here ////////

def login(request):
	if request.method=="POST":
		e=request.POST.get('em')
		p=request.POST.get('pw')
		res=userregister.objects.filter(email=e, password=p)

		if len(res)>0:
			request.session['email']=e
			msg="Welcome!!!"
			return render(request,'sidebar.html',{})
		else:
			msg="Invalid Login"
			return render(request,'login.html',{"msg":msg})
	else:
		return render(request,'login.html')

def logout(request):
	if not request.session.has_key('email'):
		return redirect("/login")
	del request.session['email']
	return redirect('/login')

def base(request):
	return render(request,'base.html')

def nav(request):
	return render(request,'NAV.html')

def footer(request):
	return render(request,'footer.html')

def allfaq(request):
	res=faq.objects.all()
	return render(request,'allfaq.html',{'data':res})	

def allvideo(request):
	if request.method=="POST":
		x=request.POST.get('se')
		res=article.objects.filter(Q(title__icontains=x))
		return render(request,'allvideos.html',{'data':res})
	else:
		res=video.objects.all()
		return render(request,'allvideos.html',{'data':res})

def contact(request):
	if request.method=="POST":
		ho=contactus()
		ho.Name=request.POST.get('nm')
		ho.email_id=request.POST.get('em')
		ho.subject=request.POST.get('sub')
		ho.message=request.POST.get('msg')
		ho.save()
		return render(request,'contactus.html',{'msg':"data successfully added"})
	else:
		return render(request,'contactus.html')

def register(request):
	if request.method=="POST":
		n=request.POST.get('nm')
		e=request.POST.get('em')
		p=request.POST.get('pw')
		c=request.POST.get('cpw')
		if userregister.objects.filter(email=e).exists():
			msg="Email Id is already registered"
			return render(request,'register.html',{'msg':msg})
		else:
			if p==c:	
				length=4
				otp=''.join(str(random.randint(0,9)) for _ in range(length))
				print("Your OTP is:",otp)
				subject="OTP"
				message="Welcome to AI Imapct Analysis....Your OTP is " + otp
				email_from=settings.EMAIL_HOST_USER
				recipient_list=[e,]
				send_mail(subject,message,email_from,recipient_list)
				rest="Your OTP is sent to your registered email account, Please check your Email Account,"
				return render(request,'register1.html',{'rest':rest,'otp':otp,'name':n,'email':e,'password':p})
			else:
				msg="password and c-pass doesnot match"
				return render(request,'register1.html',{'msg':msg})
			

	else:
		return render(request,'register.html')

def register1(request):
	if request.method=="POST":
		n=request.POST.get('nm')
		e=request.POST.get('em')
		p=request.POST.get('pw')
		otp=request.POST.get('otp')
		otp1=request.POST.get('otp1')
		if userregister.objects.filter(email=e).exists():
			msg="Email Id is already registered"
			return render(request,'register.html',{'msg':msg})
		else:
			if otp1==otp:	
				x=userregister()
				x.name=n
				x.email=e
				x.password=p
				x.save()
				msg="user successfully registered "
				return render(request,'register.html',{'msg':msg})
			else:
				return render(request,'register.html',{'msg':"otp does not match"})
			
def change(request):

	if request.method=="POST":
		re=userregister.objects.get(email=request.session['email'])
		opassword=request.POST.get('old')
		npassword=request.POST.get('new')
		cpassword=request.POST.get('cpass')

		if(npassword==cpassword):	
			pa=re.password
			print(pa)
			if(opassword==pa):
				re.password=npassword
				re.save()
				rest="Password Changed"
				return render(request,'changepassword.html',{'rest':rest})
			else:
				res="Invalid current Password"
				return render(request,'changepassword.html',{'res':res})
		else:
			res="Confirm password and new password don't match"
			return render(request,'changepassword.html',{'res':res})
	else:
		return render(request,'changepassword.html')

def reviews(request):

	if request.method=="POST":
		re=review()
		re.name=request.POST.get('nm')
		re.message=request.POST.get('msg')
		re.save()

	else:
		return render(request,'review.html')

def forget(request):
    if (request.method=='POST'):
        em=request.POST.get('em')
        user=userregister.objects.filter(email=em)
        if(len(user)>0):		
            pw=user[0].password
            subject="password"
            message="Welcome to AI impact Analysis and , Your password is "+pw
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[em,]
            send_mail(subject,message,email_from,recipient_list)
            rest="Your password sent to your respective Email Account, Please Check."
            return render(request,'forgetpassword.html',{'rest':rest})
        else:
            rest="This email id is not registered"
            return render(request,'forgetpassword.html',{'rest':rest})
    else:
        return render(request,'forgetpassword.html')

def allarticle(request):
	if request.method=="POST":
		x=request.POST.get('se')
		res=article.objects.filter(Q(title__icontains=x))
		return render(request,'allarticle.html',{'data':res})
	else:
		res=article.objects.all()
		return render(request,'allarticle.html',{'data':res})

def livenews(request):
	import datetime
	import json
	from datetime import date
	from newsapi.newsapi_client import NewsApiClient
	newsapi = NewsApiClient(api_key='60fabd41f3dc4a5d9af3a64b0e312efc')
	json_data = newsapi.get_everything(q='Artificial Intelligence', language="en", 
		from_param=str(date.today()-datetime.timedelta(days=29)),to=str(date.today()),page_size=24, page=2, sort_by='relevancy')
	k=json_data['articles']
	return render(request,'livenews.html',{"k":k})

def jobsearching(request):
	res=jobsearch.objects.all()
	return render(request,"jobsearching.html",{"res":res})

def detailarticle(request,id):
	x=article.objects.get(id=id)
	return render(request,'detailedarticle.html',{"i":x})

def allinitiative(request):
	res=initiative.objects.all()
	return render(request,'allinitiative.html',{'data':res})

def helpandsupport(request):
	if request.method=="POST":
		ho=helpnsupport()
		ho.Name=request.POST.get('nm')
		ho.email_id=request.POST.get('em')
		ho.message=request.POST.get('msg')
		ho.save()
		return render(request,'helpandsupport.html',{'msg':"data successfully added"})
	else:
		return render(request,'helpandsupport.html')
def sidebar(request):
	return render(request,'sidebar.html')

def profile(request):
	re=userregister.objects.get(email=request.session['email'])
	if request.method=="POST":
		print("yes")
		if 'image' in request.FILES:
			re.image=request.FILES['image']
		else:
			nothing="nothing"
		re.save()
		return render(request,'profile.html',{'user':re,'msg':'success'})
	else:
		return render(request,'profile.html',{'user':re})
			
	return render(request,'profile.html',{'user':re})

def editprofile(request):
	re=userregister.objects.get(email=request.session['email'])	
	if request.method=="POST":
		re.name=request.POST.get("nm")
		re.dob=request.POST.get("dob")
		re.email=request.POST.get("em")
		re.phone=request.POST.get("ph")
		re.Github=request.POST.get("git")
		re.linkedIn=request.POST.get("link")
		re.Facebook=request.POST.get("face")
		re.save()
		return redirect("/profile")
	return render(request,'editprofile.html',{'user':re})

def indexpage(request):
	vi=video.objects.all()
	ar=article.objects.all()
	fq=faq.objects.all()
	return render(request,'index.html',{'vi':vi,'ar':ar,'fq':fq})

def aboutus(request):
	return render(request,'aboutus.html')

def dashboard(request):
	return render(request,'dashboard.html')
import json
def get_bot_response1(user_message):
    import google.generativeai as genai
    genai.configure(api_key="AIzaSyA8pw1IsJb1R3JrosYMbi-pAbW47hvS5Dc")
    # Set up the model
    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
    {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

    convo = model.start_chat()
    convo.send_message(user_message)
    answer=convo.last.text
    return answer

    # If no matching question is found, use a default response
    # return "I'm sorry, I don't understand that question."
def chat(request):
    if request.method == 'POST':
        # Parse the JSON content from the request body
        data = json.loads(request.body.decode('utf-8'))
       
        # Access the 'user_input' key from the JSON data
        user_message = data.get('message', '')
       
        # Now you can use user_message in your logic
        print("User Message:", user_message)
       
        #Get bot response based on user input
        bot_response = get_bot_response1(user_message)

        # Save user message to the database
        ChatMessage.objects.create(user='User', message=user_message)
        # Save bot response to the database
        ChatMessage.objects.create(user='Bot', message=bot_response)
        #bot_response=""
        return JsonResponse({'response': bot_response})
   
    messages = ChatMessage.objects.all()
    return render(request, 'chat.html', {'messages': messages})

def aitools(request):
	obj=category.objects.all()
	return render(request,'aitools.html',{'obj':obj})

def detailedaitools(request, name):
	obj=structure.objects.filter(category_name=name)
	return render(request,'detailedaitools.html',{'obj':obj})

def maps(request):
	return render(request,'maps.html')