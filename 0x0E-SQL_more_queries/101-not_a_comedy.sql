-- Script to list all shows that do not have the genre "Comedy."
-- Results are sorted in ascending order by the show title.

SELECT 
    tv_shows.title
FROM 
    tv_shows
WHERE 
    tv_shows.id NOT IN (
        SELECT 
            tv_show_genres.show_id
        FROM 
            tv_show_genres
        JOIN 
            tv_genres ON tv_genres.id = tv_show_genres.genre_id
        WHERE 
            tv_genres.name = 'Comedy'
    )
ORDER BY 
    tv_shows.title ASC;
