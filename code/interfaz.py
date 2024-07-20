import tkinter as tk
from tkinter import *
import aprender
import pyttsx3
import tablaVerdad

voz = pyttsx3.init()
voices = voz.getProperty("voices")
voz.setProperty("voice", voices[0].id)


def leerTexto(cadena):
    voz.say(cadena)
    voz.runAndWait()

def Abrir_Ventana2():
    ventana_Teclado = Toplevel(raiz)
    ventana_Teclado.title("Tabla de verdad")
    ventana_Teclado.config(bg = "light yellow")
    
    area_Mensaje = Text(ventana_Teclado, wrap=WORD, width=50, height=20, bg="white")
    area_Mensaje.pack(fill=BOTH,expand=True,padx=10, pady=10)

    ventana_Teclado.resizable(True,True)

    def insertar_texto(texto):
        mensaje_entrada.insert(END, texto)

    # Definir las filas del teclado
    filas = [
        ('A', 'B', 'C', 'D', '∧', '∨','~', '→', '↔', ')', '(')
    ]

    # Crear los botones del teclado
    for fila in filas:
        fila_frame = Frame(ventana_Teclado)
        fila_frame.pack(padx=5,pady=5)
        for texto in fila:
            Button(fila_frame, text=texto, width=3, height=1,
                   command=lambda t=texto: insertar_texto(t)).pack(side=LEFT, padx=5, pady=5)

    
    mensaje_entrada = Entry(ventana_Teclado, width=40)
    mensaje_entrada.pack(side=LEFT, fill=X, expand=True, padx=10, pady=10)
    

    enviar_button = Button(ventana_Teclado, text="Enviar", command=lambda: enviar_mensajeTabla(area_Mensaje, mensaje_entrada))
    enviar_button.pack(side=LEFT, padx=10,pady=10)

    def enviar_mensajeTabla(chat_area, mensaje_entrada):
        mensaje_usuario = mensaje_entrada.get()
        mensaje_respuesta = tablaVerdad.tablaVerdadera(mensaje_usuario)
        chat_area.insert(END, "Tú: " + mensaje_usuario + "\n")
        mensaje_entrada.delete(0, END)
        chat_area.insert(END,  mensaje_respuesta +"\n")
        chat_area.see(END)

def Abrir_ventana():
    
    ventana= Toplevel(raiz)
    ventana.title("Amaya")
    ventana.config(bg="sky blue")
    
    area_Mensaje = Text(ventana, wrap=WORD, bg="light yellow")
    area_Mensaje.pack(fill=BOTH, expand=True,padx=10, pady=10)
    
    mensaje_entrada = Entry(ventana, width=40)
    mensaje_entrada.pack(side=LEFT, fill=X, expand=True, padx=10, pady=10)
    
    enviar_Button = Button(ventana, text="Enviar", command=lambda: enviar_Mensaje(area_Mensaje, mensaje_entrada))
    enviar_Button.pack(side=LEFT, padx=10, pady=10)
    
    ventana.resizable(True,True)

    def enviar_Mensaje(chat_area, mensaje_entrada):
        mensaje_usuario = mensaje_entrada.get()
        mensaje_bot= aprender.chat_bot(mensaje_usuario)
        sendvozmensaje= mensaje_bot
        mensaje_clave=mensaje_usuario.lower()

        if mensaje_usuario.strip():
            chat_area.insert(END, "Tú: " + mensaje_usuario + "\n")
            mensaje_entrada.delete(0, END)
            if mensaje_bot=="falso":
                chat_area.insert(END, "Bot: " + "No conozco la respuesta, me enseñas? Escribe la respuesta o escribe 'omitir' para omitir:" +"\n")
                chat_area.see(END)
                mensaje_anterior=mensaje_usuario
                enviar_Button.pack_forget()
                enviar_Button2 = Button(ventana, text="Enviar", command=lambda:retroalimentacion(chat_area, mensaje_entrada, mensaje_usuario))
                enviar_Button2.pack(side=LEFT, padx=10, pady=10)
            elif mensaje_clave=="tablaverdad":

                chat_area.insert(END, "Bot: " + mensaje_bot +"\n")
                chat_area.see(END)
                Abrir_Ventana2()


            else:
                chat_area.insert(END, "Bot: " + mensaje_bot +"\n")
                chat_area.see(END)
 
            def retroalimentacion(chat_area, mensaje_entrada, mensaje_anterior):
                mensaje_usuario = mensaje_entrada.get()
                mensaje_bot= aprender.respuesta_noconocida(mensaje_usuario,mensaje_anterior)
                if mensaje_usuario.strip():
                    chat_area.insert(END, "Tú: " + mensaje_usuario + "\n")
                    mensaje_entrada.delete(0, END)   
                    chat_area.insert(END, "Bot: " + mensaje_bot +"\n")
                    chat_area.see(END)
                enviar_Button2.pack_forget()
                enviar_Button.pack(side=LEFT, padx=10, pady=10)

            def vozMensaje():
                leerTexto(mensaje_bot)
        ventana.after(100, vozMensaje)




raiz = Tk()
raiz.title("Amaya")
raiz.config(bg="sky blue")

raiz.resizable(True, True)

logo = tk.PhotoImage(file="Amaya.png")
label_imagen = tk.Label(raiz,image=logo)
label_imagen.pack(pady=50, padx=100)

Label(raiz, text="Habla con Amaya", bg="sky blue", font=("courier new", 14)).pack(pady=10,padx=100)

boton=Button(raiz, text="Comenzar", command=lambda: Abrir_ventana()).pack(pady=10,padx=100)



raiz.mainloop()
