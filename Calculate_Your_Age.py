import tkinter as tk
from datetime import datetime, timedelta


def calculate_age():
    """ Calculate age based on birth date """
    birth_date = birth_entry.get()
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    today = datetime.now()
    age = today.year - birth_date.year - \
        ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def calculate_months():
    """ Calculate age in months """
    age = calculate_age()
    months = age * 12
    return months


def calculate_days():
    """ Calculate age in days """
    birth_date = birth_entry.get()
    days = (datetime.now() - datetime.strptime(birth_date, '%Y-%m-%d')).days
    return days


def show_result():
    """ Display the age in a label """
    age = calculate_age()
    months = calculate_months()
    days = calculate_days()
    result_label.config(text=f"Age: {age} years, {months} months, {days} days")


# Create the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")
root.configure(bg="lightblue")

# Create labels and entry fields
name_label = tk.Label(root, text="Name:", bg="lightblue")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

birth_label = tk.Label(root, text="Birth Date (YYYY-MM-DD):", bg="lightblue")
birth_label.pack()
birth_entry = tk.Entry(root)
birth_entry.pack()

result_label = tk.Label(root, bg="lightblue")
result_label.pack()

# Create calculate button
calculate_button = tk.Button(
    root, text="Calculate", command=show_result, bg="blue", fg="white")
calculate_button.pack()

# Run the Tkinter event loop
root.mainloop()
