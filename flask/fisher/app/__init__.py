#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask
from app.models.book import db


def create_app():
    '''
    初始化
    :return:
    '''
    app = Flask(__name__)
    # 加载配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app

def register_blueprint(app):
    # 蓝图注册到app中
    from app.web.book import web
    app.register_blueprint(web)