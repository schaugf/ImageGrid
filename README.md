# ImageGrid

Create a grid of images from a coordinate file and set of corresponding images.

## Examples

The coordinate file should be saved as a csv file without rownames or headers.

| x1 | y1 |
| x2 | y2 |
| x3 | y3 |


The imagedir should point to a directory on the local filesystem which contains the images that correspond to the rows in the coordfile.
Importantly, this assumes that the order in which files are listred from the directory is the same as how they are ordered in the csv.

The output will look something like this:
![ImageGrid](example_imagegrid.png)


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

