#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint

web =  Blueprint('web', __name__)

# 将视图文件绑定到蓝图中
from app.web import book
