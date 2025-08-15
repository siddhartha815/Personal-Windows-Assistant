import AppOpener

def open_desktop_app(app_name):
    AppOpener.open(app_name, match_closest=True)
    return True

def close_desktop_app(app_name):
    AppOpener.close(app_name, match_closest=True)
    return True