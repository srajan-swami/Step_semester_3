def normalizeCode(raw):
    code = raw.strip()

    if len(code) < 3:
        return code

    publisherCode = code[:3].upper()
    rest = code[3:]

    return publisherCode + rest


def validateAndFormat(code):
    if len(code) != 13:
        return "Invalid: wrong length"

    for i in range(3):
        if not code[i].isalpha():
            return "Invalid: publisher code must be 3 letters"

    for i in range(3, 13):
        if not code[i].isdigit():
            return "Invalid: body must contain only digits"

    publisherCode = code[:3]
    year = code[3:7]
    catalog = code[7:13]

    result = "[" + publisherCode + "] YEAR: " + year + " | CATALOG: " + catalog

    return result


rawCode = input("Enter ISBN code: ")

normalizedCode = normalizeCode(rawCode)
result = validateAndFormat(normalizedCode)

print(result)