import csv
from collections import defaultdict, namedtuple, Counter

movies_csv = 'movie_metadata.csv'


def get_movies_by_director(data=movies_csv):
    Movie = namedtuple('Movie', 'title year score')
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                director = row['director_name']
                movie = row['movie_title'].replace('\xa0', '')
                year = int(row['title_year'])
                score = float(row['imdb_score'])
                m = Movie(title=movie, year=year, score=score)
                directors[director].append(m)
            except ValueError:
                continue
    return directors


def get_most_movies(count):
    directors = get_movies_by_director()
    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] += len(movies)
    return cnt.most_common(count)


if __name__ == '__main__':
    print(get_most_movies(5))
