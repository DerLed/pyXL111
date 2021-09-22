class Certificate:
    def __init__(self, thickness):
        self.metal_grade = None  # Марка металла
        self.gost = None  # Гост материала
        self.melting_number = None  # Номер плавки
        self.batch_number = None  # Номер партии
        self.certificate_number = None  # Номер сертификата
        self.date_of_certificate = None  # Дата сертификата
        self.limit_fluidity = None  # Предел текучести
        self.temporary_resistance = None  # Временное сопротивление
        self.relative_extension = None  # Относительное удлинение
        self.relative_narrowing = None  # Относительное сужение
        self.impact_strength_before_aging = None  # Ударная вязкость до старения
        self.impact_strength_after_aging = None  # Ударная вязкость после старения
        self.sample_type = None  # Тип образца
        self.impact_strength_below_zero = None  # Ударная вязкость ниже ноля
        self.temperature_below_zero = None  # Температура ниже ноля
        self.sample_type_below_zero = None  # Тип образка ниже ноля
        self.thickness = thickness
        self.additional_data = None  # Доболнительные данные
        self.chemical_composition = []  # Хим.состав


if __name__ == '__main__':
    bob = Certificate(10)
    print(bob.thickness)
