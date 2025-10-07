contacts = []

print("Enter contact information (format: name|phone|email|address):")

while True:
    entry = input()
    if entry.strip().upper() == "DONE":
        break
    contacts.append(entry.strip())

print("\n=== CONTACT DIRECTORY ===\n")

cleaned_contacts = []

for i, contact in enumerate(contacts):
    parts = contact.split('|')

    if len(parts) != 4:
        print(f"Skipping invalid contact {i + 1}")
        continue

    raw_name = parts[0].strip()
    raw_phone = parts[1].strip()
    raw_email = parts[2].strip()
    raw_address = parts[3].strip()

    name_words = raw_name.split()
    clean_name = " ".join([word.title() for word in name_words])
    first_and_middle = " ".join([word.title() for word in name_words[:-1]])
    last_name = name_words[-1].title()

    digits_only = ""
    for char in raw_phone:
        if char.isdigit():
            digits_only += char
    if len(digits_only) == 10:
        clean_phone = f"({digits_only[:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    else:
        clean_phone = "Invalid Phone"

    clean_email = raw_email.lower().replace(" ", "")

    address_parts = raw_address.split()
    fixed_address = []
    for word in address_parts:
        if len(word) == 2 and word.isalpha():
            fixed_address.append(word.upper())  # State abbreviation
        else:
            fixed_address.append(word.title())
    clean_address = " ".join(fixed_address)

    print(f"CONTACT {i + 1}:")
    print(f"Name:     {clean_name}")
    print(f"Phone:    {clean_phone}")
    print(f"Email:    {clean_email}")
    print(f"Address:  {clean_address}\n")

    cleaned_contacts.append({
        "formatted_name": f"{last_name}, {first_and_middle}",
        "phone": clean_phone,
        "email": clean_email
    })

print("=== DIRECTORY SUMMARY ===")
print(f"Total contacts processed: {len(cleaned_contacts)}\n")

print("=== FORMATTED FOR PRINTING ===")
for person in cleaned_contacts:
    print(f"{person['formatted_name']:<28}{person['phone']:<21}{person['email']}")