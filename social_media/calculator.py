"""
CALCULATOR

A simple, clear calculator that handles:
- Basic: +, -, *, /
- Modulo: % (remainder)
- Power: ^ (for example, 2^3)
- Square root: sqrt(16)
- Absolute: abs(-5)
- Percentage: 50% of 100, or 100 - 50%
"""

import math
import re


class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def modulo(self, a, b):
        return a % b

    def power(self, a, b):
        return a**b

    def square_root(self, a):
        return math.sqrt(a)

    def absolute(self, a):
        return abs(a)

    def percentage(self, a, b):
        """Calculate b percent of a. For example, percentage(100, 50) == 50."""
        return (b / 100) * a

    def calculate(self, expression):
        try:
            expr = expression.strip()
            expr = expr.replace("^", "**")

            expr = self._handle_sqrt(expr)
            expr = self._handle_abs(expr)
            expr = self._handle_percentage(expr)

            result = eval(expr, {"__builtins__": {}}, {"math": math, "abs": abs})

            if isinstance(result, float):
                result = round(result, 10)

            self.history.append((expression, result))
            return result

        except Exception as error:
            return f"Error: {error}"

    def _handle_sqrt(self, expr):
        return re.sub(
            r"sqrt\s*\(([^)]+)\)",
            lambda m: f"math.sqrt(({m.group(1)}))",
            expr,
        )

    def _handle_abs(self, expr):
        return re.sub(
            r"abs\s*\(([^)]+)\)",
            lambda m: f"abs(({m.group(1)}))",
            expr,
        )

    def _handle_percentage(self, expr):
        number = r"\d+(?:\.\d+)?"

        expr = re.sub(
            rf"({number})%\s*of\s*({number})",
            lambda m: f"(({m.group(1)}/100)*{m.group(2)})",
            expr,
            flags=re.IGNORECASE,
        )

        expr = re.sub(
            rf"({number})\s*([+-])\s*({number})%",
            lambda m: (
                f"({m.group(1)} {m.group(2)} "
                f"({m.group(1)}*{m.group(3)}/100))"
            ),
            expr,
        )

        expr = re.sub(
            rf"(?<![\w.])({number})%(?!\s*(?:of|\d|\.\d))",
            lambda m: f"({m.group(1)}/100)",
            expr,
            flags=re.IGNORECASE,
        )

        return expr

    def show_history(self):
        if not self.history:
            return "No calculations yet."

        result = "Calculation History:"
        for i, (expr, value) in enumerate(self.history):
            result += f"\n{i + 1}. {expr} = {value}"
        return result


def main():
    calc = Calculator()

    print("=" * 60)
    print(" " * 18 + "CALCULATOR")
    print("=" * 60)
    print("Try these examples:")
    print("  - 2 + 6 + 8 + 7 - 5 * 8 / 9")
    print("  - 56 % 45 * 100 - 5 + 36")
    print("  - 2^3 (power)")
    print("  - sqrt(16) (square root)")
    print("  - abs(-5) (absolute value)")
    print("  - 50% of 100 (percentage)")
    print("  - 100 - 50% (subtract percentage)")
    print("=" * 60)

    while True:
        try:
            expression = input("Enter expression (or 'history'/'quit'): ").strip()

            if expression.lower() == "quit":
                print("Thank you for using Real-Life Calculator!")
                break

            if expression.lower() == "history":
                print(calc.show_history())
                continue

            if not expression:
                print("Please enter an expression.")
                continue

            result = calc.calculate(expression)

            if isinstance(result, (int, float)):
                print(f"Result: {result}")
            else:
                print(result)

        except KeyboardInterrupt:
            print("Thank you for using Real-Life Calculator!")
            break
        except EOFError:
            break


if __name__ == "__main__":
    main()
