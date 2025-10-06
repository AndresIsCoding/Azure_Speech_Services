from datetime import datetime
from num2words import num2words
import random


def procesor(commands: list):
    for i in range(len(commands)):
        if (["qué", "hora", "es"] <= commands):
            return get_time()
        if (["dime", "un", "número", "al", "azar"] <= commands):
            return "vale, el numero " + num2words(random.randint(0, 99),
                                                  lang="es")
    return "no entendi que deseas"


def get_time():
    hour = num2words(datetime.now().strftime("%I"), lang="es")
    minutes = num2words(datetime.now().strftime("%M"), lang="es")
    daytime = datetime.now().strftime("%p") == "AM"
    daytime = "de la mañana" if daytime else "de la tarde"
    txt = "son las " + hour + " y " + minutes + daytime
    return txt
