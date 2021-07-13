from plyer import notification
import time


if __name__=="__main__":
    while(True):
        notification.notify(
            title = "You are requested to please drink water.",
            message = "Drinking water improves heart health, improves muscle building, prevents bad breadth, prevents backaches, increases waste removal.",
            app_icon = "watericon.ico",
            timeout = 10
        )
        time.sleep(60*60) # here, 60*60 means 1 hours.
