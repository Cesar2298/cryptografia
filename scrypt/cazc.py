import os
def encrypt(filename,passwd):
    char_ciphered="";y=0
    fsize=os.stat(filename).st_size
    Fr=open(filename,"rb")
    fw=open("new"+filename,"wb+")
    for b in range(fsize):
        char_ciphered=list(Fr.read(1))[0]^(255-ord(passwd[y]))
        y+=1
        if y==len(passwd):y=0
      
        fw.write(bytes([char_ciphered]))
    Fr.close
    fw.close

encrypt("archivo.extencion","py")




