import os
from flask import Flask
socket=[]
app=Flask(__name__)

@app.route("/socket/<request>")
def run(request):
  socket.append(request)
  return "Done!"

@app.route("/get/")
def get():
  return " ".join(socket)

app.run(host="0.0.0.0",port=int(os.environ.get("PORT")))
