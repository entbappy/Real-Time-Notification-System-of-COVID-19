"""
Author : Bappy Ahmed
Email : bappymalik4161@gmail.com
Date : 10 sept 20
"""

from plyer import notification  #For getting notification
import requests
import time

from bs4 import BeautifulSoup  #To pull the data in a different manner


# This function will give me the notification
def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'H:\Parsonal\Practice\Mega Projects\COVID Notification system\corona.ico',
        timeout = 5
    )



def getData(url):
    r= requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        # notifyMe("Hey Bappy","Lets stop spreading of the virus togethoer")
        myHtmlData = getData("https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Bangladesh_medical_cases_by_division")
        # myHtmlData = getData("https://www.mohfw.gov.in/")
        soup = BeautifulSoup( myHtmlData, 'html.parser')
        # print(soup)
        mystr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            mystr += tr.get_text()
        itemlist= mystr.split('\n\n')
        
        lis = []
        for item in itemlist[106:108]:
            new = item
            lis.append(new)
        print(lis)
        nTittle = "Case of COVID-19"
        nText = f"{lis[0]}: {lis[1]}"
        
        notifyMe(nTittle,nText)
        time.sleep(20)





    