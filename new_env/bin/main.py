#!/usr/bin/env python

london_co = {
        "r1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.1"
            },
            "r2": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.2"
            },
            "sw1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "3850",
            "ios": "3.6.XE",
            "ip": "10.255.0.101",
            "vlans": "10,20,30",
            "routing": True
            }
        }

request_name = input("Введите имя устройства: ")
parameters = []

for k in london_co[request_name].keys():
    parameters.append(k)

str_parameters = ", ".join(parameters)

request_parameter = input(f"Введите параметр устройства ({str_parameters}): ")

if request_parameter in parameters:
    print(london_co[request_name][request_parameter])
else:
    print("Такого параметра не существует")
    



