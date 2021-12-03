import socket
import time
import datetime
import binascii

def send(s, content):
    content += '\r\n'
    s.sendall(content.encode())

now = datetime.now()
current_time = now.strftime("[%H:%M:%S]")

ip=''
controller=''
game=''
switch=''
name=''

def connect(controllerName):
  global current_time
  global switch
  global name
  name=controllerName
  if ip != '' and game != '' and controller != '':
    switch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    switch.connect((ip, 6000))
    log=open('log.txt', 'w')
    log.write(current_time+' '+name+' Controller Set Up - Ready to take commands')
    log.close()

def disconnect(controllerName):
  global current_time
  global switch
  global name
  if ip != '' and game != '' and controller != '':
    switch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    switch.disconnect((ip, 6000))
    log=open('log.txt', 'w')
    log.write(current_time+' '+name+' Controller disconnected - Reconnect to send commands')
    log.close()

def setIP(switchIP):
  global ip
  ip=switchIP

def setGame(switchGame):
  global controller
  global game
  if switchGame.lower() == "pokemon-sword" or switchGame.lower() == 'pokemon-shield':
    controller='pro'
    game=switchGame
  if switchGame.lower() == "pokemon-lg-eevee" or switchGame.lower() == 'pokemon-lg-pikachu':
    controller='joyconR'
    game=switchGame
  if switchGame.lower() == "pokemon-bdiamond" or switchGame.lower() == 'pokemon-spearl':
    controller='pro'
    game=switchGame
  if switchGame.lower() == "animal-crossing-nh":
    controller='pro'
    game=switchGame

def setController(switchController):
  global controller
  global current_time
  if switchController.lower() == "pro":
    controller='pro'
  elif switchController.lower() == "joyconL":
    controller='joyconL'
  elif switchController.lower() == "joyconR":
    controller='joyconR'
  else:
    controller='pro'
    print(current_time+" Invalid Controller Set - Defaulting to PRO CONTROLLER")

def click(button):
  global switch
  button=button.upper()
  if button == 'A' or button == 'B' or button == 'X' or button == 'Y' or button == 'L' or button == 'R' or button == 'ZL' or button == 'ZR' or button == 'HOME' or button == 'CAPTURE':
    b='click '+button
    send(switch, b)
  if button == '+':
    b='click PLUS'
    send(switch, b)
  if button == '-':
    b='click MINUS'
    send(switch, b)
  if button == 'DOWN':
    b='click DDOWN'
    send(switch, b)
  if button == 'RIGHT':
    b='click DRIGHT'
    send(switch, b)
  if button == 'LEFT':
    b='click DLEFT'
    send(switch, b)
  if button == 'UP':
    b='click DUP'
    send(switch, b)

def press(button):
  global switch
  button=button.upper()
  if button == 'A' or button == 'B' or button == 'X' or button == 'Y' or button == 'L' or button == 'R' or button == 'ZL' or button == 'ZR' or button == 'HOME' or button == 'CAPTURE':
    b='press '+button
    send(switch, b)
  if button == '+':
    b='press PLUS'
    send(switch, b)
  if button == '-':
    b='press MINUS'
    send(switch, b)
  if button == 'DOWN':
    b='press DDOWN'
    send(switch, b)
  if button == 'RIGHT':
    b='press DRIGHT'
    send(switch, b)
  if button == 'LEFT':
    b='press DLEFT'
    send(switch, b)
  if button == 'UP':
    b='press DUP'
    send(switch, b)

def release(button):
  global switch
  button=button.upper()
  if button == 'A' or button == 'B' or button == 'X' or button == 'Y' or button == 'L' or button == 'R' or button == 'ZL' or button == 'ZR' or button == 'HOME' or button == 'CAPTURE':
    b='release '+button
    send(switch, b)
  if button == '+':
    b='release PLUS'
    send(switch, b)
  if button == '-':
    b='release MINUS'
    send(switch, b)
  if button == 'DOWN':
    b='release DDOWN'
    send(switch, b)
  if button == 'RIGHT':
    b='release DRIGHT'
    send(switch, b)
  if button == 'LEFT':
    b='release DLEFT'
    send(switch, b)
  if button == 'UP':
    b='release DUP'
    send(switch, b)

def wait(waitTime):
  waitTime=int(waitTime)
  time.sleep(waitTime)

def log(logText):
  global current_time
  log=open('log.txt', 'w')
  log.write(current_time+' Log Requested - '+logText)
  log.close()