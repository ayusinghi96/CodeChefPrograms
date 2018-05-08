a = list(map(float,input().split()))
if a[0] <= 2000 and a[0] > 0:
    if a[1] >= 0 and a[1] <= 2000:
        if a[0]%5 == 0:
            if a[0] <= (a[1]-0.50):
                a[1] = a[1] -(a[0]+0.50)
## for taking output up to decimal places use " %.2f"
                print ("%.2f" % a[1])
            else:
                print ("%.2f" % a[1])
        else:
            print ("%.2f" % a[1])
