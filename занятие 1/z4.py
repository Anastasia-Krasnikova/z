# -- coding: utf-8 —
secounds = 1000008
days = secounds // 86400
hours = (secounds % 86400) // 3600
minutes = (secounds % 3600) // 60
seconds = secounds % 60
print( "дни:", days, ";", "часы:", hours,";", "минуты:", minutes,";", "секунды:", seconds)
print("   ")
