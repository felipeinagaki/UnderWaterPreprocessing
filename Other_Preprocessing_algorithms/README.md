# Preprocessing 

This folder contains methods that were tested and not chosen as the pre-processing algorithm in our Computer Vison Project. This folder was made from a fork of the project EyeSe https://github.com/SIH-22-Kyogre/EyeSea_Image-Preprocessing-Algorithms

## Procedure to Execute

- Place the input images in `data/input/` directory of the corresponding processing operation (i.e Color Restoration or Enhancement).
- Edit the corresponding `run.py` script to uncomment the algorithm to be applied.
- Execute the script:
  - To only generate the images: `python run.py`.
  - To visualize before-after stages for each image: `python run.py --visualize`.
- The processed images are stored in the corresponding `data/output/` directory.


## Image Enhancement Algorithms

- **CLAHE**: Contrast limited adaptive histogram equalization.
- **GC**: Gamma Correction.
- **HE**: Image enhancement by histogram transformation.
- **ICM**: Underwater Image Enhancement Using an Integrated Colour Model.
- **Rayleigh Distribution**: Underwater image quality enhancement through composition of dual-intensity images and Rayleigh-stretching.
- **RGHS**: Shallow-Water Image Enhancement Using Relative Global Histogram Stretching Based on Adaptive Parameter Acquisition. 
- **UCM**: Enhancing the low quality images using Unsupervised Colour Correction Method.
- **UMASK**: Unsharp Masking.
- **BF**: Bilateral Filtering. 

In our Project, we only used Rayleigh Distribution, RGHS, UCM and BF for comparison.

## Image Color Restoration Algorithms

- **DCP**: Single Image Dehazing using Dark Channel Prior.
- **GB Dehazing R Correction**: Single underwater image restoration by blue-green channels dehazing and red channel correction.
- **IBLA**: Underwater Image Restoration Based on Image Blurriness and Light Absorption.
- **LowComplexityDCP**: Low Complexity Underwater Image Enhancement Based on Dark Channel Prior.
- **MIP**: Initial results in underwater single image dehazing.
- **New Optical Model**: Single underwater image enhancement with a new optical model ([paper](http://www.jdl.link/doc/2011/201372615482341921_iscas2013_single_underwater_image_enhancement_with_an_improved_optical_model.pdf)).
- **RoWS**: Removal of water scattering. 
- **UDCP**: Transmission Estimation in Underwater Single Images.
- **ULAP**: A Rapid Scene Depth Estimation Model Based on Underwater Light Attenuation Prior for Underwater Image Restoration.


In our project we tested all but DCP.
For comparison results, please use the Comparison notebook on the previous folder

