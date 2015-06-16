#!/user/bin/python

from MortgageCalc import core

class main():
    def __init__(self):
        pass

    def run(self, argv):

        __author__ = 'Federico'

        # Must have data

        property_value = 270000
        percent_annual_interest = 4.9
        mortgage_years = 30
        percent_down = 20.0

        #Derived data

        pmi_breakeven = property_value * 0.2
        money_down = property_value * (percent_down/100.0)
        principal = property_value - money_down
        loan_to_value = principal/property_value
        payment_number = mortgage_years * 12

        if percent_down < 20.0:
            pmi_required = True
        else:
            pmi_required = False
            pmi_stop = 0

        pmi_rate = core.get_pmi_rate(loan_to_value, mortgage_years, pmi_required)

        pmt = core.pmt(principal, percent_annual_interest, mortgage_years, payment_number)

        montly_pmi_pmt = ( principal * pmi_rate )/12
        mortgage_months = mortgage_years * 12

        #Mortgage schedule printout

        print '====== Mortgage Schedule ======'
        print
        starting_balance = principal
        total_pmi_paid = 0
        total_cost = 0
        starting_balance_array = []
        pmt_array = []
        montly_pmi_pmt_array = []
        intr_applied_array = []
        intr_array = []
        end_balance_array = []

        print("%4s | %13s | %13s | %13s | %13s | %13s | %13s" %
                ("#", "Start Bal.", "Payment", "Pmt with PMI", "Principal", "Interest", "End Bal"))

        print("-" * 100)

        for n in range(1, mortgage_months + 1):
            intr = starting_balance * (percent_annual_interest / (12 * 100.0) )
            intr_applied = pmt - intr
            end_balance = starting_balance - intr_applied

            while end_balance >= (property_value - pmi_breakeven):
                total_pmi_paid += montly_pmi_pmt
                pmi_stop = n+1
                break

            print("%4s | %13s | %13s | %13s | %13s | %13s | %13s" %
                   (n, core.format_currency(starting_balance),
                   core.format_currency(pmt),
                   core.format_currency(montly_pmi_pmt + pmt),
                   core.format_currency(intr_applied),
                   core.format_currency(intr),
                   core.format_currency(end_balance)))

            # Create arrays for Table payment

            starting_balance_array.append(starting_balance)
            pmt_array.append(pmt)
            montly_pmi_pmt_array.append(montly_pmi_pmt + pmt)
            intr_applied_array.append(intr_applied)
            intr_array.append(intr)
            end_balance_array.append(end_balance)

            starting_balance = end_balance
            total_cost += pmt

        mortgage_payment_table = [starting_balance_array, pmt_array, montly_pmi_pmt_array,
                                  intr_applied_array, intr_array, end_balance_array] #mortgage schedule table

        #Variables Printouts

        print "\n"
        print '-------------- Mortgage Info-----------------'
        print 'Principal', core.format_currency(principal)
        print 'Money down: ', core.format_currency(money_down)
        print 'PMI breakeven 20%: ', core.format_currency(pmi_breakeven - money_down)
        print 'PMI Required: ', pmi_required
        print 'Loan-to-Value ratio: ', loan_to_value
        print 'PMI Rate: ', (pmi_rate * 100),'%'
        print "----------------------------------------------\n"

        print '--------------- Payment Info -----------------'
        print 'Total cost of the loan', core.format_currency(total_cost)
        print 'Total Intrest Paid', core.format_currency(n * pmt - principal)
        print 'Annual Mortgage Payment: ', core.format_currency(pmt * 12)
        print 'Annual PMI: ', core.format_currency(principal * pmi_rate)
        print 'Montly mortgage Payment: ', core.format_currency (pmt)
        print 'Montly PMI Payment: ', core.format_currency(montly_pmi_pmt)
        print 'Monltly payment', core.format_currency(montly_pmi_pmt + pmt)
        print 'PMI Stop Payment at year: ', round(pmi_stop / 12)
        print "----------------------------------------------\n"
