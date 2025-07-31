class Game:
    ...

    def guess(self, guess_num):
        if guess_num is None:
            raise TypeError()

        if len(guess_num) != 3:
            raise TypeError()