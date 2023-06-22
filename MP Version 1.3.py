
#install python library

import pyttsx3
import PyPDF2

#user interface
from tkinter.filedialog import *

#extract a file from the device
book = askopenfilename()

pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages

#html window

#write-html-2-mac.py
import webbrowser

f = open('book.html','w')

#display file
message = book 

f.write(message)
f.close()

#Change path to reflect file data
file_input = book

webbrowser.open_new_tab(file_input)

#end html

#opertaion on file
for num in range(0, pages):
    
    page = pdfreader.getPage(num)
    text = page.extractText()
   
    #initialize the module
    text_to_speech = pyttsx3.init()
   
    #voice call
    voices = text_to_speech.getProperty('voices')
    text_to_speech.setProperty('voices', voices)
   
    #adjust the speed
    text_to_speech.setProperty('rate', 200)

    #convert text to speech
    text_to_speech.say(text)

    #listen to audio
    text_to_speech.runAndWait()

#end loop

#END 
