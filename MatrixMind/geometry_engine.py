
import numpy as np
import matplotlib.pyplot as plt


class GeometryEngine:

    # Original triangle points
    def create_shape(self):
        return np.array([
            [1, 3, 2],
            [1, 1, 3]
        ])

    # Translation
    def translate(self, points, tx, ty):
        translation = np.array([
            [tx],
            [ty]
        ])

        return points + translation

    # Rotation
    def rotate(self, points, angle):
        radians = np.radians(angle)

        rotation = np.array([
            [np.cos(radians), -np.sin(radians)],
            [np.sin(radians), np.cos(radians)]
        ])

        return rotation @ points

    # Scaling
    def scale(self, points, sx, sy):
        scaling = np.array([
            [sx, 0],
            [0, sy]
        ])

        return scaling @ points

    # Reflection
    def reflect(self, points):
        reflection = np.array([
            [-1, 0],
            [0, 1]
        ])

        return reflection @ points

    # Display shape
    def display(self, original, transformed):

        original_closed = np.column_stack(
            (original, original[:, 0])
        )

        transformed_closed = np.column_stack(
            (transformed, transformed[:, 0])
        )

        plt.figure(figsize=(7, 6))

        plt.plot(
            original_closed[0],
            original_closed[1],
            "b--o",
            label="Original Shape"
        )

        plt.plot(
            transformed_closed[0],
            transformed_closed[1],
            "r-o",
            label="Transformed Shape"
        )

        plt.axhline(0)
        plt.axvline(0)

        plt.grid(True)
        plt.axis("equal")
        plt.legend()
        plt.title("MatrixMind - 2D Transformation")

        plt.show()


# Main Application
def main():

    engine = GeometryEngine()

    original = engine.create_shape()

    while True:

        print("\n========== MATRIXMIND ==========")
        print("     2D GEOMETRY ENGINE")
        print("================================")
        print("1. Translation")
        print("2. Rotation")
        print("3. Scaling")
        print("4. Reflection")
        print("5. Exit")

        choice = input("\nChoose an operation: ")

        try:

            if choice == "1":

                tx = float(input("Enter X translation: "))
                ty = float(input("Enter Y translation: "))

                result = engine.translate(original, tx, ty)

            elif choice == "2":

                angle = float(input("Enter rotation angle: "))

                result = engine.rotate(original, angle)

            elif choice == "3":

                sx = float(input("Enter X scaling factor: "))
                sy = float(input("Enter Y scaling factor: "))

                result = engine.scale(original, sx, sy)

            elif choice == "4":

                result = engine.reflect(original)

            elif choice == "5":

                print("Thank you for using MatrixMind!")
                break

            else:

                print("Invalid choice!")
                continue

            print("\nOriginal Points:")
            print(original)

            print("\nTransformed Points:")
            print(np.round(result, 2))

            engine.display(original, result)

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
