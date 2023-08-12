from tkinter import *
from model import *
from tkinter.ttk import *
import re

window = Tk()

window.title("Planning de la photocopieuse")

window.configure(bg='lightblue')

# Create model

create_train_model()

# Create an instance of a canvas
_canvas = Canvas(window, bg="lightblue", highlightthickness=0, height=750, width=1210)
_canvas.pack()

_canvas.create_text(400, 75, text="Planning Imprimante", fill="black", font=('Helvetica 32 bold underline'))

# create rectangle
_canvas.create_rectangle(10, 150, 100, 200,outline="black",fill="white")
_canvas.create_rectangle(10, 200, 100, 250,outline="black",fill="white")
_canvas.create_rectangle(10, 250, 100, 300,outline="black",fill="white")

_canvas.create_rectangle(10, 300, 100, 360,outline="black",fill="white")
_canvas.create_rectangle(10, 360, 100, 420,outline="black",fill="white")
_canvas.create_rectangle(10, 420, 100, 480,outline="black",fill="white")
_canvas.create_rectangle(10, 480, 100, 540,outline="black",fill="white")
_canvas.create_rectangle(10, 540, 100, 600,outline="black",fill="white")

_canvas.create_rectangle(10, 600, 100, 650,outline="black",fill="white")
_canvas.create_rectangle(10, 650, 100, 700,outline="black",fill="white")

_canvas.create_text(50, 225, text="06:00", fill="black", font=('Helvetica 15 bold'))
_canvas.create_text(50, 275, text="08:00", fill="black", font=('Helvetica 15 bold'))


_canvas.create_text(50, 330, text="10:00", fill="black", font=('Helvetica 15 bold'))
_canvas.create_text(50, 390, text="12:00", fill="black", font=('Helvetica 15 bold'))
_canvas.create_text(50, 450, text="14:00", fill="black", font=('Helvetica 15 bold'))
_canvas.create_text(50, 510, text="16:00", fill="black", font=('Helvetica 15 bold'))
_canvas.create_text(50, 570, text="18:00", fill="black", font=('Helvetica 15 bold'))

_canvas.create_text(50, 625, text="20:00", fill="black", font=('Helvetica 15 bold'))
_canvas.create_text(50, 675, text="22:00", fill="black", font=('Helvetica 15 bold'))


#rectangle lundi
_canvas.create_rectangle(100, 150, 200, 200,outline="black",fill="white")
_canvas.create_text(150, 175, text="Lundi", fill="black", font=('Helvetica 15 bold'))
_canvas.create_rectangle(100, 200, 200, 250,outline="black",fill="red")
_canvas.create_rectangle(100, 250, 200, 300,outline="black",fill="red")

_canvas.create_rectangle(100, 300, 200, 360,outline="black",fill="white")
_canvas.create_rectangle(100, 360, 200, 420,outline="black",fill="white")
_canvas.create_rectangle(100, 420, 200, 480,outline="black",fill="white")
_canvas.create_rectangle(100, 480, 200, 540,outline="black",fill="white")
_canvas.create_rectangle(100, 540, 200, 600,outline="black",fill="white")

_canvas.create_rectangle(100, 600, 200, 650,outline="black",fill="red")
_canvas.create_rectangle(100, 650, 200, 700,outline="black",fill="red")


#rectangle mardi
_canvas.create_rectangle(200, 150, 300, 200,outline="black",fill="white")
_canvas.create_text(250, 175, text="Mardi", fill="black", font=('Helvetica 15 bold'))
_canvas.create_rectangle(200, 200, 300, 250,outline="black",fill="red")
_canvas.create_rectangle(200, 250, 300, 300,outline="black",fill="red")

_canvas.create_rectangle(200, 300, 300, 360,outline="black",fill="white")
_canvas.create_rectangle(200, 360, 300, 420,outline="black",fill="white")
_canvas.create_rectangle(200, 420, 300, 480,outline="black",fill="white")
_canvas.create_rectangle(200, 480, 300, 540,outline="black",fill="white")
_canvas.create_rectangle(200, 540, 300, 600,outline="black",fill="white")

_canvas.create_rectangle(200, 600, 300, 650,outline="black",fill="red")
_canvas.create_rectangle(200, 650, 300, 700,outline="black",fill="red")

#rectangle mercredi
_canvas.create_rectangle(300, 150, 400, 200,outline="black",fill="white")
_canvas.create_text(350, 175, text="Mercredi", fill="black", font=('Helvetica 15 bold'))
_canvas.create_rectangle(300, 200, 400, 250,outline="black",fill="red")
_canvas.create_rectangle(300, 250, 400, 300,outline="black",fill="red")

_canvas.create_rectangle(300, 300, 400, 360,outline="black",fill="white")
_canvas.create_rectangle(300, 360, 400, 420,outline="black",fill="white")
_canvas.create_rectangle(300, 420, 400, 480,outline="black",fill="white")
_canvas.create_rectangle(300, 480, 400, 540,outline="black",fill="white")
_canvas.create_rectangle(300, 540, 400, 600,outline="black",fill="white")

_canvas.create_rectangle(300, 600, 400, 650,outline="black",fill="red")
_canvas.create_rectangle(300, 650, 400, 700,outline="black",fill="red")

#rectangle jeudi
_canvas.create_rectangle(400, 150, 500, 200,outline="black",fill="white")
_canvas.create_text(450, 175, text="Jeudi", fill="black", font=('Helvetica 15 bold'))
_canvas.create_rectangle(400, 200, 500, 250,outline="black",fill="red")
_canvas.create_rectangle(400, 250, 500, 300,outline="black",fill="red")

_canvas.create_rectangle(400, 300, 500, 360,outline="black",fill="white")
_canvas.create_rectangle(400, 360, 500, 420,outline="black",fill="white")
_canvas.create_rectangle(400, 420, 500, 480,outline="black",fill="white")
_canvas.create_rectangle(400, 480, 500, 540,outline="black",fill="white")
_canvas.create_rectangle(400, 540, 500, 600,outline="black",fill="white")

_canvas.create_rectangle(400, 600, 500, 650,outline="black",fill="red")
_canvas.create_rectangle(400, 650, 500, 700,outline="black",fill="red")

#rectangle vendredi
_canvas.create_rectangle(500, 150, 600, 200,outline="black",fill="white")
_canvas.create_text(550, 175, text="Vendredi", fill="black", font=('Helvetica 15 bold'))
_canvas.create_rectangle(500, 200, 600, 250,outline="black",fill="red")
_canvas.create_rectangle(500, 250, 600, 300,outline="black",fill="red")

_canvas.create_rectangle(500, 300, 600, 360,outline="black",fill="white")
_canvas.create_rectangle(500, 360, 600, 420,outline="black",fill="white")
_canvas.create_rectangle(500, 420, 600, 480,outline="black",fill="white")
_canvas.create_rectangle(500, 480, 600, 540,outline="black",fill="white")
_canvas.create_rectangle(500, 540, 600, 600,outline="black",fill="white")

_canvas.create_rectangle(500, 600, 600, 650,outline="black",fill="red")
_canvas.create_rectangle(500, 650, 600, 700,outline="black",fill="red")

#rectangle samedi
_canvas.create_rectangle(600, 150, 700, 200,outline="black",fill="white")
_canvas.create_text(650, 175, text="Samedi", fill="black", font=('Helvetica 15 bold'))
_canvas.create_rectangle(600, 200, 700, 250,outline="black",fill="red")
_canvas.create_rectangle(600, 250, 700, 300,outline="black",fill="red")

_canvas.create_rectangle(600, 300, 700, 360,outline="black",fill="white")
_canvas.create_rectangle(600, 360, 700, 420,outline="black",fill="white")
_canvas.create_rectangle(600, 420, 700, 480,outline="black",fill="white")
_canvas.create_rectangle(600, 480, 700, 540,outline="black",fill="white")
_canvas.create_rectangle(600, 540, 700, 600,outline="black",fill="white")

_canvas.create_rectangle(600, 600, 700, 650,outline="black",fill="red")
_canvas.create_rectangle(600, 650, 700, 700,outline="black",fill="red")

#rectangle dimanche
_canvas.create_rectangle(700, 150, 800, 200,outline="black",fill="white")
_canvas.create_text(750, 175, text="Dimanche", fill="black", font=('Helvetica 15 bold'))
_canvas.create_rectangle(700, 200, 800, 250,outline="black",fill="red")
_canvas.create_rectangle(700, 250, 800, 300,outline="black",fill="red")

_canvas.create_rectangle(700, 300, 800, 360,outline="black",fill="red")
_canvas.create_rectangle(700, 360, 800, 420,outline="black",fill="red")
_canvas.create_rectangle(700, 420, 800, 480,outline="black",fill="red")
_canvas.create_rectangle(700, 480, 800, 540,outline="black",fill="red")
_canvas.create_rectangle(700, 540, 800, 600,outline="black",fill="red")

_canvas.create_rectangle(700, 600, 800, 650,outline="black",fill="red")
_canvas.create_rectangle(700, 650, 800, 700,outline="black",fill="red")

Temps_journee = 36000 
Jour_semaine = 1 

# Section ChatBot

window.__name = StringVar()

def fonction_button():
    prediction_model(window.__name.get())
    return 0;

def prediction_model_event(event):
    prediction_model(window.__name.get())
    return 0;

def showEnd(event):
    event.widget.see(END)
    event.widget.edit_modified(0)

def prediction_model(phrase):
    txt.config(state=NORMAL)
    txt.insert(END, 'YOU -> ' + phrase + '\n', "you")
    prediction = predict_text(phrase)
    if(prediction == [1]):
        #fonction qui chope le nombre de page a imprimer
        numbers = [int(temp)for temp in phrase.split() if temp.isdigit()]
        #fonction qui chope le nom du document (ie : il doit sappeller doc quelque chose)
        pattern = 'doc[a-z0-9\-\_]+'
        flags = re.IGNORECASE
        result = re.findall(pattern, phrase, flags)

        if result == []:
            txt.insert(END,'CHATBOT -> ')
            txt.insert(END,'Erreur dans la récupération du nom du document !' + '\n')
        else:
            try:
                numbers[0]
                txt.insert(END,'CHATBOT -> ')
                txt.insert(END,'Le document ' + result[0] + ' qui fait ' + str(numbers[0]) + ' pages a été planifié !' + '\n')
                Ajout_document_imprimante(numbers[0], result)
            except IndexError:
                txt.insert(END,'CHATBOT -> ')
                txt.insert(END,'Erreur dans la récupération du nombre de pages !' + '\n')
                print('Erreur dans la récupération du nombre de pages !')  

    if(prediction == [0]):
        txt.insert(END,'CHATBOT -> ')
        txt.insert(END,'Je ne traite pas ce genre de demande' + '\n')
        print('Je ne traite pas ce genre de demande') 
    name.delete(0,'end')       
    txt.config(state=DISABLED)
    return 0;   

def Ajout_document_imprimante(nombre_pages, num_doc):
    global Temps_journee
    global Jour_semaine

    taille = nombre_pages / 60;

    if(nombre_pages > 36000):
        txt.insert(END,'CHATBOT -> ')
        txt.insert(END,'L imprimante ne peut pas imprimer autant de feuilles en une journee, veuillez segmenter votre document !' + '\n')
        print('L imprimante ne peut pas imprimer autant de feuilles en une journee, veuillez segmenter votre document !') 
        return nombre_pages

    if(Jour_semaine > 6):
        txt.insert(END,'CHATBOT -> ')
        txt.insert(END,'Revener la semaine prochaine pour imprimer votre document, il n y a plus de place dans le planning cette semaine !' + '\n')
        print("Revener la semaine prochaine pour imprimer votre document, il n'y a plus de place dans le planning cette semaine !")
        return nombre_pages  

    if(nombre_pages > Temps_journee):
        Temps_journee = 36000
        Jour_semaine = Jour_semaine + 1  

    position_x1 = Jour_semaine * 100
    position_x2 = position_x1 + 100

    position_y1 = abs(300 + ((36000 - Temps_journee)/120))
    position_y2 = (position_y1 + (taille/2))

    _canvas.create_rectangle(position_x1, position_y1, position_x2, position_y2,outline="black",fill="green")
    _canvas.create_text(((position_x1+position_x2)/2), ((position_y1+position_y2)/2), text=num_doc, fill="black", font=('Helvetica 8 bold'))

    Temps_journee = Temps_journee - (nombre_pages + 120)
    # print(Temps_journee)
    # print("X1 : ", position_y1)
    # print("X2 : ", position_y2)
    # print("---------------")

    return nombre_pages     

_canvas.create_text(1000, 75, text="ChatBot", fill="black", font=('Helvetica 32 bold underline'))

_canvas.create_rectangle(810, 150, 1200, 700,outline="black",fill="azure")

name = Entry(_canvas, width=47, textvariable=window.__name)

name.place(x=822.5, y=667.5)

name.bind('<Return>', prediction_model_event)

btn = Button(_canvas, text='Envoyer', command=fonction_button)
  
btn.place(x=1112.5, y=665.5)

txt = Text(_canvas, width=48, height=32, highlightthickness = 0, borderwidth=0)

txt.place(x=811, y=151)

txt.tag_config("you", foreground="dimgray")

txt.bind('<<Modified>>', showEnd)

txt.insert(END, "--- GESTION PALLNING IMPRIMANTE ---" + '\n')
txt.insert(END,'CHATBOT -> ')
txt.insert(END,'Veuillez entrer votre requête !' + '\n')
txt.config(state=DISABLED)

# Ajout_document_imprimante(1000000, "Doc 0")

# Ajout_document_imprimante(7200, "Doc 1")
# Ajout_document_imprimante(1800, "Doc 2")
# Ajout_document_imprimante(7200, "Doc 3")
# Ajout_document_imprimante(3600, "Doc 4")
# Ajout_document_imprimante(3600, "Doc 5")
# Ajout_document_imprimante(3600, "Doc 6")
# Ajout_document_imprimante(7200, "Doc 7")
# Ajout_document_imprimante(5000, "Doc 8")
# Ajout_document_imprimante(5000, "Doc 9")
# Ajout_document_imprimante(5000, "Doc 10")
# Ajout_document_imprimante(5000, "Doc 11")
# Ajout_document_imprimante(5000, "Doc 12")
# Ajout_document_imprimante(5000, "Doc 13")
# Ajout_document_imprimante(5000, "Doc 14")
# Ajout_document_imprimante(36000, "Doc 15")
# Ajout_document_imprimante(18000, "Doc 16")
# Ajout_document_imprimante(18000, "Doc 17")
# Ajout_document_imprimante(17000, "Doc 18")


# Ajout_document_imprimante(37000, "Doc 19")

# print(predict_text('Je veux imprimer hgdfgbjhd qui a 500 pages'))
# print(predict_text('Salut Ca va ?'))
# print(predict_text('imprime moi docxxx qui a 500 pages'))

# prediction_model('Salut Ca va ?')
# prediction_model('imprime moi docxxx qui a 500 pages')         


window.mainloop()