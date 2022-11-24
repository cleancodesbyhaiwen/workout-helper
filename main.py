import machine
from machine import Timer, Pin, RTC, ADC
import time
from IMU import *
import ssd1306
import network
import usocket as socket
import time
import json
import sh1106
from button import Button

i2c = machine.I2C(sda=machine.Pin(4), scl=machine.Pin(5),freq=100000)

imu = BNO055(i2c)
calibrated = False
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)
display.flip(flag=True, update=True)
vibrator = Pin(14,Pin.OUT)
led = Pin(12, Pin.OUT)
rotary = ADC(0)

port=10086
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('Haiwen_2.4', '432qweEWQ!@@')
    while not wlan.isconnected():
        pass
ip = wlan.ifconfig()[0]
print('Connected to WIFI\nIP Adress: ' +  str(ip))
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
s.bind((ip,port))

exercises = ['no excercise','bench press','squat']
current_exericise_index = 0
set_count = 0
rep_count = 0
rtc = RTC()

def update_display(timer):
    global current_exericise_index, set_count, rep_count
    time_now = rtc.datetime()
    display.fill(0)
    display.text(str(time_now[4])+ ":"+str(time_now[5])+ ":"+str(time_now[6]), 10, 10)
    display.text(str(imu.temperature())+'C',90,10)
    display.text(exercises[current_exericise_index],10,20)
    display.text('set count: '+str(set_count),10,30)
    display.text('rep count: '+str(rep_count),10,40)
    display.show()    
    
tim0 = Timer(0)
tim0.init(period=1000, mode=Timer.PERIODIC, callback=update_display)

def vibrator_off(timer):
    vibrator.off()
tim1 = Timer(1)
# change type of excercise
def buttonA_callback(pin):
    global current_exericise_index
    current_exericise_index += 1
    if current_exericise_index == 3:
        current_exericise_index = 0
button_a = Button(pin=Pin(15, mode=Pin.IN, pull=Pin.PULL_UP), callback=buttonA_callback)

while True:
    time.sleep(0.1)
    if not calibrated:
        calibrated = imu.calibrated()
        #print('Calibration required: sys {} gyro {} accel {} mag {}'.format(*imu.cal_status()))

    jsonFile = {"yaw":str(imu.euler()[0]),"pitch":str(imu.euler()[1]), "roll":str(imu.euler()[2]),
                "exercise":exercises[current_exericise_index],"distance":str(int(rotary.read()/13))}
    jsonFile = json.dumps(jsonFile)
    data,addr=s.recvfrom(1024)
    data = json.loads(data.decode('utf-8'))
    print(data)
    if data['unbalanced'] == 'True' or data['alarming'] == 'True':
        vibrator.on()
        led.on()
    else:
        vibrator.off()
        led.off()
    if data['hit'] == 'True':
        vibrator.on()
        tim1.init(period=1000, mode=Timer.ONE_SHOT, callback=vibrator_off)
    set_count = data['set_count']
    rep_count = data['rep_count']
    s.sendto(jsonFile,addr)