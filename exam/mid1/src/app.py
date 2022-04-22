from flask import Flask,jsonify,request,make_response
from jwcrypto import jwt,jwk
import sqlite3
app = Flask(__name__)
key=jwk.JWK(generate='oct', size=256)

@app.route('/', methods=['POST'])
@app.route('/other', methods=['POST'])
@app.route('/', methods=['GET'])
@app.route('/other', methods=['GET'])
@app.route('/token', methods=['GET'])
def index():
	response={}
	logger(request,response)
	return '<h1>Grab Your token First!</h1>'

@app.route('/token', methods=['POST'])
def login():
	print(request.get_data(as_text=True))
	exec("creds="+request.get_data(as_text=True))
	conn=sqlite3.connect('test.db')
	result=conn.execute("SELECT username,access FROM users WHERE username=? AND password=?",(locals()['creds']['username'],locals()['creds']['password'])).fetchone()
	response={}
	if (result):
		row=tuple(result)
		token=jwt.JWT(header={"alg": "HS256"},claims={"username": row[0],"access": row[1]})
		token.make_signed_token(key)
		tok=token.serialize()
		response['token']=tok
	else:
		response['msg']='invalid credentials'
	logger(request,response)
	return make_response(jsonify(response),200)    

def logger(request,response):
	tmp='headers:{'
	for header in request.headers:
		tmp=tmp+'"'+header[0]+'":"'+header[1]+'"'
	tmp=tmp+'}'
	p=open("/var/log/python/flask/app.log","a")
	p.write("\nRequest Log-------------------------------------")
	p.write(" "+request.method)
	p.write(" "+request.full_path)
	p.write(" "+tmp)
	p.write(" "+"body:"+request.get_data(as_text=True))
	p.close()

if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0",port=5000)
