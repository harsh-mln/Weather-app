import tkinter as tk
import requests

# Your OpenWeatherMap API key
API_key = "f6a70e2ae49a61f0ee8db013ed011927"

def data():
    city_name = e.get()
    ws = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&APPID={API_key}")

    if ws.json()['cod'] == '404':
        n0.config(text="ERROR 404\nCity name not found")
        n1.config(text="")
        n2.config(text="")
        n3.config(text="")
        n4.config(text="")
        n5.config(text="")
        n6.config(text="")
        n7.config(text="")
    else:
        n0.config(text="")
        n1.config(text=f"City Name: {city_name}")
        country = ws.json()['sys']['country']
        n2.config(text=f"City is in: {country}")
        weather = ws.json()['weather'][0]['main']
        n3.config(text=f"Weather: {weather}")
        temp = ws.json()['main']['temp']
        n4.config(text=f"Temperature: {temp} °F")
        pressure = ws.json()['main']['pressure']
        n5.config(text=f"Pressure: {pressure} mb")
        humidity = ws.json()['main']['humidity']
        n6.config(text=f"Humidity: {humidity}%")
        speed = ws.json()['wind']['speed']
        n7.config(text=f"Wind speed: {speed} m/s")

root = tk.Tk()
root.title("Weather App")
root.geometry("330x330")

l = tk.Label(root, text="City Name")
l.pack(pady=5)

e = tk.Entry(root)
e.pack(pady=5)

b = tk.Button(root, text="Submit", command=data)
b.pack(pady=10)

n0 = tk.Label(root, text="", fg="red")
n0.pack()
n1 = tk.Label(root, text="")
n1.pack()
n2 = tk.Label(root, text="")
n2.pack()
n3 = tk.Label(root, text="")
n3.pack()
n4 = tk.Label(root, text="")
n4.pack()
n5 = tk.Label(root, text="")
n5.pack()
n6 = tk.Label(root, text="")
n6.pack()
n7 = tk.Label(root, text="")
n7.pack()

root.mainloop()
