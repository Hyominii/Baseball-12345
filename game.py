from game_result import GameResult


class Game:
    def __init__(self):
        self.question = ""

    def guess(self, guess_num) -> GameResult:
        self._assert_illegal_value(guess_num)
        if guess_num == self.question:
            return GameResult(True, 3, 0)
        return None

    def _assert_illegal_value(self, guess_num):
        if guess_num is None:
            raise TypeError("입력이 None 입니다.")

        if not isinstance(guess_num, str) or len(guess_num) != 3:
            raise TypeError("입력은 3 자리 문자열이어야 합니다.")

        if not guess_num.isdigit():
            raise TypeError("모든 문자는 숫자로 구성되어야 합니다.")

        if self._is_duplicated_number(guess_num):
            raise TypeError("중복된 숫자가 존재합니다.")

    def _is_duplicated_number(self, guess_num):
        return len(set(guess_num)) != 3
