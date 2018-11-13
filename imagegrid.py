import os
import random
import argparse
import numpy as np
from PIL import Image

def ImageGrid(image_dir, 
              coord_file, 
              nplot=None, 
              is_npy=False,
              save_w=10000, 
              save_h=10000, 
              tile_size=100, 
              random_select=False, 
              red_ch = 0,
              green_ch = 1,
              blue_ch = 2,
              plotfile='image_grid.png'):
    """
    Plot individual images as tiles according to provided coordinates
    """
    
    def Cloud2Grid(coords, gridw, gridh):
        """ convert points into a grid
        """
        nx = coords[:,0]
        ny = coords[:,1]
        nx = nx - nx.min()
        ny = ny - ny.min()
        nx = gridw * nx // nx.max()
        ny = gridh * ny // ny.max()
        nc = np.column_stack((nx, ny))
        return(nc)
        
    # read data
    coords = np.genfromtxt(coord_file, delimiter=',')
    filenames = sorted(os.listdir(image_dir))
    
    # sample files if necessary
    if nplot==None:
       nplot = len(filenames)
    elif nplot < len(filenames):
        if random_select:
            smpl = random.sample(range(len(filenames)), nplot)
        else:
            smpl = [i for i in range(nplot)]
        filenames = [filenames[s] for s in smpl]
        coords = coords[smpl,:]
    
    # min-max tsne coordinate scaling
    for i in range(2):
        coords[:,i] = coords[:,i] - coords[:,i].min()
        coords[:,i] = coords[:,i] / coords[:,i].max()
    
    # convert point cloud to 2d grid
    grid_assignment = Cloud2Grid(coords, gridw=save_w/tile_size, gridh=save_h/tile_size)
    grid_assignment = grid_assignment * tile_size
    
    # paste tiles onto image
    grid_image = Image.new('RGB', (save_w, save_h))
    for img, grid_pos in zip(filenames, grid_assignment):
        x, y = grid_pos
        if is_npy:
            tile = np.load(os.path.join(image_dir, img))[...,[red_ch, green_ch, blue_ch]]
            if tile.dtype == 'float':
                tile = (tile * 255).astype(np.uint8)
            elif tile.dtype == 'int64':
                tile = tile.astype(np.uint8)
            tile = Image.fromarray(tile)
        else:
            tile = Image.open(os.path.join(image_dir, img))
        tile = tile.resize((tile_size, tile_size), Image.ANTIALIAS)
        grid_image.paste(tile, (int(x), int(y)))

    grid_image.save(plotfile)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='scatter images to coordinate pairs')
    parser.add_argument('--image_dir',  type=str, default='images', help='input image directory of png files')
    parser.add_argument('--coord_file', type=str, default='coords.csv', help='coordinate file, csv')
    parser.add_argument('--nplot',      type=int, default=None,  help='number of images to plot')
    parser.add_argument('--is_npy',               default=False,  help='are images saved as npy')
    parser.add_argument('--save_w',     type=int, default=10000, help='pixel width of saved image')
    parser.add_argument('--save_h',     type=int, default=10000, help='pixel height of saved image')
    parser.add_argument('--tile_size',  type=int, default=100,  help='size of tile')
    parser.add_argument('--random_select',        default=False,    help='random choice of images? 1=yes')
    parser.add_argument('--plotfile',   type=str, default='image_grid.png', help='name of output file')
    args = parser.parse_args()
    
    ImageGrid(image_dir  = args.image_dir, 
              coord_file = args.coord_file, 
              nplot      = args.nplot, 
              is_npy     = args.is_npy,
              save_w     = args.save_w, 
              save_h     = args.save_h, 
              tile_size  = args.tile_size, 
              random_select = args.random_select, 
              plotfile   = args.plotfile)

