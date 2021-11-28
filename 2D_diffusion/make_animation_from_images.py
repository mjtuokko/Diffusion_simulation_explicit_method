
import imageio

def make_animation_from_images(image_names,frames_per_second, name):
    #N is number of images
    images = []
    for image in image_names:
        images.append(imageio.imread(image))
    #save animation as gif
    imageio.mimsave(name, images,fps=frames_per_second)

