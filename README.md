
## Prerequisites
- Linux or macOS
- Python 3
- CPU or NVIDIA GPU + CUDA CuDNN

## Getting Started
### Installation

- Clone this repo:
```bash
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
cd pytorch-CycleGAN-and-pix2pix
```
### 
### CycleGAN train
训练数据集准备：

    root
    |
    ---datasets
       |
       ---data(自定义名称)
          |
          ---trainA
          ---trainB

- trainA：放入需要生成B类型的图片
- trainB：放入B类型图片



- To view training results and loss plots, run `python -m visdom.server` and click the URL http://localhost:8097.
- Train a model:
```bash
#!./scripts/train_cyclegan.sh
python train.py --dataroot ./datasets/test --name test_cyclegan --model cycle_gan
python test.py --dataroot ./datasets/test --name test_cyclegan --model cycle_gan
python test.py --dataroot ./datasets/feishi --name feishi_cyclegan --model cycle_gan
```

结果保存路径`./checkpoints/maps_cyclegan/web/index.html`.


### CycleGAN test
测试数据集准备：

    root
    |
    ---datasets
       |
       ---data(自定义名称)
          |
          ---testA
          ---testB

- testB至少放入一站图片
- Test the model:
```bash
#!./scripts/test_cyclegan.sh
python test.py --dataroot ./datasets/cz --name cz_cyclegan --model cycle_gan
```
保存A->B, B->A所有图像
```bash
python test.py --dataroot ./datasets/cz --name cz_cyclegan --model cycle_gan --saveAll
```
运行结果保存路径: `./results/maps_cyclegan/latest_test/index.html`.




## 使用padding进行图像预处理训练、测试

### CycleGAN train
```bash
#填充图像进行训练，填充尺寸与load_size一致
#若样本尺寸差异较大，影响较大。目前代码采用256x256，剔除了超过该尺寸的样本进行训练
python train.py --dataroot ./datasets/cz --name cz_cyclegan --model cycle_gan --preproces padding
```
### CycleGAN test
```bash
python test.py --dataroot ./datasets/cz --name cz_cyclegan --model cycle_gan --preproces padding --dealpadding
```


### 超参设置

    root
    |
    ---options
          ---base_options.py
          ---test_options.py
          ---train_options.py


