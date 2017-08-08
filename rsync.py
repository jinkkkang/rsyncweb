# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, jsonify
import os,commands
import json

app = Flask(__name__)
app.debug = True

# @app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
app.add_url_rule('/','home',home)

@app.route('/rsync', methods=['POST'])
def rsync():
	script={"sssm":"sssmrsync.sh","dmg":"rsync.sh"}
	content=request.form.get('content', '')
	pro=request.form.get('pro', '')
	list={};
	for x in content.split('\n'):
		print "/home/wwwroot/" + pro + x
		if  os.path.exists("/home/wwwroot/" + pro + x):
			(c,r)=commands.getstatusoutput(script[pro] + " " +  x)
			if c != 0:
	 			list[x]=1
	 		else:
	 			list[x]=0
		else:
			list[x]=2
	return jsonify(list)


@app.errorhandler(404)
def not_find(error):
	return "404"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3999)