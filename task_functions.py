def describe_pet(pet_type, *name, **info):
    result ={
        "tepe": pet_type,
        "names": list(name),
        "details": info 
    }
    return result
print(describe_pet("собака", "Бобик", age=3, color="коричневый"))