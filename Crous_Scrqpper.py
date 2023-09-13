import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

browser = webdriver.Chrome(options=options)
browser.implicitly_wait(5)  # seconds
browser.get('HERE CROUSS URL')


def test_chargement():
    if "Logement individuel" in browser.page_source:
        print('GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
        send_email_2_me("CROUS AVAILIBLE", "GO NOW CROUS DISPO ! CORDIALMEENT")
    else:
        browser.refresh()
        time.sleep(20)
        print('Nothing .....')
        test_chargement()


def send_email_2_me(msg, sub):
    print(msg, sub)
    mail = "YOUR EMAIL"
    gmail_code = "YOUR Gmail application-specific password"
    msg = MIMEMultipart()
    msg['From'] = mail
    msg['To'] = mail
    msg['Subject'] = str(sub)
    message = str(msg)
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(mail, gmail_code)
    mailserver.sendmail(mail, mail, msg.as_string())
    mailserver.quit()


test_chargement()
