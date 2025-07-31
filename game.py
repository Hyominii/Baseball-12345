class Game:
    ...

    def guess(self, guess_num):
        if guess_num is None:
            raise TypeError()

        if len(guess_num) != 3:
            raise TypeError()

        for number in guess_num:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()

        if guess_num[0] == guess_num[1] or \
            guess_num[0] == guess_num[2] or \
            guess_num[1] == guess_num[2]:
            raise TypeError()
