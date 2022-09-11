from solution import Solution
import matplotlib.pyplot as plt

if __name__ == "__main__":
    solution = Solution(0.00001, 1, 0.00001)

    solution.bisectionMethod()
    solution.goldenRatioMethond()
    solution.fibonacciMethod()
    solution.parablesMethod()
    solution.brentMethod()
    