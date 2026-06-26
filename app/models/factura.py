from app.database.database import db
from datetime import datetime

class Factura(db.Model):
    __tablename__ = 'facturas'
    
    id = db.Column(
      db.Integer, 
      primary_key=True
    )

    id_cita = db.Column(
      db.Integer, 
      db.ForeignKey('citas.id'), 
      nullable=False
    )
    
    numero_factura = db.Column(
      db.String(50), 
      nullable=False
    )

    fecha_emision = db.Column(
      db.DateTime, 
      default=datetime.utcnow
    )
    
    subtotal = db.Column(
      db.Float, 
      nullable=False
    )

    descuento = db.Column(
      db.Float, 
      default=0.0
    ) 

    total_pagar = db.Column(
        db.Float, 
        nullable=False
      )
    
    metodo_pago = db.Column(
      db.String(50), 
      nullable=False
    )
    
    puntos_ganados = db.Column(
      db.Integer, 
      default=0
    ) 