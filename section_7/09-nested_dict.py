nested_dict = {
    "Person1": {"Name": "Ricardo", "year": 29, "city": "Ciudad de México"},
    "Person2": {"Name": "Brenda", "year": 26, "city": "Huejutla de Reyes"},
    "Person3": {"Name": "Estela", "year": 50, "city": "Cancún"}
}


for key, value in nested_dict.items():
    print(f"{key}:")
    for sub_key, sub_value in value.items():
        print(f" {sub_key}: {sub_value}")