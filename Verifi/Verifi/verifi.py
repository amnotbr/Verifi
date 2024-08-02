import random

def countCompanyNumber(lowerNum, HigherNum):
    if lowerNum == HigherNum:
        return [lowerNum]
    return list(range(lowerNum, HigherNum + 1))

VISA_START = ["4"]
VISA_LENGTH = [13, 16]

MASTERCARD_START = list(map(str, list(countCompanyNumber(51, 55)))) + list(map(str, list(countCompanyNumber(2221, 2720))))
MASTERCARD_LENGTH = [16]

AMERICANEXPRESS_START = ["34", "37"]
AMERICANEXPRESS_LENGTH = [15]

DISCOVER_START = ["6011"] + list(map(str, list(countCompanyNumber(622126, 622925)))) + list(map(str, list(countCompanyNumber(644,649)))) + ["65"]
DISCOVER_LENGTH = [16]

DINERS_CLUB_INTERNATIONAL_START = ["36", "38"] + list(map(str, list(countCompanyNumber(300,305))))
DINERS_CLUB_INTERNATIONAL_LENGTH = [14]

JCB_START = list(map(str, list(countCompanyNumber(3528,3589))))
JCB_LENGTH = [16]

MAESTRO_START = ["5018", "5020", "5038", "56", "58", "6304", "6759", "6761", "6762", "6763"]
MAESTRO_LENGTH = list(range(12, 20))

UNIONPAY_START = ["62"]
UNIONPAY_LENGTH = list(range(16, 20))

CARTEBLANCHE_START = list(map(str, list(countCompanyNumber(300,305))))
CARTEBLANCHE_LENGTH = [14]

INTERPAYMENT_START = ["636"]
INTERPAYMENT_LENGTH = list(range(16, 20))

LASER_START = ["6304", "6706", "6771", "6709"]
LASER_LENGTH = list(range(16, 20))

RUPAY_START = ["60", "6521", "6522"]
RUPAY_LENGTH = [16]

SOLO_START = ["6334", "6767"]
SOLO_LENGTH = [16, 18, 19]

SWITCH_START = ["4903", "4905", "4911", "4936", "564182", "633110", "6333", "6759"]
SWITCH_LENGTH = [16, 18, 19]

DANKORT_START = ["5019"]
DANKORT_LENGTH = [16]

INSTAPAYMENT_START = list(map(str, list(countCompanyNumber(637, 639))))
INSTAPAYMENT_LENGTH = [16]

UATP_START = ["1"]
UATP_LENGTH = [15]

VOYAGER_START = ["8699"]
VOYAGER_LENGTH = [15]

def createCard(lower_num, max_num):
    LENGTH_OF_NUMBER = random.randint(lower_num, max_num)    
    
    number_list = [str(random.randint(0, 9)) for _ in range(LENGTH_OF_NUMBER)]
    number_string = ''.join(number_list)
        

    return str(number_string)

def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """

    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit
        
    return (sum % 10) == 0
        

def checkCompany(cardNumber):
    cardNumber = str(cardNumber)

    
    # VISA
    if any(cardNumber.startswith(start) for start in VISA_START) and len(cardNumber) in VISA_LENGTH:
        return "VISA"
    
    # MASTERCARD
    if any(cardNumber.startswith(start) for start in MASTERCARD_START) and len(cardNumber) in MASTERCARD_LENGTH:
        return "MASTERCARD"
    
    # AMEX
    if any(cardNumber.startswith(start) for start in AMERICANEXPRESS_START) and len(cardNumber) in AMERICANEXPRESS_LENGTH:
        return "AMERICAN EXPRESS"
    
    # DISCOVER
    if any(cardNumber.startswith(start) for start in DISCOVER_START) and len(cardNumber) in DISCOVER_LENGTH:
        return "DISCOVER"
    
    # DINERS CLUB INTERNATIONAL
    if any(cardNumber.startswith(start) for start in DINERS_CLUB_INTERNATIONAL_START) and len(cardNumber) in DINERS_CLUB_INTERNATIONAL_LENGTH:
        return "DINERS CLUB INTERNATIONAL"
    
    # JCB
    if any(cardNumber.startswith(start) for start in JCB_START) and len(cardNumber) in JCB_LENGTH:
        return "JCB"
    
    # MAESTRO
    if any(cardNumber.startswith(start) for start in MAESTRO_START) and len(cardNumber) in MAESTRO_LENGTH:
        return "MAESTRO"
    
    # UNIONPAY
    if any(cardNumber.startswith(start) for start in UNIONPAY_START) and len(cardNumber) in UNIONPAY_LENGTH:
        return "UNIONPAY"
    
    # CARTE BLANCHE
    if any(cardNumber.startswith(start) for start in CARTEBLANCHE_START) and len(cardNumber) in CARTEBLANCHE_LENGTH:
        return "CARTE BLANCHE"
    
    # INTERPAYMENT
    if any(cardNumber.startswith(start) for start in INTERPAYMENT_START) and len(cardNumber) in INTERPAYMENT_LENGTH:
        return "INTERPAYMENT"
    
    # LASER
    if any(cardNumber.startswith(start) for start in LASER_START) and len(cardNumber) in LASER_LENGTH:
        return "LASER"
    
    # RUPAY
    if any(cardNumber.startswith(start) for start in RUPAY_START) and len(cardNumber) in RUPAY_LENGTH:
        return "RUPAY"
    
    # SOLO
    if any(cardNumber.startswith(start) for start in SOLO_START) and len(cardNumber) in SOLO_LENGTH:
        return "SOLO"
    
    # SWITCH
    if any(cardNumber.startswith(start) for start in SWITCH_START) and len(cardNumber) in SWITCH_LENGTH:
        return "SWITCH"
    
    # DANKORT
    if any(cardNumber.startswith(start) for start in DANKORT_START) and len(cardNumber) in DANKORT_LENGTH:
        return "DANKORT"
    
    # INSTAPAYMENT
    if any(cardNumber.startswith(start) for start in INSTAPAYMENT_START) and len(cardNumber) in INSTAPAYMENT_LENGTH:
        return "INSTAPAYMENT"
    
    # UATP
    if any(cardNumber.startswith(start) for start in UATP_START) and len(cardNumber) in UATP_LENGTH:
        return "UATP"
    
    # VOYAGER
    if any(cardNumber.startswith(start) for start in VOYAGER_START) and len(cardNumber) in VOYAGER_LENGTH:
        return "VOYAGER"
