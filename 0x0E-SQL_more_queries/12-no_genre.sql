-- Title: Shows Without a Genre
-- Script to list all shows without a genre linked from `hbtn_0d_tvshows`
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by tv_shows.title

SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title;
