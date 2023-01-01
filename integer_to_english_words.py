def numberToWords(num):
    num_val = { 0 : '', 1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five',
          6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine',
          10 : 'Ten', 11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen',
          15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen', 19 : 'Nineteen',
          20 : 'Twenty', 30 : 'Thirty', 40 : 'Forty', 50 : 'Fifty', 60 : 'Sixty',
          70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninety' }
    def num_0_99(num, n):
        if num % 10 == 0 or 11 <= num < 20:
            return num_val[num]
        else:
            return num_val[num // 10 * n] + ' ' + num_val[num % n]
    def num_hundred(num):
        if num % 100 == 0:
            return num_val[num // 100] + ' Hundred'
        else:
            if num // 100 == 0:
                return num_0_99(num % 100, 10).strip() 
            else:
                return num_val[num // 100] + ' Hundred ' + num_0_99(num % 100, 10).strip() 
    def num_ten_thousand(num):
        if num % 1000 == 0:
            return num_val[num // 1000] + ' Thousand'
        else:
            return num_0_99(num // 1000, 10).strip() + ' Thousand ' + num_hundred(num % 1000)
    def num_thousand(num):
        if num % 100000 == 0 or num % 1000 == 0:
            return num_hundred(num // 1000) + ' Thousand'
        elif num // 1000 == 0:
            return num_hundred(num % 1000)
        else:
            return num_hundred(num // 1000) + ' Thousand ' + num_hundred(num % 1000)
    
    def num_million(num):
        if num % 10**7 == 0:
            return num_hundred(num // 10**6) + ' Million'
        elif num // 10**6 == 0:
            return num_thousand(num % 10**6)
        elif num % 10**6 == 0:
            return num_hundred(num // 10**6) + ' Million'
        else:
            return num_hundred(num // 10**6) + ' Million ' + num_thousand(num % 10**6)
    if num == 0:
        return 'Zero'

    if 0 < num < 20:
        return num_val[num]

    if 20 <= num < 100:
        return num_0_99(num, 10)

    if num < 1000:
        return num_hundred(num)

    if num < 100000:
        return num_ten_thousand(num)

    if num < 1000000:
        return num_thousand(num)

    if num < 10**8:
        if num % 10**6 == 0:
            return num_val[num // 10**6] + ' Million'
        else:
            return num_0_99(num // 10**6, 10) + ' Million ' + num_thousand(num % 10**6)
            
    if num < 10**9:
        return num_million(num)
    
    if num < 10**11:
        if num % 10**9 == 0:
            return num_val[num // 10**9] + ' Billion'
        else:
            return num_val[num // 10**9] + ' Billion ' + num_million(num % 10**9)
    
    if num < 10**12:
        if num % 10**10 == 0:
            return num_val[num // 10**9] + ' Billion'
        elif num % 10**9 == 0:
            return num_hundred(num // 10**9) + ' Billion'
        else:
            return num_hundred(num // 10**9) + ' Billion ' + num_million(num % 10**9)
    return 

print(numberToWords(123456789771))
print(numberToWords(1000000001))
print(numberToWords(105389700))
print(numberToWords(123))

