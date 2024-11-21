-- Script to list all shows and their linked genres.
-- If a show does not have a genre, display NULL in the genre column.
-- Results are sorted by tv_shows.title and tv_genres.name in ascending order.

SELECT 
    tv_shows.title, 
    tv_genres.name
FROM 
    tv_shows
LEFT JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN 
    tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY 
    tv_shows.title ASC, 
    tv_genres.name ASC;
