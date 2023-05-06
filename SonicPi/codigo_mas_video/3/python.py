from pythonosc import osc_message_builder
from pythonosc import udp_client
import time

sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

while True:
    sender.send_message('/trigger/prophet', [70, 100, 1])
    #time.sleep(10)
    #sender.send_message('/trigger/saw', [10, 130, 8])
    #sender.send_message('/trigger/tb303', [40, 120, 6])
    #sender.send_message('/trigger/dsaw', [40, 120, 6])
    sender.send_message('/trigger/fm', [70, 120, 6])
    #sender.send_message('/trigger/pulse', [40, 120, 6])
    time.sleep(2)
