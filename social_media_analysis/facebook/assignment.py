import random

def random_order_generator():
    x=[chr(i) for i in range(65,65+26)] # alphabet in alphabetical order
    secret_order=''                     # alphabet not in alphabetical order
    while (len(x)!=0):
        letter=random.choice(x)         # select random char from remaining charactors in x
        x.remove(letter)                # remove the taken one from x
        secret_order+=letter
    return secret_order                 

def encrypt_function_generator():           # Ths function creates a encrypt function
    secret_order=random_order_generator()   # Get random order of characters
    encrypt_funtion={}                      # Dictionary whitch matches char
    for i in range(26):
        encrypt_funtion[chr(65+i)]=secret_order[i]
    return encrypt_funtion

def file_encrypter(input_file_path, output_file_path):
    f=open(input_file_path,'r')
    plaintext=f.read()
    encrypt_function=encrypt_function_generator()
    ciphertext=''
    for i in plaintext:
        if (i.capitalize()>='A' and i.capitalize()<='Z' ):
            ciphertext+=encrypt_function[i.capitalize()]
            
        else:
            ciphertext+=i
    
    ff=open(output_file_path,'w')
    ff.write(ciphertext)
    print ('encrypt_function')
    print (encrypt_function)

def frequency_finder(path):
    f=open(path,'r')
    data=f.read()
    freq={ chr(i):0 for i in range(65,65+26) }
    for i in data:
        if (i.capitalize() in freq):
            freq[i.capitalize()]+=1
    freq={k: v for k, v in sorted(freq.items(), key=lambda item: item[1])}
    freq_val=[val for key, val in freq.items()][::-1]
    freq_key=[key for key, val in freq.items()][::-1]

    return (freq_key,freq_val)

def decrypt_function_finder(plaintext_file,ciphertext_file):
    (plaintext_freq_char,plaintext_freq_count)=frequency_finder(plaintext_file)
    (ciphertext_freq_char,ciphertext_freq_count)=frequency_finder(ciphertext_file)

    print(plaintext_freq_char[:5])
    print (plaintext_freq_count[:5])
    print(ciphertext_freq_char[:5])
    print (ciphertext_freq_count[:5])

    decrypt_function={}
    for i in range(5):
        decrypt_function[ciphertext_freq_char[i]]=plaintext_freq_char[i]
    return decrypt_function

def replace_decrypted_characters(decrypt_function,input_file_path,output_file_path):
    f=open(input_file_path,'r')
    data=f.read()
    output=''
    for i in data:
        if (i in decrypt_function):
            output+=decrypt_function[i]
        else:
            output+=i
    ff=open(output_file_path,'w')
    ff.write(output)


file_encrypter("C:/Users/Dane/Desktop/data.txt","C:/Users/Dane/Desktop/encrypted.txt")

decrypt_function=decrypt_function_finder("C:/Users/Dane/Desktop/data.txt","C:/Users/Dane/Desktop/encrypted.txt")

replace_decrypted_characters(decrypt_function,"C:/Users/Dane/Desktop/encrypted.txt","C:/Users/Dane/Desktop/decrypted.txt")