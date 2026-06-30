from flask import Blueprint

from api.app.controller.auth_controller import AuthController

auth_bp = Blueprint(
    "auth",
    __name__
)

auth_bp.route(
    "/login",
    methods = ["POST"]
)(
    AuthController.login
)