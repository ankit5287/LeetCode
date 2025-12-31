#20 valid parentheses

string = "(}"
hashmap = {')':'(','}':'{',']':'['}

stack = []
def check(strig):
    for c in string:
        if not c in hashmap:
            stack.append(c)
        
        else:
            if not stack:
                return False
            else:
                popped = stack.pop()
                if popped != hashmap[c]:
                    return False
    return not stack

print(check(string))