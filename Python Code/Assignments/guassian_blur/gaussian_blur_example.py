from FilterApplication import FilterApp
import time

fl = FilterApp()

start_time = time.time()
input_images = "data/input/"
output_images = "data/output/"
fl.start(input_images,output_images,sigmas=[0.5,1.5,2],edge=True)
end_time = time.time()
fl.plot()
print("Total Time Taken :",end_time-start_time)