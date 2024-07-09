import json
import difflib
from difflib import get_close_matches
from typing import List, Union
import pyttsx3
import random

voz = pyttsx3.init()
voices = voz.getProperty("voices")
voz.setProperty("voice", voices[0].id)

def leerTexto(cadena):
    voz.say(cadena)
    voz.runAndWait()

def cargarBase(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def guardarBase(file_path:str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def encontrarMejorRespuesta(cadena: str, preguntas: "list[str]") -> Union[str,None]:
    matches: list = get_close_matches(cadena, preguntas, n = 1, cutoff = 0.75)
  #  for match in preguntas:
      # similarity = difflib.SequenceMatcher(None, cadena, match).ratio()
    #    print(f"Palabra: {match}, Similitud: {similarity * 100:.2f}%")
    return matches[0] if matches else None

def obtenerRespuesta(pregunta: str, datosBase: dict) -> Union[str,None]:
    for q in datosBase["preguntas"]:
        if q["pregunta"] == pregunta:
            respuesta = q["respuesta"]
            return random.choice(respuesta)
        
def chat_bot():
    datosBase: dict = cargarBase("datos.json")

    while True:
        user_input: str = input("You: ")
        user_input = user_input.lower()
        if user_input.lower() == "salir":
            break

        best_match: Union[str,None] = encontrarMejorRespuesta(user_input, [q["pregunta"] for q in datosBase["preguntas"]])
        
        if best_match:
            answer: str = obtenerRespuesta(best_match, datosBase)
            print(f"Bot: {answer}")
            leerTexto(answer)
        else:
            print("Bot: No conosco la respuesta, me enseñas?")
            leerTexto("No conosco la respuesta, me enseñas?")
            new_answer: str = input("Escribe la respuesta o escribe 'omitir' para omitir: ")

            if new_answer.lower() != "omitir":
                datosBase["preguntas"].append({"pregunta": user_input, "respuesta": [new_answer]})
                guardarBase("datos.json", datosBase)
                print("Gracias por enseñarme")


chat_bot()