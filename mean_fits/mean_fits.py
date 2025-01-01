def mean_fits(imgs):
    """
    Calculate the mean of multiple FITS images
    
    Parameters:
        imgs: List of strings
            List of FITS file paths to process
    
    Returns:
        numpy.ndarray: Mean image array
    """
    import numpy as np
    from astropy.io import fits
    
    # Initialize array to store sum of images
    first_image = fits.getdata(imgs[0])
    total = np.zeros(first_image.shape, dtype=np.float64)
    
    # Sum all images
    for img_path in imgs:
        data = fits.getdata(img_path)
        total += data
        
    # Calculate mean by dividing by number of images
    mean_image = total / len(imgs)
    
    return mean_image

if __name__ == '__main__':
    # Test function with examples
    data = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
    print(data[100, 100])
    
    # Plot the result
    import matplotlib.pyplot as plt
    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.colorbar()
    plt.show()