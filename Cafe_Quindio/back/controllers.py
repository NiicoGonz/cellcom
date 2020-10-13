
from flask.views import MethodView
from flask import jsonify, request
from model import users, products, orders, fav
import bcrypt
import jwt
import datetime
from config import KEY_TOKEN_AUTH
class LoginUserControllers(MethodView):
    """
        Example Login
    """
    def post(self):
        content = request.get_json()
        password = bytes(str(content.get("password")), encoding= 'utf-8')
        email = content.get("email")
        print("--------", users, content.get("password"), email)
        if users.get(email):
            password_db = users[email]["password"]
            if bcrypt.checkpw(password, password_db):
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300), 'email': email}, KEY_TOKEN_AUTH , algorithm='HS256')
                return jsonify({"Status": "Login exitoso", "token": encoded_jwt}), 200
            return jsonify({"Status": "Login incorrecto 22"}), 400
        return jsonify({"Status": "Login incorrecto 11"}), 400


class RegisterUserControllers(MethodView):
    """
        Example Login
    """
    def post(self):
        content = request.get_json()
        name_c = content.get("name_c")
        email = content.get("email")
        phone = content.get ("phone")
        password = content.get("password")
        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        hash_password= hash_password.decode('utf-8')
        print(hash_password)
        users[email] = {"name": name_c,"password": hash_password, "phone":phone }
        return jsonify({"Status": "Registro ok",
                        "password_encriptado": hash_password,
                        "password_plano": password}), 200

class ProductsControllers(MethodView):
    

    def get(self):
        listproducts=products
        print(listproducts)
        return jsonify({"productos": listproducts}),200

class favsControllers(MethodView):
    def post(self,id_f):

        list_fav=fav.append([id_f])
        print(fav)
        return jsonify({"order":"se  añadio su orden",
                        "favoritos": fav}),200

    def get(self):
        fav_c=fav
        return jsonify({"productos": fav_c}),200

class ordersControllers(MethodView):
    def post(self):
        content = request.json()
        name_p = content.get("name_p")
        id_fav = content.get("id_f")
        value_p = content.get("value_p")
        orders_c=orders.append([name_p,id_fav,value_p])
        return jsonify({"order":"se  añadio su orden"})
    
    def get(self):
        orders_list=orders
        return jsonify({"productos": orders}),200