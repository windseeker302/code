# -*- coding: utf-8 -*-
# @Time: 1/1 20:39
# @DESC: 云端接收边缘侧数据服务
from flask import Flask, request

app = Flask(__name__)
import json, base64,time
from pathlib import Path

IMAGE_SAVE_DIR = Path("./image_data")
IMAGE_SAVE_DIR.mkdir(exist_ok=True)

@app.route("/upload", methods=['POST'])
def upload():
    data = request.get_data()
    data_dict = json.loads(data)
    image_base64 = data_dict['image_base64']
    class_name = data_dict['class_name']
    #base64解码
    image_base64_decode = base64.b64decode(image_base64)
    # 165268_qiezi.jpg
    filename = class_name+ "_" + str(int(time.time()))+".jpg"
    image_save_path = IMAGE_SAVE_DIR / filename
    with open(image_save_path, "wb") as f:
        f.write(image_base64_decode)
    return data, 200


if __name__ == "__main__":
    # app.debug = True
    app.run(host="0.0.0.0", port=8080)
