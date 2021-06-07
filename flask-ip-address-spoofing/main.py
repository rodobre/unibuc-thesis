from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/ip", methods=["GET"])
def print_ip():
  # https://stackoverflow.com/a/12771438
  if request.headers.getlist("X-Forwarded-For"):
    ip = request.headers.getlist("X-Forwarded-For")[0]
  else:
    ip = request.remote_addr
    
  return jsonify({"ip": request.remote_addr}), 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)