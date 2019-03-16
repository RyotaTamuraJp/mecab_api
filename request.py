# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:25:58 2018

@author: ryota_tamura
"""

import requests
import json


def get_docker_mecab_result(text, url):
    json_obj = json.dumps({"text": text}, ensure_ascii=False)
    r = requests.post(url, json=json_obj)
    return r.json()


if __name__ == "__main__":
    text = u"きゃりーぱみゅぱみゅ"
    url = "http://localhost:5000/mecab_reply"
    mecab_result = get_docker_mecab_result(text, url)
    print(mecab_result)
    print(type(mecab_result))
