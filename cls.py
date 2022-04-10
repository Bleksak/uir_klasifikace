from dataclasses import dataclass, field


@dataclass(frozen=True)
class Class:
    name: field(init=True, hash=True, compare=True)

    def __str__(self) -> str:
        return self.name
