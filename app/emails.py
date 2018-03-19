# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 11:50
# @Author  : SilverMaple
# @Site    : https://github.com/SilverMaple
# @File    : emails.py

from .decorators import async
from flask_mail import Message
from app import app, mail
from flask import render_template
from config import ADMINS
from threading import Thread

@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    # mail.send(msg)
    send_async_email(app, msg)

def follower_notification(followed, follower):
    send_email("[MoodBit] %s is now following you!" % follower.nickname,
               ADMINS[0],
               [followed.email],
               render_template('follower_email.txt',
                               user=followed, follower=follower),
               render_template('follower_email.html',
                               user=followed, follower=follower))