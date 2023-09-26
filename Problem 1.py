def DecimalToOctal(n):

    octal = [0] * 100
    i = 0
    
    while (n != 0):
        octal[i] = n % 8
        n = int(n / 8)        
        i += 1
 
    for j in range(i - 1, -1, -1):
        print(octal[j], end="")
DecimalToOctal(100)
