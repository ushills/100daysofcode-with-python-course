from directors import get_movies_by_director


def test():
    directors = get_movies_by_director()

    assert 'Sergio Leone' in directors
    assert 'Andrew Stanton' in directors  # has 3 movies, but not yet filtered
    assert len(directors['Sergio Leone']) == 4
    assert len(directors['Peter Jackson']) == 12


if __name__ == '__main__':
    print(test())
