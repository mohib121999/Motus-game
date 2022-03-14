from tkinter import *

#--------------------------------------------------------------------------------------------------------      
def Presentation1():
        """Ecrit le mot "MOTUS" sur toutes les lignes de la grille de jeu ."""
        global airDessin

        tableauDeCanevas = []
        nbrLettres =5
        airDessin = Frame(fen1)
        tableauDeCanevas = []
        for x in range(1):
          tabCanvasLigne = []
        for y in range(nbrLettres):
               canvas = Canvas(airDessin,bg='blue',height=50,width=50,borderwidth=5,relief='ridge')
               canvas.create_text(30,30,font='Century 28 bold ',text='Motus'[y])            
               canvas.grid(row=4,column=y)
               tabCanvasLigne.append(canvas)
               tableauDeCanevas.append(tabCanvasLigne)

        airDessin.grid(row=3,column=2)
        button = Button(fen1, text = 'Play',width = 32, height = 3, bd = 7, bg = "#3e646c").grid(row =10 , column = 1, columnspan = 2, padx = 1, pady = 1)
        l = Label(fen1, text ='WELCOME to motus game').grid(row =1 , column = 1, columnspan = 2, padx = 1, pady = 1)
        l = Label(fen1, text ='directed by mohib').grid(row =11 , column = 2, columnspan = 2, padx = 1, pady = 1)

    #Output = Text(fen, height = 1, width = 40,  bg = "light cyan").grid(row =6 , column = 1, columnspan = 2, padx = 1, pady = 1)



#-------------------------------------------------------------------------------------------------------
fen1 = Tk()
fen1.title("Motus")
fen1.resizable(0,0)
fen1.geometry("325x175")
Presentation1()
fen1.mainloop()










