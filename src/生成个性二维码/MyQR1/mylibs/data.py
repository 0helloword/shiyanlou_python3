from constant import char_cap,required_bytes,mindex,lindex,num_list,alphanum_list,grouping_list,mode_indicator


#ecl:Error Correction Level(L,M,Q,H)

def encode(ver,ecl,str):
    mode_encoding={
        'numeric':numeric_encoding,
        'alphanumeric':alphanumeric_encoding,
        'byte':byte_encoding,
        'kanji':kanji_encoding
                   }

    ver,mode=analyse(ver,ecl,str)
    print(ver,mode)
    print('line 16:mode:',mode)

    code=mode_indicator[mode]+get_cci(ver,mode,str)+mode_encoding[mode](str)
#     print(code)
    #add a terminator
    rqbits=8*required_bytes[ver-1][lindex[ecl]]
#     print(rqbits)#2192
    b=rqbits-len(code)#2169  len(code)=23
    code+='0000' if b>=4 else '0'*b
#     print(code)
    
    #make the length a multiple of 8
    while len(code)%8!=0:
        code+='0'
    print(code)    
    
    #add pad bytes if the string is still too short
    while len(code)<rqbits:
        code+='1110110000010001' if rqbits-len(code)>=16 else '11101100'#???
#     print(code)
    data_code=[code[i:i+8] for i in range(len(code)) if i%8==0]#分隔为8位一个字符串
#     print(data_code)
    data_code=[int(i,2) for i in data_code]#2进制转为10进制
#     print(data_code)
    
    g=grouping_list[ver-1][lindex[ecl]]
#     print(g)
    data_codewords,i=[],0
    for n in range(g[0]):
        data_codewords.append(data_code[i:i+g[1]])
        i+=g[1]
    for n in range(g[2]):
        data_codewords.append(data_code[i:i+g[3]])
        i+=g[3]
    print(ver,data_codewords)
    return ver,data_codewords
    
def analyse(ver,ecl,str):#分析str采用哪种方式进行编码，并返回ver和mode
    if all(i in num_list for i in str):
        mode='numeric'
    elif all(i in alphanum_list for i in str):
        mode='alphanumeric'
    else:
        mode='byte'
    m=mindex[mode]#获取mode的值，'numeric':0,'alphanumeric':1,'byte':2,'kanji':3
    l=len(str)
    for i in range(40):
        if char_cap[ecl][i][m]>l:
            ver=i+1 if i+1>ver else ver
            break
    return ver,mode
     


def numeric_encoding(str):#对纯数字的字符串格式编码
    str_list=[str[i:i+3] for i in range(0,len(str),3)]
    code=''
    for i in str_list:
        rqbin_len=10
        if len(i)==1:
            rqbin_len=4
        elif len(i)==2:
            rqbin_len=7
        code_temp=bin(int(i))[2:]#十进制转二进制，去掉前两位的0b标识
#         print(int(i))
#         print(bin(int(i)))
#         print(code_temp)
        code+=('0'*(rqbin_len-len(code_temp))+code_temp)#不足10位前面补0
    return code

def alphanumeric_encoding(str):#对字符串中所有元素都在alphanum_list（数字+大写字母+特殊符号）内的字符串格式编码
    code_list=[alphanum_list.index(i) for i in str]#index()方法检测字符串中是否包含子字符串 str,包含子字符串则返回开始的索引值
    print(code_list)
    code=''
    for i in range(1,len(code_list),2):
        c=bin(code_list[i-1]*45+code_list[i])[2:]#十进制转二进制，去掉前两位的0b标识
        c='0'*(11-len(c))+c#不足11位前面补0
        code+=c
        if i!=len(code_list)-1:
            c=bin(code_list[-1])[2:]
            c='0'*(6-len(c))+c
            code+=c
        return code
    
def byte_encoding(str):#对字符串中的单个字节进行编码
    code=''
    for i in str:
        c=bin(ord(i.encode('iso-8859-1')))[2:]#ord函数以一个字符作为参数，返回对应的 ASCII数值
        c='0'*(8-len(c))+c
        code+=c
    return code

def kanji_encoding(str):
    pass

# if __name__=='__main__':
#     s='123456789'
#     v,datacode=encode(1,'H',s)
#     print(v,datacode)   

#cci:character count indicator
def get_cci(ver,mode,str):
    if 1<=ver<=9:
        cci_len=(10,9,8,8)[mindex[mode]]
    elif 10<=ver<=26:
        cci_len=(12,11,16,10)[mindex[mode]]
    else:
        cci_len=(14,13,16,12)[mindex[model]]

    cci=bin(len(str))[2:]
    cci='0'*(cci_len-len(cci))+cci
    return cci

str='1a'
a=encode(10,'L',str)
