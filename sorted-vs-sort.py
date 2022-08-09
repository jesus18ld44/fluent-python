# sorted creates a new list and returns it

fruits = ['banana', 'apple', 'pinneapple', 'grape', 'raspberry']

print(f'fruits --> {id(fruits)}')

fruits_sorted = sorted(fruits)

print(f'sorted(fruits) --> {fruits_sorted}')

# fruits.sort()
fruits.sort(key=lambda f: f[-1])    # sorts by the last letter

print(f'fruits.sort() --> {fruits}')
print(f"""fruits --> {id(fruits)}
fruits_sorted --> {id(fruits_sorted)}""")


