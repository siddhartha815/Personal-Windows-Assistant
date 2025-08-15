import webbrowser
import time

def website_opener(domain):
    try:
        webbrowser.open_new_tab(domain)
        time.sleep(10)

        return True
    except Exception as e:
        print(e)

        return False