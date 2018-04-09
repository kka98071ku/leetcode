"""
Question:
    https://leetcode.com/problems/reaching-points/description/
"""


def reachingPoints(sx, sy, tx, ty):
    """
    :type sx: int
    :type sy: int
    :type tx: int
    :type ty: int
    :rtype: bool

    Consider from the last step -- it's either
        (x_{t - 1}, y_{t - 1}) -> (x_{t - 1} + y_{t - 1}, y_{t - 1})
    or
        (x_{t - 1}, y_{t - 1}) -> (x_{t - 1}, y_{t - 1} + x_{t - 1})

    So we only need to compare which one of x_{t} and y_{t} is larger
    to infer the t - 1 step.
    """
    if tx == ty:
        return sx == tx and sy == ty
    x, y = tx, ty
    while x > sx and y > sy:
        if x > y:
            x -= y
        else:
            y -= x

    return (x - sx) % sy == 0 and (y - sy) % sx == 0


def reachingPointsDumb(sx, sy, tx, ty):
    """
    :type sx: int
    :type sy: int
    :type tx: int
    :type ty: int
    :rtype: bool
    """
    if sx > tx or sy > ty:
        return False
    stack = [(sx, sy)]
    visited = {}
    while len(stack) > 0:
        (x, y) = stack.pop()
        if x == tx and y == ty:
            return True
        nextStep = x + y
        if nextStep <= ty and (not x in visited or not nextStep in visited[x]):
            stack.append((x, nextStep))
            visited.setdefault(x, set()).add(nextStep)
        if nextStep <= tx and (not nextStep in visited or visited[nextStep] != y):
            stack.append((nextStep, y))
            visited.setdefault(nextStep, set()).add(y)
    return False


if __name__ == "__main__":
    print(reachingPoints(1, 1, 3, 5))
    print(reachingPoints(1, 1, 2, 2))
