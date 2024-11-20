-- Title: List Shows and Genres
-- Script to list all shows and all genres from `hbtn_0d_tvshows`
-- Each record displays: tv_shows.title - genres.name
-- Results are sorted in ascending order by tv_shows.title and genres.name

SELECT tv_shows.title, genres.name
FROM tv_shows
CROSS JOIN genres
ORDER BY tv_shows.title, genres.name;
