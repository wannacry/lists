import requests
from bs4 import BeautifulSoup
from moviesapp.models import Movie


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
movies = Movie.objects.filter(imdb_id__isnull=False,imdb_rating__isnull=True) #imdb_rating__isnull=True for movie without rating(delete for update)

for movie in movies:

    url = f'https://www.imdb.com/title/{movie.imdb_id}/'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html_parse = BeautifulSoup(response.text,'html.parser')
        get_html_element = html_parse.find('span',class_='imUuxf')

        if get_html_element:
            try:
                movie_rating = float(get_html_element.text)
                movie.imdb_rating = movie_rating
                movie.save()
            except ValueError:
                print('problem whith type of value')
            except Exception as e:
                print(f'Unexpected error {e}')
        else:
            print('html object not found')

    else:
        print(f'Error request to imdb stage {response.status_code}')

else:
    print('end rating updating')