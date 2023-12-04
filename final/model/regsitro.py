from basededato import db, main, ma 

class login(db.Model):
    __tablename__ = "login"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    apellido= db.Column(db.String(200))
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido =  apellido
        

with main.app_context():
    db.create_all()
    
class AutoresSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'apellido')