from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
class AuthUser(Base):
    __tablename__ = "myapp_authuser"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
class Testlar(Base):
    __tablename__ = "myapp_testlar"  # Table nomi
    id = Column(Integer, primary_key=True, autoincrement=True) # primary key
    user_id = user_id = Column(Integer, ForeignKey("myapp_authuser.id"))
    test_id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    fan = Column(String)
    tavsif = Column(String)
    public = Column(Integer)  