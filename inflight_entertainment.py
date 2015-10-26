def get_two_movies_to_fill_flight(movie_lengths, flight_length):
    movie_lengths_seen_hash = {}

    for movie in movie_lengths:
        matching_second_movie_length = flight_length - movie
        if matching_second_movie_length in movie_lengths_seen_hash:
            return True

        movie_lengths_seen_hash[first_movie_length] = True

    return False

get_two_movies_to_fill_flight
