from thermo import *
from thermo.unifac import DOUFSG, DOUFIP2016
# Load constants and properties
constants, properties = ChemicalConstantsPackage.from_IDs(['acetone', '1-butanol'])
# Objects are initialized at a particular condition
T = 333.15
P = 1e5
zs = [.5, .5]

print(constants)


eos_kwargs = dict(Tcs=constants.Tcs, Pcs=constants.Pcs, omegas=constants.omegas) #, kijs=kijs
gas = CEOSGas(PRMIX, HeatCapacityGases=properties.HeatCapacityGases, eos_kwargs=eos_kwargs)
liquid = CEOSLiquid(PRMIX, eos_kwargs, HeatCapacityGases=properties.HeatCapacityGases, T=T, P=P, zs=zs)

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
# Create a T-xy plot at P bar
_ = flasher.plot_Txy(P=P, pts=100)

# Create a P-xy plot at T Kelvin
_ = flasher.plot_Pxy(T=T, pts=100)

# Create a xy diagram at T Kelvin
_ = flasher.plot_xy(T=T, pts=100)
res = flasher.flash(T=360, P=P, zs=[0.2, 0.8])
if res.VF > 0:
  print("Vapour exists")
  print(res.gas.zs)
if res.VF < 1:
  print("Liquid exists")
  print(res.liquid0.zs)