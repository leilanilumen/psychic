import builtins
from datetime import date
import mock
import pytest

from tools.horoscope import run
from tools.horoscope import signs


@pytest.mark.parametrize('birthday, expected_sign', (
    (date(1950, 3, 21), 'aries'),
    (date(1950, 4, 19), 'aries'),
    (date(1950, 4, 20), 'taurus'),
    (date(1950, 5, 20), 'taurus'),
    (date(1950, 5, 21), 'gemini'),
    (date(1950, 6, 20), 'gemini'),
    (date(1950, 6, 21), 'cancer'),
    (date(1950, 7, 22), 'cancer'),
    (date(1950, 7, 23), 'leo'),
    (date(1950, 8, 22), 'leo'),
    (date(1950, 8, 23), 'virgo'),
    (date(1950, 9, 22), 'virgo'),
    (date(1950, 9, 23), 'libra'),
    (date(1950, 10, 22), 'libra'),
    (date(1950, 10, 23), 'scorpio'),
    (date(1950, 11, 21), 'scorpio'),
    (date(1950, 11, 22), 'sagittarius'),
    (date(1950, 12, 21), 'sagittarius'),
    (date(1950, 12, 22), 'capricorn'),
    (date(1950, 1, 19), 'capricorn'),
    (date(1950, 1, 20), 'aquarius'),
    (date(1950, 2, 18), 'aquarius'),
    (date(1950, 2, 19), 'pisces'),
    (date(1950, 3, 20), 'pisces'),
))
def test_get_sign(birthday, expected_sign):
    assert signs.get_sign(birthday) == expected_sign


@pytest.mark.parametrize('invalid_birthday', (
    '',
    ' ',
    '12345',
    'not_a_date',
    '12/35/1988'
))
def test_valid_birthday(invalid_birthday, capsys):
    with mock.patch.object(builtins, 'input', lambda _: invalid_birthday):
        run.main()
        output, _ = capsys.readouterr()
        assert output == '\nblah, invalid birthday\n\n\n\n'
