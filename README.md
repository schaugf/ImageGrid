# ImageGrid

Create a grid of images from a coordinate file and set of corresponding images.

## Examples

The coordinate file should be saved as a csv file without rownames or headers.
The imagedir should point to a directory on the local filesystem which contains the images that correspond to the rows in the coordfile.
Importantly, this assumes that the order in which files are listred from the directory is the same as how they are ordered in the csv.

The output will look something like this:
![ImageGrid](example_imagegrid.png)

This image will appear in upcoming paper by Schau, et al "Variational Autoencoding Tissue Reponse to Microenvironment Perturbation", International Society for Optics and Photonics, 2018

## Usage

ImageGrid is commandline callable. For example:

```bash
python imagegrid.py \
    --image_dir path/to/image/dir \
    --coord_file path/to/coordfile.csv \
    --save_w 10000 \
    --save_h 10000 \
    --plotfile my_imagegrid.png
```

