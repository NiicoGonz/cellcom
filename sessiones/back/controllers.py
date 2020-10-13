from flask.views import MethodView
from flask import jsonify, request
from config import KEY_AUTH_TOKEN

class LoginUserControllers(MethodView):
    """
        Example Login
    """
    def post(self):
        content = request.get_json()
        email = content.get("email")
        print(email)
        password = content.get("password")
        print(password)
        if (email == "prueba@gmail.com" and password == "123"):
            return jsonify({"Status": "Login ok", "name": "Pepe Perez", "token": KEY_AUTH_TOKEN}), 200
        return jsonify({"Status": "Wrong login"}), 403
