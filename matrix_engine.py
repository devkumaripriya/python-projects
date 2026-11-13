
import numpy as np


class MatrixEngine:

    # 1. Create Matrix
    def create_matrix(self, data):
        return np.array(data, dtype=float)

    # 2. Display Matrix
    def display_matrix(self, matrix):
        print("\nYour Matrix:")
        print(matrix)
        print("Matrix Shape:", matrix.shape)
        print("Total Elements:", matrix.size)

    # 3. Matrix Addition
    def add(self, A, B):
        if A.shape != B.shape:
            raise ValueError("Matrices must have equal dimensions")
        return A + B

    # 4. Matrix Subtraction
    def subtract(self, A, B):
        if A.shape != B.shape:
            raise ValueError("Matrices must have equal dimensions")
        return A - B

    # 5. Matrix Multiplication
    def multiply(self, A, B):
        if A.shape[1] != B.shape[0]:
            raise ValueError("Incompatible dimensions for multiplication")
        return A @ B

    # 6. Transpose
    def transpose(self, A):
        return A.T

    # 7. Determinant
    def determinant(self, A):
        if A.shape[0] != A.shape[1]:
            raise ValueError("Determinant requires a square matrix")
        return np.linalg.det(A)

    # 8. Matrix Inverse
    def inverse(self, A):
        if A.shape[0] != A.shape[1]:
            raise ValueError("Inverse requires a square matrix")

        if np.isclose(np.linalg.det(A), 0):
            raise ValueError("Inverse does not exist for this matrix")

        return np.linalg.inv(A)

    # 9. Eigenvalues and Eigenvectors
    def eigen(self, A):
        if A.shape[0] != A.shape[1]:
            raise ValueError("Eigenvalues require a square matrix")

        eigenvalues, eigenvectors = np.linalg.eig(A)

        return eigenvalues, eigenvectors


# Taking Matrix Input
def get_matrix(name):

    print(f"\nEnter values for Matrix {name}")

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    if rows <= 0 or columns <= 0:
        raise ValueError("Rows and columns must be positive")

    data = []

    for i in range(rows):

        row = list(map(
            float,
            input(f"Enter values for row {i + 1}: ").split()
        ))

        if len(row) != columns:
            raise ValueError(
                f"Please enter exactly {columns} values"
            )

        data.append(row)

    return np.array(data, dtype=float)


# Main Application
def main():

    engine = MatrixEngine()

    while True:

        print("\n========== MATRIXMIND ==========")
        print("        MATRIX CALCULATOR")
        print("================================")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Matrix Multiplication")
        print("4. Transpose")
        print("5. Display Matrix")
        print("6. Determinant")
        print("7. Matrix Inverse")
        print("8. Eigenvalues and Eigenvectors")
        print("9. Exit")

        choice = input("\nChoose an operation: ")

        if choice == "9":
            print("\nThank you for using MatrixMind!")
            break

        try:

            if choice in ("1", "2", "3"):

                A = get_matrix("A")
                B = get_matrix("B")

                if choice == "1":
                    result = engine.add(A, B)
                    print("\nAddition Result:")

                elif choice == "2":
                    result = engine.subtract(A, B)
                    print("\nSubtraction Result:")

                else:
                    result = engine.multiply(A, B)
                    print("\nMultiplication Result:")

                print(result)

            elif choice == "4":

                A = get_matrix("A")
                result = engine.transpose(A)

                print("\nTranspose:")
                print(result)

            elif choice == "5":

                A = get_matrix("A")
                engine.display_matrix(A)

            elif choice == "6":

                A = get_matrix("A")
                result = engine.determinant(A)

                print("\nDeterminant:", round(result, 2))

            elif choice == "7":

                A = get_matrix("A")
                result = engine.inverse(A)

                print("\nInverse Matrix:")
                print(np.round(result, 2))

            elif choice == "8":

                A = get_matrix("A")

                eigenvalues, eigenvectors = engine.eigen(A)

                print("\nEigenvalues:")
                print(np.round(eigenvalues, 2))

                print("\nEigenvectors:")
                print(np.round(eigenvectors, 2))

            else:
                print("\nInvalid choice! Please select 1 to 9.")

        except (ValueError, np.linalg.LinAlgError) as error:
            print("\nError:", error)


if __name__ == "__main__":
    main()
