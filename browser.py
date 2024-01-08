import os.path
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


cookies_ent = {
    "BIGipServer~ADMIN~pool-WAYF-https" : "rd1o00000000000000000000ffff0a6016e7o80",
    "JSESSIONID" : "BC306071A1943A7A576A850568341DE0.tc4"
    }


def save_cookies():
    print("Saving cookies in " + selenium_cookie_file)
    pickle.dump(driver.get_cookies() , open(selenium_cookie_file,"wb"))

def load_cookies():
    if os.path.exists(selenium_cookie_file) and os.path.isfile(selenium_cookie_file):
        print("Loading cookies from " + selenium_cookie_file)
        cookies = pickle.load(open(selenium_cookie_file, "rb"))

        # Enables network tracking so we may use Network.setCookie method
        driver.execute_cdp_cmd('Network.enable', {})

        # Iterate through pickle dict and add all the cookies
        for cookie in cookies:
            # Fix issue Chrome exports 'expiry' key but expects 'expire' on import
            if 'expiry' in cookie:
                cookie['expires'] = cookie['expiry']
                del cookie['expiry']

            print("--------changing cookie--------")
            if cookie['name'] in cookies_ent.keys:
                print(f"replacing value of {cookie['name']} ( {cookie['value']}  -> {cookies_ent[cookie['name']]} )")
                cookie['value'] = cookies_ent[cookie['name']]

            # Set the actual cookie
            driver.execute_cdp_cmd('Network.setCookie', cookie)

        # Disable network tracking
        driver.execute_cdp_cmd('Network.disable', {})
        return 1

    print("Cookie file " + selenium_cookie_file + " does not exist.")
    return 0

def pretty_print(pdict):
    for p in pdict:
        print(str(p))
    print('',end = "\n\n")


# Minimal settings
selenium_cookie_file = 'cookies.txt'

browser_options = Options()
# browser_options.add_argument("--headless")

ent_url = "https://wayf.cesi.fr/login?service=https%3A%2F%2Fent.cesi.fr%2Fservlet%2Fcom.jsbsoft.jtf.core.SG%3FPROC%3DIDENTIFICATION_FRONT"
ent_accueil_url = "https://ent.cesi.fr/accueil-apprenant"

# Open a driver, get a page, save cookies
driver = webdriver.Chrome(chrome_options=browser_options)
driver.get(ent_url)
save_cookies()
pretty_print(driver.get_cookies())


# Rewrite driver with a new one, load and set cookies before any requests
driver = webdriver.Chrome(chrome_options=browser_options)
load_cookies()
driver.get(ent_accueil_url)
pretty_print(driver.get_cookies())