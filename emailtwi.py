#!/usr/bin/python
# -*- encoding: utf8 -*-

# http://jinja.pocoo.org/docs/
# http://jinja.pocoo.org/docs/intro/#installation
# pip install Jinja2

import os,sys,time,re
from jinja2 import Template
tempContent = file('templates/toptaobao.htm','r').read()
template = Template(tempContent)
newTempBody = template.render(name='John Doe')