# Lesson 7: 


Magic for notebooks

```py
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
```

| Image type | Coordinates |
|:-|:-|
| 2D grayscale | (row, column) |
| 2D multichannel | (row, column, channel) |
| 3D grayscale (or volumetric) | (plane, row, column) |
| 3D multichannel | (plane, row, column, channel) |

## Data types and image values ##

There are different conventions for representing image values (colors):

* `0 - 255   where  0 is black, 255 is white`
* `0 - 1     where  0 is black, 1 is white`

`scikit-image` supports both conventions - the choice is determined by the data-type of the array.

```py
linear0 = np.linspace(0, 1, 2500).reshape((50, 50))
linear1 = np.linspace(0, 255, 2500).reshape((50, 50)).astype(np.uint8)

print("Linear0:", linear0.dtype, linear0.min(), linear0.max())
print("Linear1:", linear1.dtype, linear1.min(), linear1.max())

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(15, 15))
ax0.imshow(linear0, cmap='gray')
ax1.imshow(linear1, cmap='gray')
```

`scikit-image` is designed in such a way that any data-type is allowed as input, as long as the range is correct (0-1 for floating point images, 0-255 for unsigned bytes, 0-65535 for unsigned 16-bit integers).

You can convert images between different representations by using img_as_float, img_as_ubyte, etc.

Your code would then typically look like this:

```py
def my_function(any_image):
    float_image = img_as_float(any_image)
    # Proceed, knowing image is in [0, 1]
```

It is recommend using the floating point representation because that `scikit-image` mostly uses that format internally.


### Image I/O ####

Since `scikit-image` operates on NumPy arrays, any image reader library that provides arrays will do. Options include `imageio`, `matplotlib`, and `pillow`. `scikit-image` conveniently wraps many of these in the io submodule, and will use whichever of the libraries mentioned above are installed: