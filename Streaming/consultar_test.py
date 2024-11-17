from conection import User, Playlist, Media, Gender, PlaylistHistory

def test_query_users(session):
    users = session.query(User).all()
    assert len(users) >= 1  # There should be at least one user
    for user in users:
        assert user.username is not None
        assert user.email is not None

def test_query_media(session):
    media_files = session.query(Media).all()
    assert len(media_files) >= 3  # There should be at least three media files
    for media in media_files:
        assert media.media_name is not None
        assert media.descriptions is not None

def test_query_genders(session):
    genders = session.query(Gender).all()
    assert len(genders) > 0  # There should be at least one gender
    for gender in genders:
        assert gender.type_name is not None

def test_query_playlists(session):
    playlists = session.query(Playlist).all()
    assert len(playlists) >= 2  # There should be at least two playlists
    for playlist in playlists:
        assert playlist.title is not None
        assert playlist.id_user is not None

def test_query_playlist_history(session):
    histories = session.query(PlaylistHistory).all()
    assert len(histories) >= 1  # There should be at least one playlist history
    for history in histories:
        assert history.id_user is not None
        assert history.media_id is not None
        assert history.date_hist is not None


        