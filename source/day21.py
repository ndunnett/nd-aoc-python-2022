import re
from input import load_input


def puzzle():
    lines = load_input(21)
    monkeys = {groups[0]: groups[1] for groups in [re.search(r"(\w+)(?::\s)(.+)", line).groups() for line in lines]}

    def parse(expression):
        if expression in monkeys:
            return parse(monkeys[expression])
        elif re.search(r"\d+", expression):
            return {
                "op": "constant",
                "n": int(expression)
            }
        elif re.search(r"[+\-*/]", expression):
            parts = expression.split()
            return {
                "op": parts[1],
                "a": parse(parts[0]),
                "b": parse(parts[2])
            }
        else:
            return {
                "op": "variable",
                "n": expression
            }

    def evaluate(ast):
        if ast["op"] in ["constant", "variable"]:
            return ast["n"]

        match ast["op"]:
            case "+": return evaluate(ast["a"]) + evaluate(ast["b"])
            case "-": return evaluate(ast["a"]) - evaluate(ast["b"])
            case "*": return evaluate(ast["a"]) * evaluate(ast["b"])
            case "/": return evaluate(ast["a"]) // evaluate(ast["b"])

    answer = evaluate(parse(monkeys["root"]))
    print(f"Part 1 answer: {answer}")

    def simplify(ast):
        if ast["op"] in ["constant", "variable"]:
            return ast

        if ast["a"]["op"] not in ["constant", "variable"]:
            ast["a"] = simplify(ast["a"])

        if ast["b"]["op"] not in ["constant", "variable"]:
            ast["b"] = simplify(ast["b"])

        if ast["a"]["op"] == "constant" and ast["b"]["op"] == "constant":
            return {
                "op": "constant",
                "n": evaluate(ast)
            }

        return ast

    def solve(a, b):
        constant, variable = (a, b) if a["op"] == "constant" else (b, a)

        if variable["op"] == "variable":
            return evaluate(constant)

        constant_side, variable_side = ("a", "b") if simplify(variable["a"])["op"] == "constant" else ("b", "a")

        if constant_side == "b":
            match variable["op"]:
                case "+": constant["n"] -= evaluate(variable[constant_side])
                case "-": constant["n"] += evaluate(variable[constant_side])
                case "*": constant["n"] //= evaluate(variable[constant_side])
                case "/": constant["n"] *= evaluate(variable[constant_side])
        else:
            match variable["op"]:
                case "+": constant["n"] -= evaluate(variable[constant_side])
                case "-": constant["n"] = evaluate(variable[constant_side]) - constant["n"]
                case "*": constant["n"] //= evaluate(variable[constant_side])
                case "/": constant["n"] = evaluate(variable[constant_side]) // constant["n"]

        return solve(variable[variable_side], constant)

    monkeys["humn"] = "x"
    ast = simplify(parse(monkeys["root"]))
    answer = solve(ast["a"], ast["b"])
    print(f"Part 2 answer: {answer}")


if __name__ == "__main__":
    puzzle()
