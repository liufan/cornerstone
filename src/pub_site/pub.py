# -*- coding: utf-8 -*-
import logging

from flask import Flask, redirect, request, render_template
from domain.user import has_login, register_user_module
from domain.exam import register_exam_module
import re

from tool.filters import *
from werkzeug.exceptions import NotFound


log = logging.getLogger(__name__)

DEBUG = False
SECRET_KEY = 'development key'
PROPAGATE_EXCEPTIONS = True

app = Flask(__name__, template_folder='')
app.config.from_object(__name__)

register_user_module(app)
register_exam_module(app)

register_filters(app)
register_global_functions(app)

logging.basicConfig(format='[%(levelname)s]%(asctime)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

@app.route('/')
def index():
    return redirect('/login')

NO_LOGIN_REQUIRE_URL=['/login']

@app.before_request
def before_request():
    if request.path not in NO_LOGIN_REQUIRE_URL and not has_login():
        return redirect('/login')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_internal_error(e):
    return render_template('500.html', e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5674)


