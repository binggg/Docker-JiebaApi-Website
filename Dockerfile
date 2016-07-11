FROM python:2-onbuild
MAINTAINER "yingkai" <yingkai.liao@madhead.com>

RUN pip install jieba
RUN git clone https://github.com/fxsjy/jieba.git


EXPOSE 8080
#CMD [ "bash" ] 
CMD [ "python", "-u", "./wsgi.py" ]