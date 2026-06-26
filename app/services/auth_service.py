from app.models.usuario import Usuario
from app.database.database import bcrypt

class AuthService:
  @staticmethod
  def login(email, password):
    usuario = Usuario.query.filter_by(email=email).first()

    if not usuario:
      return None
    
    if not bcrypt.check_password_hash(
      usuario.password,
      password
    ):
      return None
    
    return usuario