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


def init_orders(data: list[Order]) -> None:
    global _next_id
    orders.clear()
    orders.extend(data)
    if orders:
        _next_id = max(o["id"] for o in orders) + 1
    else:
        _next_id = 1


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


def update_tags(order_id: int, add: set[str] | None = None, remove: set[str] | None = None) -> Order | None:
    for order in orders:
        if order["id"] == order_id:
            if add:
                order["tags"] |= add
            if remove:
                order["tags"] -= remove
            return order
    return None


def change_status(order_id: int, status: Status) -> Order | None:
    for order in orders:
        if order["id"] == order_id:
            order["status"] = status
            if status in ("done", "cancelled"):
                order["closed_at"] = datetime.now().isoformat()
            return order
    return None
