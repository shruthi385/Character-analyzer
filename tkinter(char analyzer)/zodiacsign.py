from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as mbox
import pyttsx3

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

def set_dob():
    if mbox.askokcancel("Reset", "Do you want to reset?"):
        name_var.set("")
        date_var.set(1)
        month_var.set(1)
        year_var.set("Non Leap")
        output_text.config(state=NORMAL)
        output_text.delete(1.0, END)
        output_text.config(state=DISABLED)

def analyze_personality():
    date = date_var.get()
    month = month_var.get()
    year = year_var.get()
    name = name_var.get()

    valid = True
    if (year == 'Leap'):
        if (month == 2 and date > 29) or (month in [4, 6, 9, 11] and date > 30):
            valid = False
    else:
        if (month == 2 and date > 28) or (month in [4, 6, 9, 11] and date > 30):
            valid = False

    if valid and name:
        zodiac_sign = get_zodiac_sign(month, date)
        personality_sentence = get_personality_sentence(zodiac_sign)
        display_output(name, zodiac_sign, personality_sentence)
        speak_output(name, zodiac_sign, personality_sentence)
    else:
        mbox.showerror("Error", "Please enter a valid name and D.O.B.")

def get_zodiac_sign(month, date):
    if month == 1:
        return 'Capricorn' if date < 20 else 'Aquarius'
    elif month == 2:
        return 'Aquarius' if date < 19 else 'Pisces'
    elif month == 3:
        return 'Pisces' if date < 21 else 'Aries'
    elif month == 4:
        return 'Aries' if date < 20 else 'Taurus'
    elif month == 5:
        return 'Taurus' if date < 21 else 'Gemini'
    elif month == 6:
        return 'Gemini' if date < 21 else 'Cancer'
    elif month == 7:
        return 'Cancer' if date < 23 else 'Leo'
    elif month == 8:
        return 'Leo' if date < 23 else 'Virgo'
    elif month == 9:
        return 'Virgo' if date < 23 else 'Libra'
    elif month == 10:
        return 'Libra' if date < 23 else 'Scorpio'
    elif month == 11:
        return 'Scorpio' if date < 22 else 'Sagittarius'
    else:
        return 'Sagittarius' if date < 22 else 'Capricorn'

def get_personality_sentence(zodiac_sign):
    personality_dict = {
        'Capricorn': "You are disciplined and responsible.",
        'Aquarius': "You are innovative and humanitarian.",
        'Pisces': "You are compassionate and artistic.",
        'Aries': "You are confident and courageous.",
        'Taurus': "You are reliable and patient.",
        'Gemini': "You are adaptable and outgoing.",
        'Cancer': "You are nurturing and intuitive.",
        'Leo': "You are generous and charismatic.",
        'Virgo': "You are practical and detail-oriented.",
        'Libra': "You are charming and diplomatic.",
        'Scorpio': "You are passionate and resourceful.",
        'Sagittarius': "You are adventurous and optimistic."
    }
    return personality_dict.get(zodiac_sign, "Invalid zodiac sign.")

def display_output(name, zodiac_sign, personality_sentence):
    output_text.config(state=NORMAL)
    output_text.delete(1.0, END)
    output_text.insert(END, f"Dear {name},\n\n")
    output_text.insert(END, f"Your zodiac sign is {zodiac_sign}.\n\n")
    output_text.insert(END, f"{personality_sentence}\n")
    output_text.config(state=DISABLED)

def speak_output(name, zodiac_sign, personality_sentence):
    text_to_speech = f"Dear {name}, Your zodiac sign is {zodiac_sign}. {personality_sentence}"
    engine = pyttsx3.init()
    engine.say(text_to_speech)
    engine.runAndWait()

# Main Window & Configuration
window = Tk()
window.title("SUN SIGN CHARACTER")
window.geometry('1000x700')

# Background Image
background_img = Image.open("black.jpg")
background_img = background_img.resize((1500, 1000), Image.ANTIALIAS)
background_img = ImageTk.PhotoImage(background_img)
background_label = Label(window, image=background_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title
Title = Label(window, text="SUN SIGN CHARACTER", font=("Script MT Bold", 30), bg="black", fg="white")
Title.place(relx=0.5, rely=0.09, anchor=CENTER)

# Logo Image
logo_img = Image.open("logo.jpg")
logo_img = logo_img.resize((200, 200), Image.ANTIALIAS)
logo_img = ImageTk.PhotoImage(logo_img)
logo_label = Label(window, image=logo_img, bg="white")
logo_label.place(relx=0.5, rely=0.3, anchor=CENTER)  # Adjusted rely value

# User Input
name_label = Label(window, text="Enter Your Name:", font=("Script MT Bold", 20), bg="white", fg="blue")
name_label.place(x=50, y=320)
name_var = StringVar()
name_entry = Entry(window, textvariable=name_var, font=("Arial", 15), bg="white", fg="blue", borderwidth=3, relief="solid")
name_entry.place(x=300, y=320)


date_label = Label(window, text="Select Date:", font=("Script MT Bold", 20), bg="white", fg="blue")
date_label.place(x=50, y=390)
date_var = IntVar()
date_combobox = ttk.Combobox(window, textvariable=date_var, font=("Arial", 15), state="readonly")
date_combobox['values'] = tuple(range(1, 32))
date_combobox.place(x=300, y=390)

month_label = Label(window, text="Select Month:", font=("Script MT Bold", 20), bg="white", fg="blue")
month_label.place(x=50, y=460)
month_var = IntVar()
month_combobox = ttk.Combobox(window, textvariable=month_var, font=("Arial", 15), state="readonly")
month_combobox['values'] = tuple(range(1, 13))
month_combobox.place(x=300, y=460)

year_label = Label(window, text="Select Year:", font=("Script MT Bold", 20), bg="white", fg="blue")
year_label.place(x=50, y=530)
year_var = StringVar()
year_combobox = ttk.Combobox(window, textvariable=year_var, font=("Arial", 15), state="readonly")
year_combobox['values'] = ('Non Leap', 'Leap')
year_combobox.place(x=300, y=530)

# Buttons
analyze_button = Button(window, text='ANALYZE', command=analyze_personality, font=("Courier New", 20,"bold"), bg="green", fg="black", relief="raised")
analyze_button.place(x=60, y=600)

reset_button = Button(window, text='RESET', command=set_dob, font=("Courier New", 20,"bold"), bg="blue", fg="black", relief="raised")
reset_button.place(x=280, y=600)

exit_button = Button(window, text='EXIT', command=exit_win, font=("Courier New", 20,"bold"), bg="red", fg="black", relief="raised")
exit_button.place(x=450, y=600)

# Output Textbox
output_text = Text(window, wrap=WORD, width=35, height=10, font=("Times New Roman", 15), bg="white", fg="blue", borderwidth=3, relief="solid")
output_text.place(x=600, y=420)

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
