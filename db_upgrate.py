# -*- coding: utf-8 -*-
# @Time    : 2018/3/16 10:28
# @Author  : SilverMaple
# @Site    : https://github.com/SilverMaple
# @File    : db_upgrate.py

#!flask/bin/python

from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))