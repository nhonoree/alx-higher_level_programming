-- Title: Number of Shows by Genre
-- Script to list each genre and the number of shows linked to it from `hbtn_0d_tvshows`
-- Each record displays: genres.name - number_of_shows
-- Results are sorted in descending order by the number of shows and then ascending by genres.name

SELECT genres.name, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM genres
LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC, genres.name;
