def create_report():
    f = open('sales-report.txt')
    sales_report = {}

    for line in f:
        line = line.rstrip()
        entries = line.split('|')
        salesperson = entries[0]
        melons = int(entries[2])

        if salesperson in sales_report:
            existing_melons = sales_report.get(salesperson)
            new_melons = existing_melons + melons
            sales_report[salesperson] = new_melons
        else:
            sales_report[salesperson] = melons
    return sales_report


def generate_report():
    sales_report = create_report()

    for key, value in sales_report.items():
        print(f"{key} sold {value} melons")
    return


if __name__ == "__main__":
    generate_report()
