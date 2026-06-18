import csv
from collections import defaultdict


def main():
    try:

        sales_file = "data/sales_data.csv"
        summary_file = "data/sales_summary.csv"

        total_sales = 0
        category_sales = defaultdict(float)
        product_sales = defaultdict(float)

        valid_records = 0
        invalid_records = 0

        with open(sales_file, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:

                try:

                    if (
                        not row["Product"]
                        or not row["Quantity"]
                        or not row["Price"]
                    ):
                        invalid_records += 1
                        continue

                    quantity = int(row["Quantity"])
                    price = float(row["Price"])

                    sale_amount = quantity * price

                    total_sales += sale_amount

                    category_sales[
                        row["Category"]
                    ] += sale_amount

                    product_sales[
                        row["Product"]
                    ] += sale_amount

                    valid_records += 1

                except ValueError:
                    invalid_records += 1

        top_product = max(
            product_sales,
            key=product_sales.get
        )

        with open(
            summary_file,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow(
                ["Metric", "Value"]
            )

            writer.writerow(
                ["Total Sales", total_sales]
            )

            writer.writerow(
                ["Top Selling Product", top_product]
            )

            writer.writerow(
                ["Valid Records", valid_records]
            )

            writer.writerow(
                ["Invalid Records", invalid_records]
            )

            for category, amount in category_sales.items():
                writer.writerow(
                    [f"{category} Sales", amount]
                )

        print("\nSales Summary")
        print("------------------")
        print(
            f"Total Sales: ${total_sales}"
        )
        print(
            f"Top Product: {top_product}"
        )

    except FileNotFoundError:
        print("Sales file not found.")

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
