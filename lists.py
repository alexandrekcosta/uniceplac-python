scores = []
scores.append(float(input("Enter first score: ")))
scores.append(float(input("Enter second score: ")))
scores.append(float(input("Enter third score: ")))
print(scores)
scores.sort()
for i in range(3):
    print(scores[i])
scores.append(12.7)
for i in range(len(scores)):
    print(scores[i])
