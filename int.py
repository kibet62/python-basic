# if..elfi..else statement
# creat a program for grades input with the following
#    80-100 -A
#   60-79 -B
#   50-59 -C
#   30-49 -D
#   below 30 - fail
#   negative and above 100- invalid input
A=int(input("enter value:"))
B=int(input("enter value:"))
C=int(input("enter value"))
D=int(input("enter value:"))




if A > B and A > C and A > D:
    print(A,"is greater")

elif B < A and B > C and B > D:
    print(B,"is greater")

elif C <A and C < B and C > D:
    print(C,"is greater")


elif D < A and D < B and D < C:
    print(D,"is greater")

else:
    print("invalid input")




