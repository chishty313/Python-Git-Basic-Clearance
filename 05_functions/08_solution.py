def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name = 'Chishty', role = 'Student')
print_kwargs(university = 'BRACU')
print_kwargs(location = "ECB", district = 'Dhaka', country = 'BD')