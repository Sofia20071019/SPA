from api.app.database.database import db
from datetime import datetime

class Cita(db.Model):
    __tablename__ = 'citas'
    
    id = db.Column(
      db.Integer, 
      primary_key=True
    )
    id_cliente = db.Column(
      db.Integer, 
      db.ForeignKey('usuarios.id'), 
      nullable=False
    )
    id_esteticista = db.Column(
      db.Integer, 
      db.ForeignKey('usuarios.id'), 
      nullable=False
    )
    id_servicio = db.Column(
      db.Integer, 
      db.ForeignKey('servicios.id'), 
      nullable=False
    )
    fecha_cita = db.Column(
      db.Date, 
      nullable=False
    )
    hora_cita = db.Column(
      db.String(10), 
      nullable=False
    )
    estado_cita = db.Column(
      db.String(30), 
      default='Pendiente'
    ) 
    observaciones = db.Column(
      db.String(255), 
      nullable=True
    )
    creada_en = db.Column(
      db.DateTime, 
      default=datetime.utcnow
    )