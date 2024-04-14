import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 0.3125218*s**4/(16375.363149957*s**8 + 1602.18387099852*s**7 + 8317.61992288193*s**6 + 605.551717311528*s**5 + 1558.11373357189*s**4 + 74.987655196386*s**3 + 127.548729955613*s**2 + 3.04248157205658*s + 3.85074778811037)


# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


