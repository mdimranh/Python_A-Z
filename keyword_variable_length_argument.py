def person(name, **data):
    
    print(name)

    for i, j in data.items():
        print(i, j)


person("Imran", age = 21, city ='Gazipur', phone = +8801942504420)