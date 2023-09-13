import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import time
import cv2
import pyautogui
import instaloader
import requests
import operator
import psutil
import speedtest
import pyautogui as press
import pywhatkit
import numpy as np
import phonenumbers
import subprocess
from PIL import Image
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
from phonenumbers import timezone,geocoder,carrier
from plyer import notification  #pip install plyer
from mail import gmail, gpassword

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        print("Good morning sir")
        speak("Good Morning Sir")
        

    elif hour>=12 and hour<18:
        print("Good Afternoon sir")
        speak("Good Afternoon Sir")

    elif hour>=18 and hour<=24:
        print("Good Evening sir")
        speak("Good Evening Sir")
        
    else:
        print("good night sir")
        speak("good night sir")

    speak("I Am jarvis Your Personal Voice Assistant. What Can I Do For You.....")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()

    except Exception as e:
        print(e)
        print("Say that again please....")
        #speak("Say that again please....")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def wifi():
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile'])
    data = meta_data.decode('utf-8', errors = "backslashreplace")
    data = data.split('\n')
    profiles = []
    for i in data:
        if "All User Profile" in i:
            i = i.split(":")
            i = i[1]
            i = i[1:-1]
            profiles.append(i)
    print("{:<30}| {:<}".format("Wi-Fi", "Password"))
    print("----------------------------------------")
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key = clear'])
            results = results.decode('utf-8', errors = "backslashreplace")
            results = results.split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

            try:
                print("{:<30}| {:<}".format(i, results[0]))

            except IndexError:
                print("{:<30}| {:<}".format(i, ""))

        except subprocess.CalledProcessError:
            print("Encoding Error Occurred")
    

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=b01915aec0c2438bb88fccf6ad2182ff'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day=["first","secound","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def TaskExecution():
    wishMe()
    while True:
        query = takeCommand().lower()
   
        if "how are you" in query:
            speak("I'm fine sir, what about you...")

        elif 'hey' in query or 'hello' in query:
            speak("hello sir, may i help you with something..")

        elif 'also good' in query or 'fine' in query:
            speak("that's great to hear from you")

        elif 'thank you' in query or 'thanks' in query:
            speak("it's my pleasure sir.")

        elif "who are you" in query:
            speak("I am jarvis sir, your personal voice assistant ")

        elif "open command" in query:
            os.system("start cmd")
            speak("opening command prompt. please wait....")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            speak("Opening Camera, Please wait....")
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()


        elif "ip address" in query:
            ip = requests('https://api.ipify.org').text
            print(f"your IP address is {ip}")
            speak(f"your IP address is {ip}")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...please wait')
            query = query.replace("wikipedia", "")
            results =  wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia....")
            print(results)
            speak(results)

        elif "temperature" in query:
            search = "temperature in sindhanur"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        elif "weather" in query:
            search = "weather in sindhanur"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")


        elif'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube Please Wait....")

        elif 'data speed' in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            print("Wifi Upload Speed is", up)
            print("Wifi download speed is ",dl)
            speak(f"Wifi download speed is {dl}")
            speak(f"Wifi Upload speed is {up}")

        elif 'search on google' in query:
            speak("what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak("opening google. please wait....")

        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com/')
            speak("Opening StackoverFlow please Wait....")

        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')
            speak("Opening google, please wait....")

        elif "hidden menu" in query:
            press.hotkey('winleft', 'x')
            speak("showing hidden menu, please wait..")

        elif "task manager" in query:
            press.hotkey('ctrl', 'shift', 'esc')
            speak("opening task manager, please wait..")
            
        elif "task view" in query:
            press.hotkey('winleft', 'tab')
            speak("viewing task, please wait...")

        elif "snip" in query:
            press.hotkey('winleft', 'shift', 's')
            speak("please select the screen")

        elif "close the app" in query:
            press.hotkey('alt','f4')
            speak("closing app...")

        elif "setting" in query:
            press.hotkey('winleft', 'i')
            speak("opening setting, please wait...")

        elif "new virtual desktop" in query:
                press.hotkey('winleft', 'ctrl', 'd')
                speak("making a new desktop, please wait")
                
        elif 'play music'in query:
            codePath = "C:\\Users\\rayb5\\Desktop\\Resso.lnk"
            os.startfile(codePath)
            speak("Opening Resso Music Player. Please Wait...")

        elif 'play' in query:
            song = query.replace('play', ' ')
            speak("playing" + song + "please wait...")
            pywhatkit.playonyt(song)

        elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("Set the time")
            a = input("Please tell the time :- ")
            alarm(a)
            speak("Done,sir")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%I:%M %P")    
            speak(f"Sir, the time is {strTime}")
       
        elif 'open facebook' in query:
            webbrowser.open('https://www.facebook.com/')
            speak("Opening Facebook Please Wait....")

        elif 'open Instagram' in query:
            webbrowser.open('https://www.instagram.com/')
            speak("Opening Instagram Please Wait....")

        elif "open notepad" in query:  # if open notepad in statement
            speak("opening notepad, please wait.....")  # speak
            codePath = "C:\\Windows\\System32\\notepad.exe" # location
            notepad = subprocess.Popen(codePath)  # location of a software you want tot opem
    
        elif "close notepad" in query:
            speak("closing notepad, please wait....")
            notepad.terminate()  # terminate

        elif 'open code' in query:
            codePath = "C:\\Users\\rayb5\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening Visual Studio Code Please Wait....")

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "logout" in query:
            speak('logging out in 5 second')
            os.system("shutdown - l")

        elif 'shutdown the system' in query:
            speak("your system has shutdown...")
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            speak("restarting your system...")
            os.system("shutdown /r /t 5")

        elif 'sleep the system' in query:
            speak("your system is now spleeping")
            os.system("rundll32.exe powrprof.dil,SetSuspendState 0.1.0")

        elif 'temperature' in query:
            search = "temperature in sindhanur"
            url = f"https://www.google.com/search?={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\rayb5\\Desktop\
                \Visual Studio Code.lnk"
            os.startfile(codePath)
            speak("Opening Visual Studio 2022 Please Wait....")

        elif 'switch the Window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'tell me news' in query:
            speak("Please Wait. Feteching the latest news..")
            news()

        elif 'information' in query:
            speak("Enter the target phone number with country code")
            number = input("Enter the target phone number with country code: ")
            phone = phonenumbers.parse(number)
            car = carrier.name_for_number(phone,"en")
            reg = geocoder.description_for_number(phone,"en")
            print(phone)
            speak(phone)
            print(time)
            speak(time)
            print(car)
            speak(car)
            print(reg)
            speak(reg)

        elif 'check' in query:
            print("Checking near by wifi password, pkease wait sir")
            speak("Checking near by wifi password, pkease wait sir")
            wifi()

        elif 'activate how to do mode' in query:
            speak("how to do mode is activate")
            while True:
                speak("Please tell me what you want to know sir.")
                how = takeCommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir, how to do mode is closed")
                        break
                    else:
                        max_result = 1
                        how_to = search_wikihow(how, max_result)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry sir, i am not able to find this.")

        elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)

        elif 'email' in query:
            speak("what should i say")
            query = takeCommand().lower()
            if "file" in query:
                email = gmail
                password = gpassword
                speak("please enter destination email")
                send_to_email = input("enter destination email:")
                query = takeCommand().lower()
                subject = query
                speak("and, what is the message for this email")
                query2 = takeCommand().lower()
                message = query2
                speak("sir please enter the correct path of the file into the shell")
                file_location = input("Please enter the path here: ")

                speak("Please wait, i am sending email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("Email has been sended")

            else:
                email = gmail
                password = gpassword
                speak("please enter destination email")
                send_to_email = input("enter destination email:")
                speak("Okay, what should i say")
                subject = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, message)
                server.quit()
                speak("Email has been sended")

        elif "ipl score" in query:
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )

        elif 'where i am' in query:
            speak("wait, let me check")
            try:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                url = 'https://get.geojs.io/'+ip+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']
                country = geo_data[country]
                speak(f"sir i am not sure, but i think we are in {city} city of {country} country")

            except Exception as e:
                speak("sorry, due to network issue i am not able to find where we are.")
                pass

        elif 'instagram profile' in query:
            speak("sir please enter the username correctly.")
            name = input("Enter username here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            speak("sir would you like to download profile picture of this account.")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak(" i am done, profile pictureis saved in our main folder. now i am ready for next command")
            else:
                pass

        elif 'how much power left' in query or 'how much power we have' in query or 'battery' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f'sir our system have {percentage} percent battery')
            if percentage>=75:
                speak("we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                speak("we should connect our system to charging point to charge our battery")
            elif percentage>=15 and percentage<=30:
                speak("we don't have enough power to work, please connect to charging")
            elif percentage<=15:
                speak("we have very low power, please connect to charging the system will shutdown very soon")

        elif 'take a screenshot' in query:
            speak("sir, please tell me the name for screenshot file")
            name = takeCommand().lower()
            speak("please hold the screen for few seconds, i am taking screenshot")
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done, the screenshot is saved in our main folder. now i am ready for next command")

        elif'do some calculation' in query or 'can you calculate' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Say what you want to calculate, example: 3 plus 3")
                print("listening....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    '*' : operator.mul,
                    '/' : operator.__truediv__,
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is:")
            speak(eval_binary_expr(*(my_string.split())))
            
        elif 'you can sleep' in query or 'sleep' in query or 'sleep now' in query:
            speak("Thanks you sir, i am going to sleep you can call me anytime..")
            break

def wakeup():
    press.hotkey('esc')
    print("verification successful")
    speak("verification successful")
    print("welcome back sir")
    speak("welcome back sir")
    print("jarvis is now online")
    speak("jarvis is now online")
    print("please say wake up to activate jarvis")
    speak("please say wake up to activate jarvis")
    while True:
        query = takeCommand()
        if 'jarvis' in query:
            TaskExecution()

        elif 'add a new face' in query:
            sample() 

        elif 'train' in query:
            modeltrainer()

        elif "change password" in query:
            speak("What's the new password")
            new_pw = input("Enter the new password\n")
            new_password = open("password.txt","w")
            new_password.write(new_pw)
            new_password.close()
            speak("Done sir")
            speak(f"Your new password is{new_pw}")

        elif 'goodbye jarvis' in query or 'go now' in query:
            speak("thank you for using jarvis sir, have a good day")
            exit()

def sample():
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #create a video capture object which is helpful to capture videos through webcam
    cam.set(3, 640) # set video FrameWidth
    cam.set(4, 480) # set video FrameHeigh

    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    speak("Enter a Numeric user ID  here: ")
    face_id = input("Enter a Numeric user ID  here:  ")
    

    print("Taking samples, look at camera ....... ")
    speak("Taking samples, look at camera .......")
    count = 0 # Initializing sampling face count

    while True:

        ret, img = cam.read() #read the frames using the above created object
        converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #The function converts an input image from one color space to another
        faces = detector.detectMultiScale(converted_image, 1.3, 5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2) #used to draw a rectangle on any image
            count += 1

        
            cv2.imwrite("samples/face." + str(face_id) + '.' + str(count) + ".jpg", converted_image[y:y+h,x:x+w])
            # To capture & Save images into the datasets folder

            cv2.imshow('image', img) #Used to display an image in a window

        k = cv2.waitKey(100) & 0xff # Waits for a pressed key
        if k == 27: # Press 'ESC' to stop
            break
        elif count >= 10: # Take 50 sample (More sample --> More accuracy)
            break

    print("Samples taken now closing the program....")
    speak("Samples taken now closing the program....")
    cam.release()
    cv2.destroyAllWindows()

def modeltrainer():
    path = 'samples' # Path for samples already taken

    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #Haar Cascade classifier is an effective object detection approach
    def Images_And_Labels(path): # function to fetch the images and labels
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        faceSamples=[]
        ids = []

        for imagePath in imagePaths: # to iterate particular image path
            gray_img = Image.open(imagePath).convert('L') # convert it to grayscale
            img_arr = np.array(gray_img,'uint8') #creating an array

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_arr)

            for (x,y,w,h) in faces:
                faceSamples.append(img_arr[y:y+h,x:x+w])
                ids.append(id)
            
        return faceSamples,ids
    
    print("Training faces. It will take a few seconds. Wait ...")
    speak("Training faces. It will take a few seconds. Wait ...")

    faces,ids = Images_And_Labels(path)
    recognizer.train(faces, np.array(ids))

    recognizer.write('trainer/trainer.yml')  # Save the trained model as trainer.yml

    print("Model trained, Now we can recognize your face.")
    speak("Model trained, Now we can recognize your face.")


if __name__ == "__main__":

    recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
    recognizer.read ('trainer/trainer.yml')   #load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

    font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


    id = 2 #number of persons you want to Recognize


    names = ['','Bittu']  #names, leave first empty bcz counter starts from 0



    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
    cam.set(3, 640) # set video FrameWidht
    cam.set(4, 480) # set video FrameHeight

# Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

# flag = True

    while True:

        ret, img =cam.read() #read the frames using the above created object

        converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

        faces = faceCascade.detectMultiScale( 
            converted_image,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
            )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

            id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image
            speak("please verify your face")
            speak("verifaying your face, please wait")
        # Check if accuracy is less them 100 ==> "0" is perfect match 
            if (accuracy < 100):
                id = names[id]
                accuracy = "  {0}%".format(round(100 - accuracy))
                cv2.destroyAllWindows()
                wakeup()

            else:
                id = "unknown"
                accuracy = "  {0}%".format(round(100 - accuracy))
        
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

# Do a bit of cleanup
    print("Thanks for using this program, have a good day.")
    speak("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()
