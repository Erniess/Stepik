# Ближайшее число которое делится на 5 и не меньше введенного
closest_mod_5 = lambda x: x if x % 5 == 0 else x + 5 - x % 5
print(closest_mod_5(12))