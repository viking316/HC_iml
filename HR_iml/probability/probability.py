from math import gcd

def probability_black(W, B):
    numerator = B * (B + 1) + W * B
    denominator = (W + B) * (W + B + 1)
    common_divisor = gcd(numerator, denominator)
    return f"{numerator // common_divisor}/{denominator // common_divisor}"


W = 3  
B = 2  

print(probability_black(W, B))  
