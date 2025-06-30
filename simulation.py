import drone

mA = drone.Motor()
mB = drone.Motor()
mC = drone.Motor()
mD = drone.Motor()
d = drone.Drone(mA, mB, mC, mD)

isRunning = False

while isRunning:
    cmmd, sp = input("Comando: ").split()
    sp = int(sp)
    # Comandos de Movimento

    if cmmd == 't':
        d.thrust(sp)
    elif cmmd == 'y':
        d.yaw(sp)
    elif cmmd == 'r':
        d.roll(sp)
    elif cmmd == 'p':
        d.pitch(sp)

    # Referencia

    elif cmmd == 'pos':
        print(f"{d.pos}")
    elif cmmd == 'rot':
        print(f"{d.rot}")
    elif cmmd == 'a':
        print(f"mFL{d.mFL.a} mFR{d.mFR.a} mBL{d.mBL.a} mBR{d.mBR.a} ")

    # Programa

    elif cmmd == 'q':
        isRunning = False
    else:
        print("Comando nao detectado")

    
