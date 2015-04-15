nakup_listek = []

odgovor = "da"
while odgovor == "da":
    odgovor = raw_input("Ali zelis dodati? Da / Ne ? ")

    if odgovor == "ne":
        print("Nic ne dodaj")
        break
    elif odgovor == "da":
        print("Dodaj")


    dodatek = raw_input("Povej, kaj zelis dodati? ")

    nakup_listek.append(dodatek)
    print nakup_listek

print nakup_listek


