FROM python:3.7.12-slim-buster
ENV TZ=Asia/Shanghai
ENV PROD=yes
EXPOSE 5001

#拷贝mqtt依赖包
# COPY /mqtt /app/mqtt
COPY ./test/ /app/
WORKDIR /app/

RUN pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

ENTRYPOINT [ "python","index.py"]
