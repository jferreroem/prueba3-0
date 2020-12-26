#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
import bottle
from bottle import route,run
from datetime import datetime

bottle.debug(True)

@route('/')
def index():
	return str(datetime.utcnow())

@route('/api', methods=['GET'])
def api():
    return jsonify({"time":str(datetime.utcnow())})


