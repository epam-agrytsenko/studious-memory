import os
import random

PWD = os.path.abspath(os.path.dirname(__file__))


GOOD = [
    'http://sphinx.pocoo.org/',
    'https://wiki.python.org/moin/PythonBooks',
    'https://www.python.org/doc/av/',
    'https://github.com/pallets/flask/tree/master/examples/tutorial/',
    'https://docs.python.org/3.5/',
    'https://pypi.org/project/Flask/0.5/',
    'https://psfmember.org/civicrm/contribute/transact',
    'https://github.com/pallets/flask',
    'https://wiki.python.org/moin/BeginnersGuide',
    'http://www.python.org/dev/peps/pep-0333/',
    'https://www.python.org/',
    'https://github.com/pallets/flask/issues',
    'https://www.python.org/dev/peps/',
    'https://github.com/pallets/flask-website',
    'http://jinja.pocoo.org/docs/',
    'http://lucumr.pocoo.org/',
    'https://realpython.com/',
    'https://pypi.org/',
    'https://www.djangoproject.com/',
    'https://flask.palletsprojects.com/',
    'https://numpy.org/',
    'https://pandas.pydata.org/',
    'https://scikit-learn.org/',
    'https://jupyter.org/',
    'https://matplotlib.org/',
    'https://fastapi.tiangolo.com/',
    'https://docs.python.org/3/',
    'https://stackoverflow.com/',
    'https://github.com/',
    'https://www.reddit.com/r/Python/',
    'https://www.postgresql.org/',
    'https://www.sqlite.org/',
    'https://scipy.org/',
    'https://www.tensorflow.org/',
    'https://pytorch.org/',
    'https://pytest.org/',
    'https://docs.pytest.org/',
    'https://pydantic-docs.helpmanual.io/',
    'https://pythonspeed.com/',
    'https://www.pythonanywhere.com/',
    'https://www.heroku.com/',
    'https://www.digitalocean.com/',
    'https://www.docker.com/',
    'https://kubernetes.io/',
    'https://www.javascript.com/',
    'https://developer.mozilla.org/en-US/',
    'https://wikipedia.org/',
]


NOT_GOOD = [
    'https://www.does_not_exist.com/',
    'https://invalid-url.example.com/',
    'http://nonexistent-domain.fake/',
    'http://123.456.789.000/',
    'http://thisurldoesnotresolve.tld/',
    'http://brokenlink.xyz/',
    'https://404.example.com/',
]


def generate(count: int = 100, rate: float = 0.75) -> list[str]:
    valid, invalid = int(count * rate), count - int(count * rate)  # 75% / 25%
    good_urls = random.choices(GOOD, k=valid)
    not_good = random.choices(NOT_GOOD, k=invalid)
    result = good_urls + not_good
    random.shuffle(result)
    return result


def save_to_file(links: list[str], fname: str) -> str:
    fpath = os.path.join(PWD, fname)
    if os.path.exists(fpath):
        raise RuntimeError(f'File already exists: {fpath}')
    with open(fpath, 'w+') as f:
        f.write('\n'.join(links))
    return fpath


def main(count=100):
    links = generate(count=count)
    fpath = save_to_file(links, fname=f'links_{count}.txt')
    print(f'Generated {count} links into -> {fpath}')


if __name__ == '__main__':
    main(count=1000)
