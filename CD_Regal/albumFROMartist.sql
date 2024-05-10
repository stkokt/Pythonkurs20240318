select album_name from album
INNER JOIN track on track.artist_id = album.artist_id
INNER JOIN genre on genre.genre_id = track.genre_id
INNER JOIN artist on artist.artist_id = track.artist_id
WHERE artist.artist_name like '%Dea%'
AND genre.genre_name like '%Ro%'
