from app.database.database import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(
        db.Integer,
        primary_key = True
    )
    nombre = db.Column(
        db.String(100),
        nullable = False,
        unique = True
    )
    correo = db.Column(
        db.String(120),
        unique = True,
        nullable = False
    )
    contrasena = db.Column(
        db.String(255),
        nullable = False
    )
    estado = db.Column(
        db.Boolean,
        defautl = True
    )
    creado_en = db.Column(
        db.DateTime,
        default = datetime.utcnow
    )
    
#       Perfil de cliente

    class Cliente_Perfil(db.Model):
        __tablename__ = 'clientes_perfiles'

        id = db.Column(
            db.Integer,
            primary_key = True
        )
        id_usuario = db.Column(
            db.Integer,
            db.ForeignKey('usuario.id'),
            nullable = False
        )
        nombre = db.Column(
            db.String(100),
            nullable = False
        )
        documento = db.Column(
            db.String(20),
            nullable = False
        )
        fecha_nacimiento = db.Column(
            db.Date,
            nullable = False
        )
        genero = db.Column(
            db.String(10),
            nullable = False   
        )
        telefono = db.Column(
            db.String(20),
            nullable = True
        )
        direccion = db.Column(
            db.String(150),
            nullable = True
        )
        foto_perfil = db.Column(
            db.String(255),
            nullable = True
        )
        puntos_acumulados = db.Column(
            db.Integer,
            default = 0
        )

#           Perfil de esteticista

        class Esteticista_Perfil(db.Model):
            __tablename__ = 'esteticistas_perfiles'

            id =db.Column(
                db.Integer,
                primary_key = True
            )
            id_usuario = db.Column(
                db.Integer,
                db.ForeignKey('usuario.id'),
                nullable = False
            )
            nombre = db.Column(
                db.String(100),
                nullable = False
            )
            documento = db.Column(
                db.String(20),
                nullable = False
            )
            especialidad = db.Column(
                db.String(200),
                nullable = False
            )
            telefono = db.Column(
                db.String(20),
                nullable = True
            )
            horario_laboral = db.Column(
                db.String(100),
                nullable = True
            )
            foto = db.Column(
                db.String(255),
                nullable = True
            )