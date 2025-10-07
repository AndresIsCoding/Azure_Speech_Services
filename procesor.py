from datetime import datetime
from num2words import num2words
import random


def procesor(commands: list, voz_femenina):
    for i in range(len(commands)):
        if ("qué" in commands and "hora" in commands and
             "es" in commands):
            return get_time()
        elif ("dime" in commands and "un" in commands and
              "número" in commands and "al" in commands and
              "azar" in commands):
            return "vale, el numero " + num2words(random.randint(0, 99),
                                                  lang="es")
        elif("en" in commands and "qué" in commands and
             "curso" in commands and "estamos" in commands):
            return "Estamos en proyecto integrador dos"
        elif("cambia" in commands and "de" in commands and
             "voz" in commands):
            return change_voice(voz_femenina)
        
    return "no entendi que deseas"


def get_time():
    hour = num2words(datetime.now().strftime("%I"), lang="es")
    minutes = num2words(datetime.now().strftime("%M"), lang="es")
    daytime = datetime.now().strftime("%p") == "AM"
    daytime = "de la mañana" if daytime else "de la tarde"
    txt = "son las " + hour + " y " + minutes + daytime
    return txt

def change_voice(voz):
    voz[0] = not voz[0]
    return "listo, ¿asi te parece mejor?"