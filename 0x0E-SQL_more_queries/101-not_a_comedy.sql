-- Title: No Comedy tonight!
-- Script to list all shows without the genre "Comedy" from `hbtn_0d_tvshows`
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by show title

SELECT title 
FROM tv_shows 
WHERE id NOT IN (
    SELECT tv_show_id 
    FROM tv_show_genres 
    WHERE genre_id = (
        SELECT id 
        FROM genres 
        WHERE name = "Comedy"
    )
)
ORDER BY title;
