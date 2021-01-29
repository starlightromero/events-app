"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
import enum


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    events_attending = db.relationship(
        "Event", secondary="guest_event", back_populates="guests"
    )


class EventType(enum.Enum):
    Party = 1
    Study = 2
    Networking = 3
    Other = 4


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date_and_time = db.Column(db.DateTime)
    event_type = db.Column(db.Enum(EventType), default=EventType.Other)
    guests = db.relationship(
        "Guest", secondary="guest_event", back_populates="events_attending"
    )


guest_event_table = db.Table(
    "guest_event",
    db.Column("guest_id", db.Integer, db.ForeignKey("guest.id")),
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"))
)