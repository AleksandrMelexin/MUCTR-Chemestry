import math


def main():
    T = 298
    P = 101325
    Va = 4 * pow(10, -4)  # азот N2
    Vb = 7 * pow(10, -4)  # вода H2O
    R = 8.31
    na = (P * Va) / (R * T)
    nb = (P * Vb) / (R * T)
    answer = na * R * math.log((Va + Vb) / Va) + nb * R * math.log((Va + Vb) / Vb)
    print("изменение энтропии: ", round(answer, 4))


if __name__ == "__main__":
    main()
