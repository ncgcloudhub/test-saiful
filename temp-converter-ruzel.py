## Today is Saturday
# this is a pythong script which will create a temperate app to conver from C <> F

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # You'll need to install the Pillow library

# Function to convert temperature
def convert_temperature():
    try:
        temperature = float(entry.get())
        if unit_var.get() == "Celsius to Fahrenheit":
            result = (temperature * 9/5) + 32
            result_unit.set("Fahrenheit")
        else:
            result = (temperature - 32) * 5/9
            result_unit.set("Celsius")
        result_label.config(text=f"Result: {result:.2f} °{result_unit.get()}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

app = tk.Tk()
app.title("Ruz_Temp - Temperature Converter")
app.geometry("400x300")  # Set the window size

# Load and display the thermometer image
# Replace 'thermometer.png' with the path to your thermometer image
thermometer_image = Image.open("thermometer.png")
thermometer_image = ImageTk.PhotoImage(thermometer_image)
thermometer_label = tk.Label(app, image=thermometer_image, borderwidth=0)
thermometer_label.place(x=20, y=10)

frame = tk.Frame(app, bg="black")  # Set the background color to black
frame.place(x=150, y=10)

label = tk.Label(frame, text="Enter Temperature:", fg="white", bg="black")  # Set text and text color
label.pack()

entry = tk.Entry(frame)
entry.pack()

unit_var = tk.StringVar()
unit_var.set("Celsius to Fahrenheit")
unit_menu = ttk.Combobox(frame, textvariable=unit_var, values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
unit_menu.pack()

convert_button = tk.Button(frame, text="Convert", command=convert_temperature, bg="green", fg="white")
convert_button.pack()

result_label = tk.Label(frame, text="Result:", font=("Arial", 12), fg="blue", bg="black")
result_label.pack()

result_unit = tk.StringVar()

app.mainloop()
