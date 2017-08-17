import mock
import pytest

import horoscope
from horoscope import run


@pytest.mark.parametrize('birthday, expected_sign', (
    (None, None),
))
def test_astrological_sign(birthday, expected_sign):
    pass


@pytest.mark.parametrize('invalid_birthday', (
    '',
))
def test_valid_birthday(invalid_birthday):
    with mock.patch.object(__builtin__, 'input', lambda: invalid_birthday):
        with pytest.raises(ValueError):
            run.main()
