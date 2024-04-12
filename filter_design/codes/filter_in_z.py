import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 0.4166*s**4/(16375.363149957*s**8 + 1885.04141381847*s**7 + 8673.64722964977*s**6 + 741.61218791399*s**5 + 1691.53238517028*s**4 + 95.5264800515727*s**3 + 143.911529226533*s**2 + 4.02866954955551*s + 4.50794497815827)


# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


