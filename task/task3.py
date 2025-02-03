class GameEventException(Exception):
    """Custom exception"""

    def __init__(self, event_type: str, details: dict):
        self.event_type = event_type
        self.details = details


def game_event(event_type, details):
    raise GameEventException(event_type, details)


try:
    game_event("death", {"reason": "fall", "place": "tower"})
except GameEventException as e:
    print(f"Event: {e.event_type}")
    print("Details:")
    for key, value in e.details.items():
        print(f"  {key}: {value}")
