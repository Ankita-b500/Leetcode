class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case
        if n == 0:
            return 1
        
        # Handle negative exponent
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # If n is even: x^n = (x * x)^(n / 2)
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        
        # If n is odd: x^n = x * (x * x)^((n - 1) / 2)
        else:
            return x * self.myPow(x * x, (n - 1) // 2)