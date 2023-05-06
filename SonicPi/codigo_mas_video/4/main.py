from pythonosc import udp_client
from random import randint
import time

sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

while True:
    sender.send_message('/trigger/hola', ['rodeo', 56, randint(1, 8)])
    time.sleep(0.5)
    sender.send_message('/trigger/hola', ['kalimba', randint(50, 100), randint(1, 8)])

