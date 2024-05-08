from enum import StrEnum


class OrderStatus(StrEnum):

    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
