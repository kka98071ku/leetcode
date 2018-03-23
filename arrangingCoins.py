import math


def arrangeCoins(s):
    """
    :type s: int
    :rtype: int
    LOL..... too bad that I'm doing redundant work...

    [discussion from other people]
    The idea is about quadratic equation, the formula to get the sum of arithmetic progression is
    sum = (x + 1) * x / 2
    so for this problem, if we know the the sum, then we can know the x = (-1 + sqrt(8 * n + 1)) / 2

    public class Solution {
        public int arrangeCoins(int n) {
            return (int)((-1 + Math.sqrt(1 + 8 * (long)n)) / 2);
        }
    }
    """
    (x1, x2) = solveQuadraticEquation(1, - 2 * s)
    (y1, y2) = solveQuadraticEquation(3, 2 - 2 * s)
    if (x1 == None or x2 == None or y1 == None or y2 == None or (y1 < x1 and y2 > x2)):
        return None
    for guess in range(math.ceil(x1), math.floor(min(x2, y1)) + 1):
        return guess
    for guess in range(x1 if x1 > y2 else math.floor(y2 + 1), math.floor(x2) + 1):
        return guess


def solveQuadraticEquation(b, c):
    # a = 1
    delta = b * b - 4 * c
    if delta < 0:
        return (None, None)
    sDelta = math.sqrt(delta)
    return ((-b - sDelta) / 2, (-b + sDelta) / 2)


if __name__ == "__main__":
    print(arrangeCoins(1))
    print(arrangeCoins(5))
    print(arrangeCoins(8))
    print(arrangeCoins(719885386))
