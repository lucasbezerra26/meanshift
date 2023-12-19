
from multiprocessing import Pool
from skimage.color import rgb2gray
from skimage.filters import gaussian, threshold_otsu
from skimage import exposure
from skimage.morphology import opening, closing, disk
from sklearn.cluster import estimate_bandwidth, MeanShift
import numpy as np
from tqdm import tqdm

def aplicaMeanShiftOneImg(img):
    img_suavizada = gaussian(img, sigma=1)

    img_gray = rgb2gray(img_suavizada)

    img_eq = exposure.equalize_adapthist(img_gray, clip_limit=0.03)

    # Estimativa do bandwidth para o Mean Shif
    flat_img = img_eq.reshape((-1, 1))
    bandwidth = max(estimate_bandwidth(flat_img, quantile=0.2, n_samples=500), 0.1)

    # Mean Shift
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(flat_img)

    labels = ms.labels_
    segmented = np.reshape(labels, img_eq.shape)

    # Pós-processamento: limpeza usando operações morfológicas
    selem = disk(2)
    cleaned = closing(opening(segmented, selem), selem)

    return cleaned


def aplicar_menshift_paralelo(list_img):
    with Pool(processes=16) as pool:
        result_list = list(
            tqdm(pool.imap(aplicaMeanShiftOneImg, list_img), total=len(list_img), desc="Processando Mean Shift"))
    return result_list


