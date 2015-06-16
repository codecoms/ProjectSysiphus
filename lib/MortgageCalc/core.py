def debug(description, message):
    print("DEBUG:%s> %s\n", description, message)

def format_currency(value):
    return "${:,.2f}".format(value)

def pmt(principal, percent_annual_interest, mortgage_years, payment_number):
    monthly_interest = percent_annual_interest/(100 * 12)
    monthly_payment = principal * ( monthly_interest / (1 - (1 + monthly_interest) ** (- payment_number)))
    return monthly_payment

def get_pmi_rate(loan_to_value, mortgage_years, pmi_required ):
    if pmi_required == False:
        return 0
    else:
        if mortgage_years < 25:
            if loan_to_value <= 0.85:
                pmi_rate = 0.0030
            elif loan_to_value <= 0.90 and loan_to_value > 0.85:
                pmi_rate = 0.0049
            elif loan_to_value <= 0.95 and loan_to_value > 0.90:
                pmi_rate = 0.0067
            elif loan_to_value <= 0.97 and loan_to_value > 0.95:
                pmi_rate = 0.0110
            else:
                pmi_rate = 0
        else:
            if loan_to_value <= 0.85:
                pmi_rate = 0.0035
            elif loan_to_value <= 0.90 and loan_to_value > 0.85:
                pmi_rate = 0.0054
            elif loan_to_value <= 0.95 and loan_to_value > 0.90:
                pmi_rate = 0.0072
            elif loan_to_value <= 0.97 and loan_to_value > 0.95:
                pmi_rate = 0.0115
            else:
                pmi_rate = 0

    return pmi_rate

