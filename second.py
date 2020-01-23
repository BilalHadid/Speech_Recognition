import speech_recognition as sr 



def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print('Please say Something')


        audio = r.listen(source)
        
        print("Recognize NOW")

        try:
            print("You Have Said : " , r.recognize_google(audio))
            print("audio record Successfully")

        except Exception as e:
            print("Error" , str(e))


        with open("bilal.m4a", "wb") as f:
            f.write(audio.get_wav_data())


if __name__ == '__main__':
    main()