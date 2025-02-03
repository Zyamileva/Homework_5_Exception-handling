class InsufficientResourcesException(Exception):
    """Custom Exception raised when"""

    def __init__(
        self, required_resource: str, required_amount: int, current_amount: int
    ):
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount


def check_possibility_action(required_resource, required_amount, current_amount):
    if current_amount < required_amount:
        raise InsufficientResourcesException(
            required_resource, required_amount, current_amount
        )


try:
    check_possibility_action("gold", 1000, 500)
except InsufficientResourcesException as e:
    print(
        f"Insufficient resources: {e.required_resource} required: {e.required_amount}, available: {e.current_amount}"
    )
