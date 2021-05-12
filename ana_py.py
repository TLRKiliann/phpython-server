#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Ana_py is an analyzer of http header !
"""

import requests


r = requests.get('https://httpbin.org/')
print(r.text[:200])
