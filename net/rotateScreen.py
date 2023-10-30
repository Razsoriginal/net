import time, rotatescreen as rs

disp = rs.get_primary_display()
angle_list = [90, 180, 270, 0]
for i in range(2):
    for x in angle_list:
        disp.rotate_to(x)
        time.sleep(5)