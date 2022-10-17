from curses.textpad import Textbox
import requests
import tkinter
import tkinter.messagebox
import customtkinter

from part1 import wiki_repseonse 


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("550x580")
app.title("CustomTkinter simple_example.py")

text = "?"

def button_callback():
    wiki = entry_1.get()
    wiki_repseonse(wiki)
    entry_1.delete(0, tkinter.END)
    wiki = get_wiki(wiki)
   # set_text(wiki)
    

def set_text(wiki):
    title = wiki['Title']
    title_count = wiki['Title_Count']
    text_var = (f"{title} name dropes it's self {title_count} times.")
    label_2.config(text = text_var)

    


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1,text="Wiki Obsession", justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)

label_3 = customtkinter.CTkLabel(master=frame_1,text="Which topic name drops it's self the most in the wikipedia intro", justify=tkinter.LEFT)
label_3.pack(pady=12, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Select Topic")
entry_1.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
button_1.pack(pady=12, padx=10)

label_2 = customtkinter.CTkLabel(master=frame_1,text="?", justify=tkinter.LEFT)
label_2.pack(pady=12, padx=10)




def get_wiki(value):
    URL = "http://127.0.0.1:8000/wiki/titles/" + str(value)
    PARAMS = {"WikiTitle": value}
    response = requests.get(url = URL, params = PARAMS)
    info = response.json()
    print(info)
    return info



app.mainloop()




