import pandas as pd
import numpy as np

def Save_to_Files(th,Ar,Kc,qt,qf,qtt,qff,qtf,I1,II1):
    df = pd.DataFrame(data=np.real(Kc), columns =["Re(K_1)", "Re(K_2)", "Re(K_3)", "Re(K_4)"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Re_Curvature.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.imag(Kc), columns =["Im(K_1)", "Im(K_2)", "Im(K_3)", "Im(K_4)"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Im_Curvature.csv", sep='\t',index=False)

    df = pd.DataFrame(data=Ar, columns =["A_1", "A_2", "A_3", "A_4"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Ampl_Factor_.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.real(qt), columns =["Re(qt_1)", "Re(qt_2)", "Re(qt_3)", "Re(qt_4)"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Re_qt.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.real(qf), columns =["Re(qf_1)", "Re(qf_2)", "Re(qf_3)", "Re(qf_4)"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Re_qf.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.imag(qt), columns =["Im(qt_1)", "Im(qt_2)", "Im(qt_3)", "Im(qt_4)"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Im_qt.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.imag(qf), columns =["Im(qf_1)", "Im(qf_2)", "Im(qf_3)", "Im(qf_4)"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Im_qf.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.real(qtt), columns =["1", "2", "3", "4"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Re_qtt.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.imag(qtt), columns =["1", "2", "3", "4"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Im_qtt.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.real(qff), columns =["1", "2", "3", "4"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Re_qff.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.imag(qff), columns =["1", "2", "3", "4"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Im_qff.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.real(qtf), columns =["1", "2", "3", "4"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Re_qtf.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.imag(qtf), columns =["1", "2", "3", "4"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Im_qtf.csv", sep='\t',index=False)

    df = pd.DataFrame(data=I1, columns =["1", "2", "3", "4"])
    df.insert(0, "theta", th)
    df.to_csv("Data\First_Form.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.real(II1), columns =["1", "2", "3", "4"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Re_Second_Form.csv", sep='\t',index=False)

    df = pd.DataFrame(data=np.imag(II1), columns =["1", "2", "3", "4"])
    df.insert(0, "theta", th)
    df.to_csv("Data\Im_Second_Form.csv", sep='\t',index=False)