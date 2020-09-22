@dataclass
class Weapon:
  damage: int = 1

class HellBovine:
  health: int = 100
  weapon: Optional[Weapon] = None
