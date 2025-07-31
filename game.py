class Game:
    ...

    def guess(self, guess_num):
        if guess_num is None:
            raise TypeError()