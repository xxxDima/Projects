import base64


photo = open('C:\\Users\\USER\\PycharmProjects\\pythonProject1\\График.png', "rb")
binar_photo = base64.b64encode(photo.read())
print(binar_photo)
