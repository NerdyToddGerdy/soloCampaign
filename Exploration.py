from DiceRolls import roll_die, roll_for_omen, roll_for_discovery_type, roll_for_discovery, roll_for_danger_type, \
    roll_for_danger


def set_type() -> str:
    roll = roll_die(6)
    match roll:
        case 1, 2, 3:
            return "nothing"
        case 4:
            return "omen"
        case 5:
            return "discovery"
        case 6:
            return "danger"


class ExplorationStat:
    exploration_string: str


class OmenExplorationStat(ExplorationStat):
    def __init__(self):
        super().__init__()
        self.exploration_string = f"You have come across an omen from a/an {roll_for_omen()}"


class NothingExplorationStat(ExplorationStat):
    def __init__(self):
        super().__init__()
        self.exploration_string = "You did not encounter anything"


class DiscoveryStat(ExplorationStat):
    def __init__(self):
        super().__init__()
        discovery_type = roll_for_discovery_type()
        discovery = roll_for_discovery(discovery_type)
        self.exploration_string = f"You have made a discovery of a/an {discovery_type} {discovery}"


class DangerStat(ExplorationStat):
    danger_type: str
    danger: str

    def __init__(self, terrain: str):
        super().__init__()
        self.danger_type = roll_for_danger_type()
        self.danger = roll_for_danger(danger_type=self.danger_type, terrain=terrain)


def set_exploration_stats(
        exploration_type: str,
        terrain: str
) -> ExplorationStat:
    match exploration_type:
        case "nothing":
            return NothingExplorationStat()
        case "omen":
            return OmenExplorationStat()
        case "discovery":
            return DiscoveryStat()
        case "danger":
            return DangerStat(terrain=terrain)


class Exploration:
    type: str
    exploration_stats: ExplorationStat
    
    def __init__(self, terrain):
        self.type = set_type()
        self.exploration_stats = set_exploration_stats(
            self.type,
            terrain=terrain
        )

    def get_type(self):
        return self.type

    def get_exploration_string(self):
        return self.exploration_stats.exploration_string


if __name__ == '__main__':
    wannabe_explore = Exploration("nothing")
