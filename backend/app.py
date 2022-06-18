import os
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import cross_origin
from pymongo import MongoClient


app = Flask(__name__)
# client = MongoClient("mongo", 27017)

username = os.environ["MONGODB_USER"]
password = os.environ["MONGODB_PASSWORD"]
host = os.environ["MONGODB_HOST"]

client = MongoClient(
    "mongodb://%s:%s@%s:27017/interns?authSource=admin" % (username, password, host)
)

# client = MongoClient(
#     os.environ["MONGODB_HOST"],
#     username=os.environ["MONGODB_USER"],
#     password=os.environ["MONGODB_PASSWORD"]
# )
db = client.interns
collection = db["hits"]


@app.route("/", methods=["GET"])
@cross_origin()
def root():
    collection.insert_one({"time": datetime.utcnow()})
    message = "This page has been visited {} times.".format(collection.count())
    return jsonify({"message": message})


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080, debug=True)
