temperaturas = (36.5, 37.2, 38.0, 36.8, 39.1)
for temp in temperaturas:
    if temp < 37.5:
        print(f"{temp} -> Normal")
    elif temp <= 38.5:
        print(f"{temp} -> Febre moderada")
    else:
        print(f"{temp} -> Febre alta")