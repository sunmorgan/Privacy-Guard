import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
licenseCascade = cv2.CascadeClassifier("mscarplates.xml")
dsCascade = cv2.CascadeClassifier("dscanner.xml")

def blur():
    imginput = input("Enter the image you want to blur: ")
    img = cv2.imread(imginput)

    faces = faceCascade.detectMultiScale(img, 1.1, 4)

    for detect in faces:
        x, y, w, h = detect

        img[y:y+h, x:x+w] = cv2.GaussianBlur(img[y:y+h, x:x+w], (127, 127), 0)
        cv2.rectangle(img, (x, y,), (x+w, y+h), (50, 255, 100), 2)

    cv2.imshow("Blurred Output", img)

    cv2.waitKey(0)
        

def license():
    imginput = input("Enter the image you want to blur: ")
    img = cv2.imread(imginput)

    licence = licenseCascade.detectMultiScale(img, 1.1, 4)

    for detect in licence:
        x, y, w, h = detect

        img[y:y+h, x:x+w] = cv2.GaussianBlur(img[y:y+h, x:x+w], (555, 555), 0)
        cv2.rectangle(img, (x, y,), (x+w, y+h), (50, 255, 100), 2)

    cv2.imshow("Blurred Output", img)

    cv2.waitKey(0)

def documentScan():
    imginput = input("Enter the image you want to blur: ")
    img = cv2.imread(imginput)

    document = dsCascade.detectMultiScale(img, 1.1, 4)

    for detect in document:
        x, y, w, h = detect

        img[y:y+h, x:x+w] = cv2.GaussianBlur(img[y:y+h, x:x+w], (555, 555), 0)
        cv2.rectangle(img, (x, y,), (x+w, y+h), (50, 255, 100), 2)

    cv2.imshow("Blurred Output", img)

    cv2.waitKey(0)

keepgo = 1

while keepgo < 2:
    choose = input('1. Blur Faces\n2. Blur Car Plates\n3. Document Scanner\n4. Exit\n')

    if choose=='1':
        blur()
    elif choose=='2':
        license()
    elif choose=='3':
        documentScan()
    else:
        quit()


