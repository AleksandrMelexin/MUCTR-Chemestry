flasher = FlashVL(constants, properties, liquid=liquid, gas=gas)
res = flasher.flash(T=360, P=P, zs=[0.2, 0.8])
if res.VF > 0:*
  print("Vapour exists")
  print(res.gas.zs)
if res.VF < 1:
  print("Liquid exists")
  print(res.liquid0.zs)