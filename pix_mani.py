from PIL import Image

def encryption(source,key): #encryption of image
    c_image = source.copy()
    pxls = c_image.load()
    w, h = c_image.size
    for i in range(w):
        for j in range(h):
            r,g,b=pxls[i,j]
            pxls[i,j]=((r^key)+key)%256,((g^key)+key)%256,(key+(b^key))%256
    return c_image

def decryption(enc_image,key):  #decyption of image(reversing the encryption process)
    dec_image = enc_image.copy()
    pxls = dec_image.load()
    w, h = dec_image.size
    for i in range(w):
        for j in range(h):
            r,g,b=pxls[i,j]
            pxls[i, j] = ((r - key) ^ key) % 256, ((g - key) ^ key) % 256, ((b - key) ^ key) % 256
    return dec_image
image_path = r'C:\Users\Admin\Downloads\chikam-transformed.jpeg'
source = Image.open(image_path)
key=int(input("Enter the key: "))
encrypt=encryption(source,key)
encrypt.save('encrypt_img.jpg')
decrypt=decryption(encrypt,key)
decrypt.save('decrypt_img.jpg')

encrypt.show()
decrypt.show()
