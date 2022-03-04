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


@app.route('/get_login_pass', methods=['GET'])
def get_login_passwd():
    login = request.args.get('login')
    passwd = request.args.get('pass')
    result = data_db.get_get_login_passwd(login, passwd)
    print(result)
    return result


@app.route('/get_collaborator_list_num_groups', methods=['GET'])
def get_collaborator_list_num_groups():
    code2 = request.args.get('code')
    checked = request.args.get('checked')
    if checked == "true":
        result = [{'CODE': code, 'NAME': i} for code, i in
                  data_db.get_get_collaborator_list_num_groups_checked(code2)]
    else:
        result = [{'CODE': code, 'NAME': i, 'NUMBER': n} for code, i, n in
                  data_db.get_get_collaborator_list_num_groups(code2)]
    print(result)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
