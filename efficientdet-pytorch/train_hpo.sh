#!/bin/bash
shift
torchrun --nproc-per-node=1 --master-port 3000 train_hpo.py ../data/VOCdevkit --model tf_efficientdet_d2 --dataset voc2007 -b 8 --lr .008 --warmup-epochs 0 --model-ema --model-ema-decay 0.9966 --epochs 10 --num-classes 20 --pretrained