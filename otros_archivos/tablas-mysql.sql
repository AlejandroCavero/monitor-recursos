-- usuario -> monitorizacion
create database db_monitorizacion

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255),
    nombreusuario varchar(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    contrasena VARCHAR(255) NOT NULL
);

CREATE TABLE maquinas (
    id_maquina INT AUTO_INCREMENT PRIMARY KEY,
    nombre_maquina VARCHAR(100),
    url_maquina VARCHAR(255),
    notificaciones TINYINT(1), 
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);