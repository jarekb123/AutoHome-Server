from app import db
import datetime


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    create_date = db.Column(db.DateTime)

    sensors = db.relationship('Sensor', backref='device', lazy='dynamic')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Blog %r>' % self.name


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    create_date = db.Column(db.DateTime)

    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))

    def __init__(self, device, name, description, create_date=None):
        self.device_id = device.id
        self.name = name
        self.description = description

        if create_date is None:
            self.create_date = datetime.utcnow()
        else:
            self.create_date = create_date

    def __repr__(self):
        return '<Sensor %r, device_id = %r>' % (self.name, self.device_id)
