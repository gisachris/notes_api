from typing import Dict, Any

notes_db: Dict[int, Dict[str, any]] = {}

_counter: int = 0

def next_id() -> int:
    global _counter
    _counter += 1
    return _counter

