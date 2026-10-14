def calc(name, *args):
    total = sum(args)
    return f"Привет, {name}! Сумма: {total}"

print(calc("Аня", 1, 2, 3))     