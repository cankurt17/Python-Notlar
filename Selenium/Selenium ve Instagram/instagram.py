

from selenium import webdriver
import time

browser=webdriver.Firefox()
browser.get("https://www.instagram.com/accounts/login/")

time.sleep(2)

username=browser.find_element_by_name("username")
password=browser.find_element_by_name("password")

username.send_keys("cankurt46")
password.send_keys("29963207974")

loginButton= browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
loginButton.click()

time.sleep(7)

kayıtSorusu = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
kayıtSorusu.click()

time.sleep(5)

browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

time.sleep(2)

profilButton = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span")
profilButton.click() 
time.sleep(2)
browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]").click() 

time.sleep(2)

buttons=browser.find_elements_by_css_selector(".Y8-fY")
takipButton=buttons[2]
takipButton.click()

time.sleep(2)


jsKodları="""
followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight)
var lenOfPage=followers.scrollHeight;
return lenOfPage;
"""

 

#################################################### Scrool Özelliği

lenOfPage = browser.execute_script(jsKodları)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3) 
    lenOfPage = browser.execute_script(jsKodları)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

####################################################

followersList = []

followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")

for follower in followers:
    followersList.append(follower.text)

with open("followers.txt","w",encoding="UTF-8") as file:
    for follower in followersList:
        file.write(follower+"\n")
    

time.sleep(10)












