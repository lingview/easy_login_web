import json
import os
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/send-text", methods=["POST"])
def receive_text():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "POST")
    text = request.form.get("text")
    parts = text.split(",")
    text1=parts[0]
    text2=parts[1]
    if len(text1) >= 3 and len(text1)<=10 and len(text2)>=5 and len(text2)<=20:
        classes_path = os.path.expanduser("user_information/main")
        with open(classes_path,'r',encoding = 'UTF-8') as f:
            yonghu = f.readlines()
        yonghu = [c.strip() for c in yonghu]
        print(yonghu)
        new_list = [element.split(',')[0].strip() for element in yonghu]
        print(new_list)
        if text1 in new_list:
            response_data = {"message": "注册失败,用户名重复！！！"}
            response_json = json.dumps(response_data)
            response.headers.add("Content-Type", "application/json")
            return response_json
        else:
            file_1=open("user_information/main",mode="a",encoding='utf-8')
            file_1.write('\n')
            file_1.write(text)
            file_1.close()
            response_data = {"message": "注册成功！请返回登录！"}
            response_json = json.dumps(response_data)
            response.headers.add("Content-Type", "application/json")
            return response_json
    else:
        response_data = {"message": "注册失败"}
        response_json = json.dumps(response_data)
        response.headers.add("Content-Type", "application/json")
        return response_json




@app.route('/denglu', methods=["POST"])
def get_data():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "POST")
    text = request.form.get("text")

    classes_path = os.path.expanduser("user_information/main")
    with open(classes_path,'r',encoding = 'UTF-8') as f:
        yonghu = f.readlines()
    yonghu = [c.strip() for c in yonghu]
    if text in yonghu:
        #读取用户数据
        #先获取用户名
        user_shujv1=text
        print("123:",user_shujv1)
        

        response_data = {"message": user_shujv1}
        response_json = json.dumps(response_data)
        response.headers.add("Content-Type", "application/json")
        print("登录成功")

        return response_json
    else:
        response_data = {"message": "登录失败，请检查用户名及密码！！！"}
        response_json = json.dumps(response_data)
        response.headers.add("Content-Type", "application/json")
        print("登录失败,请检查用户名及密码")
        return "登录失败"


@app.route('/verify', methods=['POST'])
def user_verify():
    data = request.get_json()
    username=data["username"]
    password=data["password"]
    print(username,password)
    classes_path = os.path.expanduser("user_information/main")
    with open(classes_path,'r',encoding = 'UTF-8') as f:
        yonghu = f.readlines()
    yonghu = [c.strip() for c in yonghu]
    if username + "," + password in yonghu:
        return jsonify({'success': "true"})
    else:
        return jsonify({'success': "true"})





#if __name__ == '__main__':
#    app.run(debug=True,host='0.0.0.0',port=3920,ssl_context=(
#        "/var/www/html/ling-root/ling-ssl/ling2023.xyz.pem",
#        "/var/www/html/ling-root/ling-ssl/ling2023.xyz.key")
#    )


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3920)
