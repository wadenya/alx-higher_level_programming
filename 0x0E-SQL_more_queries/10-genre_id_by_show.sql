-- ists all shows contained in hbtn_0d_tvshows that 
-- have at least one genre linked.
SELECT t.`title`, gi.`genre_id`
  FROM `tv_shows` AS t
        INNER JOIN `tv_show_genres` AS gi
	ON t.`id` = gi.`show_id`
 ORDER BY t.`title`, gi.`genre_id`;
