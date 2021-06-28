import speech_recognition as kl

r = kl.Recognizer()
with kl.Microphone() as source:
    while 1:
        print("Listening you..")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(text)
            if text == 'quit':
                break

        except Exception as e:
            print(e)
print('Bye..!!')