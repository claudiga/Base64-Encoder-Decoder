import os, codecs, sys
size = 0
def getEncoding(text):
    
    fo = codecs.open('base64.txt', 'rb+')

    fo.seek(0)
    base64Map = {}

    
    while True:
        decimal = fo.readline()
        if decimal == '':
            break

        bmap = decimal.split(' ')

        dec = bmap[0]
        base64Map[dec] = bmap[1]

   
    dec = base64Encode(text)

    size = (float(len(text)) * 8) / float(6)
    if size > int(size):
        size = int( size) + 1
    else:
        size = int(size)

    size=  size*8

    if (64 - size) < 64:
        
        padd = 64 - size
        while (padd - 8) >= 0:
            dec.append(64)
            padd = padd - 8
    rv = ''
    for x in dec:
        
        enc =  base64Map[str(x)]
        rv = rv + enc[0]
    
    return rv

def encode(text):
    
    chars = []
    for i in range(len(text)):
        char = ord(text[i])        
        chars.append( format(char,'b').zfill(8))

    return chars

def base64Encode(text):
    
    byte8 = encode(text)

    bytess = float(len(byte8) * 8) 
    base6 =  float(6)


    if (bytess % base6) != 0:

        size = int((bytess / base6)+1) * 6

    else:
        size = int((bytess / base6)) * 6

    seperator = 6
    

    flat_list = flattenList(byte8)
    base6_list =[]
    curr =''
    padding = size - len(flat_list) 
    for x in range(1,size+1):
        
        if x <= (size - padding):
            curr =curr+ flat_list[x-1]
        else: 
            curr = curr + '0'    
        if x != 0 and x % seperator == 0:
            base6_list.append(curr)
            curr =''


 

    return base64Decimal(base6_list,32)
        
def flattenList(list):

    flatList = []
    for innerList in list:

        for bit in innerList:
            flatList.append(bit)
    return flatList


def base64Decimal(list,max):
    init = max
    total = 0
    base64_list = []
    
    for innerlist in list:
        for bit in innerlist:
            bit = int(bit)
            if bit > 0:
                total = total +init
            init = init / 2  
        base64_list.append(total)
        init = max
        total = 0  
    return base64_list





if __name__ == "__main__":
    b64 = getEncoding(sys.argv[1])
    print b64


