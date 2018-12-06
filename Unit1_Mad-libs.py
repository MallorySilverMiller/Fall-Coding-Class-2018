pN = input("Proper noun? ") + " City"  # 0: city
n1 = input("Noun? ")  # 1: protagonist
n2 = "THE " + input("Noun? ").upper()  # 2: antagonist
a1 = input("Adjective? ")  # 3: first protagonist desc
a2 = input("Adjective? ")  # 4: antagonist desc
v1 = input("Transitive Present participle (verb-'ing')? ")  # 5: bad thing the antagonist is doing
v2 = input("Transitive verb? ")  # 6:punishment of antagonist
n3 = input("Noun? ")  # 7: beloved obj.
a3 = input("Adjective? ")  # 8: beloved obj. desc.
n = str(input("A number? "))  # 9: how many of more desired obj
a4 = input("Adjective? ")  # 10: second protagonist desc
n4 = input("Noun? ")  # 11: more desired obj
a5 = input("Adjective? ")  # 12: more desired obj desc.
print("Once upon a time, in a land called {0}, lived a {1}.\nThis was no ordinary {1}, but a very {3} {1}.\nThis {3} \
{1} who lived in {0} had a problem.\nA(n) {4} Someone called {2} has been {5} his beloved and {8} {7}.\nBecause of this\
 obvious slight on the {1}'s honor, he simply had to avenge his {8} {7}.\nDetermined to {6} {2} for their transgression\
 s, the {3} {1} sought them out.\nBut lo, on the way to find {2}, the {3} and {10} {1} saw loads of {12} {11}!\n50, no \
 100, no {10} {12} {11}!\nForgetting all of {2}, the {1} went to steal those wonderful {12} {11}s.\nThough he may have \
 forgotten of {2}, they did not go unpunished, for you see those {9} {12} {11}s had belonged to them.\nAnd so the cycle\
  of {5} and stealing continued on.".format(pN, n1, n2, a1, a2, v1, v2, n3, a3, n, a4, n4, a5))
