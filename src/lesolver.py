class LinearEquationSolver:
    """
    Class to solve a system of linear equations with two unknowns.

    Attributes:
    - a1, b1, c1: float
        Coefficients of the first equation in the form a1*x + b1*y = c1.
    - a2, b2, c2: float
        Coefficients of the second equation in the form a2*x + b2*y = c2.
    """

    def __init__(self, a1: float, b1: float, c1: float, a2: float, b2: float, c2: float):
        """
        Constructor to instantiate the LinearEquationSolver class.

        Parameters:
        - a1, b1, c1: float
            Coefficients of the first equation in the form a1*x + b1*y = c1.
        - a2, b2, c2: float
            Coefficients of the second equation in the form a2*x + b2*y = c2.

        Raises:
        - ValueError:
            Throws an error if the coefficients of both equations are zero, 
            which would make the system of equations indeterminate.
        """

        # Verifying that the coefficients of both equations are not zero.
        if a1 == 0 and b1 == 0 and c1 == 0 and a2 == 0 and b2 == 0 and c2 == 0:
            raise ValueError("Both equations have zero coefficients.")

        # Assigning the coefficients to the instance variables.
        self.a1 = a1
        self.b1 = b1
        self.c1 = c1
        self.a2 = a2
        self.b2 = b2
        self.c2 = c2

    def solve_equations(self):
        """
        Solves the system of linear equations with two unknowns.

        Returns:
        - tuple:
            A tuple containing the values of x and y that satisfy both equations.

        Raises:
        - ValueError:
            Will raise an error if the system of equations is indeterminate or inconsistent.
        """

        # Calculating the determinant of the coefficient matrix
        determinant = self.a1 * self.b2 - self.a2 * self.b1

        # Checking if the system of equations is indeterminate or inconsistent
        if determinant == 0:
            raise ValueError("The system of equations is indeterminate or inconsistent.")

        # Calculating the values of x and y using Cramer's rule
        x = (self.b2 * self.c1 - self.b1 * self.c2) / determinant
        y = (self.a1 * self.c2 - self.a2 * self.c1) / determinant

        return x, y


if __name__ == "__main__":
   equation_solver = LinearEquationSolver(2, 3, 7, 4, -1, 2)
   try:
      x_value, y_value = equation_solver.solve_equations()
      print(f"The solution to the system of equations is x = {x_value}, y = {y_value}.")
   except ValueError as e:
      print(f"Error while solving the system of equations: {e}")
