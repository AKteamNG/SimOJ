#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import random
import string
from bottle import *
from bottle import request, route, run, static_file

value=None

@route('/')
def index():
    return static_file('index.html', './')

site = '192.68.4.124'

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
    
   
def judge(simp_name, problem_id):
#    print('JUDGE ' + simp_name + ' ' + problem_id)
    print('cp ./upload/' + simp_name + '.cpp' + ' ' + './problems/' + problem_id + '/' + simp_name + '.cpp')
    os.system('cp ./upload/' + simp_name + '.cpp' + ' ' + './problems/' + problem_id + '/' + simp_name + '.cpp')
    print('cd ./problems/' + problem_id + ' && syzoj judge ' + simp_name + '.cpp > ' + simp_name + '.txt')
    os.system('cd ./problems/' + problem_id + ' && syzoj judge ' + simp_name + '.cpp > ' + simp_name + '.txt')
    print('rm ./problems/' + problem_id + '/' + simp_name + '.cpp')
    os.system('rm ./problems/' + problem_id + '/' + simp_name + '.cpp')
    print('mv ./problems/' + problem_id + '/' + simp_name + '.txt' + ' ' + './upload/' + simp_name + '.txt')
    os.system('mv ./problems/' + problem_id + '/' + simp_name + '.txt' + ' ' + './upload/' + simp_name + '.txt')

@route('/upload/command')
def command():
	global value  
	value=request.query.value

@route('/upload', method='POST')
def do_upload():
    filedata = request.files.get('fileField')
    simp_name = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    save_name = simp_name + '.cpp'
#    print(value)
    if filedata.file:
        file_name = os.path.join(upload_path, save_name)
        try:
            filedata.save(file_name)  # 上传文件写入
        except IOError:
            return '上传文件失败'
        print(save_name)
        problem_id = value
        judge(simp_name, problem_id)
        return '<script>window.location.href="' + 'upload/' + simp_name + '.txt'+'"</script> 上传文件成功, 文件名: {}'.format(site + '/upload/' + save_name) + '评测结果：{}'.format(site + '/upload/' + simp_name + '.txt')

##        return '上传文件成功, 文件名: {}'.format(file_name)
    else:
        return '上传文件失败'

@route('/upload/<file_name>')
def show_code(file_name):
    print(file_name)
    return static_file(file_name, './upload/')



    
@error(404)
def error404(error):
    return '404 发生页面错误, 未找到内容'


run(host='0.0.0.0', port=80, debug=True)

