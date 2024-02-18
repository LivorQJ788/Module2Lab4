if __name__ == "__main__":
    class Avto:
        """Базовый класс для автомобилей.
        Атрибуты:
            mark (str): Марка автомобиля.
            model (str): Модель автомобиля.
            god_vipuska (int): Год выпуска автомобиля.
        Методы:
            __init__(self, mark: str, model: str, god_vipuska: int) -> None:
                Конструктор класса Автомобиль.
            __str__(self) -> str:
                Возвращает строковое представление автомобиля.
        """

        def __init__(self, mark: str, model: str, god_vipuska: int) -> None:
            self.mark = mark
            self.model = model
            self.god_vipuska = god_vipuska

        def __str__(self) -> str:
            return f"{self.mark} {self.model} ({self.god_vipuska})"


    class light_Avto(Avto):
        """
        Дочерний класс - легковой автомобиль.
        Атрибуты:
            mesta(int): Количество мест в автомобиле.
        Методы:
            __init__(self, mark: str, model: str, god_vipuska: int, mesta: int) -> None:
                Конструктор класса ЛегковойАвтомобиль.
            __str__(self) -> str:
                Возвращает строковое представление легкового автомобиля.
        """

        def __init__(self, mark: str, model: str, god_vipuska: int, mesta: int) -> None:
            super().__init__(mark, model, god_vipuska)
            self.mesta = mesta

        def __str__(self) -> str:
            return f"{super().__str__()} - {self.mesta} мест"


    class heavy_avto(Avto):
        """
        Дочерний класс - грузовой автомобиль.
        Атрибуты:
            gruz (float): Грузоподъемность автомобиля.
        Методы:
            __init__(self, mark: str, model: str, god_vipuska: int, gruz: float) -> None:
                Конструктор класса ГрузовойАвтомобиль.
            __str__(self) -> str:
                Возвращает строковое представление грузового автомобиля.
        """

        def __init__(self, mark:str,model: str, god_vipuska: int, gruz: float) -> None:
            super().__init__(model, model, god_vipuska)
            self.gruz = gruz

        def __str__(self) -> str:
            return f"{super().__str__()} - Грузоподъемность: {self.gruz} тонн"

    # Пример использования классов
    Avto1 = light_Avto("Toyota", "Camry", 2022, 5)
    Avto2 = heavy_avto("Volvo", "FH16", 2023, 50)

    print(Avto1)
    print(Avto2)