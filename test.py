import cv2
import time
from numpy import *
from flask import Flask,render_template,Response

class Camera(object):
    def __init__(self):
        print 'Done'

    def get_frame(self):
        cap = cv2.VideoCapture(0)
        stat,frame = cap.read()
        self.frame = cv2.imencode('.jpg',frame)[1].tobytes()
        return self.frame

#Flask structure
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
#        time.sleep(0.001)
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
        

