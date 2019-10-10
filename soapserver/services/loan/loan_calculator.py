def loanPayment(principle, rate, payments):
    """
    Calculates loan monthly payment amount.

    Keyword arguments:
    principle -- amount of loan
    rate -- annual rate for the loan
    payments -- total number of monthly payments to be made on the loan
    """
    if payments == 0:
        raise Exception('Payments cannot be zero')

    return round(( rate + rate/( ( (1 + rate)**payments) - 1 ) ) * principle, 2)
