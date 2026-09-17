# Opdracht 3 tekstfuncties
# Naam student:
# Groep:

# Hier komt je code...

print("    *" * 5)
print("   ***" * 5)
print("  ******" * 5)
print(" ********" * 5)
print("*********** " * 5)
print("    ***" * 5)
print("    ***" * 5)
print("    ***" * 5)


boom = [
    "    *".ljust(15),
    "   ***".ljust(15),
    "  ******".ljust(15),
    " ********".ljust(15),
    "***********".ljust(15),
    "    ***".ljust(15),
    "    ***".ljust(15),
    "    ***".ljust(15)
]

for regel in boom:
    print(regel * 5)