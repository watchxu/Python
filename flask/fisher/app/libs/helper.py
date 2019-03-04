#! /usr/bin/python
# -*- coding:utf-8 -*-

def is_isbn_or_key(word):
    '''

    :param word: 用户的查询参数
    :return:
    '''
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9数字组成，含一些'-'

    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if "-" in word and len(short_word) == 10 and short_word.isdight:
        isbn_or_key = 'isbn'

    return isbn_or_key