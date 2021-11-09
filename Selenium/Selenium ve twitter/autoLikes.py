

from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get("https://twitter.com/")
time.sleep(1)

giris_yap=browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/a[2]")

giris_yap.click()

time.sleep(1)

username = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")
password = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")

username.send_keys("cankurt171")
password.send_keys("29963207974Can.")

time.sleep(1)

login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div")

login.click()

time.sleep(1)

aramaSayfasi=browser.find_element_by_xpath("/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]")

aramaSayfasi.click()
time.sleep(1)

searchArea = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")

searchArea.send_keys("#yazilimayolver")
time.sleep(3)

searchButton = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div/div[2]/div")
searchButton.click()

time.sleep(1)

elements = browser.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1777fci.r-11cpok1.r-1ny4l3l.r-bztko3.r-lrvibr") 
for element in elements:
    try:
        if element.get_attribute("data-testid")=="like":
            element.click() 
    except Exception:
        print("Bir sorun oluştu...")
       

####################################################        Scrool Özelliği

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3) 

    elements = browser.find_elements_by_css_selector(".css-18t94o4.css-1dbjc4n.r-1777fci.r-11cpok1.r-1ny4l3l.r-bztko3.r-lrvibr") 
    for element in elements:
        try:
            if element.get_attribute("data-testid")=="like":
                element.click() 
        except Exception:
            print("Bir sorun oluştu...")


    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(1)

####################################################


    
  
