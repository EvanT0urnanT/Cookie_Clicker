from tkinter import *
from Interface_principale import *
def quit() :
    interface_boutique.destroy()
    
def buy ():
    gm_price.set((gm_price.get()*1.1)//1)

def interface_boutique_main():
    global interface_boutique
    interface_boutique = Tk("Fullscreen")
    interface_boutique.title("Boutique")
    interface_boutique.iconbitmap("Ico_boutique.ico")
    interface_boutique.geometry("960x720")
    interface_boutique.minsize(480,360)
    interface_boutique.config(background = "grey")
    
    label_title = Label(interface_boutique, text = "Bienvenue dans la boutique achetez des objets vous permettant de gagner des cookies en continue.", font = ("Arial", 15) , bg = "Black" , foreground = "White")
    label_title.pack(side = "top", fill = "x")
    
    gm_frame = Frame(interface_boutique,bg = "Yellow", bd = 1)
    gm_price = IntVar(value = 100)
    
    message = Message(gm_frame ,textvariable = gm_price).pack(side="right")
    
    gm_frame.pack(side="top")
    
    quit_button = Button(interface_boutique , text = "Quitter" , font = ("Arial", 20) , bg = "Black" , foreground = "white", command = quit)
    quit_button.pack(side = "bottom" ,fill = "x")



    interface_boutique.mainloop()
if __name__ == "__main__" :
    interface_boutique_main()
    