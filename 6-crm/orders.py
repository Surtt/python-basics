from typing import Literal, TypedDict

Status = Literal["new", "in_progress", "done", "cancelled"]


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: Status
    tags: set[str]
    created_at: str
    due: str | None
    closed_at: str | None


def create_order():
    pass


def list_orders():
    pass


def edit_order():
    pass


def remove_order():
    pass
