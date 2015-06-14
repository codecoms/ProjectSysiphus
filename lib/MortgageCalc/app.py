#!/user/bin/python

class main():
    def __init__(self):
        pass


## give total loan
#property_value = 200000
#percent_down = 4.0
#money_down = property_value * (percent_down/100.0)
#principal = property_value - money_down
#loan_to_value = principal/property_value
#percent_annual_interest = 6.5
#mortgage_years = 15
#payment_number = mortgage_years * 12
#
#if percent_down < 20.0:
#	pmi_required = True
#else:
#	pmi_required = False
#
#
#def format_currency(value):
#    return "${:,.2f}".format(value)
#
#def pmt(principal, percent_annual_interest, mortgage_years):
#	monthly_interest = percent_annual_interest/(100 * 12)
#	monthly_payment = principal * ( monthly_interest / (1 - (1 + monthly_interest) ** (- payment_number)))
#	return monthly_payment
#
#def get_pmi_rate(loan_to_value, mortgage_years, pmi_required ):
#	if pmi_required == False:
#		return 0
#	else:
#		if mortgage_years < 25:
#			if loan_to_value <= 0.85:
#				pmi_rate = 0.0030
#			elif loan_to_value <= 0.90 and loan_to_value > 0.85:
#				pmi_rate = 0.0049
#			elif loan_to_value <= 0.95 and loan_to_value > 0.90:
#				pmi_rate = 0.0067
#			elif loan_to_value <= 0.97 and loan_to_value > 0.95:
#				pmi_rate = 0.0110
#			else:
#				pmi_rate = 0
#		else:
#			if loan_to_value <= 0.85:
#				pmi_rate = 0.0035
#			elif loan_to_value <= 0.90 and loan_to_value > 0.85:
#				pmi_rate = 0.0054
#			elif loan_to_value <= 0.95 and loan_to_value > 0.90:
#				pmi_rate = 0.0072
#			elif loan_to_value <= 0.97 and loan_to_value > 0.95:
#				pmi_rate = 0.0115
#			else:
#				pmi_rate = 0
#
#	return pmi_rate
#
#
#
#
#
#
##test
#
#
#pmi_rate = get_pmi_rate(loan_to_value, mortgage_years, pmi_required)
#pmt = pmt(principal, percent_annual_interest, mortgage_years)
#montly_pmi_pmt = ( principal * pmi_rate )/12
#mortgage_months = mortgage_years * 12
#
#print '====== Mortgage Schedule ======'
#starting_balance = principal
#
#print '#  |', '  Start Bal.  |', '   Payment   |', 'Pmt with PMI |' , ' Principal   |', '   Interest |', '   End Bal |', "\n"
#
#for n in range( 1, mortgage_months +1):
#	intr = starting_balance * (percent_annual_interest / (12 * 100.0) )
#	intr_applied = pmt - intr
#	end_balance = starting_balance - intr_applied
#
#	print n,' | ',  format_currency(starting_balance), ' | ', format_currency(pmt), ' | ', format_currency(montly_pmi_pmt + pmt), ' | ', format_currency(intr_applied), ' | ', format_currency(intr), ' | ', format_currency(end_balance), "  | \n"
#
#	starting_balance = end_balance
#
#
#print "\n"
#print ' -------------- Vars -----------------'
#print 'loan to value: ', loan_to_value
#print 'money_down: ', format_currency(money_down)
#print 'principal', format_currency(principal)
#print 'PMI Required: ', pmi_required
#print 'pmi_rate: ', pmi_rate
#print 'Annual Payment: ', format_currency(pmt * 12)
#print 'Montly mortgage Payment: ', format_currency (pmt)
#print 'Annual PMI: ', format_currency(principal * pmi_rate)
#print 'Montly PMI Payment: ', format_currency(montly_pmi_pmt)
#print 'Monltly total payment', format_currency(montly_pmi_pmt + pmt)
#print "------------------------------- \n"
#
#
##total_cost = payment_number * monthly_payment
##total_interest = payment_number * monthly_payment - principal
##print ("Total cost: "), format_currency(total_cost)
##print ("Total Interest: "),  format_currency(total_interest)
##print ("Monthly Payment: "), format_currency(monthly_payment)
