# Вариант 14
from cmath import log, exp
from numpy import real


def H0(a):
    global t
    global R
    return (a[0] + a[1]/2 * t + a[2]/3 * pow(t, 2) + a[3]/4 * pow(t, 3) + a[4]/5 * pow(t,4) + a[5]/t ) *R * t


def G(H, S):
    global t
    return real(H - (t * S))


def S(a):
    global t
    global R
    return real(R * (a[0] * log(t) + a[1] * t + a[2]/2 * pow(t,2) + a[3]/3*pow(t,3) + a[4]/4 * pow(t,4) + a[6]))


def n(p):
    global t
    global R
    return p * R * t

    
def main():
    global t
    global R
    t = 298.15
    R = 8.3144
    SO2 = [3.26653380E+00, 5.32379020E-03, 6.84375520E-07, -5.28100470E-09, 2.55904540E-12, -3.69081480E+04, 9.66465108E+00]    
    SO3 = [2.57803850E+00, 1.45563350E-02, -9.17641730E-06, -7.92030220E-10, 1.97094730E-12, -4.89317530E+04, 1.22651384E+01]
    O2 = [3.78245636E+00, -2.99673415E-03, 9.84730200E-06, -9.68129508E-09, 3.24372836E-12, -1.06394356E+03, 3.65767573E+00]
    
    # задание 1
    # 2SO2+O2=2SO3

    dH = 2*H0(SO3) - (2*H0(SO2) + H0(O2))
    
    # задание 2
    # SO2 + 1/2O2 ⇄ SO3

    p_A = 3 * pow(10, 4)
    p_B = 1 * pow(10, 4)
    p_C = 1.5 * pow(10, 4)
    t = 900

    dS = S(SO3) - (S(SO2) + 0.5*S(O2))
    dH =  H0(SO3) - (H0(SO2) + 0.5*H0(O2))
    dG = G(dH, dS)

    # количество молей вещества помноженное на объем
    n_a = n(p_A)
    n_b = n(p_B)
    n_c = n(p_C)

    #общее количество молей в реакции
    sum_n = n_a + n_b + n_c

    #мольные доли веществ
    x_a = n_a / sum_n
    x_b = n_b / sum_n
    x_c = n_c / sum_n
    
    # Расчёт равновесных концентраций веществ
    Kp = real(exp(-dG/(R * t))) # расчёт константы равновесия
    x = 1.9999 * pow(10, 4) # решаем уравнение относительно x: Kp = (1.5*10^4+x)/((3*10^4-x)*(1*10^4-0.5x)^0.5)
    p1 = p_A - x
    p2 = p_B - 0.5*x
    p3 = p_C + x
    print(x)
    
    # Расчёт равновесной степени вещества А
    A = round((x/p_A)*100, 2)
    
    
    print("Задание 1")
    print(f"Изменение энтальпии для реакции 2SO2 + O2 = 2SO3: {dH}")
    if(dH > 0):
        print("При повышении температуры равновесие будет сдвинуто в сторону продуктов")
    else:
        print("При повышении температуры равновесие будет сдвинуто в сторону реагентов")
    print("Повышение давления сдвигает равновесие системы в сторону продуктов т.к. количество молей газообразных веществ в продуктах меньше чем в реагентах")
    print("Добавление инертного газа сдвигает равновесие в сторону продуктов (т.к. добавление инертного газа влияет обратно повышению давления)")
    print("\nЗадание 2")
    print(f"dG = {dG}")
    print(f"Мольные доли веществ в начале реакции: \nSO2 = {x_a} \nO2 = {x_b} \nSO3 = {x_c}")
    print(f"Константа равновесия = {Kp}")
    print(f"Равновесные концентрации веществ: \nP1 = {p1} \nP2 = {p2} \nP3 = {p3}")
    print(f"Равновесная степень превращения для вещества А (SO2): {A}")
    

if __name__ == "__main__":
    main()
