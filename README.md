# websites-scraping

This script main purpose is to scrap CROUS logement and notify when there is one availible.

## Dependencies

- Selenium
- email
- smtplib

## How to use

1. Install the dependencies
2. Download google chrome V 1.14 /u can find an exe here /
   (or download the chromedriver.exe compatible with ur chrome version , make sure chromedriver is inside the folder of the script)
3. Update the script with your Crous URL(Search for ur region in crous website and copy link , ez)
4. Change variables _mail_ and _code_ with ur email and ur Gmail code (in order to get this gmail code , follow here https://support.google.com/accounts/answer/185833?hl=en)
5. Run the script
6. Wait for the email

_ps : if u want to test if the email thingy work , just call the function outside the loop and test._
