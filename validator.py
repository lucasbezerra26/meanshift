import numpy as np


def dice(imagem, mascara, empty_score=1.0):
    imagem_b = np.asarray(imagem).astype(np.bool)
    mascara_b = np.asarray(mascara).astype(np.bool).squeeze()

    if imagem_b.shape != mascara_b.shape:
        raise ValueError("Shape diferentes!")

    im_sum = imagem_b.sum() + mascara_b.sum()

    if im_sum == 0:
        return empty_score

    intersection = np.logical_and(imagem_b, mascara_b)

    return 2. * intersection.sum() / im_sum


def media_dice(imagem, mascara):
    soma = map(dice, imagem, mascara)
    return sum(list(soma)) / len(imagem)

