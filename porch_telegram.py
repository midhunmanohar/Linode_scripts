import sys
import requests
from time import sleep
from datetime import timedelta
import random
import datetime
import telepot
import os
import json
from telepot.loop import MessageLoop

bot = telepot.Bot('513037377:AAGkmqHkoobVIXqYjv5x47V9Ev3fgY_SZGc')
url = "https://api.telegram.org/bot513037377:AAGkmqHkoobVIXqYjv5x47V9Ev3fgY_SZGc/sendMessage?chat_id=-260318820&text="


def handle(msg):

    chat_id = msg['chat']['id']
    command = msg['text']
    temp1 = {'ontime':"",'offtime':""}
    print (command)
    if command=='/set0615pm@porchlight_bot':
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','w') as json_file:
            temp["ontime"] = 1815
            temp["offtime"] = temp1["offtime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light on time set to 06:15 PM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)
    if command=='/set0630pm@porchlight_bot':
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','r') as json_file:
            temp= json.load(json_file)
            print(temp)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','w') as json_file:
            print(temp1)
            temp["ontime"] = 1830
            temp["offtime"] = temp1["offtime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light on time set to 06:30 PM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)
    if command=='/set0645pm@porchlight_bot':
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','w') as json_file:
            temp["ontime"] = 1845
            temp["offtime"] = temp1["offtime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light on time set to 06:45 PM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)
    if command=='/set0700pm@porchlight_bot':
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','w') as json_file:
            temp["ontime"] = 1900
            temp["offtime"] = temp1["ontime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light on time set to 07:00 PM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)



    if command=='/set0600am@porchlight_bot':
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','w') as json_file:
            temp["offtime"] = 600
            temp["ontime"] = temp1["ontime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light off time set to 06:00 AM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)
    if command=='/set0615am@porchlight_bot':
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','w') as json_file:
            temp["offtime"] = 615
            temp["ontime"] = temp1["ontime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light off time set to 06:15 AM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)
    if command=='/set0630am@porchlight_bot':
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','w') as json_file:
            temp["offtime"] = 630
            temp["ontime"] = temp1["ontime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light off time set to 06:30 AM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)
    if command=='/set0645am@porchlight_bot':
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','w') as json_file:
            temp["offtime"] = 645
            temp["ontime"] = temp1["ontime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light off time set to 06:45 AM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)
    if command=='/set0700am@porchlight_bot':
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/porch_timer.json','w') as json_file:
            temp["offtime"] = 700
            temp["ontime"] = temp1["ontime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light off time set to 07:00 AM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)



#print ("main loop")
MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    sleep(10)


