from django.shortcuts import render,redirect
import pickle
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages
import requests
from . import models


with open('D:\Clg\EDI\RandomForest.pkl' , 'rb') as f:
    lr = pickle.load(f)

# Create your views here.
def main(request):
    return render(request,"main/index.html")

def home(request):
    return render(request,"main/home.html")

def login_user(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['polyID']
        user=authenticate(request,username=username,password=password)
        api_url = "https://api.thingspeak.com/channels/2092912/feeds.json?results=2"
        response = requests.get(api_url)
        x=response.json()
        temperature=x['feeds'][0]['field1']
        humidity=x['feeds'][0]['field2']
        rainfall=x['feeds'][0]['field3']
        if user is not None:
            login(request,user)
            print(user.username)
            request.session['user_id'] = user.username
            request.session['temperature'] = temperature
            request.session['humidity'] = humidity
            request.session['rainfall'] = rainfall
            return redirect('user')
        else:
            messages.success(request,("There was an error logging in!"))
            return redirect('login_user')
    else:
        return render(request,"authenticate/login.html",{})

def user(request):
    username = request.session.get('user_id')
    temperature=request.session.get('temperature')
    humidity = request.session.get('humidity')
    humidity=float(humidity)
    temperature=float(temperature)
    return render(request,"main/user.html",{'username':username, 'temperature':temperature,'humidity':humidity})

def predict(request):
    username = request.session.get('user_id')
    password = request.session.get('password')
    username = request.session.get('user_id')
    temperature=request.session.get('temperature')
    humidity = request.session.get('humidity')
    humidity=float(humidity)
    temperature=float(temperature)
    if request.method == 'POST':
        # Process form inputs here
        Nitrogen=request.POST.get('Nitrogen')
        Phosphorus=request.POST.get('Phosphorous')
        Pottasium=request.POST.get('Potassium')
        pH=request.POST.get('pH')
        rainfall=request.POST.get('rainfall')
        print(temperature)
        # Perform necessary actions with the input value
        # humidity temperature rainfall from thingspeak api
        result=lr.predict([[Nitrogen, Phosphorus, Pottasium, temperature, humidity, pH, rainfall]])
        reading = models.readings(temperature=temperature, humidity=humidity, rainfall=rainfall,
                           Nitrogen=Nitrogen, Phosphorus=Phosphorus, Potassium=Pottasium,
                           ph=pH, result=result)
        reading.save()
        all_readings = models.readings.objects.all()
        return render(request, 'main/predict.html', {'result': result[0],'username':username,'temperature':temperature,'humidity':humidity,'readings': all_readings})
    else:
        all_readings = models.readings.objects.all()
        # Handle GET requests or initial form rendering
        return render(request,"main/predict.html",{'username':username,'temperature':temperature,'humidity':humidity,'readings': all_readings})
    

def control(request):
    username = request.session.get('user_id')
    temperature=request.session.get('temperature')
    humidity = request.session.get('humidity')
    humidity=float(humidity)
    temperature=float(temperature)
    return render(request,"main/control.html",{'username':username, 'temperature':temperature,'humidity':humidity})

def crop(request):
    username = request.session.get('user_id')
    temperature=request.session.get('temperature')
    humidity = request.session.get('humidity')
    humidity=float(humidity)
    temperature=float(temperature)
    return render(request,"main/cropInfo1.html",{'username':username, 'temperature':temperature,'humidity':humidity})


def crop1(request):
    username = request.session.get('user_id')
    temperature=request.session.get('temperature')
    humidity = request.session.get('humidity')
    humidity=float(humidity)
    temperature=float(temperature)
    return render(request,"main/cropInfo1.html",{'username':username, 'temperature':temperature,'humidity':humidity})