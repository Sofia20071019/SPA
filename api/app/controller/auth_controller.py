from flask import request, jsonify
from flask_jwt_exrended import create_accsess_token

from api.app.services.auth_service import AuthService

class AuthController:

    @staticmethod
    def login():

        data = request.get_json()
        
        email = data.get("email")
        password = data.get("password")

        usuario = AuthService.login(email, password)

        if usuario is None:

            return jsonify({
                "message": "Credenciales incorrectas"
            }), 401
        token = create_accsess_token(
            identify = str (usuario.id)
        )
        return jsonify({
            "accessToken": token,

            "user":{
                "id": usuario.id,
                "nombre_usuario": usuario.nombre_usuario,
                "email": usuario.email,
                "rol": usuario.rol.nombre,
                "avatar": usuario.avatar
            }
        }),200