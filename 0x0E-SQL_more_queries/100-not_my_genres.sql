-- Title: Not my genre
-- Script to list all genres not linked to the show "Dexter" from `hbtn_0d_tvshows`
-- Each record displays: genres.name
-- Results are sorted in ascending order by genre name

SELECT name 
FROM genres 
WHERE id NOT IN (
    SELECT genre_id 
    FROM tv_show_genres 
    WHERE tv_show_id = (
        SELECT id 
        FROM tv_shows 
        WHERE title = "Dexter"
    )
)
ORDER BY name;
