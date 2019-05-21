"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
"""

def balanced_parenthesis(s_string):
    char_stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for c in s_string:
        if c in ['(', '[', '{']:
            char_stack.append(c)
        if c in [')', ']', '}'] and char_stack[-1] == pairs[c] :
            char_stack.pop()
    return True if not char_stack else False

def test_balanced_parentheses():
    assert balanced_parenthesis("()") == True
    assert balanced_parenthesis("[]") == True
    assert balanced_parenthesis("([])[]({{}})") == True
    assert balanced_parenthesis("{{}}") == True
    assert balanced_parenthesis("([)]") == False
    assert balanced_parenthesis("((()") == False

# if __name__ == '__main__':