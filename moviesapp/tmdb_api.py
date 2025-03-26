YEAR_START = 2001
YEAR_END = 2025

import requests
from moviesapp.models import Movie
from lists.settings import TMDB_API_KEY


headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_KEY}",
}

for year in range(YEAR_START,YEAR_END+1):
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&year={year}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        total_page = response.json().get('total_pages')

        for page_number in range(1,total_page+1):
            url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={page_number}&sort_by=popularity.desc&year={year}"
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                movies=response.json().get('results',[])

                for movie in movies:
                    movie_id = movie.get('id')
                    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
                    response = requests.get(url, headers=headers)

                    if response.status_code == 200:
                        movie_item = response.json()
                        try:
                            created_movie, create = Movie.objects.update_or_create(
                                defaults={'popularity':movie_item.get('popularity')},
                                id=movie_item.get('id'), imdb_id=movie_item.get('imdb_id'),
                                title=movie_item.get('title'), overview=movie_item.get('overview'),
                                poster_path=movie_item.get('poster_path'),
                                release_date=movie_item.get('release_date'), revenue=movie_item.get('revenue'),
                                budget=movie_item.get('budget'),
                                runtime=movie_item.get('runtime'), vote_average=movie_item.get('vote_average'),
                                vote_count=movie_item.get('vote_count'),
                                status=movie_item.get('status')
                            )
                            if create:
                                genres = [genre["id"] for genre in movie_item.get('genres')]
                                created_movie.genres.set(genres)
                        except Exception as e:
                            # print(f'Unexpected error {e}')
                            continue
                    else:
                        print(f'Error on take movie detail {movie_id} stage: {response.status_code}')
                        continue

            else:
                print(f'Error on take page {page_number} stage: {response.status_code}')
                continue

    else:
        print(f'Error on take year {year} stage: {response.status_code}')
        continue