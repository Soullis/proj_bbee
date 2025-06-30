speed = 0.1

class Drone():
    def __init__(self, mFL, mFR, mBR, mBL):
        self.pos = [400, 0, 300] # [x, y, z]
        self.rot = 0 # [x, y, z]
        self.mFL = mFL
        self.mFR = mFR
        self.mBL = mBL
        self.mBR = mBR

    def sum_all(self):
        return self.mFL.t + self.mFR.t + self.mBL.t + self.mBR.t
    
    def dFandB(self):
        return - self.mFL.t - self.mFR.t + self.mBL.t + self.mBR.t
    
    def dLandR(self):
        return self.mFL.t - self.mFR.t + self.mBL.t - self.mBR.t
    
    def dCross(self):
        return self.mFL.t - self.mFR.t - self.mBL.t + self.mBR.t

    def update_pos(self):
        if self.dLandR() != 0:
            self.pos[0] += speed*self.dLandR()
        if self.sum_all() != 0:
            self.pos[1] += speed*self.sum_all()
        if self.dFandB() != 0:
            self.pos[2] += speed*self.dFandB()
        if self.dCross() != 0:
            self.rot += speed*self.dCross()
            self.rot = self.rot%360

    def print_mob(self):
        print()
        print(self.mFL.t + self.mFR.t + self.mBL.t + self.mBR.t)
        print(- self.mFL.t - self.mFR.t + self.mBL.t + self.mBR.t)
        print(self.mFL.t - self.mFR.t + self.mBL.t - self.mBR.t)
        print(self.mFL.t - self.mFR.t - self.mBL.t + self.mBR.thub)


    # MMA

    # def thrust(self, a=1):
    #     self.mFL.a = a
    #     self.mFR.a = a
    #     self.mBL.a = a
    #     self.mBR.a = a
    #     self.update_pos()

    # def yaw(self, a=1):
    #     self.mFL.a = -a
    #     self.mFR.a = a
    #     self.mBL.a = a
    #     self.mBR.a = -a
    #     self.update_pos()

    # def roll(self, a=1):
    #     self.mFL.a = a
    #     self.mFR.a = -a
    #     self.mBL.a = a
    #     self.mBR.a = -a
    #     self.update_pos()

    # def pitch(self, a=1):
    #     self.mFL.a = -a
    #     self.mFR.a = -a
    #     self.mBL.a = a
    #     self.mBR.a = a
    #     self.update_pos()

    def throttle(self, a=1):
        self.mFL.t += a
        self.mFR.t += a
        self.mBL.t += a
        self.mBR.t += a
        self.update_pos()

    def yaw(self, a=1):
        self.mFL.y -= a
        self.mFR.y += a
        self.mBL.y += a
        self.mBR.y -= a
        self.update_pos()

    def roll(self, a=1):
        self.mFL.t += a
        self.mFR.t -= a
        self.mBL.t += a
        self.mBR.t -= a
        self.update_pos()

    def pitch(self, a=1):
        self.mFL.t -= a
        self.mFR.t -= a
        self.mBL.t += a
        self.mBR.t += a
        self.update_pos()
    

class Motor():
    def __init__(self):
        self.t = 0
        self.y = 0

