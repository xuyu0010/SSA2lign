### Overview

This repository is the official code for the ICCV-23 paper [_Augmenting and Aligning Snippets for Few-Shot Video Domain Adaptation_](https://arxiv.org/abs/2303.10451), with the proposed SSA<sup>2</sup>lign method. Read more in our project page [Here](https://xuyu0010.github.io/fsvda.html).

### Requirements (Recommended)
- Python 3.9
- PyTorch 1.12.0
- Numpy
- opencv-python

### Running

- Code will be updated soon. The generation of the few-shot sets are available in the ```/dataset``` folder.

<!-- ### Running:

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
``` -->


### Contact

For more information please do not hesitate to raise an issue or to contact xuyu0010 at e.ntu.edu.sg or yang0478 at e.ntu.edu.sg.