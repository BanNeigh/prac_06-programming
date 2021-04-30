from prac_06.guitar import Guitars


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitars(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    guitars.append(Guitars("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitars("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            if guitar.is_vintage():
                print(f"Guitar {i + 1}:     {guitar.name:10} ({guitar.year:5}), worth $ {guitar.cost:10} (vintage)")
            else:
                print(f"Guitar {i + 1}:     {guitar.name:10} ({guitar.year:5}), worth $ {guitar.cost:10}")

    else:
        print("No guitars :( Quick, go and buy one!")


main()