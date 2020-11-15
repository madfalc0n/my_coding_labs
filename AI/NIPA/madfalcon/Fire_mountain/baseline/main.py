# -*- coding: utf-8 -*- 

import os
import math
import datetime
import numpy as np
import pandas as pd
import time
import torchvision
import torch
import torch.nn as nn
from torch.optim import Adam

#옵티마이저 관련 : http://www.gisdeveloper.co.kr/?p=8443
from torch.optim.lr_scheduler import StepLR, ReduceLROnPlateau
import argparse

from dataloader import data_loader


DATASET_PATH = '/home/workspace/data/.train/.task142/'
device = torch.device("cuda")


def _infer(model, cuda, data_loader):
    pred = []
    for idx, (img, _) in enumerate(data_loader):
        if cuda:
            img = img.cuda()

        output = model(img)
        output = output['out'].detach().cpu().numpy()
        output = output.argmax(1)
        pred.extend(output)

    return pred


def feed_infer(output_file, infer_func):
    prediction = infer_func()
    print('write output')
    out_pred = pd.DataFrame()
    for pred in prediction:
        pred = pd.DataFrame(pred)
        out_pred = pd.concat([out_pred, pred], axis=0)
    
    out_pred.to_csv(output_file, index=None)
    
    if os.stat(output_file).st_size == 0:
        raise AssertionError('output result of inference is nothing')


def test(prediction_file_name, model, test_dataloader, cuda):
    feed_infer(prediction_file, lambda : _infer(model, cuda, data_loader=test_dataloader))


def save_model(save_dir, model_name, model, optimizer, scheduler):
    state = {
        'model': model.state_dict(),
        'optimizer': optimizer.state_dict(),
        'scheduler': scheduler.state_dict()
    }
#     torch.save(state, save_dir + model_name + 'best_model.pth')
    torch.save(state, save_dir + 'best_model.pth')
    print('model saved')


def load_model(model_name, model, optimizer=None, scheduler=None):
    """
    https://tutorials.pytorch.kr/beginner/saving_loading_models.html
    https://discuss.pytorch.org/t/loading-a-saved-model-for-continue-training/17244/4
    """
    state = torch.load(os.path.join(model_name))
#     print(state)
    model.load_state_dict(state['model'])
    model.to(device)
    if optimizer is not None:
        optimizer.load_state_dict(state['optimizer'])
    if scheduler is not None:
        scheduler.load_state_dict(state['scheduler'])
    print('model loaded')


if __name__ == '__main__':
    # mode argument
    args = argparse.ArgumentParser()
    args.add_argument("--lr", type=float, default=0.001)
    args.add_argument("--cuda", type=bool, default=True)
    args.add_argument("--num_epochs", type=int, default=500)
    args.add_argument("--print_iter", type=int, default=500)
    args.add_argument("--model_name", type=str, default="model.pth")
    args.add_argument("--prediction_file", type=str, default="prediction.csv")
    args.add_argument("--batch", type=int, default=8)
    args.add_argument("--mode", type=str, default="train")
    args.add_argument("--load_trained_model", type=bool, default=False)
    args.add_argument("--save_model_dir", type=str, default='')
    args.add_argument("--original_ep", type=int, default=0)

    config = args.parse_args()

    base_lr = config.lr
    cuda = config.cuda
    num_epochs = config.num_epochs
    print_iter = config.print_iter
    model_name = config.model_name
    prediction_file = config.prediction_file
    batch = config.batch
    mode = config.mode
    load_trained_model = config.load_trained_model
    save_model_dir = config.save_model_dir
    original_ep = config.original_ep

    # create model
#     model = torchvision.models.segmentation.fcn_resnet101(pretrained=False, progress=True, num_classes=9).cuda()
    model = torchvision.models.segmentation.deeplabv3_resnet101(pretrained=False, progress=True, num_classes=9).cuda()
    if load_trained_model != False:
        load_model(model_name, model)
    else:
        print("No model loaded")

    if cuda:
        model = model.cuda()

    if mode == 'train':
        # Specify the loss function
        loss_fn = nn.CrossEntropyLoss()
        # define loss function
        if cuda:
            loss_fn = loss_fn.cuda()
        # set optimizer
        optimizer = Adam(
            [param for param in model.parameters() if param.requires_grad],
            lr=base_lr, weight_decay=1e-4)
        
#         scheduler = StepLR(optimizer, step_size=40, gamma=0.1)
        # 원하는 에폭마다, 이전 학습률 대비 변경폭에 따라 학습률을 감소시켜주는 방식
        # 스케쥴러 방식에 따라 적용방법이 다르다 : http://www.gisdeveloper.co.kr/?p=8443
        scheduler = ReduceLROnPlateau(optimizer, factor=0.15, patience=10, verbose=1)

        # get data loader
        train_dataloader = data_loader(root=DATASET_PATH, phase='train', batch_size=batch)
        time_ = datetime.datetime.now()
        num_batches = len(train_dataloader)

        
        #check parameter of model
        print("------------------------------------------------------------")
        total_params = sum(p.numel() for p in model.parameters())
        print("num of parameter : ",total_params)
        trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        print("num of trainable_ parameter :",trainable_params)
        print("------------------------------------------------------------")
        
        # train
        mid_epochs = num_epochs//2
        for epoch in range(num_epochs):
            model.train()
            for iter_, (i, l) in enumerate(train_dataloader):
                if cuda:
                    i= i.cuda()
                    l = l.cuda()
                out = model(i)
                loss = loss_fn(out['out'], l)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                
                if (iter_ + 1) % print_iter == 0:
                    elapsed = datetime.datetime.now() - time_
                    expected = elapsed * (num_batches / print_iter)
                    _epoch = epoch + ((iter_ + 1) / num_batches)
                    print('[{:.3f}/{:d}] loss({}) '
                          'elapsed {} expected per epoch {}'.format(
                              _epoch, num_epochs, loss.item(), elapsed, expected))
                    time_ = datetime.datetime.now()

            # scheduler update
            scheduler.step(loss)
            if epoch == mid_epochs:
                state = {
                    'model': model.state_dict(),
                    'optimizer': optimizer.state_dict(),
                    'scheduler': scheduler.state_dict()
                }
                torch.save(state, save_model_dir + 'best_model_ep'+str(epoch+original_ep)+'.pth')

            # save model
            save_model(save_model_dir, str(epoch + 1), model, optimizer, scheduler)

            elapsed = datetime.datetime.now() - time_
            print('[epoch {}] elapsed: {}'.format(epoch + 1, elapsed))
        state = {
            'model': model.state_dict(),
            'optimizer': optimizer.state_dict(),
            'scheduler': scheduler.state_dict()
        }
        torch.save(state, save_model_dir + 'best_model_ep'+str(epoch+original_ep)+'.pth')

    else:
        print("Predict mode")
        model.eval()
        # get data loader
        test_dataloader = data_loader(root=DATASET_PATH, phase=mode, batch_size=batch)
        test(prediction_file, model, test_dataloader, cuda)
        # submit test result
        
