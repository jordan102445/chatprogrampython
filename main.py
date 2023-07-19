



pocetnakonverazcija = ["Dobro utro i na vas", "Dobar den i na vas ", "Dobra vecer i na vas", "Zdravo i nas",
                       "Super fala na prasanje", "Sekako deka da"]  # starten muabet
Vicovi = {"Vic za vlav": "Малото влавче му вика на татко си: – "
                         "Тато, тато купи ми чипс! "
                         "Таткото му одговара:"
                         "– Аааа не може, те тера на сок.",
          "Vic za riba": "Што дуваат рибите?"
                         "– Морска трева.",
          "Vic za odmor": "Македонец на царина: "
                          "– Носите нешто недозволено…дрога, алкохол, оружје? "
                          "– Не знам, мене мама ме пакува…",
          "Vic za vegan": "Позади секој успешен веган стои разочарана баба."}

Sport = {
    "Lebron James": "Американски кошаркар кој моментално настапува за екипата на Лос Анџелес Лејкерс од НБА лигата. Често е споредуван со Мајкл Џордан, "
                    "Тој бил изгласан во Ол-НБА првиот тим дванаесет пати и пет пати во првиот одбранбен тим.",
    "Micheal Jordan": "американски НБА-кошаркар, активен стопанственик, и моментален сопственик на НБА-клубот Шарлот Хорнетс. "
                      "Сметан е за еден од најдобрите кошаркари на сите времиња.Мајкл Џордан поминал 15 сезони во НБА лигата "
                      "„најдобар северноамерикански спортист во XX век“ по изборот на спортскиот канал ЕСПН. Неговиот силен одраз и забивањата од линијата за слободни ",
    "Lionel Messi": " аргентински фудбалер кој настапува за екипата за Париз Сен Жермен и репрезентацијата на Аргентина. "
                    "Тој се смета за еден од најдобрите фудбалери на својата генерација,",
    "Cristiano Ronaldo": "португалски фудбалер, напаѓач на Ал-Наср и на португалската репрезентација."
                         "Роналдо е роден во Сан Педро, Фуншал на португалскиот остров Мадеира. Пораснал во палатата Фуншал во Санто Антонио,"

}

prasanja = ["Која земја има најдолго крајбрежје во светот?",
            "Која е најнаселената земја во светот?",
            "Кој е главен град на Филипините?",
            "Која е најмалата земја на светот?",
            "Во која земја се наоѓа највисокиот водопад на светот?",
            "Кој е главен град на Австралиа",
            "Која земја има најголем број активни вулкани?",
            "Каде е забележана најжешката температура досега?",
            "Во кој океан се наоѓа островот Мадагаскар?"]

odgovori = ["Kanada", "Kina", "Manila", "Vatikan city", "Venecuela", "Kanbera", "Indonezija", "Libija",
            "Indiskiot okean", ]

GeneralKnowlegeKviz = {"Која земја има најдолго крајбрежје во светот?": "Канада",
                       "Која е најнаселената земја во светот?": "Kина",
                       "Кој е главен град на Филипините?": "Манила",
                       "Која е најмалата земја на светот?": "Ватикан Цити",
                       "Во која земја се наоѓа највисокиот водопад на светот?": "Венецуела",
                       "Кој е главен град на Австралиа": "Канбера",
                       "Која земја има најголем број активни вулкани?": "Индонезија",
                       "Каде е забележана најжешката температура досега?": "Либија",
                       "Во кој океан се наоѓа островот Мадагаскар?": "Индискиот океан",
                       }

import random

from datetime import date
from datetime import datetime

import webbrowser
import subprocess

import pyttsx3






def funkcija():

    n = 10
    i = 0
    k = 3
    deneska = date.today()

    casotsega = datetime.now().strftime("%H:%M")  # :%M

    while i < n:

        vnesi = str(input("Vnesete"))
        if "utro" in vnesi:
            engine = pyttsx3.init()
            engine.say("Dobro utro")
            engine.runAndWait()
            print("Znaci ",pocetnakonverazcija[0])
        else:
            if "den" in vnesi:
                engine = pyttsx3.init()
                engine.say("Dobar den")
                engine.runAndWait()
                print("Znaci ", pocetnakonverazcija[1])
            else:
                if "vecer" in vnesi:
                    engine = pyttsx3.init()
                    engine.say("Dobra vecer")
                    engine.runAndWait()
                    print("Znaci ", pocetnakonverazcija[2])
                else:
                    if "Zdravo" in vnesi:
                            engine = pyttsx3.init()
                            engine.say("How are you today")
                            engine.runAndWait()
                            print("Znaci ", pocetnakonverazcija[3])
                    else:
                        if "Kako ste" in vnesi:
                                engine = pyttsx3.init()
                                engine.say("Super fala na prasanje")
                                engine.runAndWait()
                                print("Znaci ", pocetnakonverazcija[4])
                        else:
                            if "polozime" in vnesi:
                                engine = pyttsx3.init()
                                engine.say("DAAA")
                                engine.runAndWait()
                                print("Znaci ", pocetnakonverazcija[5])

                            else:
                                if "Lebron James" in vnesi:
                                    print(Sport["Lebron James"])
                                else:
                                    if "Micheal Jordan" in vnesi:
                                        print(Sport["Micheal Jordan"])
                                    else:
                                        if "Lionel Messi" in vnesi:
                                            print(Sport["Lionel Messi"])
                                        else:
                                            if "Cristiano Ronaldo" in vnesi:
                                                print(Sport["Cristiano Ronaldo"])
                                            else:
                                                if "vic" in vnesi:
                                                    print(random.choice(list(Vicovi.values())))
                                                else:
                                                    if "data" in vnesi:
                                                        print("Datata deneska e ", deneska.day)

                                                    else:
                                                        if "mesec" in vnesi:
                                                            if deneska.month == 1:
                                                                print(deneska.month, "Januari")
                                                            else:
                                                                if deneska.month == 2:
                                                                    print(deneska.month, "Fevruari")
                                                                else:
                                                                    if deneska.month == 3:
                                                                        print(deneska.month, "Mart")
                                                                    else:
                                                                        if deneska.month == 4:
                                                                            print(deneska.month, "April")
                                                                        else:
                                                                            if deneska.month == 5:
                                                                                print(deneska.month, "Maj")
                                                                            else:
                                                                                if deneska.month == 6:
                                                                                    print(deneska.month, "Juni")
                                                                                else:
                                                                                    if deneska.month == 7:
                                                                                        print(deneska.month, "Juli")
                                                                                    else:
                                                                                        if deneska.month == 8:
                                                                                            print(deneska.month,
                                                                                                  "Avgust")
                                                                                        else:
                                                                                            if deneska.month == 9:
                                                                                                print(deneska.month,
                                                                                                      "Septemvri")
                                                                                            else:
                                                                                                if deneska.month == 10:
                                                                                                    print(deneska.month,
                                                                                                          "Oktomvri")
                                                                                                else:
                                                                                                    if deneska.month == 11:
                                                                                                        print(
                                                                                                            deneska.month,
                                                                                                            "Noemvri")
                                                                                                    else:
                                                                                                        if deneska.month == 12:
                                                                                                            print(
                                                                                                                deneska.month,
                                                                                                                "Dekemvri")

                                                        else:
                                                            if "godina" in vnesi:
                                                                print("Godinata e", deneska.year)
                                                            else:
                                                                if "casot" in vnesi:
                                                                    if casotsega == 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24:
                                                                        print("Casot deneska e :", casotsega, "Den")
                                                                    else:
                                                                        if casotsega == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12:
                                                                            print("Casot deneska e :", casotsega, "Nok")

                                                                if "chrome facebook" in vnesi:
                                                                    new = 2
                                                                    url = 'https://www.facebook.com/'
                                                                    webbrowser.register('chrome', None,
                                                                                        webbrowser.BackgroundBrowser(
                                                                                            "C:\Program Files\Google\Chrome\Application\chrome.exe"))
                                                                    webbrowser.get('chrome').open_new(url)
                                                                else:
                                                                    if "chrome twitter" in vnesi:
                                                                        new = 2
                                                                        url = 'https://twitter.com/home'
                                                                        webbrowser.register('chrome', None,
                                                                                            webbrowser.BackgroundBrowser(
                                                                                                "C:\Program Files\Google\Chrome\Application\chrome.exe"))
                                                                        webbrowser.get('chrome').open_new(url)
                                                                    else:
                                                                        if "chrome ugd" in vnesi:
                                                                            new = 2
                                                                            url = 'https://www.ugd.edu.mk/index.php/studenti/e-ugd'
                                                                            webbrowser.register('chrome', None,
                                                                                                webbrowser.BackgroundBrowser(
                                                                                                    "C:\Program Files\Google\Chrome\Application\chrome.exe"))
                                                                            webbrowser.get('chrome').open_new(url)
                                                                        else:
                                                                            if "chrome youtube" in vnesi:
                                                                                new = 2
                                                                                url = 'https://www.youtube.com/'
                                                                                webbrowser.register('chrome', None,
                                                                                                    webbrowser.BackgroundBrowser(
                                                                                                        "C:\Program Files\Google\Chrome\Application\chrome.exe"))
                                                                                webbrowser.get('chrome').open_new(url)
                                                                            else:
                                                                                if "chrome gmail" in vnesi:
                                                                                    new = 2
                                                                                    url = 'https://www.google.com/gmail/about/'
                                                                                    webbrowser.register('chrome', None,
                                                                                                        webbrowser.BackgroundBrowser(
                                                                                                            "C:\Program Files\Google\Chrome\Application\chrome.exe"))
                                                                                    webbrowser.get('chrome').open_new(
                                                                                        url)
                                                                                else:

                                                                                    if "chrome spotify" in vnesi:
                                                                                        new = 2
                                                                                        url = 'https://open.spotify.com/'
                                                                                        webbrowser.register('chrome',
                                                                                                            None,
                                                                                                            webbrowser.BackgroundBrowser(
                                                                                                                "C:\Program Files\Google\Chrome\Application\chrome.exe"))
                                                                                        webbrowser.get(
                                                                                            'chrome').open_new(url)
                                                                                    else:
                                                                                        if "calculator" in vnesi:
                                                                                            subprocess.Popen((
                                                                                                'C:\\Windows\\System32\\calc.exe'))
                                                                                        else:
                                                                                            if "microsoft edge" in vnesi:
                                                                                                subprocess.Popen((
                                                                                                    '"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"'))
                                                                                            else:
                                                                                                if "notepad" in vnesi:
                                                                                                    subprocess.Popen((
                                                                                                        'C:\\Windows\\System32\\notepad.exe'))

                                                                                            if "izlezi od sistem" in vnesi:
                                                                                                exit()

                                i = i + 1






vlezete = str(input("Vlezete vo Programata"))

if "vlezi vo programa" in vlezete:
    funkcija()


from pywhatkit import search


def funkcija2():
    i = 0



    while i < len(prasanja):
        print(prasanja[0])
        odgovor1 = str(input("Odgovori go prvoto prasanje"))
        if odgovor1 != odgovori[0]:
            print("Ne tocen odgovor")
            query = "Која земја има најдолго крајбрежје во светот?"
            print(f"Searching for the query : {query}")
            search(query)
            break
        else:
            if odgovor1 == odgovori[0]:
                print("Tocen odgovor")

                print(prasanja[1])
                odgovor2 = str(input("Odgovori go vtoroto prasanje"))
                if odgovor2 != odgovori[1]:
                    print("Ne tocen odgovor")
                    query ="Која е најнаселената земја во светот?"
                    print(f"Searching for the query : {query}")
                    search(query)
                    break
                else:
                    if odgovor2 == odgovori[1]:
                        print("Tocen odgovor")

                        print(prasanja[2])
                        odgovor3 = str(input("Odgovori go tretoto prasanje"))
                        if odgovor3 != odgovori[2]:
                            print("Ne tocen odgovor")
                            query ="Кој е главен град на Филипините?"
                            print(f"Searching for the query : {query}")
                            search(query)
                            break
                        else:
                            if odgovor3 == odgovori[2]:
                                print("Tocen odgovor")

                                print(prasanja[3])
                                odgovor4 = str(input("Odgovori go cetvrtoto prasanje"))
                                if odgovor4 != odgovori[3]:
                                    print("Ne tocen odgovor")
                                    query ="Која е најмалата земја на светот?"
                                    print(f"Searching for the query : {query}")
                                    search(query)
                                    break
                                else:
                                    if odgovor4 == odgovori[3]:
                                        print("Tocen odgovor")

                                        print(prasanja[4])
                                        odgovor5 = str(input("Odgovori go petoto prasanje"))
                                        if odgovor5 != odgovori[4]:
                                            print("Ne tocen odgovor")
                                            query ="Во која земја се наоѓа највисокиот водопад на светот?"
                                            print(f"Searching for the query : {query}")
                                            search(query)
                                            break
                                        else:
                                            if odgovor5 == odgovori[4]:
                                                print("Tocen odgovor")

                                                print(prasanja[5])
                                                odgovor6 = str(input("Odgovori go sestoto prasanje"))
                                                if odgovor6 != odgovori[5]:
                                                    print("Ne tocen odgovor")
                                                    query ="Кој е главен град на Австралиа?"
                                                    print(f"Searching for the query : {query}")
                                                    search(query)
                                                    break
                                                else:
                                                    if odgovor6 == odgovori[5]:
                                                        print("Tocen odgovor")

                                                        print(prasanja[6])
                                                        odgovor7 = str(input("Odgovori go sedmoto prasanje"))
                                                        if odgovor7 != odgovori[6]:
                                                            print("Ne tocen odgovor")
                                                            query ="Која земја има најголем број активни вулкани?"
                                                            print(f"Searching for the query : {query}")
                                                            search(query)
                                                            break
                                                        else:
                                                            if odgovor7 == odgovori[6]:
                                                                print("Tocen odgovor")

                                                                print(prasanja[7])
                                                                odgovor8 = str(input("Odgovori go osmoto prasanje"))
                                                                if odgovor8 != odgovori[7]:
                                                                    print("Ne tocen odgovor")
                                                                    query ="Каде е забележана најжешката температура досега?"
                                                                    print(f"Searching for the query : {query}")
                                                                    search(query)
                                                                    break
                                                                else:
                                                                    if odgovor8 == odgovori[7]:
                                                                        print("Tocen odgovor")

                                                                        print(prasanja[8])
                                                                        odgovor9 = str(input("Odgovori go devetoto prasanje"))
                                                                        if odgovor9 != odgovori[8]:
                                                                            print("Ne tocen odgovor")
                                                                            query ="Во кој океан се наоѓа островот Мадагаскар?"
                                                                            print(f"Searching for the query : {query}")
                                                                            search(query)
                                                                            break
                                                                        else:
                                                                            if odgovor9 == odgovori[8]:
                                                                                print("Tocen odgovor")







            i = i +1



vlezete2 = str(input("Vlezete vo Kvizot"))

if "vlezi vo kviz" in vlezete2:
    funkcija2()





































