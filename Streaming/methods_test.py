from conection import User, Media, Playlist, Gender, PlaylistHistory
from datetime import date as current_date

def test_user_auth(session):
    user = User(username='user_temp', password_user='password_temp', email='user_temp@example.com')
    session.add(user)
    session.commit()
    query = session.query(User).filter_by(username=user.username, password_user=user.password_user)
    assert query.count() > 0, "User authentication failed"

def test_generate_playlist_history(session):
    gender = Gender(type_name="test gender")
    session.add(gender)
    session.commit()

    media = Media(media_name="test media", gender_id=gender.id, descriptions="This is a test media description")
    session.add(media)
    session.commit()

    first_user = session.query(User).first().id
    playlist_history = PlaylistHistory(id_user=first_user, media_id=media.id, date_hist=current_date.today())
    session.add(playlist_history)
    session.commit()

    assert playlist_history.id_user is not None, "User ID should not be None"
    assert playlist_history.media_id is not None, "Media ID should not be None"
    assert playlist_history.date_hist is not None, "Date should not be None"

def test_create_user(session):
    user = User(username='new_user', password_user='new_password', email='new_user@example.com')
    session.add(user)
    session.commit()
    assert user.id is not None, "User ID should not be None"

def test_create_media(session):
    gender = Gender(type_name="test gender 2")
    session.add(gender)
    session.commit()
    
    media = Media(media_name='new_media', gender_id=gender.id, descriptions='New media description')
    session.add(media)
    session.commit()
    assert media.id is not None, "Media ID should not be None"

def test_create_playlist(session):
    user = User(username='playlist_user', password_user='playlist_password', email='playlist_user@example.com')
    session.add(user)
    session.commit()

    media = Media(media_name='playlist_media', descriptions='Playlist media description')
    session.add(media)
    session.commit()

    playlist = Playlist(id_user=user.id, media_id=media.id, title='My Playlist')
    session.add(playlist)
    session.commit()
    assert playlist.id is not None, "Playlist ID should not be None"

def test_create_gender(session):
    gender = Gender(type_name='new_gender')
    session.add(gender)
    session.commit()
    assert gender.id is not None, "Gender ID should not be None"