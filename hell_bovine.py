@dataclass
class Weapon:
  damage: int

class Halberd:
  damage: int = 30

class HellBovine:
  health: int = 100
  weapon: Optional[Weapon] = Halberd
