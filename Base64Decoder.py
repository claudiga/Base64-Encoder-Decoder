import os, codecs, binascii, sys
from  Base64Encoder import flattenList,base64Decimal


def decode(text):

    fo = codecs.open('base64Decode.txt', 'rb+')

    fo.seek(0)
    base64Map = {}

    
    while True:
        decimal = fo.readline()
        if decimal == '':
            break

        bmap = decimal.split(' ')

        dec = bmap[0]
        base64Map[dec] = bmap[1]   

    bytess = []
    for x in range(len(text)):
        charr = base64Map[text[x]]
        if(charr != '64'):
            byt = format(int(charr),'b').zfill(6)
            bytess.append(byt)

    
    bytess = flattenList(bytess)

    size = len(bytess) / 8
    byte8 = []
    p = 0
    for i in range(size):
        curr = ''
        for j in range(8):
            curr = curr + bytess[p]  
            p = p + 1
        byte8.append(curr)
     
    nums = base64Decimal(byte8,128)
    decoded = ''
    for num in nums:
        decoded = decoded + unichr(num)

    return decoded
        
    



            
if __name__ == '__main__':
    dec = decode(sys.argv[1])
    print dec