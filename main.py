def is_antipalindrome(n: int) -> bool:
    """
    Determina daca un numar n este antipalindrom
    :param n: nr. intreg
    :return: True daca n este antipalindrom si False in caz contrar
    """
    n = abs(n)
    cn = n
    nr_cifre = 0
    # Determinam cate cifre are numarul citit
    while cn != 0:
        nr_cifre += 1
        cn = cn // 10
    # Determinam daca numarul citit este antipalindrom
    while n > 9:
        if n // (10 ** (nr_cifre - 1)) == n % 10:
            return False
        n = n % (10 ** (nr_cifre - 1))
        n = n // 10
        nr_cifre -= 2
    return True


def test_is_antipalindrome():
    assert is_antipalindrome(-1) is True
    assert is_antipalindrome(0) is True
    assert is_antipalindrome(2773) is False
    assert is_antipalindrome(2783) is True


def get_base_2(n: str) -> str:
    """
    Transforma un numar dat din baza 10 in baza 2
    :param n: sir de caractere
    :return: numarul n transformat in baza 2
    """
    n_base_2 = ""
    if int(n) == 0:
        return "0"
    elif int(n) < 0:
        return "Numar invalid!"
    else:
        while n != "0":
            n_base_2 = str(int(n) % 2) + n_base_2
            n = str(int(n) // 2)
        return n_base_2


def test_get_base_2():
    assert get_base_2("-1") == "Numar invalid!"
    assert get_base_2("0") == "0"
    assert get_base_2("1") == "1"
    assert get_base_2("2") == "10"
    assert get_base_2("3") == "11"
    assert get_base_2("4") == "100"


def get_temp(temp: float, from_scale: str, to_scale: str) -> float:
    """
    Transforma o temperatura dintr-o scara data intr-o alta scara data
    :param temp: nr. real
    :param from_scale: string de o litera
    :param to_scale: string de o litera
    :return: temperatura transformata din scara data intr-o alta scara data
    """
    transformation = 0
    from_celsius_to_fahrenheit = 32
    from_celsius_to_kelvin = 273.15
    if from_scale == "C" and to_scale == "K":
        transformation = temp + from_celsius_to_kelvin
    elif from_scale == "C" and to_scale == "F":
        transformation = temp * 1.8 + from_celsius_to_fahrenheit
    elif from_scale == "K" and to_scale == "C":
        transformation = temp - from_celsius_to_kelvin
    elif from_scale == "K" and to_scale == "F":
        transformation_in_celsius = temp - from_celsius_to_kelvin
        transformation = transformation_in_celsius * 1.8 + from_celsius_to_fahrenheit
    elif from_scale == "F" and to_scale == "C":
        transformation = (temp - from_celsius_to_fahrenheit) / 1.8
    elif from_scale == "F" and to_scale == "K":
        transformation_in_celsius = (temp - from_celsius_to_fahrenheit) / 1.8
        transformation = transformation_in_celsius + from_celsius_to_kelvin
    transformation = round(transformation, 2)
    return transformation


def test_get_temp():
    assert get_temp(20, "C", "K") == 293.15
    assert get_temp(20, "C", "F") == 68.0
    assert get_temp(20, "K", "C") == -253.15
    assert get_temp(20, "K", "F") == -423.67
    assert get_temp(20, "F", "C") == -6.67
    assert get_temp(20, "F", "K") == 266.48


def main():
    should_run = True
    while should_run:
        print("1.Determina daca un numar este antipalindrom")
        print("2.Transforma un numar dat din baza 10 in baza 2")
        print("3.Transforma o temperatura data intr-o scara data")
        print("4.Iesire")
        optiune = input("Selectati optiunea: ")
        if optiune == "1":
            n = int(input("Dati numarul: "))
            print(is_antipalindrome(n))
        elif optiune == "2":
            n = int(input("Dati numarul: "))
            print(get_base_2(str(n)))
        elif optiune == "3":
            temp = float(input("Dati temperatura: "))
            from_scale = input("Transforma din: ")
            to_scale = input("Transforma in: ")
            print(get_temp(temp, from_scale, to_scale))
        elif optiune == "4":
            should_run = False
        else:
            print("Optiune gresita! Reincercati!")


if __name__ == '__main__':
    test_is_antipalindrome()
    test_get_base_2()
    test_get_temp()
    main()
