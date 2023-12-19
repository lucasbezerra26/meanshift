# Plota imagens
from matplotlib import pyplot as plt


def exibe2imagens(img1, img2):
    fig, ax = plt.subplots(1, 2, figsize=(10, 6))
    ax = ax.ravel()

    ax[0].imshow(img1, cmap="gray")
    ax[0].set_title("Recorte Original")

    ax[1].imshow(img2, cmap="gray")
    ax[1].set_title("Máscara")

def funcaoPlot(imagens, title=None):
    fig, ax = plt.subplots(1, len(imagens), figsize=(60, 60))
    for i, folha in enumerate(imagens):
        ax[i].imshow(folha, cmap="gray")
        if title:
            ax[i].set_title(title[i])
        else:
            ax[i].set_title(str(i))