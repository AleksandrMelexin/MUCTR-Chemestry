from thermo import ChemicalConstantsPackage, CEOSGas, CEOSLiquid, PRMIX, FlashVL, FlashVLN, FlashPureVLS
from thermo.interaction_parameters import IPDB


constants, properties = ChemicalConstantsPackage.from_IDs(['acetone', '1-butanol']) # данные вещества
T = 333.15 # температура
P = 1e5 # давление
zs = [.5, .5] # мольные доли
k12 = 0.03 # коэффициент из excel
kijs = [[0, k12], [k12, 0]]

eos_kwargs = dict(Tcs=constants.Tcs, Pcs=constants.Pcs, omegas=constants.omegas, kijs=kijs)
gas = CEOSGas(PRMIX, eos_kwargs, HeatCapacityGases=properties.HeatCapacityGases, T=T, P=P, zs=zs)
liquid = CEOSLiquid(PRMIX, eos_kwargs, HeatCapacityGases=properties.HeatCapacityGases, T=T, P=P, zs=zs)
flasher = FlashVL(constants, properties, liquid=liquid, gas=gas)

_ = flasher.plot_Txy(P=P, pts=100) # создание Tx-y диаграммы
_ = flasher.plot_Pxy(T=T, pts=100) # создание Px-y диаграммы
_ = flasher.plot_xy(T=T, pts=100) # создание x-y диаграммы

liquid2 = CEOSLiquid(PRMIX, eos_kwargs, HeatCapacityGases=properties.HeatCapacityGases, T=T, P=P, zs=zs)
flasher2 = FlashVLN(constants, properties, liquids=[liquid, liquid2], gas=gas)
res = flasher2.flash(T=T, P=P, zs=zs)
print('There are %s phases present at %f K and %f bar' %(res.phase_count,T,P/1e5))
if res.VF > 0:
	print(res.gas.zs)
if res.VF == 1:  
	print("Only vapour")
else:
	print("Liquid0: ")
	print(res.liquid0.zs)
	if res.liquid_count>1:
		print("LIQUID PHASE SEPARATION")
		print("Liquid1: ")
		print(res.liquid1.zs)