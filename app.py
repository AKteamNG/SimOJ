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

upload_path = os.path.join(base_path, 'codes')   # 上传文件目录
if not os.path.exists(upload_path):
    os.makedirs(upload_path)


@route('/', method='GET')


#@route('/codes', method='GET')
#@route('/index.html', method='GET')
#@route('/upload.html', method='GET')
def index():
    return static_file('index.html', './')
    
   
def judge(simp_name, problem_id):
#    print('JUDGE ' + simp_name + ' ' + problem_id)
    print('cp ./codes/' + simp_name + '.cpp' + ' ' + './problems/' + problem_id + '/' + simp_name + '.cpp')
    os.system('cp ./codes/' + simp_name + '.cpp' + ' ' + './problems/' + problem_id + '/' + simp_name + '.cpp')
    print('cd ./problems/' + problem_id + ' && syzoj judge ' + simp_name + '.cpp > ' + simp_name + '.txt')
    os.system('cd ./problems/' + problem_id + ' && syzoj judge ' + simp_name + '.cpp > ' + simp_name + '.txt')
    print('rm ./problems/' + problem_id + '/' + simp_name + '.cpp')
    os.system('rm ./problems/' + problem_id + '/' + simp_name + '.cpp')
    print('mv ./problems/' + problem_id + '/' + simp_name + '.txt' + ' ' + './codes/' + simp_name + '.txt')
    os.system('mv ./problems/' + problem_id + '/' + simp_name + '.txt' + ' ' + './codes/' + simp_name + '.txt')

@route('/codes', method='POST')
def do_upload():
    problem_id = request.forms.get('ProblemId')
    code = request.forms.get('answer')
    
    simp_name = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    save_name = simp_name + '.cpp'
    file_name = os.path.join(upload_path, save_name)
    print(file_name)
    try:
        tmpfile = open(file_name, "w")
        tmpfile.write(code)  # 提交代码写入
        tmpfile.close()
    except IOError:
        return '提交代码失败'
    judge(simp_name, problem_id)
    return '<script>window.location.href="' + 'codes/' + simp_name + '.txt'+'"</script> 提交代码成功, 文件名: {}'.format(site + '/codes/' + save_name) + '评测结果：{}'.format(site + '/codes/' + simp_name + '.txt')

@route('/codes/<file_name>')
def show_code(file_name):
    #print(file_name)
    return static_file(file_name, './codes/')

@route('/static/<file_name>')
def show_code(file_name):
    #print(file_name)
    return static_file(file_name, './static/')

@error(404)
def error404(error):
    return '404 发生页面错误, 未找到内容'


run(host='0.0.0.0', port=80, debug=True)

