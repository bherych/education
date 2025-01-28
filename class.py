class Sorter:
    def __init__(self, matrix1=[]):
        self.matrix1 = matrix1
    
    def __str__(self):
        result = ""
        for i in range(len(self.matrix1)):
             result += (str(self.matrix1[i])) + "\n"
        return result

    def __repr__(self):
        pass

    def __del__(self):
        return print("Deleted Sorter")
    
    def __sub__(self, other):

        matrix3 = []

        for i in range(len(self.matrix1)):
            matrix3.append([])
            for j in range(len(self.matrix1[i])):
                result = self.matrix1[i][j] - other.matrix1[i][j]
                matrix3[i].append(result)

        
        return Sorter(matrix3)


# Mean - середнє арифмертичне
    def mean(values):
        return sum(values) / len(values)
    
def main():

    sorter1 = Sorter(matrix1 = [
        [90, 7, 89, -2, 17],
        [1, -4, 8, 56, 32],
        [-4, -6, -99, 19, 39],
        [2, 4, -7, 0, 75],
        [11, 41, 22, 80, -5]
    ])
    sorter2 = Sorter(matrix1 = [
        [87, 7, 89, -2, 17],
        [1, -4, 8, 56, 32],
        [-4, -6, -99, 19, 39],
        [2, 4, -7, 0, 75],
        [11, 41, 22, 80, -5]
    ])

    result = sorter1 - sorter1

    print(result)

    return

main()