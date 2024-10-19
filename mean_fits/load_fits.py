# Write your load_fits function here.
def load_fits(img):
    import numpy as np
    from astropy.io import fits

    hdulist = fits.open(img)
    data = hdulist[0].data
    
    # Use np.argmax() to find the index of the maximum value in the flattened array
    max_index_flat = np.argmax(data)
    
    # Convert the flattened index to a 2D index
    max_index_2d = np.unravel_index(max_index_flat, data.shape)

    print(f'Maximum value {max_index_flat} is at x, y {max_index_2d}')
    
    return data    

if __name__ == '__main__':
    # Run your `load_fits` function with examples:
    data = load_fits('ngc1261.fits')
    #print(data)

    # You can also confirm your result visually:
    from astropy.io import fits
    import matplotlib.pyplot as plt

    #hdulist = fits.open('ngc1261.fits')
    #data = hdulist[0].data

    # Plot the 2D image data
    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()
