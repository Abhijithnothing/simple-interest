# Simple & Compound Interest Program

P = int(input("Enter principal amount: "))
T = int(input("Enter time period (in years): "))
R = float(input("Enter rate of interest: "))

print("--- Simple Interest ---")
SI = (P * R * T) / 100
print("Simple Interest is:", SI)

print("--- Compound Interest ---")
A = P * (1 + R/100) ** T
CI = A - P
print("Compound Interest is:", CI)
