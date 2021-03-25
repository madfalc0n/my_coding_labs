import numpy as np 


def rand_bbox(size, lamb, batch_size):
    """ Generate random bounding box 
    Args:
        - size: [width, breadth] of the bounding box
        - lamb: (lambda) cut ratio parameter
    Returns:
        - Bounding box
    """
    W = size[0]
    H = size[1]
    cut_rat = np.sqrt(1. - lamb)
    # print(cut_rat)
    cut_w = np.array(W * cut_rat).astype('int8')
    print(cut_w)
    cut_h = np.array(H* cut_rat).astype('int8')
    print(cut_h)

    result = np.ones(shape=(batch_size,), dtype=np.int8)
    # uniform
    cx = np.random.randint(W*result)
    cy = np.random.randint(H*result)
    # print(cx,cy)
    # print(cx-cut_w//2)

    bbx1 = np.clip(cx - cut_w // 2, 0, W).reshape(-1,1)
    bby1 = np.clip(cy - cut_h // 2, 0, H).reshape(-1,1)
    bbx2 = np.clip(cx + cut_w // 2, 0, W).reshape(-1,1)
    bby2 = np.clip(cy + cut_h // 2, 0, H).reshape(-1,1)

    return np.concatenate([bbx1,bby1,bbx2,bby2], axis=1)


beta = 1.0
batch_size = 4
lamb = np.random.beta(beta, beta,size=batch_size)
print(lamb)
print(rand_bbox([256,256], lamb,batch_size))