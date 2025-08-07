from check_db import check_db 
from select_db import select_db
from insert_db import insert_db
from flask import Flask, jsonify, request

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/status")

def db():
    retorno = check_db()

    return jsonify(retorno), 200

@app.route("/consulta")

def consulta():
    retorno = select_db()
    return jsonify(retorno), 200

@app.route("/dados", methods=["POST"])
def inserir():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    retorno = insert_db(name, email)
    return jsonify(retorno), 201 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


