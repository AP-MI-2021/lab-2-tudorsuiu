def is_antipalindrome(n):
    '''
    Determina daca un numar n este antipalindrom
    :param n: nr. intreg
    :return: True daca n este antipalindrom si False in caz contrar
    '''

    n = abs(n)
    antipalindrom = True
    cn = n
    nr_cifre = 0

    # Determinam cate cifre are numarul citit
    while cn != 0:
        nr_cifre += 1
        cn = cn // 10
    # Determinam daca numarul citit este antipalindrom
    while n > 9:
        if n // (10 ** (nr_cifre - 1)) == n % 10:
            antipalindrom = False
        n = n % (10 ** (nr_cifre - 1))
        n = n // 10
        nr_cifre -= 2

    return antipalindrom

def test_is_antipalindrome():
    assert is_antipalindrome(-1) == True
    assert is_antipalindrome(0) == True
    assert is_antipalindrome(5) == True
    assert is_antipalindrome(11) == False
    assert is_antipalindrome(21) == True
    assert is_antipalindrome(353) == False
    assert is_antipalindrome(335) == True
    assert is_antipalindrome(2773) == False
    assert is_antipalindrome(2783) == True
    assert is_antipalindrome(27733) == True
    assert is_antipalindrome(27373) == False

def get_base_2(n: str):
    '''
    Transforma un numar dat din baza 10 in baza 2
    :param n: sir de caractere
    :return: numarul n transformat in baza 2
    '''

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

def main():

    shouldRun = True

    while shouldRun:
        print("1.Determina daca un numar este antipalindrom")
        print("2.Transforma un numar dat din baza 10 in baza 2")
        print("x.Iesire")
        optiune = input("Selectati optiunea: ")
        if optiune == "1":
            n = int(input("Dati numarul: "))
            print(is_antipalindrome(n))
        elif optiune == "2":
            n = int(input("Dati numarul: "))
            print(get_base_2(str(n)))
        elif optiune == "x":
            shouldRun = False
        else:
            print("Optiune gresita! Reincercati!")

test_is_antipalindrome()
test_get_base_2()
main()