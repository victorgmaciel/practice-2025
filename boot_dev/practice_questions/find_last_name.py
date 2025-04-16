def find_last_name(names_dict, first_name):
    if first_name in names_dict:
        return names_dict[first_name]
    else:
        return None





test_dict = {
    'John' : 'Boone',
    'Kenny': 'Thompson',
    'Benny': 'Anderson',
}

first_name = 'Benny'

print(find_last_name(test_dict, first_name))