-- Title: Best genre
-- Script to list all genres by their rating from `hbtn_0d_tvshows_rate`
-- Each record displays: genres.name - rating sum
-- Results are sorted in descending order by the rating

SELECT genres.name, SUM(rating) AS rating 
FROM genres 
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id 
JOIN tv_show_ratings ON tv_show_genres.tv_show_id = tv_show_ratings.tv_show_id 
GROUP BY genres.name 
ORDER BY rating DESC;
