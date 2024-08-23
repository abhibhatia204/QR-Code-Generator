import qrcode
a=input("Enter the link : ")
features=qrcode.QRCode(version=1,box_size=40,border=3)
features.add_data(a)
features.make(fit=True)
generate_image=features.make_image(fill_color="blue",back_color="white")
generate_image.save('image3.png')