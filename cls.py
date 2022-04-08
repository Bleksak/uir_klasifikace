from dataclasses import dataclass, field


@dataclass
class Row:
    name: str
    count: int