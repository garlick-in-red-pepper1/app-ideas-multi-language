def checker_of_standart(num: str) -> bool:
    """проверяет соответствует ли код требованиям"""
    return 0 < len(num) < 9


def bin_2_dec() -> str:
    """получает значение в двоичном формате и возвращает в десятичном"""
    bin_num: str = input("Введите число до 8 символов состоящее из 1/0: ")

    if checker_of_standart(bin_num):
        num: int = int(bin_num, 2)
        return f"Ваше число:{num}"

    else:
        return "Чило не соответствует требованиям"
