-- Найдем название и год выхода альбомов, вышедших после 2000 года.
SELECT album_title, year_of_releas FROM album
WHERE year_of_releas >= 2000;

-- Найдем название и продолжительность самого длительного трека.
SELECT track_title, duration FROM track
ORDER BY duration DESC LIMIT 1;

-- Найдем название треков, продолжительность которых не менее 3,5 минуты.
SELECT track_title, duration FROM track
WHERE duration > '00:03:30';

-- Найдем названия сборников, вышедших в период с 2018 по 2040 год включительно.
SELECT collection_title, release_year FROM collection
WHERE release_year BETWEEN 2000 AND 2040;

-- Найдем исполнители, чье имя состоит из 1 слова.
SELECT artist_name FROM artist
WHERE artist_name NOT LIKE '% %';

-- Найдем название треков, которые содержат слово “мы”/“We”.
SELECT track_title FROM track 
WHERE string_to_array(lower(track_title), ' ') && ARRAY['за', 'of', 'the', 'нам'];

SELECT  genre_title, count(id_artist) c FROM genre g
LEFT JOIN genre_artist ga ON ga.id_genre = g.id_genre
GROUP BY genre_title;