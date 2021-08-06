#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

pload = {'username':'olivia','password':'123'}
r = requests.post('https://httpbin.org/post',data = pload)

r_dictionary= r.json()
print(r_dictionary['form'])
