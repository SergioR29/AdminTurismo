CREATE TABLE "Categorias" (
	"ID"	INTEGER NOT NULL,
	"Nombre"	TEXT NOT NULL UNIQUE,
	"Prioridad"	INTEGER DEFAULT 0,
	"Color"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE "Ciudades" (
	"ID"	INTEGER NOT NULL,
	"Nombre"	TEXT NOT NULL UNIQUE,
	"Imagen"	BLOB,
	"Descripcion"	TEXT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
CREATE TABLE "Sitios" (
	"ID"	INTEGER NOT NULL,
	"Nombre"	TEXT NOT NULL UNIQUE,
	"Descripcion"	TEXT,
	"Imagen"	BLOB,
	"Ciudad"	INTEGER DEFAULT 0,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("Ciudad") REFERENCES "Ciudades"("ID")
);
CREATE TABLE "Tareas" (
	"ID"	INTEGER NOT NULL,
	"Titulo"	TEXT NOT NULL UNIQUE,
	"Icono"	BLOB,
	"Descripcion"	TEXT,
	"Fecha_Inicio"	TEXT,
	"Hora_Inicio"	TEXT,
	"Plazo_Fecha"	TEXT NOT NULL,
	"Plazo_Hora"	TEXT,
	"Prioridad"	INTEGER,
	"Categoria"	INTEGER DEFAULT 0,
	PRIMARY KEY("ID" AUTOINCREMENT),
	FOREIGN KEY("Categoria") REFERENCES "Categorias"("ID")
);
CREATE TABLE "VersionTurismo" (
	"Ver"	INTEGER
);