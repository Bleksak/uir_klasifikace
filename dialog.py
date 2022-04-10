from dataclasses import dataclass
from cls import Class


@dataclass(frozen=True)
class Dialog:
    text: str
    cls: Class