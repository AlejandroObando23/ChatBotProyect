from tkinter import *
import aprender

def Abrir_ventana():
    ventana= Toplevel(raiz)
    ventana.title("Amaya")
    ventana.config(bg="sky blue")
    
    area_Mensaje = Text(ventana, wrap=WORD, width=50, height=20, bg="light yellow")
    area_Mensaje.pack(padx=10, pady=10)
    
    mensaje_entrada = Entry(ventana, width=40)
    mensaje_entrada.pack(side=LEFT, padx=10, pady=10)
    
    enviar_Button = Button(ventana, text="Enviar", command=lambda: enviar_Mensaje(area_Mensaje, mensaje_entrada))
    enviar_Button.pack(side=LEFT, padx=10, pady=10)

def enviar_Mensaje(chat_area, mensaje_entrada):
    mensaje_usuario = mensaje_entrada.get()
    mensaje_bot= aprender.chat_bot(mensaje_usuario)
    if mensaje_usuario.strip():
        chat_area.insert(END, "Tú: " + mensaje_usuario + "\n")
        mensaje_entrada.delete(0, END)
        chat_area.insert(END, "Bot: " + mensaje_bot +"\n")
        chat_area.see(END)

raiz = Tk()
raiz.title("Chat Bot")
raiz.config(bg="sky blue")

Label(raiz, text="Habla con Amaya", bg="sky blue", font=("courier new", 14)).pack(pady=50,padx=100)
bonotn=Button(raiz, text="OK", command= Abrir_ventana).pack(pady=50,padx=100)


raiz.mainloop()
