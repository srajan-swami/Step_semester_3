def parseInventoryRecord(csvLine):
    fields = csvLine.split(",")

    if len(fields) != 3:
        print("Invalid Record")
    else:
        product = fields[0]
        sku = fields[1]
        quantity = fields[2]

        print("Product:", product, "| SKU:", sku, "| Qty:", quantity)


csvLine = input("Enter inventory record: ")
parseInventoryRecord(csvLine)