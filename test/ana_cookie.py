#!/usr/bin/python3

"""
    This Script is Created Only For
    Educational Purpose.
"""

import requests

sender = requests.Session()

sender.get('https://meteonews.ch/cookies/set/sessioncookie/31251425')
requ = sender.get('https://meteonews.ch/cookies')

print(requ.text)
