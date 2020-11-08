import socket
import sys
import time
import datetime

ip = '127.0.0.1'
port = 8888

argv_len = len(sys.argv)
if argv_len >= 3:
  ip = sys.argv[1]
  port = sys.argv[2]
elif argv_len == 2:
  ip = sys.argv[1]
else:
  pass

address = (ip, port)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while (True):
  now = datetime.datetime.now()
  print(now.strftime("%Y-%m-%d %H:%M:%S") + ' HELLO SERVER')
  s.sendto(b'HELLO SERVER', address)
  time.sleep(10*60)
