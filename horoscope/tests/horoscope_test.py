import pytest

import horoscope


@pytest.mark.parametrize('birthday, expected_sign', (
    (),
))
def test_astrological_sign(birthday, expected_sign):
    pass


@pytest.mark.parametrize('invalid_birthday', (
    '',
))
def test_valid_birthday(invalid_birthday):
    with pytest.raises(ValueError):
        horoscope.input = invalid_birthday
