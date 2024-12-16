#JEZYK PYTHON
#GRUPA CWICZENIOWA 02
#Zadania z zajec z dnia 11.12.2024
#Autor: Szymon Szeliga


#Napisać program z GUI, który realizuje grę Papier-Kamień-Nożyce użytkownika z komputerem.
#Wybór komputera jest losowany.
#Program może zawierać trzy przyciski dla każdego wyboru użytkownika (P, K, N)
#oraz etykietę wyświetlającą wybór człowieka, komputera i wynik gry.


import tkinter as tk
import random

def createWindow(rozmiar="800x600", tytul="Gra"):
    window = tk.Tk()
    window.geometry(rozmiar)
    window.title(tytul)
    return window

def createFrame(panelNadrzedny):
    frame = tk.Frame(panelNadrzedny)
    frame.pack(expand=True)
    return frame

def createLabel(panelNadrzedny, tekst="pusty tekst", font="Ariel 20" ):
    label = tk.Label(panelNadrzedny, text=tekst, font=font)
    return label

def createButton(panelNadrzedny, tekst="pusty tekst", font="Ariel 15", com=None):
    button = tk.Button(panelNadrzedny, text=tekst, font=font, command=com)
    return button

def wyborGracza(wybor):
    wybor_komputera = wyborKomputera()
    wynik = wynikGry(wybor, wybor_komputera)
    label_wynik.config(text=f"Wynik: {wynik}")
    label_wybor_komputera.config(text=f"Wybór komputera: {wybor_komputera}")
    label_twoj_wybor.config(text=f"Twój wybór: {wybor}")


def frameGry(frame):
    przycisk_papier = createButton(frame, "PAPIER", "Ariel 20", lambda: wyborGracza("P") )
    przycisk_kamien = createButton(frame, "KAMIEN", "Ariel 20", lambda: wyborGracza("K") )
    przycisk_nozyce = createButton(frame, "NOZYCE", "Ariel 20", lambda: wyborGracza("N") )

    global label_wynik
    label_wynik = createLabel(frame, "Wynik:", "Ariel 25")
    global label_wybor_komputera
    label_wybor_komputera = createLabel(frame, "Wybór komputera:", "Ariel 25")
    global label_twoj_wybor
    label_twoj_wybor = createLabel(frame, "Twój wybór:", "Ariel 25")

    label_wynik.pack(side=tk.TOP, pady=10, padx=10)
    label_wybor_komputera.pack(side=tk.TOP, pady=10, padx=10)
    label_twoj_wybor.pack(side=tk.TOP, pady=10, padx=10)

    przycisk_nozyce.pack(side=tk.LEFT, pady=10, padx=10)
    przycisk_kamien.pack(side=tk.LEFT, pady=10, padx=10)
    przycisk_papier.pack(side=tk.LEFT, pady=10, padx=10)


def deleteContentFrame(frame, frame_2) -> None:
    frame.pack_forget()
    frame_gry = createFrame(frame_2)
    frameGry(frame_gry)

def wyborKomputera() -> str:
    lista = ("P", "K", "N")
    wybor = random.choice(lista)
    return wybor

def wynikGry(wybor_gracza, wybor_komputera) -> str:
    wynik = ""
    if wybor_gracza == wybor_komputera:
        wynik = "REMIS"
    elif wybor_gracza == "P" and wybor_komputera == "K" or \
        wybor_gracza == "K" and wybor_komputera == "N" or \
        wybor_gracza == "N" and wybor_komputera == "P":
        wynik = "WYGRAŁEŚ"
    else:
        wynik = "PRZEGRAŁEŚ"
    return wynik



window = createWindow("1024x768", "Papier_Kamien_Nozyce")

frame_glowny = createFrame(window)
frame_startowy = createFrame(frame_glowny)

label_startowy = createLabel(frame_startowy, "Witaj, zagrajmy w papier kamien nozyce", "Ariel 25")
przycisk_startowy = createButton(frame_startowy, "START", "Ariel 20", lambda: deleteContentFrame(frame_startowy, frame_glowny))
label_startowy.pack()
przycisk_startowy.pack(pady=15)

window.mainloop()

