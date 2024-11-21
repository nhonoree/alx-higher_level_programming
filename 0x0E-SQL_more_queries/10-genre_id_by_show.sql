-- List each TV show's title with its associated genre IDs
-- If a show has multiple genres, list them on separate rows

SELECT 
    tv_shows.title,          -- Title of the TV show
    tv_show_genres.genre_id  -- ID of the genre linked to the show
FROM 
    tv_shows
JOIN 
    tv_show_genres 
ON 
    tv_shows.id = tv_show_genres.show_id  -- Linking TV shows with the linking table
ORDER BY 
    tv_shows.title ASC,      -- Sort results by show title
    tv_show_genres.genre_id ASC;  -- Then sort by genre ID
