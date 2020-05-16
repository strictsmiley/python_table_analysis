import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

taslak = Blueprint('taslak',__name__,url_prefix='/index')


@taslak.route('/')
def index():
	return render_template(current_app.config['INDEX_TEMPLATE'])
