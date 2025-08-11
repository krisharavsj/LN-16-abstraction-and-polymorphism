class DueAmount:
    def __init__(self, total_bill: float, amount_paid: float):
        if total_bill < 0 or amount_paid < 0:
            raise ValueError("Amounts must be non-negative")
        self.total_bill = total_bill
        self.amount_paid = amount_paid

    def due(self) -> float:
        return max(self.total_bill - self.amount_paid, 0.0)

def main():
    try:
        bill = float(input("Enter the total bill amount").strip())
        paid = float(input("Enter the amount paid").strip())
        customer = DueAmount(bill, paid)
        print(f"Total bill{bill:.2f}")
        print(f"Amount paid{paid:.2f}")
        print(f"Amount due{customer.due():.2f}")
    except ValueError as e:
        print("Error", e)

if __name__ == "__main__":
    main()
