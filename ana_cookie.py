#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

sender = requests.Session()

sender.get('https://meteonews.ch/cookies/set/sessioncookie/31251425')
requ = sender.get('https://meteonews.ch/cookies')

print(requ.text)
