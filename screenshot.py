from selenium import webdriver

# doesn't support flash player :/

driver = webdriver.PhantomJS()
driver.set_window_size(2048, 2048) # set the window size that you need 
driver.get('http://www.dot.ca.gov/d4/d4cameras/ct-cam-pop-E80_at_Powells_St_Or.html')
driver.save_screenshot('screenshot.png')