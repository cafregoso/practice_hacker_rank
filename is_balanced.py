#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    if len(s) % 2 != 0:
        return "NO"

    is_balanced = True
    for i in range(int(len(s)/2)):
        if s[i] == "(" and s[-(i+1)] == ")":
            is_balanced = True
        elif s[i] == "{" and s[-(i+1)] == "}":
            is_balanced = True
        elif s[i] == "[" and s[-(i+1)] == "]":
            is_balanced = True
        else:
            is_balanced = False

    return "YES" if is_balanced else "NO"
 

if __name__ == "__main__":
    print(isBalanced("{(([])[])[]}"))
