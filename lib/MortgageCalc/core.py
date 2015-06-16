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

def get_mortgage_schedule(pmi_required, property_value, percent_annual_interest, mortgage_years,
                          payment_number, pmi_rate, percent_down, pmt, pmi_breakeven):
    intr = 0
    intr_applied = 0
    money_down = property_value * (percent_down/100.0)
    starting_balance = property_value - money_down
    monthly_pmi_pmt = ( starting_balance * pmi_rate )/12
    total_pmi_paid = 0
    total_cost = 0
    pmi_stop = 0
    months_array = []
    starting_balance_array = []
    pmt_array = []
    monthly_pmi_pmt_array = []
    intr_applied_array = []
    intr_array = []
    end_balance_array = []

    for n in range(1, payment_number + 1):
        intr = starting_balance * (percent_annual_interest / (12 * 100.0) )
        intr_applied = pmt - intr
        end_balance = starting_balance - intr_applied

        while end_balance >= (property_value - pmi_breakeven):
            total_pmi_paid += monthly_pmi_pmt
            pmi_stop = n+1
            break

        # Create arrays for Table payment

        months_array.append(n)
        starting_balance_array.append(starting_balance)
        pmt_array.append(pmt)
        monthly_pmi_pmt_array.append(monthly_pmi_pmt + pmt)
        intr_applied_array.append(intr_applied)
        intr_array.append(intr)
        end_balance_array.append(end_balance)

        starting_balance = end_balance
        total_cost += pmt

    mortgage_payment_table = []

    for n in range(0, payment_number ):
        mortgage_payment_table.append({ 'month': months_array[n],
                                        'starting_balance': starting_balance_array[n],
                                        'pmt': pmt_array[n],
                                        'monthly_pmi_pmt': monthly_pmi_pmt_array[n],
                                        'intr_applied': intr_applied_array[n],
                                        'intr': intr_array[n],
                                        'end_balance': end_balance_array[n]
                                      })


    #mortgage_payment_table = [months_array, starting_balance_array, pmt_array, monthly_pmi_pmt_array,
    #                          intr_applied_array, intr_array, end_balance_array] #mortgage schedule table

    return mortgage_payment_table #, pmi_stop, total_cost


