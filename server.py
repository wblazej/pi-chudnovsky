from flask import Flask
from src.read_pi import ReadPI

app = Flask(__name__)

def return_error(error_message: str, error_code: int):
    return {
        'ok': False,
        'error_code': error_code,
        'error': error_message
    }, error_code

@app.get('/digits/<digits>')
def digits(digits):
    try:
        digits = int(digits)
    except ValueError:
        return return_error('Bad request. Not a number.', 400)

    if digits > 10 ** 6:
        return return_error('Bad request. Max digits is 10^6.', 400)

    try:
        reading = ReadPI('1b.pi')
        pi = reading.read(digits)
    except FileNotFoundError:
        return return_error('PI file not found.', 500)

    return {
        'ok': True,
        'pi': pi
    }

@app.get('/range/<_from>/<_to>')
def range(_from, _to):
    try:
        _from = int(_from)
        _to = int(_to)
    except ValueError:
        return return_error('Bad request. Not a number.', 400)

    if _from < 0 or _to > 10 ** 9 or _from >= _to:
        return return_error('Bad request.', 400)

    if _to - _from > 10 ** 6:
        return return_error('Bad request. Max range is 10^6.', 400)

    try:
        reading = ReadPI('1b.pi')
        pi = reading.read(_from=_from, _to=_to)
    except FileNotFoundError:
        return return_error('PI file not found.', 500)

    return {
        'ok': True,
        'pi': pi
    }

if __name__ == "__main__":
    app.debug = True
    app.run()
