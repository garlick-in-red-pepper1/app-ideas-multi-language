langRU: dict = {
    "status": 1,
    "inputer": "Введите число до 8 символов состоящее из 1/0: ",
    'printer': "Ваше число: ",
    "lose": "Чило не соответствует требованиям"
}
langEN: dict = {
    "status": 1,
    "inputer": "Enter a number of up to 8 characters consisting of 1 and 0: ",
    'printer': "Your number: ",
    "lose": "The number does not meet the requirements."
}
loselang: dict = {"status": 0}


def language() -> dict:
    """Choose a language of sistem"""
    lang: str = input('language of sistem(Русский/English): ')
    if lang.lower() == 'русский':
        return langRU
    elif lang.lower() == 'english':
        return langEN
    else:
        return loselang


def checker_of_standart(num: str) -> bool:
    """Verifies the data's compliance with the requirements"""
    return (0 < len(num) < 9) and (num.count("1") + num.count("0") == len(num))


def bin_2_dec() -> str:
    """receives a value in binary format and returns it in decimal format"""
    lang_tab: dict = language()
    if lang_tab["status"] == 0:
        return "This language not using in this sistem"
    bin_num: str = input(lang_tab["inputer"])

    if checker_of_standart(bin_num):
        num: int = int(bin_num, 2)
        return f"{lang_tab['printer']}{num}"

    else:
        return f"{lang_tab['lose']}"
