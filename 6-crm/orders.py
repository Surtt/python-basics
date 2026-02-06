from datetime import datetime
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


orders: list[Order] = []
_next_id: int = 1


def create_order(
    title: str,
    amount: float,
    email: str,
    status: Status = "new",
    tags: set[str] | None = None,
    due: str | None = None,
) -> Order:
    global _next_id
    order: Order = {
        "id": _next_id,
        "title": title,
        "amount": amount,
        "email": email,
        "status": status,
        "tags": tags if tags is not None else set(),
        "created_at": datetime.now().isoformat(),
        "due": due,
        "closed_at": None,
    }
    orders.append(order)
    _next_id += 1
    return order


def list_orders() -> list[Order]:
    return orders


def edit_order(order_id: int, **kwargs) -> Order | None:
    for order in orders:
        if order["id"] == order_id:
            for key, value in kwargs.items():
                if key in order:
                    order[key] = value  # type: ignore[literal-required]
            return order
    return None


def remove_order(order_id: int) -> Order | None:
    for i, order in enumerate(orders):
        if order["id"] == order_id:
            return orders.pop(i)
    return None
