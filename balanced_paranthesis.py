# %%
"""
A balanced parenthesis string starts with an opening character ((, [, {),
ends with a matching closing character (), ], } respectively), and has only other matching parenthesis in
between.
Example
Input Output
()[]{} True
([{}]) True
([]{}) True
([]{}) True
([)] False
([] False
[]) False
([}) False
"""


def paranthesis_check(input: str) -> bool:
    brackets_type_open: list = ["[", "{", "("]
    brackets_type_close: list = ["]", "}", ")"]
    test_stack: list = []
    for paranthesis in input:
        if paranthesis in brackets_type_open:
            test_stack.append(paranthesis)
        elif paranthesis in brackets_type_close:
            pos = brackets_type_close.index(paranthesis)
            if (len(test_stack) > 0) and (brackets_type_open[pos] == test_stack[len(test_stack) - 1]):
                test_stack.pop()
            else:
                return False
    if len(test_stack) == 0:
        return True
    else:
        return False


# driver code
inputs: list = ["()[]{}", "([{}])", "([]{})", "([]{})", "([)]", "([]", "[])", "([})"]
for test_input in inputs:
    print(f"{test_input}: {paranthesis_check(test_input)}")

# %%
