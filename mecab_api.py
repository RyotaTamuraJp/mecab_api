# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:46:07 2018

@author: ryota_tamura
"""

from flask import Flask, request, jsonify
import json
import ast
import MeCab
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
tagger = "-d /usr/lib/mecab/dic/mecab-ipadic-neologd"
m = MeCab.Tagger(tagger)


@app.route('/mecab_reply', methods=['POST'])
def mecab_reply():
    data = ast.literal_eval(json.loads(request.data))
    text = data["text"]
    return jsonify(m.parse(text).split('\n')[:-2])


if __name__ == '__main__':
    port = 5000
    app.run(host='0.0.0.0', port=port)
