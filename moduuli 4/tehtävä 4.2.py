
tuumat = int(input("Anna tuumat: "))

while tuumat>0:
    cm = (tuumat * 2.54)
    print ("senttimetreinä: " + str(cm))
    tuumat = int(input("Anna tuumat: "))

    if tuumat < 0:
        break