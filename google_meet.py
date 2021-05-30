#This is a program to automate logging into G-Meet as long as you system is awake.
#When used in combination with crontab, it can start your meeting at the correct time and you will never be late for ameeting again :)
#The same meeting ID has to be used.

#Import all the necessary modules.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#my_details.py has all the attributes that are to be filled by the user.
import my_details

#If you haven't modified the my_details.py file, then do it else your details will not be taken only the default balues will be considered.
email=my_details.email
password=my_details.password
meeting_id=my_details.meeting_id
duration_in_min=my_details.duration_in_min

#Before you run the program, fill in the following details.


#Default preferences= Mic: OFF, Camera=OFF, Notifications=Allowed

chrome_pref = Options()
chrome_pref.add_experimental_option("prefs", {
	"profile.default_content_setting_values.media_stream_mic": 1,
	"profile.default_content_setting_values.media_stream_camera": 1,
	"profile.default_content_setting_values.geolocation": 0,
	"profile.default_content_setting_values.notifications": 1
})

#Chrome driver is initialised. You may use Geckodriver as well, if you are a Firefox user. 

browser=webdriver.Chrome(options=chrome_pref)

#The browser window is maximized
browser.maximize_window()

#Google meet is opened and the program halts for 5 seconds.
browser.get('https://meet.google.com/')

time.sleep(5)

#It clicks on sign in button to sign in to your G-Mail account.
element=browser.find_element_by_xpath("/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a").click()
time.sleep(5)

#Your User ID is entered into the input box.
element=browser.find_element_by_id("identifierId")
element.send_keys(email)
element.send_keys(Keys.RETURN)
time.sleep(5)

#Your password is entered as well. You are signed in.... 
# This happens provided your credentials are correct and you have given the disabled additional security authentication for the system in use. 
element=browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
element.send_keys(password)
element.send_keys(Keys.RETURN)
time.sleep(5)

#The meeting ID is entered and the 'Ask to join' page is opened.
element=browser.find_element_by_id("i3")
element.send_keys(meeting_id)
element.send_keys(Keys.RETURN)
time.sleep(5)

#The Mic is turned off.
element=browser.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
time.sleep(2)

#Camera is turned off.
element=browser.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
time.sleep(2)

#Join button is clicked.
element=browser.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
time.sleep(2)

#Meeting ends after the given duration.
end_it=duration_in_min*60
time.sleep(end_it)
browser.quit()
