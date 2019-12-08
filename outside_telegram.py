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

bot = telepot.Bot('684752974:AAGGRJKTwDLOXwkR25ApQAeLPzYLL8kTu0c')
url = "https://api.telegram.org/bot684752974:AAGGRJKTwDLOXwkR25ApQAeLPzYLL8kTu0c/sendMessage?chat_id=-245713034&text="


def handle(msg):

    chat_id = msg['chat']['id']
    command = msg['text']
    temp1 = {'onetime':"",'offtime':""}
    print (command)
    # if command=='/help':
    #    while True:
    #       try:
    #          bot.sendMessage(chat_id, text="Available commands: Switch on time: \n/set0600PM\n/set0630PM\n/set0700PM\n/set0730PM\nSwitch off time:\n/set0900PM\n/set0930PM\n/set1000PM\n/set1030PM\n")
    #          break
    #       except:
    #          print("No Internet, retrying...")
    #          sleep(10)

    if command=='/set0600pm@outside_light_bot':
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','w') as json_file:
            temp["ontime"] = 1800
            temp["offtime"] = temp1["offtime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light on time set to 06:00 PM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)
    if command=='/set0630pm@outside_light_bot':
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','r') as json_file:
            temp= json.load(json_file)
            print(temp)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','w') as json_file:
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
    if command=='/set0700pm@outside_light_bot':
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','w') as json_file:
            temp["ontime"] = 1900
            temp["offtime"] = temp1["offtime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light on time set to 07:00 PM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)
    if command=='/set0730pm@outside_light_bot':
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','w') as json_file:
            temp["ontime"] = 1930
            temp["offtime"] = temp1["ontime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light on time set to 07:30 PM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)



    if command=='/set0900pm@outside_light_bot':
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','w') as json_file:
            temp["ontime"] = 2100
            temp["offtime"] = temp1["offtime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light off time set to 09:00 PM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)
    if command=='/set0930pm@outside_light_bot':
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','w') as json_file:
            temp["offtime"] = 2130
            temp["ontime"] = temp1["ontime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light off time set to 09:30 PM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)
    if command=='/set1000pm@outside_light_bot':
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','w') as json_file:
            temp["offtime"] = 2200
            temp["ontime"] = temp1["ontime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light off time set to 10:00 PM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)
    if command=='/set1030pm@outside_light_bot':
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','r') as json_file:
            temp= json.load(json_file)
            temp1 = temp
        with open('/home/pi/Python_Scripts/timer_test/timer1.json','w') as json_file:
            temp["offtime"] = 2230
            temp["ontime"] = temp1["ontime"]
            json.dump(temp,json_file)
            json_file.write("\n")
        while True:
            try:
                bot.sendMessage(chat_id, text="Light off time set to 10:30 PM!")
                break
            except:
                print("No Internet, retrying...")
                sleep(10)



#print ("main loop")
MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    sleep(10)

