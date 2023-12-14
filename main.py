import pogyasz1

print("III/A,B:")
csomag_lista=pogyasz1.faljbeolvasas()
print(f"\tA pogyászok száma: {len(csomag_lista)}")

print("III/C:")
atlag=pogyasz1.pogyasz_atlagsuly(csomag_lista)
print(f"\tAz 51 cm-es pogyászok átlag súlyértéke: {round(atlag)} g")
print("III/D:")
max_index=pogyasz1.legmagasabb(csomag_lista)
print(f"\tA legmagasabb pogyasz méretei: {csomag_lista[max_index]}")


