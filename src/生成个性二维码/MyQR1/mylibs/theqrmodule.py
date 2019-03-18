#-*-coding:utf-8-*-
import data,ECC
#ver:version from 1 to 40
#ecl:error correction level(L,M,Q,H)
#get a qrcode picture of 3*3 pixels per Module

def get_qrcode(ver,ecl,str,save_place):
    #data coding
    ver,data_codewords=data.encode(ver,ecl,str)
    
    #error correction coding
    ecc=ECC.encode(ver,ecl,data_codewords)
    
    #structure final bits
    final_bits=structure.structure_final_bits(ver,ecl,data_codewords,ecc)
    
    #get the qr matrix
    qrmatrix=matrix.get_qrmatrix(ver,ecl,final_bits)
    
    #draw the picture and save it ,then return the real ver and the absolute Name
    return ver,draw.draw_qrcode(save_place,qrmatrix)

get_qrcode(1,'L','123','source/')