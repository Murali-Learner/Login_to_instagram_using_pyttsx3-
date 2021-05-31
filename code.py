import pyttsx3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class tts:
    def txttospeech():    
        engine=pyttsx3.init()
        engine.setProperty('rate',150)
        engine.setProperty('voice', 'english_rp+f3')
        
        name=input("enter your name : ")
        while True:
            answer=input(f"hello {name},what do you want ?   \n")
            if answer=="instagram" and answer != 'q' :
                
                engine.say('Login to, '+answer)
                
                username=input("enter ur username :")
                password=input("enter ur password :")
                engine.runAndWait()

                
                print("""
 
 _________________________________________________________________________________________________________
     _                              ______               __                                               
     /                  ,             /                  /                                                
 ---/-------__----__--------__-------/-------__---------/-----__---__--_/_----__----__---)__----__---_--_-
   /      /   ) /   ) /   /   )     /      /   )       /    /   ) (_ ` /    /   ) /   ) /   ) /   ) / /  )
 _/____/_(___/_(___/_/___/___/_____/______(___/_____ _/_ __/___/_(__)_(_ __(___(_(___/_/_____(___(_/_/__/_
                  /                                                                 /                     
              (_ /                                                              (_ /                      
 
""")
                driver = webdriver.Chrome(executable_path="./chromedriver")
                driver.maximize_window()
                driver.get(r'https://www.instagram.com/')
                driver.implicitly_wait(3)

                usernameBtn=driver.find_element_by_name('username')
                usernameBtn.clear()
                usernameBtn.send_keys(username)

                passwordBtn=driver.find_element_by_name('password')
                passwordBtn.clear()
                passwordBtn.send_keys(password)

                loginBtn=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
                loginBtn.click()
                print(' Login Successfully')

                notnowBtn=driver.find_element(by=By.XPATH,value='//button[contains(text(), "Not Now")]')
                notnowBtn.click()
                print(' notnow clicked')
                time.sleep(2)

                notnowBtn1=driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
                notnowBtn1.click()
                print(' notnow1 clicked')
                time.sleep(2)

            elif answer=="q" or answer=='exit' :
                engine.say("Good bye")
                engine.runAndWait()
                break
            else:
                engine.say(answer)
                engine.runAndWait()
      
  
speech=tts()
tts.txttospeech()

        
