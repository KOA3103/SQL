CREATE TABLE IF NOT EXISTS Artist (
	id_artist SERIAL UNIQUE NOT NULL PRIMARY KEY,
	artist_name VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Genre (
	id_genre SERIAL UNIQUE NOT NULL PRIMARY KEY,
	genre_title VARCHAR(20) UNIQUE NOT NULL
);

-- многие ко многим 
CREATE TABLE IF NOT EXISTS genre_artist (
	id_artist INTEGER REFERENCES artist(id_artist),
	id_genre INTEGER REFERENCES genre(id_genre),
	CONSTRAINT g_a PRIMARY KEY (id_artist, id_genre)
);

CREATE TABLE IF NOT EXISTS album (
	id_album SERIAL UNIQUE NOT NULL PRIMARY key,
	album_title VARCHAR(40) UNIQUE NOT NULL,
	year_of_releas INTEGER NOT null
);

-- многие ко многим
CREATE TABLE IF NOT EXISTS album_artist (
	id_artist INTEGER NOT NULL REFERENCES artist(id_artist),
	id_album INTEGER NOT NULL REFERENCES album(id_album),
	CONSTRAINT a_a PRIMARY KEY (id_artist, id_album)
);

CREATE TABLE IF NOT EXISTS track (
	id_track SERIAL UNIQUE NOT NULL PRIMARY KEY,
	id_album INTEGER NOT NULL REFERENCES album(id_album),
	track_title VARCHAR(40) NOT NULL,
	duration TIME NOT NULL
);

CREATE TABLE IF NOT EXISTS collection (
	id_collection SERIAL UNIQUE NOT NULL PRIMARY KEY,
	collection_title VARCHAR(40) NOT NULL,
	release_year INTEGER NOT NULL);

-- многие ко многим
CREATE TABLE IF NOT EXISTS track_collection (
	id_collection INTEGER NOT NULL REFERENCES Collection(id_collection),
	id_track INTEGER NOT NULL REFERENCES track(id_track),
	CONSTRAINT t_c PRIMARY KEY (id_collection, id_track)
);



