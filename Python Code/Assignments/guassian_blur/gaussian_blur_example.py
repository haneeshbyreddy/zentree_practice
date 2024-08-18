from Blur import Gaussian_blur

gb = Gaussian_blur()

gb.set_gf([[1,0,-1],[1,0,-1],[1,0,-1]])
gb.blur('data/input.png', 'data/output_1.png')
gb.set_gf([[-1,0,1],[-1,0,1],[-1,0,1]])
gb.blur('data/input.png', 'data/output_2.png')
gb.set_gf([[1,1,1],[0,0,0],[-1,-1,-1]])
gb.blur('data/input.png', 'data/output_3.png')
gb.set_gf([[-1,-1,-1],[0,0,0],[1,1,1]])
gb.blur('data/input.png', 'data/output_4.png')