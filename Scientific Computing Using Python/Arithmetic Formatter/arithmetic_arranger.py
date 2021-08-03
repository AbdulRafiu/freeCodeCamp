def arithmetic_arranger(problems, result_=False):
    numerators = ''
    denominators = ''
    dashes = ''
    results = ''
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for problem in problems:
            problem = problem.rstrip().split(' ')
            first_operand = problem[0]
            second_operand = problem[2]
            operator = problem[1]
            if not (first_operand.isdigit() and second_operand.isdigit()):
                return "Error: Numbers must only contain digits."
            elif not (len(first_operand) <= 4 and len(second_operand) <= 4):
                return "Error: Numbers cannot be more than four digits."
            else:
                length = max(len(first_operand), len(second_operand)) + 2
                first_operand = first_operand.rjust(length)
                second_operand = second_operand.rjust(length - 1)
                numerators += first_operand + "    "
                denominators += operator + second_operand + "    "
                dashes += "-" * length + "    "
                if operator == "+":
                    result = int(first_operand) + int(second_operand)
                elif operator == "-":
                    result = int(first_operand) - int(second_operand)
                else:
                    return "Error: Operator must be '+' or '-'."
                result = str(result).rjust(length)
                results += result + "    "
        if result_:
            arranged = numerators.rstrip() + "\n" + denominators.rstrip() + "\n" + dashes.rstrip() + "\n" + results.rstrip()
            return arranged
        else:
            arranged = numerators.rstrip() + "\n" + denominators.rstrip() + "\n" + dashes.rstrip()
            return arranged

