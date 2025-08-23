import numpy as np

def otpGenerator():
    otp = np.random.randint(0,9, size =6)
    print(otp)

otpGenerator()
