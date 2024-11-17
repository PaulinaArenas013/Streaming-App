from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Table, text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import datetime

Base = declarative_base()

class Gender(Base):
    __tablename__ = 'gender'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String(50))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password_user = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    playlists = relationship('Playlist', back_populates="user")
    history = relationship('PlaylistHistory', back_populates="user")

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True, autoincrement=True)
    media_name = Column(String(250), nullable=False)
    gender_id = Column(Integer, ForeignKey('gender.id'))
    descriptions = Column(String(500), nullable=False)
    history = relationship('PlaylistHistory', back_populates='media')
    gender = relationship('Gender')

class PlaylistHistory(Base):
    __tablename__ = 'playlist_history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    media_id = Column(Integer, ForeignKey('media.id'))
    date_hist = Column(Date, default=datetime.datetime.utcnow)
    user = relationship('User', back_populates="history")
    media = relationship('Media', back_populates='history')

class Playlist(Base):
    __tablename__ = 'playlist'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    media_id = Column(Integer, ForeignKey('media.id'))
    title = Column(String(100), nullable=False)
    user = relationship('User', back_populates="playlists")
    media = relationship('Media')

# Create the database
DATABASE_URL = "mysql+pymysql://root:DragonFly131@localhost/streaming2"
engine = create_engine(DATABASE_URL, pool_size=5, max_overflow=10, pool_timeout=30)

# Verificar la conexión
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Connection to the database was successful!")
except Exception as e:
    print(f"An error occurred: {e}")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def perform_database_operations():
    with Session() as session:
        try:
            user = session.query(User).first()
            print(f"First user: {user.username}")
        except Exception as e:
            print(f"An error occurred while accessing the database: {e}")
            session.rollback()

# Llama a la función para realizar las operaciones
perform_database_operations()

