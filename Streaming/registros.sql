INSERT INTO gender (type_name) VALUES 
('Animación'), ('Comedia'), ('Acción'), ('Drama');

-- Insertar datos en la tabla user
INSERT INTO user (username, password_user, email) VALUES 
('user1', 'password1', 'user1@example.com'), 
('user2', 'password2', 'user2@example.com');

-- Insertar datos en la tabla media
INSERT INTO media (media_name, gender_id, descriptions) VALUES 
('Zootopia', 1, 'Una conejita policía y un astuto zorro deben trabajar juntos para resolver un misterio en la metrópolis de animales de Zootopia.'),
('Legalmente rubia', 2, 'Una joven rubia y alegre decide estudiar derecho en Harvard para recuperar a su novio, y termina sorprendiendo a todos con su talento legal.'),
('Clueless', 2, 'Una adolescente rica y popular de Beverly Hills se dedica a jugar a ser casamentera con sus amigos, mientras aprende algunas lecciones de vida en el proceso.'),
('C.I.P.O.L.', 3, 'Durante la Guerra Fría, un agente de la CIA y otro de la KGB deben colaborar en una misión conjunta contra una organización criminal internacional.');

-- Insertar datos en la tabla playlist_history
INSERT INTO playlist_history (id_user, media_id, date_hist) VALUES 
(1, 1, '2024-07-01'),
(1, 2, '2024-07-02'),
(2, 3, '2024-07-01'),
(2, 4, '2024-07-02');

-- Insertar datos en la tabla playlist
INSERT INTO playlist (id_user, media_id, title) VALUES 
(1, 1, 'Favoritas de Animación'),
(1, 2, 'Comedias favoritas'),
(2, 3, 'Películas de adolescentes'),
(2, 4, 'Películas de Acción');