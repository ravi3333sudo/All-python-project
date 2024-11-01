from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message="Rest is vital for better mental health",
            app_icon= r"c:\\users\\91971\\Documents\\Downloads\\images.png",
            timeout=5)
        time.sleep()
