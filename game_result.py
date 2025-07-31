from dataclasses import dataclass

@dataclass
class GameResult:
    _solved: bool
    _strikes: int
    _balls: int

    @property
    def solved(self):
        return self._solved

    @property
    def strikes(self):
        return self._strikes

    @property
    def balls(self):
        return self._balls
