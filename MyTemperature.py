# Programa para converter temperaturas...
print("Qual conversão você deseja realizar?")
ESCOLHA = int(input("1. Celsius / 2. Kelvin / 3. Fahrenheit: "))
TEMPERATURA = int(input("Digite o valor da temperatura: "))

match ESCOLHA:
    case 1:
        KELVIN = TEMPERATURA + 273
        FAHRENHEIT = (9 / 5 * TEMPERATURA) - 32
        print(f"A conversão de Celsius para Kelvim será {KELVIN}.")
        print(f"A conversão de Celsius para Fahrenheit será {FAHRENHEIT}.")
    case 2:
        CELSIUS = TEMPERATURA - 273
        FAHRENHEIT = 1.8 * (TEMPERATURA - 273) + 32
        print(f"A conversão de Kelvin para Celsius será {CELSIUS}.")
        print(f"A conversão de Kelvin para Fahrenheit será {FAHRENHEIT}.")
    case 3:
        CELSIUS = 5/9 * (TEMPERATURA - 32)
        KELVIN = (TEMPERATURA - 32) / 1.8 + 273
        print(f"A conversão de Fahrenheit para Celsius será {CELSIUS}.")
        print(f"A conversão de Fahrenheit para Kelvin será {KELVIN}.")