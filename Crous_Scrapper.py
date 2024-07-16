import re
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
browser.get('https://trouverunlogement.lescrous.fr/tools/36/search?bounds=5.2286902_43.3910329_5.5324758_43.1696205')
# browser.get('https://trouverunlogement.lescrous.fr/tools/31/search?bounds=6.7872143_47.6713057_6.8948707_47.6203259')


def test_chargement():
    page_source = browser.page_source  # Get the page source

    # Use a regular expression with optional 's' character
    match = re.search(r'CITE LUMINY', page_source)

    if match:
        send_email_2_me(
        f"CROUS AVAILIBLE CITE LUMINY", "GO NOW CROUS DISPO ! CORDIALMEENT")
    else:
        browser.refresh()
        time.sleep(20)
        print('Nothing .....')
        test_chargement()



def send_email_2_me(msg, sub):
    print(msg, sub)
    mail = "croustest@outlook.com"
    password = "Lyesipog@@13102001"
    msg = MIMEMultipart()
    msg['From'] = mail
    msg['To'] = mail
    msg['Subject'] = str(sub)
    message = str(msg)
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.office365.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login(mail, password)
    mailserver.sendmail(mail, mail, msg.as_string())
    mailserver.quit()


test_chargement()
