# http://vle-calc.com/phase_diagram.html
from thermo import ChemicalConstantsPackage, CEOSGas, CEOSLiquid, PRMIX, FlashVL, FlashVLN, FlashPureVLS
from thermo.interaction_parameters import IPDB


def calc(P, T, z):
    constants, properties = ChemicalConstantsPackage.from_IDs(['acetone', '1-butanol']) # данные вещества
    zs = [z, 1-z] # мольные доли
    k12 = 0.03
    kijs = [[0, k12],
            [k12, 0]]
    eos_kwargs = dict(Tcs=constants.Tcs, Pcs=constants.Pcs, omegas=constants.omegas, kijs=kijs)
    gas = CEOSGas(PRMIX, eos_kwargs, HeatCapacityGases=properties.HeatCapacityGases, T=T, P=P, zs=zs)
    liquid = CEOSLiquid(PRMIX, eos_kwargs, HeatCapacityGases=properties.HeatCapacityGases, T=T, P=P, zs=zs)
    liquid2 = CEOSLiquid(PRMIX, eos_kwargs, HeatCapacityGases=properties.HeatCapacityGases, T=T, P=P, zs=zs)
    flasher = FlashVLN(constants, properties, liquids=[liquid, liquid2], gas=gas)
    res = flasher.flash(T=T, P=P, zs=zs)
    ans = [[0.0, 0.0], [0.0, 0.0]]
    if res.VF > 0:
        ans[1] = res.gas.zs
    if res.VF == 1:  
        pass
    else:
        ans[0] = res.liquid0.zs
    return ans


T_e = [116.027, 106.992, 100.954, 89.1905, 67.0128]
P_e = [1.0, 1.0, 1.0, 1.0, 1.0]
x1_e = [0.008, 0.06, 0.1, 0.2, 0.6]
y1_e = [0.0585364, 0.356559, 0.510315, 0.728513, 0.943063]
zs = [0.0255, 0.17, 0.3, 0.45, 0.72]
x2_e = [1-num for num in x1_e]
y2_e = [1-num for num in y1_e]
x1_r = []
x2_r = []
y1_r = []
y2_r = []
T_e = [round(num+273.15, 2) for num in T_e] # перевод цельсий - кельвин
P_e = [round(num*1e5, 2) for num in P_e] # перевод bar - Pa
error_x1 = 0
error_y1 = 0
error_x2 = 0
error_y2 = 0
for i in range(len(P_e)):
    r_info = calc(P_e[i], T_e[i], zs[i])
    x1_r.append(r_info[0][0])
    y1_r.append(r_info[1][0])
    x2_r.append(r_info[0][1])
    y2_r.append(r_info[1][1])
    error_x1 += (abs(x1_e[i]-x1_r[i])/x1_e[i])*100
    error_y1 += (abs(y1_e[i]-y1_r[i])/y1_e[i])*100
    error_x2 += (abs(x2_e[i]-x2_r[i])/x2_e[i])*100
    error_y2 += (abs(y2_e[i]-y2_r[i])/y2_e[i])*100
# print(*T_e)
# print(*P_e)
# print(*x1_r)
# print(*x2_r)
# print(*y1_r)
# print(*y2_r)

# вывод средней отсночительной ошибки в процентах
print("average error for x1:", round(error_x1/5.0, 2))
print("average error for y1:", round(error_y1/5.0, 2))
print("average error for x2:", round(error_x2/5.0, 2))
print("average error for y2:", round(error_y2/5.0, 2))