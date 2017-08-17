import builtins
import mock
import pytest

from horoscope import run


@pytest.mark.parametrize('birthday, expected_sign', (
    ('3/21/1950', 'ARIES'),
    ('4/19/1950', 'ARIES'),
    ('4/20/1950', 'TAURUS'),
    ('5/20/1950', 'TAURUS'),
    ('5/21/1950', 'GEMINI'),
    ('6/20/1950', 'GEMINI'),
    ('6/21/1950', 'CANCER'),
    ('7/22/1950', 'CANCER'),
    ('7/23/1950', 'LEO'),
    ('8/22/1950', 'LEO'),
    ('8/23/1950', 'VIRGO'),
    ('9/22/1950', 'VIRGO'),
    ('9/23/1950', 'LIBRA'),
    ('10/22/1950', 'LIBRA'),
    ('10/23/1950', 'SCORPIO'),
    ('11/21/1950', 'SCORPIO'),
    ('11/22/1950', 'SAGITTARIUS'),
    ('12/21/1950', 'SAGITTARIUS'),
    ('12/22/1950', 'CAPRICORN'),
    ('1/19/1950', 'CAPRICORN'),
    ('1/20/1950', 'AQUARIUS'),
    ('2/18/1950', 'AQUARIUS'),
    ('2/19/1950', 'PISCES'),
    ('3/20/1950', 'PISCES'),
))
def test_astrological_sign(birthday, expected_sign, capsys):
    with mock.patch.object(builtins, 'input', lambda _: birthday):
        run.main()
        output, _ = capsys.readouterr()
        assert bool(set(output) & set(expected_sign))


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
