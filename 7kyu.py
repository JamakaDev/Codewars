from math import ceil
def main() -> None:    
    def solution(digits):
        i, maxNums = 0, 0
        while i < len(digits):
            maxNums = int(digits[i:i+5]) if maxNums < int(digits[i:i+5]) else maxNums
            i += 1
        return maxNums;

    def factorial(n):
        if n < 0: return None
        elif n == 0: return 1
        else:
            res = 1
            for i in range(1, n+1): res *= i
            return res

    
    
if __name__ == '__main__':
    main()
  