def sort_by_insertion_ascending(row):
    for i in range(1, len(row)):
        key = row[i]
        j = i - 1
        while j >= 0 and row[j] > key:
            row[j + 1] = row[j]
            j -= 1
        row[j + 1] = key
    return row


def column_products(matrix):
    num_columns = len(matrix[0])
    products = []
    for col in range(num_columns):
        product = 1
        for row in matrix:
            product *= row[col]
        products.append(product)
    return products

# Mean - середнє арифмертичне
def mean(values):
    return sum(values) / len(values)

matrix = [
        [90, 7, 89, -2, 17],
        [1, -4, 8, 56, 32],
        [-4, -6, -99, 19, 39],
        [2, 4, -7, 0, 75],
        [11, 41, 22, 80, -5]
    ]

sorted_matrix = [sort_by_insertion_ascending(row) for row in matrix]

first_values = column_products(sorted_matrix)

second_value = mean(first_values)

print("Відсортована матриця:")
for row in sorted_matrix:
    print(row)

print("Значення добутків у стовпцях):")
print(first_values)

print("Середнє арифметичне значення після добутків:")
print(second_value)