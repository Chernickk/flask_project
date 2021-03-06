from app import socketio, db
from flask import request
from flask_login import current_user
from flask_socketio import emit, join_room
from app.models import Message

clients = {'user.id': 'session.id'}


@socketio.on('send_from')
def send_message(data, target_id):
    message = Message(sender_id=current_user.id,
                      receiver_id=target_id,
                      body=data)
    db.session.add(message)
    db.session.commit()

    emit('send_to', {'data': data, 'from_id': request.sid}, to=clients[target_id])


@socketio.on('user_connect')
def connect(user_id):
    clients[user_id] = request.sid
    join_room(request.sid)
