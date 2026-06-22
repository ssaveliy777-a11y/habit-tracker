import json
import os

DATA_FILE = "data.json"

def load_habits():
    """Загружает привычки из файла. Если файла нет — создает пустой список."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_habits(habits):
    """Сохраняет список привычек в файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(habits, f, ensure_ascii=False, indent=4)

def add_habit(name, habits):
    """Добавляет привычку. Возвращает True, если успешно, False если уже есть."""
    name = name.strip()
    if not name:
        return False
    if any(h['name'] == name for h in habits):
        return False
    
    habits.append({"name": name, "completed": False})
    save_habits(habits)
    return True
def delete_habit(index, habits):
    """Удаляет привычку по индексу (0-based). Возвращает True если успешно."""
    if 0 <= index < len(habits):
        removed = habits.pop(index)
        save_habits(habits)
        return True
    return False

def toggle_habit(index, habits):
    """Переключает статус выполнения привычки (сделано/не сделано)."""
    if 0 <= index < len(habits):
        habits[index]["completed"] = not habits[index]["completed"]
        save_habits(habits)
        return True
    return False

def get_all_habits():
    """Просто возвращает текущий список привычек."""
    return load_habits()
