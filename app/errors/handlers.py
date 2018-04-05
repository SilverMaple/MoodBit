# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 13:45:03
# @Author  : SilverMaple
# @Site    : https://github.com/SilverMaple
# @File    : handlers.py

from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500