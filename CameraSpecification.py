from pyflycap2.interface import Camera

cam_serial = 12345678  
print(cam_serial)
c = Camera(serial=cam_serial, context_type=context_type)
# c = Camera(guid=guid, context_type=context_type)
# c = Camera(index=0, context_type=context_type)

c.connect()
c.start_capture()

c.read_next_image()
frame = c.get_current_image()
print(frame.keys())

#Get frame information
for key in frame.keys():
    if key == 'buffer': continue
    print(key, frame[key])
