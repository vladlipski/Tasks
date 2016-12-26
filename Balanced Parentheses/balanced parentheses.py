def check_balance(characters, string):
    stack = []
    opening_characters = list(characters.keys())
    string = [c for c in string if c in opening_characters
                                or c in characters.values()]
    for i in range(len(string)):
        if string[i] in opening_characters:
            stack.append(string[i])
        else:
            if len(stack) == 0 or characters[stack[-1]] != string[i]:
                return False
            else:
                stack.pop()
    if len(stack) > 0:
        return False
    else:
        return True

if __name__ == "__main__":
    characters = {'{': '}', '[': ']', '(': ')'}
    print(check_balance(characters, "{(){}}[[{}]]"))