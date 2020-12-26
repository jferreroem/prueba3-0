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

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
