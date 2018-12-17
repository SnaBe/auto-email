#Our config containing our dictionaries
from config import details
#Let us use the chrome web browser for automation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Import times sleep
from time import sleep
users = ['fynboen1999@gmail.com', 'thesilverflekker@gmail.com']
#Our custom email function
def mail():
	#Log succes to the given web page
	print('The bot made it to ' + details['portal_url'])
	#Find the email element
	driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(details['email_address'])
	#Click the next button
	driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
	#Sleep so the page can load
	sleep(1)
	#Find the password element after a quick delay
	driver.find_element_by_name('password').send_keys(details['email_password'])
	#Click the next button
	driver.find_element_by_id('passwordNext').click()
	#Sleep
	sleep(1)
	#Click the 'Write' button
	driver.find_element_by_xpath('//*[@id=":kb"]/div/div').click()
	#Wait for the pop element to load
	sleep(5)
	#Loop trough a email list and fill out
	for user in details['users']:
		#Users to email
		print('We\'ll email: ' + user + ' regarding ' + details['subject'])
		#Our to element
		to = driver.find_element_by_xpath('//*[@id=":q3"]')
		#Send the users email and press enter
		sleep(4)
		to.send_keys(user)
		to.send_keys(Keys.ENTER)
	#Continue with mailing proces
	print('For-loop is done.')
	#Send our subject
	driver.find_element_by_xpath('//*[@id=":pl"]').send_keys(details['subject'])
	#Send the mail subject
	driver.find_element_by_xpath('//*[@id=":qq"]').send_keys(details['message'])
	sleep(0.5)
	#Click the send button
	driver.find_element_by_xpath('//*[@id=":pb"]').click()
	sleep(2)
	#Quit the driver
	driver.quit()

#Only if run as a script
if __name__ == '__main__':
	#Our chrome driver and its path
	driver = webdriver.Chrome('./chromedriver/chromedriver.exe')
	#What url our driver should go to (portal_url)
	driver.get(details['portal_url'])
	#Call our function
	mail()
