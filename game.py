from game_result import GameResult


class Game:
    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError("읽을 수 없는 속성")

    @question.setter
    def question(self, value: str):
        self._question = value

    def guess(self, guess_num: str) -> GameResult | None:
        self._assert_illegal_value(guess_num)
        if guess_num == self._question:
            return GameResult(True, 3, 0)
        strike_cnt = self._get_strike(guess_num)
        ball_cnt = self._get_ball(guess_num, strike_cnt)
        return GameResult(False, strike_cnt, ball_cnt)

    def _get_strike(self, guess_num: str) -> int:
        strike_cnt = 0
        for num, answer in zip(guess_num, self._question):
            if num == answer:
                strike_cnt += 1

        return strike_cnt

    def _get_ball(self, guess_num: str, strike_cnt: int) -> int:
        ball_cnt = 0
        for num in guess_num:
            if num in self._question:
                ball_cnt += 1
        ball_cnt -= strike_cnt

        return ball_cnt

    def _assert_illegal_value(self, guess_num: str):
        if guess_num is None:
            raise TypeError("입력이 None 입니다.")

        if not isinstance(guess_num, str) or len(guess_num) != 3:
            raise TypeError("입력은 3 자리 문자열이어야 합니다.")

        if not guess_num.isdigit():
            raise TypeError("모든 문자는 숫자로 구성되어야 합니다.")

        if self._is_duplicated_number(guess_num):
            raise TypeError("중복된 숫자가 존재합니다.")

    def _is_duplicated_number(self, guess_num: str) -> bool:
        return len(set(guess_num)) != 3
