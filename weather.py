from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root=Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

def getWeather():
    city=textField.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()

    result=obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)
    lat=location.latitude
    long=location.longitude
    long_lat.config(text=f"lat: {round(lat),4}° N, long: {round(long), 4} ° E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    API_KEY="2f18cebac7921bdde8279189a7f39841"
    URL="https://api.openweathermap.org/data/2.5/weather"
    parametros={"appid" : API_KEY, "q": city, "units": "metric", "lang":"es"}
    response= requests.get(URL, params=parametros)
    clima=response.json()

    #current
    humidity=clima['main']['humidity']
    pressure=clima['main']['pressure']
    wind=clima['wind']['speed']
    temp_max=clima['main']['temp_max']
    temp_min=clima['main']['temp_min']
    desc=clima["weather"][0]["description"]
    temp=clima["main"]["temp"]

    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=(desc))
    

    #first cell
    firstdayImage=clima['weather'][0]['icon']
    photo1=ImageTk.PhotoImage(file=f"C:/Users/ferna/Downloads/python/clima/icon/{firstdayImage}@2x.png")
    firstImage.config(image=photo1)
    firstImage.image=photo1

    day1temp.config(text=f"Max: {temp_max} °C\nMin: {temp_min} °C")


    #days
    first=datetime.now()
    day1.config(text=first.strftime("%A"))
    day1.place(x=210, y=20)


#icon
image_icon=PhotoImage(file="C:/Users/ferna/Downloads/python/clima/Images/logo.png")
root.iconphoto(False, image_icon)


Round_box=PhotoImage(file="C:/Users/ferna/Downloads/python/clima/Images/Rounded Rectangle 4.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=110)

#label
label1=Label(root, text="Temperature", font=('Helvetica', 12), fg="white", bg="#203243")
label1.place(x=50, y=125)

label2=Label(root, text="Humidity", font=('Helvetica', 12), fg="white", bg="#203243")
label2.place(x=50, y=150)

label3=Label(root, text="Pressure", font=('Helvetica', 12), fg="white", bg="#203243")
label3.place(x=50, y=175)

label4=Label(root, text="Wind Speed", font=('Helvetica', 12), fg="white", bg="#203243")
label4.place(x=50, y=200)

label5=Label(root, text="Description", font=('Helvetica', 12), fg="white", bg="#203243")
label5.place(x=50, y=225)


#search box
Search_image=PhotoImage(file="C:/Users/ferna/Downloads/python/clima/Images/Rounded Rectangle 3.png")
myImage=Label(image=Search_image, bg="#57adff")
myImage.place(x=270, y=120)

weat_image=PhotoImage(file="C:/Users/ferna/Downloads/python/clima/Images/Layer 7.png")
weatherImage=Label(root, image=weat_image, bg="#203243")
weatherImage.place(x=290, y=127)

textField=tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textField.place(x=370, y=130)
textField.focus()

Search_icon=PhotoImage(file="C:/Users/ferna/Downloads/python/clima/Images/Layer 6.png")
myImage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myImage_icon.place(x=645, y=125)

#Bottom box
frame=Frame(root, width=1200, height=180, bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox=PhotoImage(file="C:/Users/ferna/Downloads/python/clima/Images/Rounded Rectangle 2.png")
Label(frame, image=firstbox, bg="#212120").place(x=150, y=20)


#clock (place time)
clock=Label(root, font=("Helvetic", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=20)


#timezone
timezone=Label(root, font=("Helvetic", 20), fg="white", bg="#57adff")
timezone.place(x=500, y=20)

long_lat=Label(root, font=("Helvetic", 10), fg="white", bg="#57adff")
long_lat.place(x=500, y=50)

#thpwd
t=Label(root, font=("Helvetica", 12), fg="white", bg="#203243")
t.place(x=150,y=125)
h=Label(root, font=("Helvetica", 12), fg="white", bg="#203243")
h.place(x=150,y=150)
p=Label(root, font=("Helvetica", 12), fg="white", bg="#203243")
p.place(x=150,y=175)
w=Label(root, font=("Helvetica", 12), fg="white", bg="#203243")
w.place(x=150,y=200)
d=Label(root, font=("Helvetica", 12), fg="white", bg="#203243")
d.place(x=150,y=225)


#first cell
firstframe=Frame(root, width=550,height=132, bg="#282829")
firstframe.place(x=160,y=315)

day1=Label(firstframe, font="arial 30", bg="#282829", fg="#fff")
day1.place(x=120, y=5)

firstImage=Label(firstframe, bg="#282829")
firstImage.place(x=80, y=15)

day1temp=Label(firstframe, bg="#282829", fg="#57adff", font="arial 15 bold")
day1temp.place(x=210, y=72)


root.mainloop()