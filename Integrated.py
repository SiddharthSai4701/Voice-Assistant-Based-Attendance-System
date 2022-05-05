'''
Main program!!
'''
import pandas as pd
import pyttsx3
import speech_recognition as sr
from datetime import date as d
import smtplib


# Opening the excel file and adding the present date column.
atd = pd.read_excel("Attendance_sheet2.xlsx",sheet_name = 'Sheet1')

sheet_id = "1Y9s6f1ttdYJnbLk6tdFwcf1EHWLxL9y8s-C80bnC034"
nick = pd.read_excel(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx") #For nicknames

date = str(d.today())
atd[date] = 0

n = len(atd)

# Creating a recognizer object
r = sr.Recognizer()

# SpeakText function is to make the bot read out things
def SpeakText(command):
    global engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Bot voice controls
def voice_control():
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')      #getting details of current voice
    engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female and 0 for male


# Actual attendance taker
def attendance():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        r.adjust_for_ambient_noise(source,duration = 0.2)
        SpeakText("Sai Raam! I am Phyborg and I will be taking your attendance!! Let's begin") 
        for i in range(n):
            SpeakText(f"{atd.Names[i]}")
            
            try:
                print("Listening...")
                audio = r.listen(source,5,5)
                text = r.recognize_google(audio,language = 'en-in')
                
                if text == 'present':
                    SpeakText(f"Hello {nick.Nicknames[i]}")
                    atd[date][i] = 'Present'
                    
                else:
                    SpeakText(f"{atd.Names[i]} are you present?")
                    
                    try:
                        print("Listening...")
                        audio = r.listen(source,5,5)
                        text = r.recognize_google(audio,language = 'en-in')
                        
                        if text == 'present':
                            SpeakText(f"Hello {nick.Nicknames[i]}")
                            atd[date][i] = 'Present'
                        else:
                            SpeakText(f"{atd.Names[i]}, you have been marked absent.")
                            atd[date][i] = 'Absent'
                    except Exception:
                        SpeakText(f"{atd.Names[i]}, you have been marked absent.")
                        atd[date][i] = 'Absent'
                
            except Exception:
                SpeakText(f"I repeat, are you present {atd.Names[i]}")
                try:
                    print("Listening...")
                    audio = r.listen(source,5,5)
                    text = r.recognize_google(audio,language = 'en-in')
                    
                    if text == 'present':
                        SpeakText(f"Hello {nick.Nicknames[i]}")
                        atd[date][i] = 'Present'
                    else:
                        SpeakText(f"{atd.Names[i]}, you have been marked absent.")
                        atd[date][i] = 'Absent'
                except Exception:
                        SpeakText(f"{atd.Names[i]}, you have been marked absent.")
                        atd[date][i] = 'Absent'


# Email automation. Sends the attendance data to as an email.
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('phyborg2022@gmail.com','jthxydiypubhqmvj') #Use gmail appp password
    
    subject='Test'
    body1 = '''
    Sairam Sir, this is the attendance for today\n
    '''
    body2 = atd.loc[:,['Names',date]]
    msg = f"subject:{subject} \n\n\n {body1}\n{body2}"
    
    server.sendmail('phyborg2022@gmail.com','abishekh@sssihl.edu.in',msg) #From,to,message
    print("Message sent")
    

voice_control()
attendance()
SpeakText('Thank you! Your attendance has been taken')
send_mail()

atd.to_excel("Attendance_sheet2.xlsx",sheet_name = 'Sheet1',index = False)
###########################################################################################