from flask import Flask
from flask import request
from flask import Response
from flask import send_file
from io import BytesIO
import qrcode

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
