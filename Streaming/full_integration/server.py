from flask import Flask, send_from_directory, jsonify, request, redirect, url_for, render_template, abort
from db_integration import User, Playlist, Media, Gender, PlaylistHistory, Session
from PIL import Image
import os

app = Flask(__name__, template_folder='static/html')
app.config['UPLOAD_FOLDER'] = 'static/upload'

@app.route('/')
def home():
	return render_template('login.html')

@app.route('/user/login', methods=['POST'])
def login():
	session = Session()
	data = request.json
	user = session.query(User).filter_by(username=data['username'], password_user=data['password']).first()
	if user:
		return jsonify({"status": "success", "user": user.username})
	else:
		return jsonify({"status": "failure"}), 401

@app.route('/add_media', methods=['GET', 'POST'])
def upload_image():
    session = Session()
    if request.method == 'POST':
        file = request.files['file']
        description = request.form['description']
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            new_media = Media(media_name=filename, descriptions=description)
            session.add(new_media)
            session.commit()
        return redirect(url_for('display_images'))
    return render_template('add_media.html')

@app.route('/display_media')
def display_images():
    session = Session()
    media_list = session.query(Media).all()
    session.close()  # Añadir esto para cerrar la sesión
    return render_template('display_media.html', media_list=media_list)

@app.route('/thumbnail/<int:media_id>')
def get_thumbnail(media_id):
    session = Session()
    media = session.query(Media).filter_by(id=media_id).first()
    if media:
        filename = media.media_name
        thumbnail_filename = f'thumbnail_{filename}'
        thumbnail_path = os.path.join(app.config['UPLOAD_FOLDER'], thumbnail_filename)
        # Generar miniatura si no existe
        if not os.path.exists(thumbnail_path):
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image = Image.open(image_path)
            image.thumbnail((100, 100))  # Tamaño de la miniatura
            image.save(thumbnail_path)
        return send_from_directory(app.config['UPLOAD_FOLDER'], thumbnail_filename)
    else:
        abort(404)

@app.route('/delete_media/<int:media_id>')
def delete_media(media_id):
    session = Session()
    media = session.query(Media).filter_by(id=media_id).first()
    if media:
        session.query(Playlist).filter(Playlist.media_id == media_id).delete()
        session.delete(media)
        session.commit()
        return redirect(url_for('display_images'))
    else:
        abort(404)

@app.route('/edit_media/<int:media_id>', methods=['GET', 'POST'])
def edit_media(media_id):
    session = Session()
    media = session.query(Media).filter_by(id=media_id).first()
    if media:
        if request.method == 'POST':
            media.descriptions = request.form['description']
            if 'file' in request.files and request.files['file']:
                file = request.files['file']
                filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                media.media_name = filename
            session.commit()
            session.close()
            return redirect(url_for('display_images'))
        else:
            session.close()
            return render_template('edit_media.html', media=media)
    else:
        session.close()
        abort(404)

@app.route('/image/<int:media_id>')
def get_image(media_id):		
	session = Session()
	media = session.query(Media).filter_by(id=media_id).first()
	session.close()
	if media:
		filename = media.media_name		
		try:
			return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
		except FileNotFoundError:
			abort(404)
	else:
		abort(404)

if __name__ == '__main__':
	app.run(host = '0.0.0.0',port='8080',debug=True)