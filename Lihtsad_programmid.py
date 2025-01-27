# from calendar import *
# from datetime import *
# tana = date.today()
# print(f"Tere tana on: {tana}")

# #27/12/2025
# tana1 = tana.strftime("%d/%m/%Y")
# print(f"Tere, tana on {tana1}")

# #jaanuar 27, 2025
# tana1 = tana.strftime("%B %d, %Y")
# print(f"Tere, tana on {tana1}")

# # 12/27/22
# tana1 = tana.strftime("%m/%d/%y")
# print(f"Tere, tana on {tana1}")

# # Dec-27-2022
# tana1 = tana.strftime("%b-%d-%Y")
# print(f"Tere, tana on {tana1}")
# paevadekogus=date(tana.year, 12, 31)
# print(paevadekogus)
# print(f"Jaanuaris on {paevadekogus} paeva")
# paevad=tana.day
# onjaanud=paevadekogus-paevad
# print(f"Jaanuaris on jaanud {onjaanud} paeva")
# aastalopuni=365-monthrange(2025,1)[1]+onjaanud
# print(f"Assta lopuni on jaanud {aastalopuni} paeva")