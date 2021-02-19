from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException
from tkinter import *
import screens
import time
from functools import partial
import os.path
# import smtplib
# from email.message import EmailMessage

# Enter you MacID and Password here! (between the paraenthesis)
myUsername = ""
myPassword = ""

# Please enter the path to your chrome driver between the parenthesis
chromeDriverPath = ""

username = '//*[@id="userid"]'
password = '//*[@id="pwd"]'
login = '//*[@id="login"]/div/div[1]/div[6]/span/input'
gradesbutton = '//*[@id="win0divPTNUI_LAND_REC_GROUPLET$9"]'
continue1 = '//*[@id="#ICOK"]'

changeterm1 = '//*[@id="DERIVED_SSS_SCT_SSS_TERM_LINK"]'
changeterm2 = '//*[@id="SSR_DUMMY_RECV1$sels$1$$0"]'
changeterm3 = '//*[@id="DERIVED_SSS_SCT_SSR_PB_GO"]'
changeterm4 = '//*[@id="#ICOK"]'


def getGrades(Current, Previous):

    # Headless driver
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(executable_path=chromeDriverPath, chrome_options=options)
    
    # Development Driver
    # driver = webdriver.Chrome(chromeDriverPath)
    
    # Get mosaic webpage
    driver.get('https://epprd.mcmaster.ca/psp/prepprd/?cmd=login')

    # print("Username and password are not working, please try again")
    # Login Process
    enterData(username, myUsername, driver)
    time.sleep(.5)
    enterData(password, myPassword, driver)
    time.sleep(.5)
    clickButton(login,driver)
    time.sleep(.5)

    moveTo(gradesbutton, driver)
    time.sleep(.5)
    clickButton(gradesbutton, driver)
    time.sleep(.5)
    clickButton(continue1,driver)
    time.sleep(.5)

    # Collect current term grades
    if (Current):
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    
    else:
    # Collect last term grades (comment out for current term)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        clickButton(changeterm1,driver)
        time.sleep(.5)
        clickButton(changeterm2,driver)
        time.sleep(.5)
        clickButton(changeterm3,driver)
        time.sleep(.5)
        driver.switch_to_default_content()
        clickButton(changeterm4,driver)
        time.sleep(.5)
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

    # Path to first grades
    grade1xpath = '/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[8]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/'
    grades = []
    class1xpath = '/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[8]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/'
    classes = []

    # Collect loop
    try:
        i = 2
        while True:
            grade_path = grade1xpath + "tr[" + str(i) + "]/td[5]/div/span"
            grades.append(driver.find_element_by_xpath(grade_path).text)

            class_path = class1xpath + "tr[" + str(i) + "]/td[1]/div/span/a"
            classes.append(driver.find_element_by_xpath(class_path).text)
            i = i + 1
    except (ElementNotVisibleException, WebDriverException, NoSuchElementException):
            pass
    

    i=0

    grade_msg = "Class: Grade"
    for i in range(len(classes)):
        grade_msg += "\n" + classes[i] + ": " + grades[i]
        i = i+1

    time.sleep(.5)

    print(grade_msg)
    
    root = Tk() 
    root.title("Results!")
    root.geometry("300x300")

    contentFrame = Frame(root)
    contentFrame.grid(columnspan=1)

    window = screens.Screens(contentFrame)
    home = screens.Home(contentFrame,window)
    home.gradesMsg(grade_msg)

    return grade_msg
    

# Button function
def clickButton(xpath ,driver):
    try:
        driver.find_element_by_xpath(xpath).click()
        pass
    except Exception:
        time.sleep(1)
        clickButton(xpath, driver)

def moveTo(xpath, driver):
    try:
        I = driver.find_element_by_xpath('//*[@id="win0groupletPTNUI_LAND_REC_GROUPLET$9"]')
        a = ActionChains(driver)
        a.move_to_element(I).perform()
    except Exception:
        time.sleep(1)
        moveTo(xpath, driver)

# Enter data function
def enterData(field, data ,driver):
    try:
        driver.find_element_by_xpath(field).send_keys(data)
        pass
    except Exception:
        time.sleep(1)
        enterData(field, data, driver)


# Get username and password non working method
# file = open("user.txt","r")
# line = file.read()
# myUsername,myPassword = line.split("\t") 
# str(myUsername.strip())
# str(myPassword.strip())
# file.close()