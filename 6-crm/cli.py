import argparse
from datetime import date

import orders
import storage


def handle_list(args):
    result = orders.list_orders()

    if args.tag:
        result = [o for o in result if args.tag in o["tags"]]

    if args.overdue:
        today = date.today().isoformat()
        result = [
            o for o in result
            if o["due"] is not None
            and o["due"] < today
            and o["status"] not in ("done", "cancelled")
        ]

    if args.limit:
        result = result[: args.limit]

    header = f"{'id':<6}{'title':<20}{'amount':<12}{'status':<14}{'due':<12}"
    print(header)
    print("-" * len(header))
    for o in result:
        due = o["due"] or ""
        print(f"{o['id']:<6}{o['title']:<20}{o['amount']:<12}{o['status']:<14}{due:<12}")


def handle_add(args):
    tags = set(args.tags.split(",")) if args.tags else set()
    order = orders.create_order(
        title=args.title,
        amount=args.amount,
        email=args.email,
        due=args.due,
        tags=tags,
    )
    storage.save(orders.orders)
    print(f"Заказ #{order['id']} создан.")


def handle_remove(args):
    order = orders.remove_order(args.id)
    if order is None:
        print(f"Заказ #{args.id} не найден.")
        return
    storage.save(orders.orders)
    print(f"Заказ #{args.id} удалён.")


def handle_edit(args):
    kwargs = {}
    if args.title is not None:
        kwargs["title"] = args.title
    if args.amount is not None:
        kwargs["amount"] = args.amount
    if args.email is not None:
        kwargs["email"] = args.email
    if args.due is not None:
        kwargs["due"] = args.due

    order = orders.edit_order(args.id, **kwargs)
    if order is None:
        print(f"Заказ #{args.id} не найден.")
        return
    storage.save(orders.orders)
    print(f"Заказ #{args.id} обновлён.")


def handle_tags(args):
    add = set(args.add.split(",")) if args.add else None
    remove = set(args.remove.split(",")) if args.remove else None
    order = orders.update_tags(args.id, add=add, remove=remove)
    if order is None:
        print(f"Заказ #{args.id} не найден.")
        return
    storage.save(orders.orders)
    print(f"Теги заказа #{args.id}: {order['tags']}")


def handle_status(args):
    order = orders.change_status(args.id, args.status)
    if order is None:
        print(f"Заказ #{args.id} не найден.")
        return
    storage.save(orders.orders)
    print(f"Статус заказа #{args.id} → {args.status}")


def main():
    parser = argparse.ArgumentParser(description="CRM CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    # list
    p_list = sub.add_parser("list", help="Список заказов")
    p_list.add_argument("--overdue", action="store_true", help="Только просроченные")
    p_list.add_argument("--tag", help="Фильтр по тегу")
    p_list.add_argument("--limit", type=int, help="Лимит записей")

    # add
    p_add = sub.add_parser("add", help="Добавить заказ")
    p_add.add_argument("--title", required=True)
    p_add.add_argument("--amount", type=float, required=True)
    p_add.add_argument("--email", required=True)
    p_add.add_argument("--due")
    p_add.add_argument("--tags")

    # remove
    p_remove = sub.add_parser("remove", help="Удалить заказ")
    p_remove.add_argument("--id", type=int, required=True)

    # edit
    p_edit = sub.add_parser("edit", help="Редактировать заказ")
    p_edit.add_argument("--id", type=int, required=True)
    p_edit.add_argument("--title")
    p_edit.add_argument("--amount", type=float)
    p_edit.add_argument("--email")
    p_edit.add_argument("--due")

    # tags
    p_tags = sub.add_parser("tags", help="Управление тегами")
    p_tags.add_argument("--id", type=int, required=True)
    p_tags.add_argument("--add")
    p_tags.add_argument("--remove")

    # status
    p_status = sub.add_parser("status", help="Сменить статус")
    p_status.add_argument("--id", type=int, required=True)
    p_status.add_argument("status", choices=["new", "in_progress", "done", "cancelled"])

    args = parser.parse_args()

    data = storage.load()
    orders.init_orders(data)

    handlers = {
        "list": handle_list,
        "add": handle_add,
        "remove": handle_remove,
        "edit": handle_edit,
        "tags": handle_tags,
        "status": handle_status,
    }
    handlers[args.command](args)
