import Verifi
import time

while 1:
    # create card number
    ccn = Verifi.createCard(16,16)
    # check if the card passes the luhn's algorithm
    luhnCheck = Verifi.cardLuhnChecksumIsValid(ccn)

    # check the company
    comp = Verifi.checkCompany(ccn)

    #print(luhnCheck)

    if luhnCheck and comp == "VISA":
        print(f"Card: {ccn} from company {comp}")
        time.sleep(1)


#if comp is not None and luhnCheck:
#    print(f"COMPANY: {comp}, CARDNUMBER: {ccn}")
#else:
#    pass