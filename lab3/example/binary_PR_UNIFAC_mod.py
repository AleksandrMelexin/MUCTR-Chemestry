from thermo import *
from thermo.unifac import DOUFSG, DOUFIP2016
# Load constants and properties
constants, properties = ChemicalConstantsPackage.from_IDs(['acetone', 'water'])
# Objects are initialized at a particular condition
T = 333.15
P = 1e5
zs = [.5, .5]

print(constants)

# Use Peng-Robinson for the vapor phase
#k12 = -0.4
#kijs = [[0, k12],
#        [k12, 0]]
#print(k12)
eos_kwargs = dict(Tcs=constants.Tcs, Pcs=constants.Pcs, omegas=constants.omegas) #, kijs=kijs
gas = CEOSGas(PRMIX, HeatCapacityGases=properties.HeatCapacityGases, eos_kwargs=eos_kwargs)

# Configure the activity model
GE = UNIFAC.from_subgroups(chemgroups=constants.UNIFAC_Dortmund_groups, version=1, T=T, xs=zs,
						   interaction_data=DOUFIP2016, subgroups=DOUFSG)
# Configure the liquid model with activity coefficients
liquid = GibbsExcessLiquid(
	VaporPressures=properties.VaporPressures,
	HeatCapacityGases=properties.HeatCapacityGases,
	VolumeLiquids=properties.VolumeLiquids,
	GibbsExcessModel=GE,
	equilibrium_basis='Psat', caloric_basis='Psat',
	T=T, P=P, zs=zs)

flasher = FlashVL(constants, properties, liquid=liquid, gas=gas)
res = flasher.flash(T=360, P=P, zs=[0.2, 0.8])
if res.VF > 0:
  print("Vapour exists")
  print(res.gas.zs)
if res.VF < 1:
  print("Liquid exists")
  print(res.liquid0.zs)