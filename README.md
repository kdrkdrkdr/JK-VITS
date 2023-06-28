# JK-VITS
Bilingual-TTS (Japanese and Korean)
This Repository can speak Japanese even if you train with Korean dataset, and can speak Korean even if you train with Japanese dataset.
By transcribing pronunciation from Japanese to Korean and Korean to Japanese, the unstable voice produced when using the existing multilingual ipa cleaners has been improved.



## Table of Contents 
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Prepare_Datasets](#Prepare_Datasets)
- [Usage](#usage)
- [Inference](#inference)
- [References](#References)


## Pre-requisites
- A Windows/Linux system with a minimum of `16GB` RAM.
- A GPU with at least `12GB` of VRAM.
- Python >= 3.8
- Anaconda installed.
- PyTorch installed.
- CUDA 11.7 installed.



Pytorch install command:
```sh
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117
```

CUDA 11.7 Install:
`https://developer.nvidia.com/cuda-11-7-0-download-archive`

CUDNN 11.x Install:
`https://developer.nvidia.com/rdp/cudnn-archive`


---
## Installation 
1. **Create an Anaconda environment:**
```sh
conda create -n jk python=3.8
```

2. **Activate the environment:**
```sh
conda activate jk
```

3. **Clone this repository to your local machine:**
```sh
git clone https://github.com/kdrkdrkdr/JK-VITS.git
```

4. **Navigate to the cloned directory:**
```sh
cd JK-VITS
```

5. **Install the necessary dependencies:**

```sh
pip install -r requirements.txt
pip install -U pyopenjtalk==0.2.0 --no-build-isolation
```

---
## Preparing Dataset Example

- Place the audio files as follows. 
.wav files are okay. The sample rate of the audio must be 44100 Hz.


- Preprocessing (g2p) for your own datasets. Preprocessed phonemes for your dataset.
```sh
python preprocess.py --filelists filelists/train.txt filelists/val.txt
```

- Set configs.
  * If you train with japanese dataset, refer [configs/ja.json](configs/ja.json)
  * If you train with korean dataset, refer [configs/ko.json](configs/ko.json)

- You can download and use [pretrained_model](https://github.com/kdrkdrkdr/JK-VITS/releases) to finetuning.
  * If you train with korean dataset, use [korean_pretrained_dataset](https://github.com/kdrkdrkdr/JK-VITS/releases/tag/korean_pretrained_model) (Completed)
  * If you train with japanese dataset, use [japanese_pretrained_dataset](https://github.com/kdrkdrkdr/JK-VITS/releases/tag/japanese_pretrained_model) (Work In Process)

- Write Transcripts.
  * If you train with japanese dataset
  ```
  path/to/XXX.wav|[JA]こんいちわ。[JA]
  ```
  * If you train with korean dataset
  ```
  path/to/XXX.wav|[KO]안녕하세요.[KO]
  ```


---
## Training Exmaple
```sh
python train.py -c configs/ft.json -m ft
```

---
## Inference Exmaple
See [inference.ipynb](inference.ipynb)


---
## References
For more information, please refer to the following repositories: 
- [jaywalnut310/vits](https://github.com/jaywalnut310/vits.git)
- [MasayaKawamura/MB-iSTFT-VITS](https://github.com/MasayaKawamura/)
- [Kyubyong/g2pK](https://github.com/Kyubyong/g2pK)