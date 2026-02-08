import json
from pathlib import Path

STORAGE_FILE = Path(__file__).parent / "orders.json"


def load() -> list[dict]:
    if not STORAGE_FILE.exists():
        return []

    try:
        data = json.loads(STORAGE_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, ValueError):
        print(f"Файл {STORAGE_FILE.name} повреждён, начинаем с пустого списка.")
        return []

    for item in data:
        if "tags" in item:
            item["tags"] = set(item["tags"])

    return data


def save(items: list[dict]) -> None:
    data = []
    for item in items:
        copy = dict(item)
        if "tags" in copy:
            copy["tags"] = list(copy["tags"])
        data.append(copy)

    STORAGE_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
