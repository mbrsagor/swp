from enum import IntEnum


class ROLE(IntEnum):
    ADMIN = 0
    MENTOR = 1
    STUDENT = 2

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]
