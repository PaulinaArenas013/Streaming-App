CREATE TABLE gender(
	id INT PRIMARY KEY AUTO_INCREMENT,
	type_name VARCHAR(50)
);

CREATE TABLE user(
	id INT PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(50) NOT NULL,
	password_user VARCHAR(50) NOT NULL,
	email VARCHAR(50) NOT NULL
);

CREATE TABLE media(
	id INT PRIMARY KEY AUTO_INCREMENT,
	media_name VARCHAR(250) NOT NULL,
	gender_id INT,
	descriptions VARCHAR(500) NOT NULL,
	FOREIGN KEY (gender_id) REFERENCES gender(id)
);

CREATE TABLE playlist_history (
	id INT PRIMARY KEY AUTO_INCREMENT,
	id_user INT,
	media_id INT,
	date_hist DATE,
	FOREIGN KEY (id_user) REFERENCES user(id),
	FOREIGN KEY (media_id) REFERENCES media(id)
);

CREATE TABLE playlist(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_user INT,
    media_id INT,
    title VARCHAR(100) NOT NULL,
    FOREIGN KEY (id_user) REFERENCES user(id),
    FOREIGN KEY (media_id) REFERENCES media(id)
);