-- Title: Only Comedy
-- Script to list all shows with the genre "Comedy" from `hbtn_0d_tvshows`
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by tv_shows.title

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN genres ON tv_show_genres.genre_id = genres.id
WHERE genres.name = "Comedy"
ORDER BY tv_shows.title;
