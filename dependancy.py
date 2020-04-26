inputs = []
results = []


def get_value_from_input(input_arg, results, inputs):
    if input_arg == "_":
        return 0
    if input_arg.find("$") > -1:
        ref = int(input_arg.replace("$", ""))
        return get_cell_i(results, inputs, ref)
    else:
        return int(input_arg)


def compute_input(results, inputs, i):
    input = inputs[i]
    arg_1 = get_value_from_input(input["arg_1"], results, inputs)
    arg_2 = get_value_from_input(input["arg_2"], results, inputs)

    operation = input["operation"]
    if operation == "VALUE":
        return arg_1
    if operation == "ADD":
        return arg_1 + arg_2
    if operation == "SUB":
        return arg_1 - arg_2
    if operation == "MULT":
        return arg_1 * arg_2
    return "WTF"


def get_cell_i(results, inputs, i):
    if not bool(results[i]):
        results[i] = compute_input(results, inputs, i)
        return results[i]
    else:
        return results[i]


n = int(input())
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    inputs.append({
        "operation": operation,
        "arg_1": arg_1,
        "arg_2": arg_2
    })
for i in range(n):
    results.append(False)
for i in range(len(inputs)):
    results[i] = get_cell_i(results, inputs, i)

for result in results:
    print(result)
