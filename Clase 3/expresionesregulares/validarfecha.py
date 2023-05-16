import re
# DD/MM/AAAA
fecha = "30/12/2020"
test = re.match('^\d{2}/\d{2}/\d{4}$',fecha)
if (test):
    print("Ok")
else:
    print("NO Ok")