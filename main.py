from PIL import Image

while True:
    a=input("Enter entire path")
    
    if a.endswith((".jpeg",".jpg",".JPEG",".JPG")):
        l=a.split(".")
        im1=Image.open(a)
        im1.save(l[0]+'.png')
        print("file converted")
        
    elif a.endswith("png"):
        print("File already in png format")
    else:
        print("Wrong file type")
    s=input("do you want to continue?y/n:")
    if s=="n":
        break
    
