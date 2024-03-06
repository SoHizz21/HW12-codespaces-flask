from flask import Flask, jsonify
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

books=[
    {"id":1,"title":"Helle","author":"Author 1"},
    {"id":2,"title":"Book 2","author":"Author 2"},
    {"id":3,"title":"Book 3","author":"Author 3"}
]

@app.route("/books",methods=["GET"])
@cross_origin()
def get_all_books():
    return jsonify({"books":books})

@app.route("/")
@cross_origin()
def hello_world():
    return  "<h1>Hello_world</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)