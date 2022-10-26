from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

query = input("What images U like :: ")

driver = webdriver.Chrome('C:\Program Files\chromedriver.exe')   \\chromedriver path

driver.maximize_window()

driver.get('https://images.google.com/')


box = driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

box.send_keys(query)

box.send_keys(Keys.ENTER)

def scroll_to_bottom():
    last_height = driver.execute_script('\
	return document.body.scrollHeight')

    while True:
        driver.execute_script('\
		window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)

        new_height = driver.execute_script('\
		return document.body.scrollHeight')

    
        try:
            driver.find_element_by_css_selector(".YstHxe input").click()
            time.sleep(3)

        except:
            pass

        if new_height == last_height:
            break

        last_height = new_height


scroll_to_bottom()

for i in range(1, 40):

    try:
        img = driver.find_element('xpath' ,
            '//*[@id="islrg"]/div[1]/div[' +
            str(i) + ']/a[1]')
        img.screenshot('C:\\Users\\sreem\\OneDrive\\Desktop\\New\\images' + query + ' (' + str(i) + ').png')    \\images download path
        time.sleep(0.2)

    except:
        continue
print('Close driver')
driver.close()
