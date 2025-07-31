class Game:
    ...

    def guess(self, guess_num):
        self._assert_illegal_value(guess_num)

    def _assert_illegal_value(self, guess_num):
        if guess_num is None:
            raise TypeError()
        if len(guess_num) != 3:
            raise TypeError()
        for number in guess_num:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
        if self._is_duplicated_number(guess_num):
            raise TypeError()

    def _is_duplicated_number(self, guess_num):
        return guess_num[0] == guess_num[1] or \
            guess_num[0] == guess_num[2] or \
            guess_num[1] == guess_num[2]
