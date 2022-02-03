import threading
from sqlalchemy import Column, String
from Predator.modules.sql import BASE, SESSION
class KukiChats(BASE):
    __tablename__ = "knight_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id

knightChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_knight(chat_id):
    try:
        chat = SESSION.query(knightChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()

def set_knight(chat_id):
    with INSERTION_LOCK:
        kukichat = SESSION.query(knightChats).get(str(chat_id))
        if not knightchat:
           knightchat = knightChats(str(chat_id))
        SESSION.add(knightchat)
        SESSION.commit()

def rem_knight(chat_id):
    with INSERTION_LOCK:
        kukichat = SESSION.query(knightChats).get(str(chat_id))
        if kukichat:
            SESSION.delete(knightchat)
        SESSION.commit()


def get_all_kuki_chats():
    try:
        return SESSION.query(knightChats.chat_id).all()
    finally:
        SESSION.close()
