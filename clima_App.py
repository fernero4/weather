from tkinter import *
import requests
#2f18cebac7921bdde8279189a7f39841
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def mostrar_respuesta(clima):
    try:
        nombre_ciudad=clima["name"]
        desc=clima["weather"][0]["description"]
        temp=clima["main"]["temp"]
        mostrar_ciudad["text"] = nombre_ciudad
        mostrar_temp["text"] = str(int(temp)) + "°C"
        mostrar_desc["text"] = desc

    except:
        mostrar_ciudad["text"]="intenta nuevamente"
        mostrar_temp["text"] = ""
        mostrar_desc["text"] = ""

def conexion_API_clima(ciudad):
    try:
        API_KEY="2f18cebac7921bdde8279189a7f39841"
        URL="https://api.openweathermap.org/data/2.5/weather"
        parametros={"appid" : API_KEY, "q": ciudad, "units": "metric", "lang":"es"}
        response= requests.get(URL, params=parametros)
        clima=response.json()
        mostrar_respuesta(clima)

    except:
        print("La ciudad que escribio esta mal escrita o no existe")
    


ventana = Tk()
ventana.geometry("350x550")

texto_ciudad = Entry(ventana, font = ("Courier", 20, "normal"), justify = "center")
texto_ciudad.pack(padx= 30, pady= 30)

obtener_clima=Button(ventana, text="Obtener clima", font = ("Courier", 20, "normal"),
                      command=lambda:conexion_API_clima(texto_ciudad.get()))
obtener_clima.pack()

mostrar_ciudad=Label(font=("Courier", 20, "normal"))
mostrar_ciudad.pack(padx=20, pady=20)

mostrar_temp=Label(font=("Courier", 50, "normal"))
mostrar_temp.pack(padx=10, pady=10)

mostrar_desc=Label(font=("Courier", 20, "normal"))
mostrar_desc.pack(padx=10, pady=10)

ventana.mainloop()
