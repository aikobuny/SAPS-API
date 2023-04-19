class UserDoesNotExist(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return """User does not exist on the database."""


class ExamYearDoesNotExist(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return """Exam year does not exist on the database."""


class SchoolCodeDoesNotExist(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return """Exam year does not exist on the database."""


class ExamResultsDoesNotExist(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return """Exam year does not exist on the database."""
