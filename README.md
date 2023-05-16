# 17544-RTS---LAB2
from yolobit import *
from mqtt import *
from event_manager import *
import time
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20
from aiot_lcd1602 import LCD1602

mqtt.connect_wifi('abcd','123456789')
mqtt.connect_broker(server = 'io.adafruit.com', port = 1883, username = 'vienkimlan', password = 'aio_RauH70zveDL2uGRhC3IiHmW08aP8')


aiot_dht20 = DHT20(SoftI2C(scl = Pin(22), sda = Pin(21)))
aiot_lcd1602 = LCD1602()
status = 0

def iot_task():
  mqtt.publish('temperature', temperature())
  mqtt.publish('humidity', light_level())

def sensing_task():
  aiot_dht20.read_dht20()
  aiot_lcd1602.clear()
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr((aiot_dht20.dht20_temperature()))
  aiot_lcd1602.move_to(0, 1)
  aiot_lcd1602.putstr((aiot_dht20.dht20_humidity()))

def blinky_task():
  global status
  if status == 0:
    display.show(Image.HEART)
  else:
    display.show(Image.HEART_SMALL)
  
  status = 1 - status

def automation_task():
  aiot_dht20.read_dht20()
  if aiot_dht20.dht20_temperature() > 28:
    pin0.write_digital(1) 
  else:
    pin0.write_digital(0)


event_manager.reset()

event_manager.add_timer_event(1000, blinky_task)
event_manager.add_timer_event(5000, sensing_task)
event_manager.add_timer_event(1000, automation_task)
event_manager.add_timer_event(5000, iot_task)


display.scroll('EX3')

while True:
  event_manager.run()
  time.sleep_ms(1000)
