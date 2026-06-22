from ui_handler import print_menu, get_int_input, handle_add, handle_toggle, handle_delete, display_habits

def main():
    while True:
        print_menu()
        choice = get_int_input("Выберите действие (1-5): ")
        
        if choice == 1:
            display_habits()
        elif choice == 2:
            handle_add()
        elif choice == 3:
            handle_toggle()
        elif choice == 4:
            handle_delete()
        elif choice == 5:
            print("👋 До свидания!")
            break
        else:
            print("⚠️ Такого пункта меню не существует.")

if __name__ == "__main__":
    main()