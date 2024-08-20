from app import db

class Person(db.Model):
    __tablename__ = 'people'
    
    pid = db.Column(db.Double, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Double)
    
    
    def __repr__(self):
        return f'Person whit the name{self.name} and age {self.age}'