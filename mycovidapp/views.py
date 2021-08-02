from django.shortcuts import render
import requests
import json


url = "https://sheetdb.io/api/v1/5s7icoj7ea81q"



response = requests.get(url).json()


 

# Create your views here.
def hello(request):
     data=len(response)
     country=[]
    
     for i in range(4,data):
        
        country.append(response[i]['Country'])







     if request.method=="POST":
         selectcountry = request.POST['selectcountry']
         data=len(response)

         for i in range(4,data):
            if selectcountry== response[i]['Country']:
                  ActiveCases=(response[i]["ActiveCases"])
                  NewCases=(response[i]["NewCases"])
                  TotalCases=(response[i]["TotalCases"])
                  NewDeaths=(response[i]["NewDeaths"])
                  TotalDeaths=(response[i]["TotalDeaths"])
                  NewRecovered=(response[i]["NewRecovered"])
                  TotalRecovered=(response[i]["TotalRecovered"])

         context = { "selectcountry" : selectcountry, "country" : country,  "ActiveCases" : ActiveCases, "NewCases" : NewCases, "TotalCases" : TotalCases, "NewDeaths" : NewDeaths, "TotalDeaths" : TotalDeaths, "NewRecovered" : NewRecovered, "TotalRecovered" : TotalRecovered }
         return render(request,'mycovidapp/index.html',context)  

                 
        
            

 


    
    
    
     data=len(response)
     country=[]
    
     for i in range(4,data):
        
        country.append(response[i]['Country'])
     context={"country" : country}    
     return render(request,'mycovidapp/index.html',context)
  




