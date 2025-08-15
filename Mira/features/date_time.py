import datetime


def date():
    try:
        date = datetime.datetime.now().strftime("%A") + " " + datetime.datetime.now().strftime("%d") + " " + datetime.datetime.now().strftime("%B") + "," + datetime.datetime.now().strftime("%Y")
    except Exception as e:
        print(e)
        date = False
    return date


def month():
    try:
        month = datetime.datetime.now().strftime("%B")
    except Exception as e:
        print(e)
        month = False
    return month


def year():
    try:
        year = datetime.datetime.now().strftime("%Y")
    except Exception as e:
        print(e)
        year = False
    return year


def weekday():
    try:
        day = datetime.datetime.now().strftime("%A") + " " + datetime.datetime.now().strftime("%d") + " " + datetime.datetime.now().strftime("%B") + "," + datetime.datetime.now().strftime("%Y")
    except Exception as e:
        print(e)
        day = False
    return day


def time():
    try:
        time = str(datetime.datetime.now().strftime("%I")) + ":" + str(datetime.datetime.now().strftime("%M")) + " " + datetime.datetime.now().strftime("%p")
    except Exception as e:
        print(e)
        time = False
    return time