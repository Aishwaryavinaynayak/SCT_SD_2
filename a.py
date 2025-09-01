import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        from_scale = combo_from.get()
        to_scale = combo_to.get()

        if from_scale == to_scale:
            result.set(f"{temp:.2f} {to_scale}")
            return

        # Convert input temperature to Celsius first
        if from_scale == "Celsius":
            celsius = temp
        elif from_scale == "Fahrenheit":
            celsius = (temp - 32) * 5/9
        elif from_scale == "Kelvin":
            celsius = temp - 273.15

        # Convert from Celsius to target scale
        if to_scale == "Celsius":
            converted = celsius
        elif to_scale == "Fahrenheit":
            converted = (celsius * 9/5) + 32
        elif to_scale == "Kelvin":
            converted = celsius + 273.15

        result.set(f"{converted:.2f} {to_scale}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x250")
root.resizable(False, False)

# Title Label
title = tk.Label(root, text="🌡 Temperature Converter", font=("Arial", 14, "bold"))
title.pack(pady=10)

# Input frame
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Enter Temperature:").grid(row=0, column=0, padx=5, pady=5)
entry_temp = tk.Entry(frame, width=10)
entry_temp.grid(row=0, column=1, padx=5, pady=5)

# Dropdowns
scales = ["Celsius", "Fahrenheit", "Kelvin"]

tk.Label(frame, text="From:").grid(row=1, column=0, padx=5, pady=5)
combo_from = ttk.Combobox(frame, values=scales, state="readonly", width=10)
combo_from.current(0)
combo_from.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="To:").grid(row=2, column=0, padx=5, pady=5)
combo_to = ttk.Combobox(frame, values=scales, state="readonly", width=10)
combo_to.current(1)
combo_to.grid(row=2, column=1, padx=5, pady=5)

# Convert button
btn_convert = tk.Button(root, text="Convert", command=convert_temperature, bg="#4CAF50", fg="white", width=15)
btn_convert.pack(pady=10)

# Result
result = tk.StringVar()
lbl_result = tk.Label(root, textvariable=result, font=("Arial", 12, "bold"))
lbl_result.pack(pady=5)

# Run application
root.mainloop()