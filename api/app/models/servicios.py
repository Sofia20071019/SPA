from api.app.database.database import db
from datetime import datetime

#     Tabla intermedia de servicios y productos

class servicio_producto(db.Table):
    __tablename__ = 'servicio_producto'

    id_servicio = db.Column(
      'id_servicio', 
      db.Integer, 
      db.ForeignKey('servicios.id'), 
      primary_key=True)
    id_producto = db.Column(
      'id_producto', 
      db.Integer, 
      db.ForeignKey('productos.id'), 
      primary_key=True)

#     Tabla principal comercial

class Servicio(db.Model):
    __tablename__ = 'servicios'

    id = db.Column(
        db.Integer, 
        primary_key=True
      )
    nombre = db.Column(
      db.String(100), 
      nullable=False
    )
    descripcion = db.Column(
      db.String(255), 
      nullable=False
    )
    duracion = db.Column(
      db.Integer, 
      nullable=False
    )
    precio_base = db.Column(
      db.Float, 
      nullable=False
    )
    imagen = db.Column(
      db.String(255), 
      nullable=True
    )
    categoria = db.Column(
      db.String(50), 
      nullable=False
    )
    estado = db.Column(db.Boolean, default=True)

#     Tabla del historial de precios de los servicios

class HistorialPrecio(db.Model):
    __tablename__ = 'historial_precios'

    id = db.Column(
      db.Integer, 
      primary_key=True
    )
    id_servicio = db.Column(
      db.Integer, 
      db.ForeignKey('servicios.id'), 
      nullable=False
    )
    precio_anterior = db.Column(
      db.Float, 
      nullable=False
    )
    precio_nuevo = db.Column(
      db.Float, 
      nullable=False
    )
    fecha_inicial = db.Column(
      db.DateTime, 
      default=datetime.utcnow
    )
    fecha_final = db.Column(
      db.DateTime, 
      nullable=True
    )
    motivo_cambio = db.Column(
      db.String(255), 
      nullable=False
    )