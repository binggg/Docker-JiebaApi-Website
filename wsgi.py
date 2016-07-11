#!/usr/bin/python
#encoding=utf-8

from __future__ import unicode_literals
import os
from bottle import route,run,default_app,request, response,get,post,template,debug,static_file

import sys
sys.path.append("../")

import jieba
import jieba.posseg
import jieba.analyse

jieba.set_dictionary("jieba/extra_dict/dict.txt.big")
#jieba.analyse.set_stop_words("jieba/extra_dict/stop_words.txt")
jieba.initialize()

import functools
import json

@route('/static/:filename')
def serve_static(filename):
    return static_file(filename, root='static')


@route('/textrank', method='GET')
@route('/textrank', method='POST')
def textrank():
    s = request.params.message;    

    result = jieba.analyse.textrank(s, withWeight=True)
    message = json.dumps(result)

    return message;

@route('/extract', method='GET')
@route('/extract', method='POST')
def extract():
    s = request.params.message;    

    result = jieba.analyse.extract_tags(s, withWeight=True)
    message = json.dumps(result)

    return message;

@route('/')
def main():
    return "hello world";
    

if __name__ == "__main__":

    from wsgiref.simple_server import make_server
    httpd = make_server('0.0.0.0', 8080, default_app())
    # Wait for a single request, serve it and quit.
    httpd.serve_forever()
else:
    # Mod WSGI launch
    os.chdir(os.path.dirname(__file__))
    application = default_app()
