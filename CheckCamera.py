from pyflycap2.interface import CameraContext

context_type = 'IIDC' 

cc = CameraContext(context_type)
print('Num. of cameras:', cc.get_num_cameras())