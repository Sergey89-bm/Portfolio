def Int3D(Fun,a1,b1,zz1,a2,b2,zz2,a3,b3,zz3):

    xx = [-0.906179845938664,-0.538469310105683,0.0,0.538469310105683,0.906179845938664]
    w = [0.236926885056189,0.478628670499366,0.568888888888889,0.478628670499366,0.236926885056189]

    dx1=(b1-a1)/zz1
    dx2=(b2-a2)/zz2
    dx3=(b3-a3)/zz3

    Ih1=0.
    x1=a1-dx1
    for l in range(0,zz1):
        x1=x1+dx1
        x2=a2-dx2
        Ci1=0.
        for m in range(0,zz2):
            x2=x2+dx2
            x3=a3-dx3
            S1=0.
            for n in range(0,zz3):
                x3=x3+dx3
                Ii1=0.
                for kk in range(0,5):
                    y1=(2.*x1+dx1)/2.+dx1/2.*xx[kk]
                    y2=(2.*x2+dx2)/2.+dx2/2.*xx[kk]
                    y3=(2.*x3+dx3)/2.+dx3/2.*xx[kk]

                    Ii1=Ii1+w[kk]*Fun(y1,y2,y3)

                S1=S1+Ii1*dx3/2.
            Ci1=Ci1+S1*dx2
        Ih1=Ih1+Ci1*dx1
    return Ih1

def Int2D(Fun,a1,b1,zz1,a2,b2,zz2):

    xx = [-0.906179845938664,-0.538469310105683,0.0,0.538469310105683,0.906179845938664]
    w = [0.236926885056189,0.478628670499366,0.568888888888889,0.478628670499366,0.236926885056189]

    dx1=(b1-a1)/zz1
    dx2=(b2-a2)/zz2
    

    Ih1=0.
    x1=a1-dx1
    for l in range(0,zz1):
        x1=x1+dx1
        x2=a2-dx2
        Ci1=0.
        for m in range(0,zz2):
            x2=x2+dx2
            S1=0.
            for kk in range(0,5):
                y1=(2.*x1+dx1)/2.+dx1/2.*xx[kk]
                y2=(2.*x2+dx2)/2.+dx2/2.*xx[kk]
                S1=S1+w[kk]*Fun(y1,y2)
            Ci1=Ci1+S1*dx2/2
        Ih1=Ih1+Ci1*dx1
    return Ih1
