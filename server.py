from flask import Flask
from flask_caching import Cache
from src.pi import PI


app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 3600})
cache.init_app(app)

def return_error(error_message: str, error_code: int):
    return {
        'ok': False,
        'error_code': error_code,
        'error': error_message
    }, error_code

@app.get('/calc/<digits>')
@cache.cached()
def main(digits):
    try:
        digits = int(digits)
    except ValueError:
        return return_error('Bad request. Not a number.', 400)

    if digits > 10 ** 4:
        return return_error('Bad request. Max digits is 10^4.', 400)

    pi = str(PI(digits).calc())
    pi = f'{pi[:1]}.{pi[1:]}'

    return {
        'ok': True,
        'pi': pi
    }

@app.get('/get/<digits>')
def get(digits):
    try:
        digits = int(digits)
    except ValueError:
        return return_error('Bad request. Not a number.', 400)

    if digits > 10 ** 6:
        return return_error('Bad request. Max digits is 10^6.', 400)

    try:
        with open('1b.pii', 'r') as f:
            pi = f.read(2 + digits)
    except FileNotFoundError:
        return return_error('PI file not found.', 500)

    return {
        'ok': True,
        'pi': pi
    }

if __name__ == "__main__":
    app.debug = True
    app.run()