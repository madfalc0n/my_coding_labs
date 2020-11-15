import os
import pandas as pd
import numpy as np
import cv2
import random
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms

class CustomDataset(Dataset):
    def __init__(self, root, phase='train'):
        self.root = root
        self.phase = phase
        self.data = {}
        
        img_cropped = []
        label_cropped = []
        if phase == 'train':
            self.data_path=os.path.join(self.root, 'train.png')
            self.label_path=os.path.join(self.root, 'train_label.png')
            img = cv2.imread(self.data_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = (img / 255.)
            img = img.transpose(2,0,1)
            norm_image = np.zeros((8750, 7225))
            norm_image = cv2.normalize(img, norm_image, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
            class_mask = pd.read_csv('/home/workspace/user-workspace/Fire_mountain/Madfalcon/change_class_mask.csv').values
                                    
            
            for i in range(0, 8704, 512):
                for j in range(0, 7168, 512):
                    img_cropped.append(norm_image[:, i:i+512, j:j+512].copy())
                    label_cropped.append(class_mask[i:i+512, j:j+512].copy())

                    
        elif phase == 'test':
            for i in range(238):
                img = cv2.imread(f'/home/workspace/data/.train/.task142/test/{i}.png')
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                img = (img / 255.)
                img = img.transpose(2,0,1)
                norm_image = np.zeros((8750, 7225))
                norm_image = cv2.normalize(img, norm_image, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
                img_cropped.append(norm_image)
                
        self.data['input'] = img_cropped
        self.data['output'] = label_cropped     
        
    def __getitem__(self, index):
        img = self.data['input'][index]
        input_img = torch.tensor(img, dtype=torch.float)
        if self.phase == 'train':
            mask = self.data['output'][index]
            output_mask = torch.tensor(mask, dtype=torch.long)
            return (input_img, output_mask)
        else:
            dummy = []
            return (input_img, dummy)
    
    def __len__(self):
        return len(self.data['input'])
    
    def get_label_file(self):
        return self.label_path

def data_loader(root, phase='train', batch_size=4):
    if phase == 'train':
        shuffle = True
    else:
        shuffle = False
    
    dataset = CustomDataset(root, phase)
    dataloader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=shuffle)
    return dataloader
