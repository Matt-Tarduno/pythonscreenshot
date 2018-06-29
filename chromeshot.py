from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# preferences to allow flash player (from stackoverflow)

prefs = {
    "profile.default_content_setting_values.plugins": 1,
    "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
    "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    "PluginsAllowedForUrls": "http://www.dot.ca.gov/d4/d4cameras/ct-cam-pop-E80_at_Lower_Deck_Bryant_St_OR.html"
}


options= webdriver.ChromeOptions()
options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options = options)

browser.get('http://www.dot.ca.gov/d4/d4cameras/ct-cam-pop-E80_at_Lower_Deck_Bryant_St_OR.html') #webcam

time.sleep(20) #allow to load properly 


# loop and take screenshots 
for i in range(5): 
	time.sleep(20) # wait

	# would probably be more efficient to save just the small screen? 

	browser.get_screenshot_as_file('shots/file_'+str(i)+'.png') #save screenshot



# question: will this work on an amazon EC2 instance?? 





