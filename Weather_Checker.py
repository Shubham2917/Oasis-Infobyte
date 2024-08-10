import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk

# Use your actual API key
API_KEY = '3dfd1cbc01b97b8035838a7a343092ef'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather():
    location = entry.get()
    if not location:
        messagebox.showerror("Error", "Please enter a location")
        return
    
    try:
        response = requests.get(f"{BASE_URL}?q={location}&appid={API_KEY}&units=metric")
        data = response.json()
        
        if data.get('cod') != 200:
            result_label.config(text=f"Error: {data.get('message')}")
        else:
            main = data['main']
            weather = data['weather'][0]
            temp = main['temp']
            humidity = main['humidity']
            description = weather['description']
            icon_code = weather['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
            icon_image = ImageTk.PhotoImage(Image.open(requests.get(icon_url, stream=True).raw))
            
            result_label.config(text=f"City: {data['name']}\nTemperature: {temp}°C\nHumidity: {humidity}%\nCondition: {description.capitalize()}")
            icon_label.config(image=icon_image)
            icon_label.image = icon_image  # keep a reference to the image
    except requests.exceptions.RequestException as e:
        result_label.config(text="Error: Unable to connect to the weather service.")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

app = tk.Tk()
app.title("Weather App")

entry_label = tk.Label(app, text="Enter location:")
entry_label.pack(padx=10, pady=5)

entry = tk.Entry(app, width=30)
entry.pack(padx=10, pady=5)

button = tk.Button(app, text="Get Weather", command=get_weather)
button.pack(pady=10)

result_label = tk.Label(app, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

icon_label = tk.Label(app)
icon_label.pack()

app.mainloop()
