sec = 12345
min = sec // 60
hours = min // 60

print("%02d:%02d:%02d" % (hours, min % 60, sec % 60))