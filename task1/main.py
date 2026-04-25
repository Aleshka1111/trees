from company import Company


company = Company()
company.build_from_json("data.json")

print("Компания в начале")
company.print_all_positions()

print("\n Добавление позиции с челиком")
company.add_position("Математика", "Курсы", "Лешка", "Промыслов")
company.print_all_positions()

print("\n Добавление позиции без челика")
company.add_position("ООП", "Информатика")
company.print_all_positions()

print("\n Увольнение:")
company.remove_employee("Дмитрий", "Шахов")
company.print_all_positions()

print("\n Назначение сотрудника:")
company.assign_employee_to_free_position("Робототехника", "Дмитрий", "Шахов")
company.print_all_positions()

print("\nПеренос направления")
company.move_position("Информатика", "Лагеря")
company.print_all_positions()

print("\n Закрытие направления")
company.close_position("Лагеря")
company.print_all_positions()