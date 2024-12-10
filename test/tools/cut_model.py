# -*- coding: utf-8 -*-
# @Time: 2/8 12:06
# @DESC:  模型切分
from pathlib import Path
import requests
def cut():
    src = Path('../vegetable_model_v2.h5')
    tmp_dir = Path('./tmp_dir')
    tmp_dir.mkdir(exist_ok=True)

    #切分分片大小
    buf_size = 1*1024*1024
    index = 0
    with open(src,'rb')as f1:
        while True:
            buf = f1.read(buf_size)
            if buf:
                save_path = tmp_dir / f'vegetable_model_v2${index}.part'
                index+=1
                with open(save_path,'wb') as f2:
                    f2.write(buf)
                res = requests.post(
                    url='http://124.71.165.169:9443/imooc-edge02/default/receive_model',
                    files = {
                        'file':open(save_path,'rb')
                    }
                )
                print(res.text)

            else:
                break

cut()