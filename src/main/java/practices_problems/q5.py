def normalizeReference(raw):
    reference = raw.strip()

    if len(reference) < 3:
        return reference

    bankCode = reference[:3].upper()
    rest = reference[3:]

    return bankCode + rest


def validateAndFormat(reference):
    if len(reference) != 14:
        return "Invalid: wrong length"

    for i in range(3):
        if not reference[i].isalpha():
            return "Invalid: bank code must be 3 letters"

    for i in range(3, 14):
        if not reference[i].isdigit():
            return "Invalid: body must contain only digits"

    bankCode = reference[:3]
    date = reference[3:9]
    sequence = reference[9:]

    formattedDate = date[:2] + "/" + date[2:4] + "/" + date[4:6]

    result = "[" + bankCode + "] DATE: " + formattedDate + " | SEQ: " + sequence

    return result


rawReference = input("Enter transaction reference: ")

normalizedReference = normalizeReference(rawReference)
result = validateAndFormat(normalizedReference)

print(result)