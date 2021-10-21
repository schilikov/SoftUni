# Are the parentheses balanced or not?
parentheses = input()
stack = []
balanced = True

for ch in parentheses:
    if ch in "[{(":
        stack.append(ch)
    elif ch in ")}]":
        if len(stack) == 0:
            balanced = False
            break

        opening_paren = stack.pop()

        if f"{opening_paren}{ch}" not in ["[]", "{}", "()"]:
            balanced = False
            break

if balanced and len(stack) == 0:
    print("YES")
else:
    print("NO")

# Test Inputs

# {[()]}
# {[(])}
# {{[[(())]]}}