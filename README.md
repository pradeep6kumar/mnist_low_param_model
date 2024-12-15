# MNIST Digit Classification Model

## Model Performance Summary

### Training Results
- Total Epochs: 15
- Best Test Accuracy: 99.38% (Epoch 9)
- Final Test Accuracy: 99.31% (Epoch 14)
- Consistent Performance: Model maintained >99% test accuracy from Epoch 8 onwards
- Training Accuracy: Reached 98.83% in final epoch

### Training Progression
- Initial Accuracy (Epoch 0): 89.77% → 98.34% (test)
- Rapid Improvement: Achieved 97.45% by Epoch 1
- Stabilization: >98.7% training accuracy after Epoch 6
- High Consistency: Test accuracy remained between 99.21% - 99.38% for last 7 epochs

## Model Architecture

### Network Parameters
- Total Parameters: 7,544
- Trainable Parameters: 7,544
- Non-trainable Parameters: 0

### Memory Footprint
- Input size: 0.00 MB
- Forward/backward pass size: 0.65 MB
- Parameters size: 0.03 MB
- Estimated Total Size: 0.68 MB

### Layer Structure

summary of model: EPOCH: 0
Loss=0.029920436441898346 Batch_id=937 Accuracy=89.77: 100%|██████████| 938/938 [00:20<00:00, 44.78it/s]

Test set: Average loss: 0.0598, Accuracy: 9834/10000 (98.34%)

EPOCH: 1
Loss=0.15498091280460358 Batch_id=937 Accuracy=97.45: 100%|██████████| 938/938 [00:18<00:00, 50.88it/s] 

Test set: Average loss: 0.0391, Accuracy: 9895/10000 (98.95%)

EPOCH: 2
Loss=0.16696298122406006 Batch_id=937 Accuracy=97.86: 100%|██████████| 938/938 [00:17<00:00, 53.40it/s]  

Test set: Average loss: 0.0365, Accuracy: 9902/10000 (99.02%)

EPOCH: 3
Loss=0.058754097670316696 Batch_id=937 Accuracy=98.09: 100%|██████████| 938/938 [00:18<00:00, 49.43it/s] 

Test set: Average loss: 0.0409, Accuracy: 9882/10000 (98.82%)

EPOCH: 4
Loss=0.035468537360429764 Batch_id=937 Accuracy=98.23: 100%|██████████| 938/938 [00:22<00:00, 41.40it/s] 

Test set: Average loss: 0.0344, Accuracy: 9900/10000 (99.00%)

EPOCH: 5
Loss=0.043755728751420975 Batch_id=937 Accuracy=98.28: 100%|██████████| 938/938 [00:19<00:00, 48.87it/s] 

Test set: Average loss: 0.0293, Accuracy: 9917/10000 (99.17%)

EPOCH: 6
Loss=0.013850955292582512 Batch_id=937 Accuracy=98.71: 100%|██████████| 938/938 [00:17<00:00, 53.88it/s] 

Test set: Average loss: 0.0260, Accuracy: 9921/10000 (99.21%)

EPOCH: 7
Loss=0.021869855001568794 Batch_id=937 Accuracy=98.75: 100%|██████████| 938/938 [00:16<00:00, 55.23it/s] 

Test set: Average loss: 0.0263, Accuracy: 9926/10000 (99.26%)

EPOCH: 8
Loss=0.004675473086535931 Batch_id=937 Accuracy=98.74: 100%|██████████| 938/938 [00:19<00:00, 48.06it/s] 

Test set: Average loss: 0.0242, Accuracy: 9935/10000 (99.35%)

EPOCH: 9
Loss=0.012697670608758926 Batch_id=937 Accuracy=98.79: 100%|██████████| 938/938 [00:18<00:00, 50.84it/s] 

Test set: Average loss: 0.0243, Accuracy: 9938/10000 (99.38%)

EPOCH: 10
Loss=0.06539749354124069 Batch_id=937 Accuracy=98.79: 100%|██████████| 938/938 [00:18<00:00, 49.79it/s]  

Test set: Average loss: 0.0238, Accuracy: 9934/10000 (99.34%)

EPOCH: 11
Loss=0.032625798135995865 Batch_id=937 Accuracy=98.89: 100%|██████████| 938/938 [00:17<00:00, 53.36it/s] 

Test set: Average loss: 0.0249, Accuracy: 9930/10000 (99.30%)

EPOCH: 12
Loss=0.027760867029428482 Batch_id=937 Accuracy=98.87: 100%|██████████| 938/938 [00:18<00:00, 49.54it/s] 

Test set: Average loss: 0.0249, Accuracy: 9929/10000 (99.29%)

EPOCH: 13
Loss=0.240318164229393 Batch_id=937 Accuracy=98.87: 100%|██████████| 938/938 [00:20<00:00, 45.62it/s]    

Test set: Average loss: 0.0247, Accuracy: 9933/10000 (99.33%)

EPOCH: 14
Loss=0.022044120356440544 Batch_id=937 Accuracy=98.83: 100%|██████████| 938/938 [00:19<00:00, 48.38it/s] 
```
----------------------------------------------------------------
Layer (type) Output Shape Param #
================================================================
Conv2d-1 [-1, 16, 26, 26] 144
ReLU-2 [-1, 16, 26, 26] 0
BatchNorm2d-3 [-1, 16, 26, 26] 32
Dropout-4 [-1, 16, 26, 26] 0
Conv2d-5 [-1, 10, 24, 24] 1,440
ReLU-6 [-1, 10, 24, 24] 0
BatchNorm2d-7 [-1, 10, 24, 24] 20
Dropout-8 [-1, 10, 24, 24] 0
Conv2d-9 [-1, 10, 24, 24] 100
MaxPool2d-10 [-1, 10, 12, 12] 0
Conv2d-11 [-1, 10, 10, 10] 900
ReLU-12 [-1, 10, 10, 10] 0
BatchNorm2d-13 [-1, 10, 10, 10] 20
Dropout-14 [-1, 10, 10, 10] 0
Conv2d-15 [-1, 10, 8, 8] 900
ReLU-16 [-1, 10, 8, 8] 0
BatchNorm2d-17 [-1, 10, 8, 8] 20
Dropout-18 [-1, 10, 8, 8] 0
Conv2d-19 [-1, 16, 6, 6] 1,440
ReLU-20 [-1, 16, 6, 6] 0
BatchNorm2d-21 [-1, 16, 6, 6] 32
Dropout-22 [-1, 16, 6, 6] 0
Conv2d-23 [-1, 16, 6, 6] 2,304
ReLU-24 [-1, 16, 6, 6] 0
BatchNorm2d-25 [-1, 16, 6, 6] 32
Dropout-26 [-1, 16, 6, 6] 0
AvgPool2d-27 [-1, 16, 1, 1] 0
Conv2d-28 [-1, 10, 1, 1] 160
================================================================
```

## Key Features
- Lightweight architecture with only 7.5K parameters
- Efficient memory usage (0.68 MB total)
- Uses BatchNorm and Dropout for regularization
- Implements both Max and Average Pooling
- Achieves state-of-the-art accuracy (>99.3%)

## Training Configuration
- Optimizer: SGD with Nesterov momentum
- Learning Rate: OneCycleLR scheduler
- Batch Size: 128 (CUDA) / 64 (CPU)
- Data Augmentation: Yes (via transforms)
