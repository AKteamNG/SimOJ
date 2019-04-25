#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import random
import string
from bottle import *


base_path = os.path.dirname(os.path.realpath(__file__))  # 获取脚本路径

upload_path = os.path.join(base_path, 'upload')   # 上传文件目录
if not os.path.exists(upload_path):
    os.makedirs(upload_path)


@route('/', method='GET')
#@route('/upload', method='GET')
#@route('/index.html', method='GET')
#@route('/upload.html', method='GET')
def index():
    return static_file('index.html', './')


@route('/upload', method='POST')
def do_upload():
    filedata = request.files.get('fileField')

    savename = ''.join(random.sample(string.ascii_letters + string.digits, 10)) + '.cpp'
    
    if filedata.file:
        file_name = os.path.join(upload_path, savename)
        print(savename)
        try:
            filedata.save(file_name)  # 上传文件写入
        except IOError:
            return '上传文件失败'
        return '上传文件成功, 文件名: {}'.format('192.68.4.124/upload/' + savename)
##        return '上传文件成功, 文件名: {}'.format(file_name)
    else:
        return '上传文件失败'

@route('/upload/<filename>')
def show_code(filename):
    return static_file(filename, './upload/')
"""
@route('/favicon.ico', method='GET')
def server_static():
    return static_file('favicon.ico', root=base_path)
"""


@error(404)
def error404(error):
    return '404 发生页面错误, 未找到内容'


run(host='0.0.0.0', port=80, debug=True)

