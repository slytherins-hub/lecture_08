import json

def criminals(most_wanted, new_criminals):
    for novacek in new_criminals:
        if novacek not in most_wanted:
            most_wanted[novacek] = new_criminals[novacek]
        else:
            most_wanted[novacek].extend(new_criminals[novacek])

    print(most_wanted)



def main():
    names = ["Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"]
    production = [[138, 164, 151], [125, 113, 113], [52, 50, 63]]
    most_wanted = dict(zip(names, production))

    with open("new_criminals.json", mode="r") as json_data:
        new_criminals = json.load(json_data)
    print(new_criminals)

    criminals(most_wanted, new_criminals)

if __name__ == "__main__":
    main()