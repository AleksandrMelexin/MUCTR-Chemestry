# расчёт энтропии вариант 14
import math


def S(array, T):
    R = 8.31
    result = array[0] * math.log(T)
    for i in range(1, 5):
        result += (array[i]/i)*math.pow(T, i)
    result += array[6]
    return result * R
        
    
def main():
    T = 250
    BLUE_C3H4 = [0.26130445E+01, 0.12122575E-01, 0.18539880E-04, 0.12791347E-07, -0.10482247E-10, 0.21541567E+05, 0.10226139E+02] # Third Milenium стр. 68 pdf
    print("Энтропия вещества C3H4 равна:", round(S(BLUE_C3H4, T), 4), "Дж/К")


if __name__ == "__main__":
    main()
