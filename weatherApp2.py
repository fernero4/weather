from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

rutaImagen = "C:/Users/ferna/Downloads/python/clima/Images/"

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# funtions


def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
            city+"&appid=2f18cebac7921bdde8279189a7f39841"
        json_data = requests.get(api).json()

        # data
        desc = json_data['weather'][0]['main']
        temp_data = int(json_data['main']['temp']-273.15)
        press = json_data['main']['pressure']
        humid = json_data['main']['humidity']
        wind_data = json_data['wind']['speed']

        # place data
        temp_title.config(text=(temp_data, "°"))

        wind.config(text=wind_data)
        humidity.config(text=humid)
        description.config(text=desc)
        pressure.config(text=press)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!")


# search box
search_image = PhotoImage(file=rutaImagen+"blackBox.png")
my_image = Label(image=search_image)
my_image.place(x=20, y=20)

# text
textfield = tk.Entry(root, justify="center", width=17, font=(
    "poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=30)
textfield.focus()

# logo
Logo_image = PhotoImage(file=rutaImagen+"logo.png")
my_image_icon = Label(image=Logo_image)
my_image_icon.place(x=150, y=100)


# Buttom
search_icon = PhotoImage(file=rutaImagen+"search_icon.png")
my_icon = Button(image=search_icon, borderwidth=0,
                 cursor="hand2", bg="#404040", command=getWeather)
my_icon.place(x=400, y=34)

# time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)


# box
box_image = PhotoImage(file=rutaImagen+"box.png")
frame_image = Label(image=box_image)
frame_image.pack(padx=5, pady=5, side=BOTTOM)

# labels
wind_title = Label(root, text="Wind", font=(
    "Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
wind_title.place(x=120, y=400)

humidity_title = Label(root, text="Humidity", font=(
    "Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
humidity_title.place(x=250, y=400)

description_title = Label(root, text="Description", font=(
    "Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
description_title.place(x=430, y=400)

pressure_title = Label(root, text="Pressure", font=(
    "Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
pressure_title.place(x=650, y=400)


temp_title = Label(font=("arial", 70, "bold"), fg="#ee666d")
temp_title.place(x=400, y=150)

wind = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
wind.place(x=120, y=430)

humidity = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
humidity.place(x=280, y=430)

description = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
description.place(x=450, y=430)

pressure = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
pressure.place(x=670, y=430)


root.mainloop()