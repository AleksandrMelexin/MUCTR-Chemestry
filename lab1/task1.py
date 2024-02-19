def H(array, T):  # расчёт энтальпии по формуле на слайде 37 лекции 1
    R = 8.3144
    result = 0
    for i in range(5):
        result += (array[i] / (i + 1)) * pow(T, i)
    result += array[5] / T
    return result * R * T


def Cp(array, T):  # расчёт теплоёмкости по формуле на слайде 37 лекции 1
    R = 8.3144
    result = 0
    for i in range(5):
        result += array[i] * pow(T, i)
    return result * R


def main():
    # красные: 1000 - 6000 K
    # синие: 200 - 1000 K
    BLUE_METHANOL = [5.65851051E+00, -1.62983419E-02, 6.91938156E-05, -7.58372926E-08, 2.80427550E-11, -2.56119736E+04, -8.97330508E-01] # Метанол Third Milenium стр. 68 pdf
    BLUE_CO = [0.35795335E+01, -0.61035369E-03, 0.10168143E-05, 0.90700586E-09, -0.90442449E-12, -0.14344086E+05, 0.35084093E+01] # Оксид углерода Third Milenium стр. 71 pdf
    BLUE_H2 = [0.23443029E+01, 0.79804248E-02, -0.19477917E-04, 0.20156967E-07, -0.73760289E-11, -0.91792413E+03, 0.68300218E+00] # Водород Third Milenium стр. 242 pdf
    T = 525
    print("Тепловой эффект реакции синтеза метанола:", round(H(BLUE_METHANOL, T) - (H(BLUE_CO, T) + 2*H(BLUE_H2, T)), 4), "Дж/Моль")  # продукт - реагнеты
    print("Теплоемкость метанола:", round(Cp(BLUE_METHANOL, T), 4), "Дж/(Кг*К)")


if __name__ == "__main__":
    main()
