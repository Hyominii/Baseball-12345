import pytest
from game import Game


@pytest.fixture()
def game():
    return Game()


def assert_illegal_argument(game, guess_num):
    try:
        game.guess(guess_num)
        pytest.fail()
    except TypeError:
        pass

def test_exception_when_input_is_none(game):
    assert_illegal_argument(game, None)

def test_exception_when_input_length_is_unmatched(game):
    assert_illegal_argument(game, "12")


