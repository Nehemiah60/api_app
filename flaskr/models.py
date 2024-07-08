from flaskr import db


class Plant(db.Model):
    __tablename__ = 'plants'
    id          =      db.Column(db.Integer, primary_key=True)
    name        =      db.Column(db.String())
    scientific_name =  db.Column(db.String())
    is_poisonous  =    db.Column(db.Boolean)
    primary_color =    db.Column(db.String())

    def __init__(self, name, scientific_name, is_poisonous, primary_color):
        self.name            = name
        self.scientific_name = scientific_name
        self.is_poisonous    =    is_poisonous
        self.primary_color   =   primary_color
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'scientific_name': self.scientific_name,
            'is_poisonous': self.is_poisonous,
            'primary_color':self.primary_color
        }