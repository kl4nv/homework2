data_structure = [
    [{(1, 2, 3)}],
  {'a': 4, 'b': 5},
  (6, {'key': { '555': 1, 'y': 2}, 'drum': 8}),
  "Hello", True,
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    count = 0
    type_structure = [int, float]
    type_structure1 = [tuple, list]
    if type(data_structure) in type_structure:
        count += data_structure
    elif isinstance(data_structure, str):
        count += len(data_structure)
    elif type(data_structure) in type_structure1:
        for i in data_structure:
            count += calculate_structure_sum(i)
    elif isinstance(data_structure, dict):
        keys = list(data_structure.keys())
        vol = list(data_structure.values())
        count += calculate_structure_sum(keys)
        count += calculate_structure_sum(vol)
    elif isinstance(data_structure, set):
        s = list(data_structure)
        count += calculate_structure_sum(s)
    return count

result = calculate_structure_sum(data_structure)
print(result)

