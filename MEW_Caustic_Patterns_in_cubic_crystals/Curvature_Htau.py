import numpy as np

def Curv(Gq, Gt, Gf, Gqq, Gtt, Gff, Gtf, Gqt, Gqf, w, q, tq, fq):
    # G... - Функции от w, q, tq, fq
    
    if np.absolute(q) < 1e2: 
        return {'Ampl': np.nan, 'Curvature': np.nan}
    else:

        sub1 = {'q': q, 't_q': tq, 'f_q': fq}

        Gq  = complex(Gq.subs(sub1))
        Gqq = complex(Gqq.subs(sub1))
        Gt  = complex(Gt.subs(sub1)) 
        Gtt = complex(Gtt.subs(sub1)) 
        Gf  = complex(Gf.subs(sub1)) 
        Gff = complex(Gff.subs(sub1))
        Gtf = complex(Gtf.subs(sub1)) 
        Gqt = complex(Gqt.subs(sub1))
        Gqf = complex(Gqf.subs(sub1))

        qt = - Gt/Gq
        qf = - Gf/Gq

        qtt = -(Gqq*qt**2 + 2*Gqt*qt + Gtt)/Gq
        qff = -(Gqq*qf**2 + 2*Gqf*qf + Gff)/Gq
        qtf = -(Gqq*qt*qf + Gqt*qf + Gqf*qt + Gtf)/Gq

        qt_v = np.array([(qt*np.sin(tq) + q*np.cos(tq))*np.cos(fq), (qt*np.sin(tq) + q*np.cos(tq))*np.sin(fq), 
                       qt*np.cos(tq) - q*np.sin(tq)])
        qf_v = np.array([np.sin(tq)*(qf*np.cos(fq) - q*np.sin(fq)), (qf*np.sin(fq) + q*np.cos(fq))*np.sin(tq), 
                       qf*np.cos(tq)])

        qtt_v = np.array([(qtt*np.sin(tq) + 2*qt*np.cos(tq) - q*np.sin(tq))*np.cos(fq),
                        (qtt*np.sin(tq) + 2*qt*np.cos(tq) - q*np.sin(tq))*np.sin(fq),
                        qtt*np.cos(tq) - 2*qt*np.sin(tq) - q*np.cos(tq)])

        qff_v = np.array([(qff*np.cos(fq) - 2*qf*np.sin(fq) - q*np.cos(fq))*np.sin(tq),
                        (qff*np.sin(fq) + 2*qf*np.cos(fq) - q*np.sin(fq))*np.sin(tq), qff*np.cos(tq)])

        qtf_v = np.array([qtf*np.sin(tq)*np.cos(fq) - qt*np.sin(tq)*np.sin(fq) + qf*np.cos(tq)*np.cos(fq) - q*np.cos(tq)*np.sin(fq),
                        qtf*np.sin(tq)*np.sin(fq) + qt*np.sin(tq)*np.cos(fq) + qf*np.cos(tq)*np.sin(fq) + q*np.cos(tq)*np.cos(fq),
                        qtf*np.cos(tq) - qf*np.sin(tq)])

        n_v = np.array([qt_v[1]*qf_v[2] - qt_v[2]*qf_v[1], 
                      qt_v[2]*qf_v[0] - qt_v[0]*qf_v[2], qt_v[0]*qf_v[1] - qt_v[1]*qf_v[0]])

        E = np.absolute(qt)**2 + np.absolute(q)**2
        G = np.absolute(qf)**2 + np.absolute(q)**2*np.sin(tq)*np.sin(tq)
        F = qt*np.conjugate(qf)

        I = E*G - np.absolute(F)**2

        L = np.vdot(qtt_v, n_v)/np.sqrt(I)
        M = np.vdot(qtf_v, n_v)/np.sqrt(I)
        N = np.vdot(qff_v, n_v)/np.sqrt(I)

        # Curvature and amlification factor
        K = (L*N - M**2)/I
        cosVq = -1/np.sqrt(1 + (qt/q)**2 + (qf/q/np.sin(tq))**2)
        Ampl = np.absolute(cosVq/(K*q*q))

        return {'Ampl': Ampl, 'Curvature': K}