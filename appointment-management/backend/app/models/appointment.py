from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from backend.app import db

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    time = Column(String, nullable=False)
    client_name = Column(String, nullable=False)

    def __init__(self, date, time, client_name):
        self.date = date
        self.time = time
        self.client_name = client_name

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()