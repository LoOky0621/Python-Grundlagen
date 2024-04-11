#Übung Seite 80 Teil 1


def steuer(x):
    
    if x > 2500:
        y = 22/100
        summe = x * y
        print("Ihre Steuer beträgt: ", summe)
    else:
        y = 18/100
        summe = x * y
        print("Ihre Steuer beträgt: ", summe)   

steuer(1800)
steuer(2000)
steuer(2500)
steuer(2900)        