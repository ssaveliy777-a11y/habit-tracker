from habits_logic import get_all_habits, add_habit, delete_habit, toggle_habit

def print_menu():
    print("\n--- Трекер Привычек ---")
    print("1. Показать все привычки")
    print("2. Добавить привычку")
    print("3. Отметить как выполненную")
    print("4. Удалить привычку")
    print("5. Выход")
    print("-----------------------")

def get_int_input(prompt):
    """Валидация ввода: просит число, пока не получит корректное."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("❌ Ошибка: введите целое число.")

def display_habits():
    """Красивый вывод списка привычек."""
    habits = get_all_habits()
    
    if not habits:
        print("\n📭 Список привычек пуст.")
        return

    print("\n📝 Ваши привычки:")
    print(f"{'№':<3} {'Статус':<8} {'Название'}")
    print("-" * 40)
    
    for i, habit in enumerate(habits):
        status = "✅" if habit["completed"] else "⬜"
        print(f"{i:<3} {status:<8} {habit['name']}")

def handle_add():
    name = input("Введите название привычки: ").strip()
    from habits_logic import add_habit, get_all_habits
    current_habits = get_all_habits()
    
    if add_habit(name, current_habits):
        print("✅ Привычка успешно добавлена!")
    else:
        print("⚠️ Такая привычка уже существует или имя пустое.")

def handle_toggle():
    display_habits()
    if not get_all_habits():
        return
    
    idx = get_int_input("Введите номер привычки для переключения статуса: ")
    from habits_logic import toggle_habit
    
    if toggle_habit(idx, get_all_habits()):
        print("✅ Статус изменен!")
    else:
        print("⚠️ Неверный номер привычки.")

def handle_delete():
    display_habits()
    if not get_all_habits():
        return
        
    idx = get_int_input("Введите номер привычки для удаления: ")
    from habits_logic import delete_habit
    
    if delete_habit(idx, get_all_habits()):
        print("🗑️ Привычка удалена.")
    else:
        print("⚠️ Неверный номер привычки.")