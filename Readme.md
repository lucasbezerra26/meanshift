# Leishmania Image Segmentation Using Mean Shift Clustering

This repository contains a Python toolkit for segmenting Leishmania parasites in microscopic images using the Mean Shift clustering algorithm. The toolkit includes preprocessing, segmentation, and post-processing utilities.

## Setup

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/leishmania-segmentation.git
cd leishmania-segmentation
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```
# Usage
To use this toolkit, you can follow the example provided in `exemplo.ipynb`. For a quick start, use the following steps in your Python script:

```python   

pool = Pool(processes=16) # 16 is the number of processes to be used
imagens_meanshift2 = aplicar_menshift_paralelo(imagens)
pool.close()
pool.join()

```

Note that the `aplicar_menshift_paralelo` function receives a list of images and returns a list of segmented images. The `pool` object is used to parallelize the segmentation process. The number of processes to be used can be changed according to the number of cores available in your machine.