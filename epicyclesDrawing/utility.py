import cmath
def functionPoints(filename = 'batcurve.txt'):
    points = []
    with open(filename) as bat:
        for lines in bat:
            line = bat.readline()
            #print(line)
            #now separate x coords and y coords
            if(line != '\n'):
                l =  line.split(',')
                point = [float(l[0]),float(l[1])]
                #print(point[0],point[1])
                points.append(point)

    #print(points)

    averageX = 0
    averageY = 0
    for i in range(len(points)):
        points[i][0] = points[i][0]/100
        points[i][1] = points[i][1]/100
        averageX += points[i][0]
        averageY += points[i][1]

    averageX = averageX/len(points)
    averageY = averageY/len(points)

    print(averageX,averageY)
    for i in range(len(points)):
        points[i][0] =(averageX - points[i][0])
        points[i][1] =(averageY - points[i][1])

    #print(points)
    return points

#functionPoints()
def dft(points):
    coeffs = []
    for k in range(len(points)):
        cof = 0
        for n in range(len(points)):
            cof += (points[n][0] + points[n][1]*1j)*cmath.exp((-1j*2* cmath.pi*k*n )/len(points))

        #print(cof)
        coeffs.append(cof/len(points))
    
    return coeffs

#points = functionPoints()
#print(points)
#coefficients = dft(points)
#print(coefficients)
