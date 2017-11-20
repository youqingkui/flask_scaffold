#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 17:17
# @Author  : youqingkui
# @File    : __init__.py
# @Desc    :


import time
import traceback

from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    return 'success'

