from app.database.database import db

class Producto(db.Model):
    __tablename__ = 'productos'
    
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
    stock_actual = db.Column(
        db.Float, 
        default=0.0
      )
    stock_minimo = db.Column(
      db.Float,
      default=5.0
    )
    precio_costo = db.Column(
      db.Float, 
      nullable=False
    )
    unidad_medida = db.Column(
      db.String(20), 
      nullable=False
    )