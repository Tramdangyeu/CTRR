# 1. Determine and print domain D, predicate P of the following expression
# then write the statement in formal form:
# (a) For all fishes, they need water to survive.
print("D is 'fishes'")
print("P is 'need water to survive'")
print("Formal form: For all x in D ,P(x)")
# (b) Exist a person, who is left handed
print("D is 'person'")
print("P is 'is left hand'")
print("Formal form: Exist x such that D(x) ^ P(x)")
# (c) Exist an employee in the company, who is late to work everyday.
print("D is 'employee in the company'")
print("P is 'is late to work everyday'")
print("Formal form: Exist x such that D(x) ^ P(x)")
# (d) For all fishes in this pond, they are Koi fish.
print("D is 'fishes in this pond'")
print("P is 'are Koi fish'")
print("Formal form: For all x in D ,P(x)")
# (e) There is at least one creature in the ocean, it can live on land
print("D is 'creature in the ocean '")
print("P is 'live on land'")
print("Formal form: Exist x such that D(x) ^ P(x)")
# (f) Every students in class A did not pass the test
print("D is 'student in class A'")
print("P is 'not pass the test'")
print("Formal form: For all x in D ,P(x)")

# Write a function [D,P,F]=formalConvert(S) to extract D and P then con-
# vert the statement S from Exercise 1. excluded (f) to formal form F.

# Hint: D contains the words between For all/ Exist/ There is at least one
# and a comma (,);
# P contains the words after the first word from the comma (,).
def formalConvert(S):
    tach = S.split(",")
    for_all = S[0:7]
    if for_all =="For all":
        beforeString =tach[0]
        afterString = tach[1].strip()
        count =0
        for i in tach[1].strip():
            if i != " ":
                count = count +1
            else:
                break
        P = afterString[count :].strip()
        D = beforeString [7:]
        F = f'For all x in D, P(x)'
        return D,P,F
S = "For all fishes, they need water to survive"
[D,P,F] =formalConvert(S)

print("D is " ,D)
print("P is " ,P)
print("Formal form:",F)
