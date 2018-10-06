def measure_temperature():
    temperature = 22
    print("当前的室温是:%d"%temperature)
    return temperature

def measure_temperature_fahrenheit(temperature):
    print("-4---")#测bug
    temperature = temperature + 3
    print("-5---")
    print("当前的温度（华氏度）是：%d"%temperature)
    print("-6---")

print("-1---")
result = measure_temperature()
print("-2---")
measure_temperature_fahrenheit(result)
print("-3---")
