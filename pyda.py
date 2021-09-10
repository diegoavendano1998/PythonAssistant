# pip install pipenv
# pipenv install --two
# pipevn shell


import wolframalpha
import wikipedia
import pyttsx3
from pyttsx import voice


engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[20].id)

engine.say("En que te puedo ayudar")
engine.runAndWait()

while True:
    input = raw_input("\n\n\nEn que te puedo ayudar :   ")
    try:
        try:
            app_id = "V5863E-LHTKV2KAP5"

            client = wolframalpha.Client(app_id)
            res = client.query(input)

            answer = next(res.results).text
            print answer
            engine.say(str(answer))
            engine.runAndWait()
        except:
            wikipedia.set_lang("es")
            # Trear el resultado de wikipedia en 3 sentencias
            answer= (wikipedia.summary(input, sentences=2))
            print (answer)
            engine.say(answer)
            engine.runAndWait()
    except Exception as e: 
        print(e)





# V5863E-LHTKV2KAP5