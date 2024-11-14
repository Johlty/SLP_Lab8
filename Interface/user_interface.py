def get_chart_type():
    """Функція для вибору типу графіка користувачем"""
    print("Оберіть тип візуалізуції діаграми\n1.line\n2.bar\n3.scatter\n4.hist\n5.pie")
    choice = input("Ваш вибір: ")
    chart_types = {"1": "line", "2": "bar", "3": "scatter", "4": "hist", "5": "pie"}
    return chart_types.get(choice, None)

def ask_save_choice():
    """Функція для запиту у користувача про збереження графіка"""
    save_choice = input("Бажаєте зберегти графіки у PNG форматі? (так/ні): ").strip().lower()
    return save_choice == "так"
