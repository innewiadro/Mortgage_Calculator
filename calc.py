from calendar import monthrange

total_interest = 0


def welcome():
    print("Program do szacunkowego licznia długości trwania kredytu oraz ilości odesetek")
    print("=============")


def main_loop():
    credit_amount = int(input("Kwota kredytu?>"))
    funding_fee = int(input("Prowizja za udzielnie kredytu?>"))
    bank_margin = float(input("Marża banku?>"))
    wibor = float(input("wysokość WIBOR?>"))
    loan_rate = bank_margin + wibor
    loan_length = int(input("Długość kredytu w miesiącach?>"))
    first_payoff_year = int(input("Rok rozpoczęcia spłaty?>"))
    first_payoff_month = int(input("Miesiąc rozpczęcia spłaty?>"))
    loan_rate = loan_rate / 100
    total_interest = 0
    print("=============")
    print()
    while credit_amount > 0:

        mortgage_installment = credit_amount * loan_rate / (12 * (1 - (12 / (12 + loan_rate)) ** loan_length))

        for i in range(0, loan_length):

            if first_payoff_month <= 12:
                num_days = monthrange(first_payoff_year, first_payoff_month)[1]

            else:

                first_payoff_month = first_payoff_month % 12
                first_payoff_year = first_payoff_year + 1
                num_days = monthrange(first_payoff_year, first_payoff_month)[1]

            print(f"rata nr. {i + 1} data raty: {first_payoff_year}-{first_payoff_month}")
            first_payoff_month = first_payoff_month + 1
            loan_installment = credit_amount * loan_rate * num_days / 365
            capital_installment = mortgage_installment - loan_installment
            credit_amount = credit_amount - capital_installment

            total_interest = total_interest + loan_installment

            print(
                f"wysokosć raty = {round(mortgage_installment)} rata kapitałowa = {round(capital_installment)} rata odesetkowa = {round(loan_installment)} ")
            print(
                f"pozostała ilość kredytu = {round(credit_amount)} suma zapłaconych odsetek = {round(total_interest)}")
            print("=============")

        if mortgage_installment > credit_amount:
            print("Podsumowanie:")
            total = total_interest + funding_fee + credit_amount
            print(
                f"całkowity koszt kredytu{round(total)}. Wyskokość odesetk {round(total_interest)} prowizja za udzielnie {funding_fee}")
            break


if __name__ == "__main__":
    welcome()
    main_loop()