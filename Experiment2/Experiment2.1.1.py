a, b, c = map(float, input().split())


D = b*b - 4*a*c


if D > 0:

root1 = (-b + math.sqrt(D)) / (2*a)

root2 = (-b - math.sqrt(D)) / (2*a)


print(f"root1 = {root1:.2f}")

print(f"root2 = {root2:.2f}")


elif D == 0:

root = -b / (2*a)

print(f"root1 = root2 = {root:.2f}")


else:

realPart = -b / (2*a)

imaginaryPart = math.sqrt(-D) / (2*a)


print(f"root1 = {realPart:.2f}+{imaginaryPart:.2f}i")

print(f"root2 = {realPart:.2f}-{imaginaryPart:.2f}i")
