"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""

if __name__ == "__main__":
    # Write your solution here
    for _ in range(int(input())):
        def areBracketsBalanced(expr):
            stack = []

            # Traversing the Expression
            for char in expr:
                if char in ["("]:

                    # Push the element in the stack
                    stack.append(char)
                else:
                    if not stack:
                        return False
                    current_char = stack.pop()
                    if current_char == '(':
                        if char != ")":
                            return False
            if stack:
                return False
            return True


        s = list(map(str, input()))
        l = []
        quest = '?'
        left = '('
        right = ')'
        if s[0] != ')' and s[-1] != '(' and len(s) % 2 == 0:
            for i in range(1, len(s) + 1):
                if s[i - 1] == left:
                    l.append('(')
                elif s[i - 1] == quest and s[i] == quest:
                    l.append('(')
                    l.append(')')
                elif s[i - 1] == right:
                    l.append(')')
            finalString = ''.join(l)
            if areBracketsBalanced(finalString):
                print("YES")
        else:
            print('NO')
    pass
