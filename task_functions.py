def calc(name, *args):
    return f"Привет, {name}! Сумма: {sum(args)}"

print(calc("Аня", 1, 2, 3))