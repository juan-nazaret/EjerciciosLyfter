"""
Ejercicio 1

"""

print("\nEJERCICIO 1\n")

sales = [
    {
        "date": "07/02/26",
        "customer_email":"email@gmail.com",
        "items":[
            {
                "name": ":x-box",
                "upc": "ITEM-453",
                "unit_price": 65.76,
            },
            {
                "name": "play-station",
                "upc": "ITEM-324",
                "unit_price": 32.45,
            },
            {
                "name": "switch",
                "upc": "ITEM-432",
                "unit_price": 12.54,
            },
        ]
    },
    {
        "date" : "27/02/26",
        "customer_email" : "dos_email@gmail.com",
        "items" :[
            {   
                "name": "x-box",
                "upc": "ITEM-453",
                "unit_price": 65.76
            },
            {
                "name":"x-box series x",
                "upc": "ITEM-69",
                "unit_price": 56.89,
            },
        ]
    },
    {
        "date": "29/08/2026",
        "customer_email": "email2@gmail.com",
        "items" : [
            {
                "name" : "switch",
                "upc":"ITEM-432",
                "unit_price": 12.54, 
            },
            {
                "name":"play-station",
                "upc": "ITEM-324",
                "unit_price" : 32.45,
            },
            {
                "name":"x-box",
                "upc": "ITEM-453",
                "unit_price" : 65.76,
            },
        ]
    },
    {
        "date" : "26/09/2026",
        "customer_email" : "email32@gmail.com",
        "items":[
            {
                "name":"x-box series x",
                "upc": "ITEM-69",
                "unit_price": 56.89,
            },
            {
                "name":"play-station 5",
                "upc": "ITEM-569",
                "unit_price": 56.98,
            },
            {
                "name": "switch",
                "upc": "ITEM-432",
                "unit_price": 12.54,
            },
        ]
    },
]


result = {
    "ITEM-69" : 0,
    "ITEM-453" : 0,
    "ITEM-432" : 0, 
    "ITEM-324" : 0,
    "ITEM-569" : 0,
}

for i in range(len(sales)):
    for x in range(len(sales[i].get("items"))):
        upc =  sales[i].get("items")[x].get("upc")
        price = sales[i].get("items")[x].get("unit_price")
        match upc:
            case "ITEM-69":
                result["ITEM-69"] = result["ITEM-69"] + price
            case "ITEM-453":
                result["ITEM-453"] = int(result["ITEM-453"]) + price
            case "ITEM-432":
                result["ITEM-432"] = result["ITEM-432"] + price
            case "ITEM-324":
                result["ITEM-324"] = result["ITEM-324"] + price
            case "ITEM-569":
                result["ITEM-569"] = result["ITEM-569"] + price


print(f"Result = {result}")

"""
Ejercicio 2

"""
print("\nEJERCICIO 2\n")

employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

departments = {
    "Ventas" : [],
    "TI" : [],
    "RRHH" : [],
}    

for i in range(len(employees)):
    department = employees[i].get("department")
    name = employees[i].get("name")
    email = employees[i].get("email")

    match department:
        case "Ventas":
            departments["Ventas"].append({"name":name, "email":email})
        case "TI":
            departments["TI"].append({"name":name,"email":email})
        case "RRHH":
            departments["RRHH"].append({"name":name,"email":email})
print(f"DEPARTMENTS= {departments}")

"""
Ejercicio 3

"""

print("\nEjercicio 3\n")
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

categories = {
    "Electrónica" : [],
    "Muebles" : [],
}

for i in range(len(products)):
    products_name = products[i].get("name")
    products_price = products[i].get("price")
    
    if products[i].get("category") == "Electrónica":
        categories["Electrónica"].append({"name" : products_name, "price": price,})
    elif products[i].get("category") == "Muebles":
        categories["Muebles"].append({"name":products_name, "price":products_price})

print(f"CATEGORIAS= {categories}" )

