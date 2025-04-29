
# ABSOLUTE path to your optix libary
optix_include = "/home/andrew/Downloads/NVIDIA-OptiX-SDK-6.5.0-linux64/include"
optix_ld = "/home/andrew/Downloads/NVIDIA-OptiX-SDK-6.5.0-linux64/lib64"

# cmd to call meshlabserver
meshlabserver_cmd = "/home/andrew/Downloads/MeshLabServer2020.04-linux.AppImage"
# if you are using a headless server, you may need to prepend `DISPLAY=:0`
# meshlabserver_cmd = "DISPLAY=:0 " + meshlabserver_cmd

# choose a directory to exchange temporary mesh file with meshlabserver
tmp_path = "/dev/shm/DR/"

# path to hdf5 file and visual hull mesh
data_path = "/home/andrew/DRT/data/"
result_path = "./result/"

HyperParams = {
    # available model:
    # hand, mouse, monkey, horse, dog, rabbit, tiger, pig
    'name' :  'hand',
    'IOR' : 1.4723,
    'Pass' : 20, # num of optimization stages
    'Iters' : 200, # in each stage

    # loss weight
    "ray_w" : 40,
    "sm_w": 0.08,
    # "sm_w": 0.02,
    "vh_w": 2e-3,

    # optimization parameters
    "momentum": 0.95,
    "start_lr": 0.1,
    "lr_decay": 0.5,
    "start_len": 10, # remesh target length
    "end_len": 1, # remesh target length
    # "end_len": 0.5, 
    'num_view': 72, # used for refraction loss
                }