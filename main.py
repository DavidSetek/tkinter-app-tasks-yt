from tkinter import *
import customtkinter

# Okno
window = customtkinter.CTk()
window.title("Seznam úkolů")
window.geometry("600x430")
window.iconbitmap("icon.ico")
window.resizable(False, False)

# Definujeme fonty a barvy
main_font = ("Times New Roman", 12)
main_color = "#dd7f00"
button_color = "#ffbe66"


# Funkce
def add_text():
    # přidání textového úkolu
    list_box.insert(END, user_input.get())
    user_input.delete(0, END)


def remove_text_item():
    # odstraní jednu položku seznamu
    list_box.delete(ANCHOR)


def clear_all_list():
    # odstraní všechny položky ze seznamu
    list_box.delete(0, END)


def save_tasks():
    # uloží úkoly do textového souboru
    with open("tasks.txt", "w") as file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                file.write(f"{one_task}")
            else:
                file.write(f"{one_task}\n")


def open_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for one_line in file:
                list_box.insert(END, one_line)
    except:
        print("Chyba ve funkci na otevírání souboru tasks.txt")


# Framy
input_frame = customtkinter.CTkFrame(window, bg=main_color)
text_frame = customtkinter.CTkFrame(window, bg=main_color)
button_frame = customtkinter.CTkFrame(window, bg=main_color)
input_frame.pack(pady=5)
text_frame.pack(pady=5)
button_frame.pack()

# Input frame - obsah
user_input = customtkinter.CTkEntry(input_frame, width=400, borderwidth=3)
user_input.grid(row=0, column=0, padx=5, pady=5)
add_button = customtkinter.CTkButton(input_frame, text="Přidat", borderwidth=2, bg=button_color, command=add_text)
add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=10)

# Scrollbar
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky=N+S)

# Text frame - obsah
list_box = Listbox(text_frame, height=15, width=70, borderwidth=3, font=main_font, yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0)
# Propojíme scrollbar s list_boxem
text_scrollbar.config(command=list_box.yview)

# Button frame - obsah
remove_button = customtkinter.CTkButton(button_frame, text="Odstranit položku", borderwidth=2, bg=button_color, command=remove_text_item)
clear_button = customtkinter.CTkButton(button_frame, text="Smazat seznam", borderwidth=2, bg=button_color, command=clear_all_list)
save_button = customtkinter.CTkButton(button_frame, text="Uložit", borderwidth=2, bg=button_color, command=save_tasks)
quit_button = customtkinter.CTkButton(button_frame, text="Zavřít", borderwidth=2, bg=button_color, command=window.destroy)

remove_button.grid(row=0, column=0, padx=2, pady=5)
clear_button.grid(row=0, column=1, padx=2, pady=5)
save_button.grid(row=0, column=2, padx=2, pady=5)
quit_button.grid(row=0, column=3, padx=2, pady=5)

# Výuková zóna
# try:
#     print(x)
# except:
#     print("Byla zjištěna chyba. Proměnná x neexistuje.")

# Načteme seznam úkolů do list_boxu
open_tasks()

# Hlavní cyklus
window.mainloop()
