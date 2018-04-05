# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 13:47:27
# @Author  : SilverMaple
# @Site    : https://github.com/SilverMaple
# @File    : __init__.py

from flask import Blueprint
bp = Blueprint('auth', __name__)

from app.auth import routes