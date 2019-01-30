from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class ChoiceList(db.Model):
    """This class represents choice list"""

    __tableaname__ = "choicelists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_on = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )

    def __init__(self, name):
        """initialize with name."""
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return ChoiceList.query.all()

    def delete(self):
        self.session.delete(self)
        self.session.commit()

    def __repr__(self):
        return "<ChoiceList: {}>".format(self.name)
