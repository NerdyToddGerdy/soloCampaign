import game


class TestCharacterCreation:
    def test_name(self):
        assert game.hello_world(name="Todd") == "Hello Todd"


    # def test_character_creation(self):
    #     Character(Todd)