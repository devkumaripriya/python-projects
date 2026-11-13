
import numpy as np


class VectorEngine:

    # 1. Create a vector
    def create_vector(self, data):
        return np.array(data, dtype=float)

    # 2. Display vector
    def display_vector(self, vector):
        print("\nYour Vector:", vector)
        print("Dimensions:", vector.shape)
        print("Number of elements:", vector.size)

    # 3. Vector Addition
    def add(self, A, B):
        if A.shape != B.shape:
            raise ValueError("Vectors must have equal dimensions")
        return A + B

    # 4. Vector Subtraction
    def subtract(self, A, B):
        if A.shape != B.shape:
            raise ValueError("Vectors must have equal dimensions")
        return A - B

    # 5. Dot Product
    def dot_product(self, A, B):
        if A.shape != B.shape:
            raise ValueError("Vectors must have equal dimensions")
        return np.dot(A, B)

    # 6. Magnitude
    def magnitude(self, A):
        return np.linalg.norm(A)

    # 7. Normalization
    def normalize(self, A):
        magnitude = self.magnitude(A)

        if magnitude == 0:
            raise ValueError("Zero vector cannot be normalized")

        return A / magnitude


# Taking vector input from user
def get_vector(name):

    print(f"\nEnter values for Vector {name}")

    data = list(map(
        float,
        input("Enter vector elements separated by spaces: ").split()
    ))

    if not data:
        raise ValueError("Vector cannot be empty")

    return np.array(data)


# Main application
def main():

    engine = VectorEngine()

    while True:

        print("\n========== MATRIXMIND ==========")
        print("VECTOR CALCULATOR")
        print("1. Create Vector")
        print("2. Vector Addition")
        print("3. Vector Subtraction")
        print("4. Dot Product")
        print("5. Magnitude")
        print("6. Normalize Vector")
        print("7. Exit")

        choice = input("\nChoose an operation: ")

        if choice == "7":
            print("Thank you for using MatrixMind!")
            break

        try:

            if choice == "1":
                A = get_vector("A")
                engine.display_vector(A)

            elif choice in ("2", "3", "4"):
                A = get_vector("A")
                B = get_vector("B")

                if choice == "2":
                    result = engine.add(A, B)

                elif choice == "3":
                    result = engine.subtract(A, B)

                else:
                    result = engine.dot_product(A, B)

                print("\nResult:", result)

            elif choice in ("5", "6"):
                A = get_vector("A")

                if choice == "5":
                    result = engine.magnitude(A)

                else:
                    result = engine.normalize(A)

                print("\nResult:", result)

            else:
                print("Invalid choice!")

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
