
def symmetricTree(root1, root2):
    if root1 is None and root2 is None:
        return True

    elif root1 is None and  root2 is not None:
        return False
    
    elif root1.val != root2.val:
        return False

    else:
        return symmetricTree(root1.left, root2.right) and symmetricTree(root1.right, root2.left)


def isSymmetric(root):
    if root is None:
        return True
    else:
        return symmetricTree(root.left, root.right)


#generic parenthesis


def permutation(nums):
    result = []
    if len(nums) ==1:

        return [[1]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permutation(nums)

        for perm in perms:
            perm.append(n)

        result.extend(perms)
        nums.append(n)

    return result

result = permutation([1, 2, 3])
print(result)


def isValid(s):
    stack = []
    closeToopen = {
        "}":"{", ")":"(","]":"["
    }

    for c in s:

        if c in closeToopen:
            if stack and stack[-1] == closeToopen[c]:
                stack.pop()
            else:
                return False

        else:
            stack.append(c)

    return True if not stack else False
