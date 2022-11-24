import socket
import json
from vpython import *
from classes import Sensor,User,Barbell
from animation import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("192.168.1.119", 10086)

sensor = Sensor()
user = User()
barbell = Barbell()

squat_anims = Squat_anims()
bench_press_anims = Bench_press_anims()
squat_anims.invisible()
bench_press_anims.invisible()

while True:
    jsonFile = {"unbalanced":str(barbell.unbalanced),"hit":str(barbell.hit_check),
                "alarming":str(user.alarming),"set_count":str(user.set_count),"rep_count":str(user.rep_count)}
    jsonFile = json.dumps(jsonFile).encode('utf-8')
    client_socket.sendto(jsonFile, addr)
    try:
        data, server = client_socket.recvfrom(1024)
        data = json.loads(data)
        user.change_exercise(data['exercise'])
        if user.exercise=='bench press':
            bench_press_anims.visible()
            squat_anims.invisible()
            barbell_anim.visible = True
            sensor.update(data)
            #sensor.print_data()
            bench_press_anims_update(sensor,user)
            unbalance_detect(sensor,barbell)
            # Rep Count
            barbell.hit_detect(user,sensor)
            user.rest_detect(sensor)
            rest_anims(user)

        elif user.exercise=='squat':
            bench_press_anims.invisible()
            squat_anims.visible()
            barbell_anim.visible = True
            sensor.update(data)
            #sensor.print_data()
            squat_anims.update(sensor)
            squat_anims_update(sensor,user)
            unbalance_detect(sensor,barbell)
            # Rep Count
            barbell.hit_detect(user,sensor)
            user.rest_detect(sensor)
            rest_anims(user)
        else:
            bench_press_anims.invisible()
            squat_anims.invisible()
            barbell_anim.visible = False
            rest_anims(user)
            L.text = ''

    except socket.timeout:
        print('REQUEST TIMED OUT')


