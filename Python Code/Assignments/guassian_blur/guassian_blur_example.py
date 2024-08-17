import Blur

gb = Blur.Gaussian_blur()

gb.set_gf([[-1,0,1],[-1,0,1],[-1,0,1]])
gb.blur('data/input.png', 'data/output.png')