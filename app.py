from flask import Flask, jsonify, request

import db as data_db

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def get_status():
    return 'OK'


@app.route('/get_tp', methods=['GET'])
def get_tp():
    result = [{'CODE': code, 'NAME': name} for name, code in data_db.get_get_tp_data()]
    return jsonify(result)


@app.route('/get_tp_names/<code>', methods=['GET'])
def get_tp_names(code):
    print(code)
    result = [{'FIO': fio, 'PASS': passw} for fio, passw in data_db.get_get_tp_names_data(code)]
    return jsonify(result)


if __name__ == '__main__':
    app.run()