def check_types(order):
    types = {}  
    for statement in order:
        if "=" in statement: 
            name, value = statement.split("=")
            value_type = type(eval(value)) 
            if name in types and types[name] != value_type:
                print(f"Error: Type mismatch for {name}")
            else:
                types[name] = value_type  

order = ["x = 10", "y = 5.0", "x = 'hello'"]
check_types(order) 
