from tkinter import *
from Interface_boutique import *
import time

def boutique():
    interface_boutique_main()

def pos_clic(event):
    x , y = event.x, event.y
    print(x,y)

def detect_clic(event):
    x , y = event.x, event.y
 
    # renvoie la position de l'image sous la forme [x, y] :
    cookie_coords = canvas.coords("cookie")
 
    # détection du clic sur l'image :
    if x >= 0 and x <= 960:
        if y >= 0 and y <= 720:
            compteur.set(compteur.get()+1)
            
            
def parametre():
    global interface
    interface = Tk()
    interface.title("Cookie Clicker")
    interface.iconbitmap("Ico_cookie.ico")
    interface.geometry("960x720")
    interface.minsize(480,360)
    interface.config(background = "grey")
    
    
    interface.bind("<Button-1>", pos_clic)
    
    
    frame = Frame(interface , bg = "Grey", bd = 1 )
    boutique_button = Button(frame , text = "Boutique", font = ("Arial" ,10) , bg = "White" , fg = "Black", command = boutique)
    boutique_button.pack(side = "left" , padx = 100)
    frame.pack(side ="bottom",fill = "x")
    
    
    
    
    
    
    
    
def image_para():
    width = 520
    height = 520
    global compteur
    compteur = IntVar(value = 0)
    Label(textvariable=compteur, foreground = "white",bg = "grey" ,font = ("Arial", 20) ).pack()
    text = Label(text = "Cookies !" ,foreground = "white",bg = "grey" ,font = ("Arial", 20) ).pack()
    image = PhotoImage(file = "cookie.png")
    global canvas
    canvas = Canvas(interface , width= width , height = height , bg = "grey", bd = 0, highlightthickness = 0)
    canvas.create_image(width/2, height/2, image = image)
    canvas.pack()
    canvas.bind("<Button-1>", detect_clic)
    canvas.mainloop()
    
    
def interface_principale_main():
    parametre()
    image_para()
    interface.mainloop()





if __name__ == "__main__" :
    interface_principale_main()


