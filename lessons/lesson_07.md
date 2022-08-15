# Lesson 7: Image Processing and Visualization \# 2 #

In this lesson we will use `scikit-image` to do simple image processing in Python. `scikit-image` is an open-source image processing library for the Python programming language. It includes algorithms for segmentation, geometric transformations, color space manipulation, analysis, filtering, morphology, feature detection, and more.

We will be using the following magic statements for `matplotlib` in this session (is you use a notebook):

```py
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
```


`matplotlib inline`: With this backend, the output of plotting commands is displayed inline within frontends like the Jupyter notebook, directly below the code cell that produced it. The resulting plots will then also be stored in the notebook document.

`config InlineBackend.figure_format = 'retina'`: With this backend formatting, the resultant lines will have a retina quality of high resolution.

is similar to

```py
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')
```

> **_Magic commands:_** Magic commands are special commands that can help you with running and analyzing data in your notebook. They add a special functionality that is not straight forward to achieve with python code or jupyter notebook interface. Magic commands are easy to spot within the code. They are either proceeded by `%` if they are on one line of code or by `%%` if they are written on several lines.

We will also need to include the following dependencies

```py
import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_float, img_as_ubyte, io
```

## 7.1 Images are arrays ##

Images are represented in `scikit-image` using standard `numpy` arrays. This allows maximum interoperability with other libraries in the scientific Python ecosystem, such as `matplotlib` and `scipy`.

Build, store and show a white noise grayscale image from a 2D array:

```py
random_image = np.random.random([500, 500])
print(random_image)
plt.imshow(random_image, cmap='gray')
plt.colorbar()
plt.show()
plt.savefig('random_img.png', dpi=150)
plt.close()
```

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/random_img.png?raw=true" alt="white noise" width="400"/> |
|:--:|
| *Grayscale image created from a rank 2 `numpy` array* |


Real images are also 'just' `numpy` arrays 

```py
coins = data.coins()
print(type(coins))
print(coins.dtype)
print(coins.shape)
plt.imshow(coins, cmap='gray')
plt.savefig('figures/coins.png', dpi=150)
```

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/coins.png?raw=true" alt="coins" width="400"/> |
|:--:|
| *Real images are also represented as `numpy` array* |


### Color images ###

A color image is a 3D array, where the last dimension has size 3 and represents the __<span style="color:red">red</span>__, __<span style="color:green">green</span>__, and __<span style="color:blue">blue</span>__ channels.

Images can also include transparent regions by adding a 4th dimension, called an alpha layer.

```py
cat = data.chelsea()
print("Shape:", cat.shape)
print("Values min/max:", cat.min(), cat.max())
plt.imshow(cat)
plt.savefig('cat.png', dpi=150)
```

These are just NumPy arrays. E.g., we can make a red square by using standard array slicing and manipulation

```py
cat[10:110, 10:110, :] = [255, 0, 0]
plt.imshow(cat)
plt.savefig('figures/cat_red.png', dpi=150)
plt.close()
```

Images can also include transparent regions by adding a 4th dimension, called an alpha layer.

#### Color space ####

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/rgb_color_model.png?raw=true" alt="coins" width="400"/> |
|:--:|
| *RGB color model which, typically, represents each channel as 8-bit unsigned integers.* |


8-bit unsigned integers is a subset of all integers:

$\{ 0, 1, 2, \dots, 253, 254, 255 \}$

An image whose data matrix has type `uint8` is called an 8-bit image. RGB model predominantly uses the the 24-bit implementation, with 8 bits, or 256 discrete levels of color per channel, which limits the color space to $256 \times 256 \times 256 \approx 16.7$ million colors. Notice that 8-bit unsigned cannot represent negative numbers.

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/grayscale_histogram.png?raw=true" width="800"/><img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/color_histogram.png?raw=true" width="800"/> |
|:--:|
| *Grayscale and RGB images and their corresponding color histograms* |

### Other shapes and corresponding meanings ###

| Image type | Coordinates |
|:-|:-|
| 2D grayscale | (row, column) |
| 2D multichannel | (row, column, channel) |
| 3D grayscale (or volumetric) | (plane, row, column) |
| 3D multichannel | (plane, row, column, channel) |

## Displaying images with `matplotlib`


Start by creating to image variables

```py
img0 = data.chelsea()
img1 = data.rocket()
```

We can now add annotations to the image

```py
figure, (ax0, ax1) = plt.subplots(1, 2, figsize=(20, 10))

ax0.imshow(img0)
ax0.set_title('Cat', fontsize=18)
ax0.axis('off')

ax1.imshow(img1)
ax1.set_title('Rocket', fontsize=18)
ax1.set_xlabel(r'Launching position $\alpha=320$')

ax1.vlines([202, 300], 0, img1.shape[0], colors='magenta', linewidth=3, label='Side tower position')
ax1.plot([168, 190, 200], [400, 200, 300], color='white', linestyle='--', label='Side angle')
ax1.legend();

plt.savefig('figures/image_display_matplotlib.png', dpi=150)
plt.show()
plt.close()
```

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/image_display_matplotlib.png?raw=true" alt="coins" width="800"/> |
|:--:|
| *Images can be displayed in `matplotlib` figures to use the library's figure functionalities.* |


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

figure, (ax0, ax1) = plt.subplots(1, 2, figsize=(15, 7))
ax0.imshow(linear0, cmap='gray')
ax1.imshow(linear1, cmap='gray')
plt.savefig('image_values.png', dpi=150)
plt.close()
```

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/image_values.png?raw=true" alt="coins" width="600"/> |
|:--:|
| *Images can be represented using 0.-1. for floating point images and 0-255 for unsigned bytes.* |


`scikit-image` is designed in such a way that any data-type is allowed as input, as long as the range is correct (0-1 for floating point images, 0-255 for unsigned bytes, 0-65535 for unsigned 16-bit integers).

You can convert images between different representations by using `img_as_float`, `img_as_ubyte`, etc. 

```py
image = data.chelsea()

image_ubyte = img_as_ubyte(image)
image_float = img_as_float(image)
print("type, min, max:", image_ubyte.dtype, image_ubyte.min(), image_ubyte.max())
print("type, min, max:", image_float.dtype, image_float.min(), image_float.max())
print(f"231/255 = {231/255}")
```

Your code would then typically look like:

```py
def my_function(any_image):
    float_image = img_as_float(any_image)
    # Proceed, knowing image is in [0, 1]
```

It is recommend using the floating point representation because that `scikit-image` mostly uses that format internally.


### Image I/O ####

Since `scikit-image` operates on NumPy arrays, any image reader library that provides arrays will do. Options include `imageio`, `matplotlib`, and `pillow`. `scikit-image` conveniently wraps many of these in the io submodule, and will use whichever of the libraries mentioned above are installed.

```py
image = io.imread('balloon.jpg')
print(type(image))
print(image.dtype)
print(image.shape)
print(image.min(), image.max())
plt.imshow(image)
plt.show()
plt.close()
```

You can also load multiple images, or multi-layer TIFF images:

```py
ic = io.ImageCollection('../images/*.png:../images/*.jpg')
print('Type:', type(ic))
print(ic.files)
```

And now we can build a visualization of all images in `images` by looping over the `axes` object and adding an image one at a time

```py
import os
figure, axes = plt.subplots(nrows=3, ncols=len(ic) // 3 + 1, figsize=(20, 5))

axes = axes.ravel()

for ax in axes:
    ax.axis('off')

for i, image in enumerate(ic):
    axes[i].imshow(image, cmap='gray')
    axes[i].set_title(os.path.basename(ic.files[i]))
    
plt.tight_layout()
plt.show()
plt.savefig('collection_image.png', dpi=150)
```





| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/collection_images.png?raw=true" alt="coins" width="1200"/> |
|:--:|
| *Embedding multiple images with a for loop in one `matplotlib` figure.* |



Note: `axes.ravel()` is used to turn the array of axes (subplots) into a list that we can easily iterate over. In general, `ravel()` is a `numpy` method that returns a contiguous flattened array

```sh
>>> x = np.array([[1, 2, 3], [4, 5, 6]])
>>> np.ravel(x)
array([1, 2, 3, 4, 5, 6])
```

## 7.2 3d visualization with `matplotlib` ##

[source](https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html)

`matplotlib` was originally designed for 2d plotting, but today it offers a set of tools for three-dimensional data visualization through the `mplot3d` toolkit


```py
from mpl_toolkits import mplot3d
```

Once this submodule is imported, a three-dimensional axes can be created by passing the keyword `projection='3d'` to any of the normal axes creation routines

```py
fig = plt.figure()
ax = plt.axes(projection='3d')
plt.savefig('figures/axes_3d.png', dpi=300)
plt.close()
```

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/axes_3d.png?raw=true" alt="axes3d" width="600"/> |
|:--:|
| *caption* |

With 3d axes enabled, we can now plot a variety of three-dimensional plot types. 

Note: Three-dimensional plotting is one of the functionalities that benefits from viewing figures interactively rather than statically in the notebook. To use interactive figures, you can use the magic statment `%matplotlib notebook` rather than `%matplotlib inline`.

### 3d Points and Lines ###

The most basic three-dimensional plot is a line or collection of scatter plot created from sets of `(x, y, z)` triples. Similar to the common two-dimensional plots discussed in [lesson 4](line here), these can be created using the `ax.plot3D` and `ax.scatter3D` functions.

Plot a trigonometric spiral, along with some points drawn randomly near the line

```py
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)

ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
plt.savefig('trigonometric_spiral.png', dpi=300)
plt.close()
```

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/trigonometric_spiral.png?raw=true" alt="trigo-spiral" width="600"/> |
|:--:|
| *caption* |

Notice that by default, the scatter points have their transparency adjusted to give a sense of depth on the page.

### 3d Contour Plots ###

`mplot3d`can create create three-dimensional relief plots similar to density and contour plots

```py
def sinosoidal_3d(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z =  sinosoidal_3d(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.savefig('sinosoidal_relief.png', dpi=300)
```

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/sinosoidal_relief.png?raw=true" alt="sinosoidal" width="600"/> |
|:--:|
| *Change the elevation to 60 degrees (that is, 60 degrees above the x-y plane) and the azimuth to 35 degrees (that is, rotated 35 degrees counter-clockwise about the z-axis):* |


Sometimes the default viewing angle is not optimal, in which case we can use the `view_init` method to set the elevation and azimuthal angles.

```py
ax.view_init(60, 35)
fig
plt.savefig('figures/sinosoidal_relief_rotate.png', dpi=300)
plt.close()
```


| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/sinosoidal_relief_rotate.png?raw=true" alt="rotatecoins" width="600"/> |
|:--:|
| *Change the elevation to 60 degrees (that is, 60 degrees above the x-y plane) and the azimuth to 35 degrees (that is, rotated 35 degrees counter-clockwise about the z-axis).* |

### Example: Visualizing a Möbius Strip ###

A Möbius strip is similar to a strip of paper glued into a loop with a half-twist. Topologically, it's quite interesting because despite appearances it has only a single side! Here we will visualize such an object using `matplotlib`'s 3d tools. The key to creating the Möbius strip is to think about it's parametrization: it's a 2d strip, so we need two intrinsic dimensions. Let's call them $\theta$, which ranges from $0$ to $2\pi$ around the loop, and $w$ which ranges from $-1$ to $1$ across the width of the strip.

```py
theta = np.linspace(0, 2 * np.pi, 30)
w = np.linspace(-0.25, 0.25, 8)
w, theta = np.meshgrid(w, theta)
```

From this parametrization, we must determine the (x, y, z) positions of the embedded strip. There are two rotations happening: one is the position of the loop about its center (what we've called $\theta$), while the other is the twisting of the strip about its axis (we'll call this $\phi$). For a Möbius strip, we must have the strip makes half a twist during a full loop, or $\Delta \phi = \Delta \theta / 2$.

```py
phi = 0.5 * theta
```

We can use trigonometry to derive the three-dimensional embedding. We'll define $r$, the distance of each point from the center, and use this to find the embedded $(x,y,z)$ coordinates

```py
# radius in x-y plane
r = 1 + w * np.cos(phi)

x = np.ravel(r * np.cos(theta))
y = np.ravel(r * np.sin(theta))
z = np.ravel(w * np.sin(phi))
```

To plot the object, we must make sure the triangulation is correct. The best way to do this is to define the triangulation within the underlying parametrization, and then let `matplotlib` project this triangulation into the 3d space of the Möbius strip. This can be accomplished as follows:

```py
# triangulate in the underlying parametrization
from matplotlib.tri import Triangulation
tri = Triangulation(np.ravel(w), np.ravel(theta))

ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap='viridis', linewidths=0.2);
ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1)
plt.savefig('mobius_strip.png', dpi=300)
```

| <img src="https://github.com/CHCAA-EDUX/introduction-to-scientific-computing/blob/main/lessons/figs/mobius_strip.png?raw=true" alt="rotatecoins" width="600"/> |
|:--:|
| *Möbius strip plotted with `matplotlib`'s 3d toolkit.* |
