#This project is implented using pure python code with libraries such as time.
#Point to be noted that is: 
#this works for mac, linux, windows.
#This is a simple project and it will come in handy when you are working productive.
#The moral of the project is to work productive each day and not to be distracted by different websites such as facebook, instagram, youtube.etc
#To run this program, run in as the adminstrator.

#I had fun building this project and I am sure you will have too.

import time #importing time libraries for to get the time
from datetime import datetime as dt 

#hosts_path="/etc/hosts"
hosts_path= "C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["https://www.facebook.com/","facebook.com","youtube.com","https://www.youtube.com/"] # The url of the websites to be blocked

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16): # My time for working productive is from 8am to 4pm. you can change time
        print("Working hours...")
        with open(hosts_path,'r+') as file: # opening the host file
            content=file.read()  # reading the content inside the file and storing inside content variable
            for website in website_list: # A for loop for checking that if the url is already inside the host file
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n") # Redirecting the url
    else:
        with open(hosts_path,'r+') as file:  # if the productive time is over then we have to again read the file and bring the host file to noramal stage
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):  #using any() function to check wheather there is url or not.
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5) # You can check every 5 seconds or 5 minutes if you want
