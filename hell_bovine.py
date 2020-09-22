from dataclasses import dataclass, field

@dataclass
class AttackSpeed:
  speed: str = field(default_factory=lambda _: ['slow', 'medium', 'fast'])

@dataclass
class Weapon:
  damage: int
  attack_speed: AttackSpeed

@dataclass
class Halberd:
  damage: int = 30
  attack_speed = 'slow'

@dataclass
class HellBovine:
  health: int = 100
  weapon: Optional[Weapon] = Halberd
