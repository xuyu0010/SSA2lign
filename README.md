### Overview

This code is for Action Recognition (Domain adaptation), specifically for Black-box Video Unsupervised Domain Adaptation and the proposed SSA<sup>2</sup>lign.

### Requirements (Recommended)
- Python 3.9
- PyTorch 1.12.0
- Numpy
- opencv-python

### Running:

The default benchmark is the Daily-DA benchmark, the default cross-domain task is HMDB51&rarr;ARID (H&rarr;A). To use other benchmarks you may choose from the following options for the ```--dataset``` option: (DATASET_OPTION)
```
'Daily', 'Sports'
```

- Step 1: To train, run the following command:
```python
python train_multisnippet.py --dataset DATASET_OPTION --source-dataset SOURCE_DATASET_NAME --target-dataset TARGET_DATASET_NAME --k-shot K_SHOT_SETTING --network TimeSFormer
```
The "SOURCE_DATASET_NAME" and "TARGET_DATASET_NAME" defines domains of the cross domain task to be performed. For Daily-DA benchmark the possible names are "HMDB51", "ARID", "MIT", and "Kinetics-Daily". For Sports-DA benchmark the possible names are "UCF101", "Sports1M", and "Kinetics-Sports". 

- Step 3: To evaluate the trained model, and run the following command:
```python
python evaluate_multisnippet.py --dataset DATASET_OPTION --target-dataset TARGET_DATASET_NAME
```