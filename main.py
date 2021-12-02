from kahoot import client
import threading
import random
import os
import multiprocess

pin = input("Pin del el juego: ")
name = input("Nombre de el bot: ")
#pointss = 0
def main(name, pin):
  while True:
    bot = client()
    points = random.randint(1, 5000000000000000000)
    bot.join(pin, name + " " + str(points))
    bot.on("Joined", print(f"Bot Nº{str(points)} Unido al pin {pin}"))

while True:
  multiprocess.Process(target=main, args=[name, pin])
  th = threading.Thread(target=main, args=[name, pin])
  th.start()
