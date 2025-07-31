class Game:
    ...

    def guess(self, guess_num):
        self._assert_illegal_value(guess_num)

    def _assert_illegal_value(self, guess_num):
        if guess_num is None:
            raise TypeError("입력이 None 입니다.")

        if len(guess_num) != 3:
            raise TypeError("입력은 3 자리 문자열이어야 합니다.")

        for number in guess_num:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError("모든 문자는 숫자로 구성되어야 합니다.")

        if self._is_duplicated_number(guess_num):
            raise TypeError("중복된 숫자가 존재합니다.")

    def _is_duplicated_number(self, guess_num):
        return guess_num[0] == guess_num[1] or \
            guess_num[0] == guess_num[2] or \
            guess_num[1] == guess_num[2]
