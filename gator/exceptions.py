"""Provide Exception and Error classes for use by GatorGrader."""


class InvalidCheckArgumentsError(ValueError):
    """The check arguments are invalid."""

    def __init__(self, arguments, usage, message, check_name=None):
        """Initialize the InvalidCheckArgumentsError."""
        self.arguments = arguments
        self.usage = usage
        self.message = message
        self.check_name = check_name


class InvalidSystemArgumentsError(ValueError):
    """The system arguments are invalid."""

    def __init__(self, arguments):
        """Initialize the InvalidSystemArgumentsError."""
        self.arguments = arguments


class InvalidCheckError(InvalidSystemArgumentsError):
    """The check is invalid."""

    def __init__(self, arguments, check_name) -> None:
        """Initialize the InvalidCheckError."""
        super().__init__(arguments)
        self.check_name = check_name
