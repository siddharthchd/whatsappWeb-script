from selenium import webdriver 

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

name = input('Enter name of user / group : ')
msg = input('Enter message : ')
count = int(input('Enter count : '))
msgList = msg.split()

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msgBox = driver.find_element_by_class_name('_3uMse')

for i in range(count):
    for j in range(len(msgList)):
        msgBox.send_keys(msgList[j])
        button = driver.find_element_by_class_name('_1U1xa')
        button.click()
