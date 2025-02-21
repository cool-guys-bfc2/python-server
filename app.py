from flask import Flask
socket=[]
app=Flask(__name__)

@app.route("/socket/<request>")
def run(request):
  socket.append(socket)
  return "Done!"

@app.route("/get/"):
def get():
  return " ".join(socket)

app.run()
