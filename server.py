import os

from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from PIL import Image
from io import BytesIO
import base64
import datetime
import time

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/handleImage',methods=['POST'])
def handleImage():
    ts = time.time()
    image = request.form['imageString']
    print image
    im = Image.open(BytesIO(base64.b64decode(image)))
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    im.convert('RGB').save(os.path.join(app.config['UPLOAD_FOLDER'],st+".jpg"))
    return '{"status": "OK","code": 200,"message": "Data processed sucessfully","result": {"leafName": "Apple","healthState": "Unhealthy","cropDisease":"Apple Black Rot"}}'

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8000")
    )
