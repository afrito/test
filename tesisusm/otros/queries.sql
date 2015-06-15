--crea la base de datos "tesis_core"
CREATE DATABASE tesis_core;

--crea el usuario "tesis"
CREATE USER tesis IDENTIFIED BY 'tesis123';

--establece los permisos del usuario "tesis"
GRANT ALL PRIVILEGES ON tesis_core.* TO tesis;
