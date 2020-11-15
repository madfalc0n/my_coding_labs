해당 폴더에는 데이터가 존재하지 않음

0. 모델 대략 설명
    - 데이터 전처리
        1. 파이토치 학습을 위한 세그멘테이션 값 전체를 -1
        2. 정규화 진행(255 값으로 나누고 opencv 명령어를 이용하여 normalize 진행)
    - resnet101 + deeplabv3 모델을 사용하여 학습진행
    - 학습이미지 input 과정에서 사이즈를 작게 조절하여 중복되는 구간을 늘려 정확도를 향상 시킬 수 있었음
        - baseline/dataloader.py : 30line 에서 
        """
        1. as-is:
                for i in range(0, 8704, 512):
                        for j in range(0, 7168, 512):
                            img_cropped.append(norm_image[:, i:i+512, j:j+512].copy())
                            label_cropped.append(class_mask[i:i+512, j:j+512].copy())
        
        2. to-be:
                for i in range(0, 8000, 256):
                        for j in range(0, 6500, 256):
                            img_cropped.append(norm_image[:, i:i+512, j:j+512].copy())
                            label_cropped.append(class_mask[i:i+512, j:j+512].copy())
               
        """
    - 학습이미지가 1개이므로 최대한 적게 학습을 하는 것이 좋아보였음(epoch 10 이내?)

1. 모델 학습
    - Step1_model_train.ipynb 파일을 이용하여 학습 진행
    
2. 데이터 예측
    - Step2_model_predict.ipynb 파일을 이용하여 예측 진행