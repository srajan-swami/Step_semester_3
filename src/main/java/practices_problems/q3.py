def validateFileExtension(filename):
    lastDot = filename.rfind(".")

    if lastDot == -1:
        print("Rejected — invalid file type")
        return

    extension = filename[lastDot + 1:].lower()

    if extension == "pdf" or extension == "docx" or extension == "zip":
        print("Accepted")
    else:
        print("Rejected — invalid file type")


filename = input("Enter filename: ")

validateFileExtension(filename)