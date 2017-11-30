from selenium import webdriver
browser = webdriver.Firefox()

browser.get('http://gmail.com')

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('MyUserName')
nextButton = browser.find_element_by_id('next')
nextButton.click()
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('MyPassword')
signinButton = browser.find_element_by_id('signIn')
signinButton.click()
