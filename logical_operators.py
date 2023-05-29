''''''# if applicant have high income and good credit 
#eligible for loan 

has_high_income= False
has_good_credit= True

if has_high_income and has_good_credit:
    print("eligible for loan")
else: 
    print("not eligible")

'''
'''#logical OR operator
has_high_income= False
has_good_credit= False

if has_high_income or has_good_credit:
    print("eligible for loan")
else: 
    print("not eligible")
    ''''''
#using NOT operator
has_high_income= True
has_criminal_record= False

if has_high_income and not has_criminal_record:
    print("eligible for loan")
else: 
    print("not eligible")
 