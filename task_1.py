salary_list = []
name_list = []
productivity_list = []


class PaperMill:
    def __init__(self, name, personal_number, working_hours):
        self.name = name
        self.personal_number = personal_number
        self.working_hours = working_hours
        name_list.append(name)

    def full_salary(self):
        self.hourly_salary = self.working_hours * 100
        salary_list.append(self.hourly_salary)
        print(f'Почасовой оклад - {self.hourly_salary}')

    def productivity(self):
        self.percentage_productivity = 100 / 40 * self.working_hours
        productivity_list.append(self.percentage_productivity)
        print(f'Процент продуктивность - {self.percentage_productivity}%\n')


class Manager(PaperMill):
    def __init__(self, name, personal_number, salary, working_hours):
        super().__init__(name, personal_number, working_hours)
        self.salary = salary
        salary_list.append(salary)
        print(f'Имя - {name}\n'
              f'ЗП - {salary}\n'
              'Количество проработанных часов '
              f'за последнюю неделю - {working_hours}\n'
              f'Персональный номер - {personal_number}')


class Secretary(PaperMill):
    def __init__(self, name, personal_number, salary, working_hours):
        super().__init__(name, personal_number, working_hours)
        self.salary = salary
        salary_list.append(salary)
        print(f'Имя - {name}\n'
              f'ЗП - {salary}\n'
              f'Количество проработанных часов '
              f'за последнюю неделю - {working_hours}\n'
              f'Персональный номер - {personal_number}')


class Seller(PaperMill):
    def __init__(self, name, personal_number, salary, working_hours, sales):
        super().__init__(name, personal_number, working_hours)
        self.salary = salary
        self.sales = sales
        print(f'Имя - {name}\n'
              f'Фиксированная ЗП - {salary}\n'
              f'Кол-во произведенных продаж - {sales}\n'
              f'Персональный номер - {personal_number}\n'
              'Количество проработанных часов '
              f'за последнюю неделю - {working_hours}')

    def full_salary(self):
        self.salary += 50 * self.sales
        salary_list.append(self.salary)
        print(f'Полна ЗП - {self.salary}')


class ShopWorker(PaperMill):
    def __init__(self, name, personal_number, working_hours):
        super().__init__(name, personal_number, working_hours)
        print(f'Имя - {name}\n'
              'Количество проработанных часов '
              f'за последнюю неделю - {working_hours}\n'
              f'Персональный номер - {personal_number}')


class ReplacementSecretary(PaperMill):
    def __init__(self, name, personal_number, working_hours):
        super().__init__(name, personal_number, working_hours)
        print(f'Имя - {name}\n'
              'Количество проработанных часов '
              f'за последнюю неделю - {working_hours}\n'
              f'Персональный номер - {personal_number}')


def func(all_salary):
    total_salary = 0
    for i in all_salary:
        total_salary += i
    return f'Общую сумму оплаты сотрудников - {total_salary}'


manger_1 = Manager('Барсбек Канаткулов', 1, 45000, 18)
manger_1.productivity()
secretary_1 = Secretary('Алымкул Тилекбаев', 2, 20000, 38)
secretary_1.productivity()
seller_1 = Seller('Айпери Шалымбекова', 3, 20000, 38, 20)
seller_1.full_salary()
seller_1.productivity()
shop_worker_1 = ShopWorker('Бакыт Рустамов', 4, 25)
shop_worker_1.full_salary()
shop_worker_1.productivity()
shop_worker_2 = ShopWorker('Алтынай Ширинбаева', 5, 40)
shop_worker_2.full_salary()
shop_worker_2.productivity()
replacement_secretary_1 = ReplacementSecretary('Жанар Рыскулов', 6, 33)
replacement_secretary_1.full_salary()
replacement_secretary_1.productivity()

print(func(salary_list))

productivity_dict = {
    names: numbers for names, numbers in zip(name_list, productivity_list)
    }
max_list = ['Самый продуктивный']
min_list = ['Cамый непродуктивный']
for name, num in productivity_dict.items():
    if num == max(productivity_dict.values()):
        max_list.append(name)
        max_list.append(num)
    if num == min(productivity_dict.values()):
        min_list.append(name)
        min_list.append(num)
print(max_list)
print(min_list)
