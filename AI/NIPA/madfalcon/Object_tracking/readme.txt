해당 폴더에는 데이터가 존재하지 않음

0. tensorflow 의 models를 기반으로 학습시켰음
    - "https://github.com/tensorflow/models"에서 다운로드 후 사용
    - pretrain 모델 다운로드 후 config를 각자에 맞게 변경하여 사용

1. 아래 해당 파일들은 "models/research/"에 존재해야 함, tfrecord, train 시 자체적으로 커스텀 하여 사용 하였음, 
    - 20201106_predict_bb.ipynb (학습모델 예측용 코드)
    - 20201104_custom_create_tfrecord.py (데이터 tfrecord 변환 코드)
    - 20201104_model_main_tf2.py (모델 학습 코드)
    - 20201106_model_main_tf2.py
    - 20201107_exporter_main_v2.py (학습모델 export 코드)

2. 모델 학습시 따로 전처리 하지 않음, 다만 동영상으로 데이터가 제공되었기 때문에 프레임 추출 작업을 진행하였음
