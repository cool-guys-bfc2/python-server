import os
from flask import Flask,request
socket=[]
app=Flask(__name__)

@app.route("/socket/<req>")
def run(req):
  socket.append(req)
  return "Done!"

@app.route("/get/")
def get():
  return " ".join(socket)

@app.route("/db/write/<fn>")
def write(fn):
  fc=request.args.get("content")
  fh=open(fn,"w")
  fh.write(fc)
  fh.close()
  return "Done!"

@app.route("/db/read/<fn>")
def read(fn):
  try:
    return open(fn,"r").read(),200
  except:
    return "404",404
@app.route("/page/<fn>")
def host(fn):
  try:
    return open("src/"+fn,"r").read(),200
  except:
    return "404",404

app.run(host="0.0.0.0",port=int(os.environ.get("PORT")))
