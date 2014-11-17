import EF

f = EF.query("SELECT * FROM COUNTRY")
print(f[5].__dict__)
f[5].read()
f[5].update({'id' : 1000, 'name' : 'vasa'})
f[5].read()
