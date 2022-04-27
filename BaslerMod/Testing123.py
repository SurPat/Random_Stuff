import Baslermod as bl

check = bl.BaslerCam()

cap = check.initiate(0)

check.CamRead(cap)
