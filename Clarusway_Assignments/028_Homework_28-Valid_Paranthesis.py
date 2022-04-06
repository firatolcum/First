"""
Valid Paranthesis

Input      Output
"()"        True
"()[]{}"    False
"(]"        False
"([)]"      False
"{[]}"      True
""          True

"""
x = "[([{({})}]({}))"


def is_valid(x):
    while "()" in x or "[]" in x or "{}" in x:
        x = x.replace("()", "").replace("{}", "").replace("[]", "")
        return x == ""


print(is_valid(x))
