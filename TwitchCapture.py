import socket
import sys
import string
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

print ("### Hello and welcome to VAC bot ### \r\n")
HOST = "irc.twitch.tv"      
CHANNEL = raw_input("What channel would you like to join? ").lower()
NICK = "vac_bot_v1"
PASS = "oauth:rs4hqbqptqoxw5gm8x4v2b49p1784d"

chromedriver = "C:\Python27\Scripts\chromedriver.exe"
browser = webdriver.Chrome(chromedriver)
browser.get("https://www.twitch.tv/" + CHANNEL)

### Sends a message to the chatroom ###
def sendMessage(s,message):
	messageMain = "PRIVMSG " + CHANNEL + " :" + message
	s.send(messageMain + "\r\n")
	print("Sent: " + messageMain)

### Login Page 	
def TwitchLogIn():
	
	
	UsernameBoxID = 'username'
	PasswordBoxID = 'password'
	TwitchUsername = 'vac_bot_v1'
	TwitchPassword = 'LooneyCooney14'	
	
	LoginButton = WebDriverWait(browser,30).until(lambda browser: browser.find_element_by_css_selector('button.follow-button.button.is-initialized.is-logged-out.button--icon'))
	LoginButton.click()
	
	WebDriverWait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME,'passport')))
	UsernameBox = WebDriverWait(browser,10).until(lambda browser: browser.find_element_by_name(UsernameBoxID))
	UsernameBox.send_keys(TwitchUsername)
	PasswordBox = browser.find_element_by_name(PasswordBoxID)
	PasswordBox.send_keys(TwitchPassword)
	LoginButton_2 = browser.find_element_by_css_selector('button.primary.button.js-login-button')
	LoginButton_2.click()
	
	
	
	
	
###VAC counter function ###
def counter(text):
	number = 0
	text=s.recv(2040)  
	print text
	if ("vac") in text.lower():
		end = time.time() + 30
		number = number + 1
		while time.time() < end  :   	
			text=s.recv(2040)  
			if ("vac") in text.lower():
				number = number + 1
				print (text)
				if number == 5:
					ClipButton = WebDriverWait(browser,5).until(lambda browser: browser.find_element_by_css_selector('button.player-button.player-button--clips.js-control-clips'))
					ClipButton.click()
					end = time.time()
					time.sleep(30)
					
			else: 
				print (text)
				
		

###Socket connection###
s = socket.socket() 
print "Connecting to:"+HOST
s.connect((HOST, 6667))                                                         
s.send("PASS " + PASS + "\r\n")
s.send("USER "+ NICK +" "+ NICK +" "+ NICK +"\n") 
s.send("NICK "+ NICK +"\n")                               
s.send("JOIN #"+ CHANNEL +"\n") 

###Loading sequence###
Loading = True
while Loading:    
   text=s.recv(2040)  
   print text
   if text.find("End of /NAMES list") != -1:
		Loading = False
   if text.find('PING') != -1:                          
      s.send('PONG ' + text.split() [1] + '\r\n')


TwitchLogIn()	  
sendMessage(s,"Successfully joined chat")
while True:
	counter(text)
  




