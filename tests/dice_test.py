from DiceRolls import roll_die


class TestRandomSixSidedDieRolls:
    value: int = roll_die(6)

    def test_greater_than_zero(self):
        assert self.value > 0

    def test_less_than_7(self):
        assert self.value < 7
