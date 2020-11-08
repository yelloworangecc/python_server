from flask import Flask
from flask import request
from flask import Response
from flask import send_file
from io import BytesIO
import qrcode
from threading import Thread
import socket

# udp接收线程函数
def udp_recv(dict):
    host_addr = ('0.0.0.0',8888)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #允许重复绑定
    sock.bind(host_addr)
    while True:
        data, peer_addr = sock.recvfrom(64)
        print('data from ' + peer_addr[0] + ':' + bytes.decode(data))
        dict['ip'] = peer_addr[0]

dict = {'ip': 'none'}
t = Thread(target=udp_recv, args=(dict,), daemon=True)
t.start()
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World'

@app.route('/qrcode')
def generate_qrcode():
  text = request.args.get('text')
  img = qrcode.make(text)
  b_img= BytesIO()
  img.save(b_img,'png')
  # img.save('./test2.png','png')
  # image = open('test2.png','rb')
  resp = Response(b_img.getvalue(), content_type="image/png")
  return resp
  # return send_file(b_img,mimetype='image/png')

@app.route('/home_ip')
def get_home_ip():
    return dict['ip']
