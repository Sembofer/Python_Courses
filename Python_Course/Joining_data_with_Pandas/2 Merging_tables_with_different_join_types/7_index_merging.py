movies_genres = movies.merge(movie_to_genres, left_on='id', left_index=True,
                            right_on='movie_id', right_index=True)
print(movies_genres.head())
