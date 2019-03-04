#! /usr/bin/python
# -*- coding:utf-8 -*-
from app.web import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from flask import jsonify, request
from app.forms.book import SearchForm

@web.route('/book/search')
def search():
    '''
    q: 普通关键字或isbn
    page
    :return:
    '''
    # 将不可变的字典变更为可变的
    # a = request.args.to_dict()
    # 验证层
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        is_or_key = is_isbn_or_key(q)
        if is_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            # dict
        return jsonify(result)
    else:
        return jsonify(form.errors)