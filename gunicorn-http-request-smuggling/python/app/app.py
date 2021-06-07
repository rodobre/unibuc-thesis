from flask import Flask, jsonify, request

app = Flask(__name__)

persistent_kv_db = {}

@app.route("/api/store", methods=["POST"])
def store_key():
  global persistent_kv_db
  
  key = request.headers.get('key')
  value = request.data.decode('utf-8')
  
  if key and value:
    persistent_kv_db[key] = value
    return 'OK', 200
  
  return 'Invalid parameters', 400

@app.route("/api/fetch/<key>", methods=["GET"])
def get_value(key):
  global persistent_kv_db

  if key:
    if key in persistent_kv_db:
      return jsonify(persistent_kv_db[key]), 200
    else :
      return 'Invalid parameters', 400
  
  return 'Invalid parameters', 400