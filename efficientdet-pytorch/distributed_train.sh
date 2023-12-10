#!/bin/bash
shift
torchrun --nproc-per-node=1 train.py ../data/VOCdevkit --model tf_efficientdet_d2 --dataset voc2007 -b 8 --lr .008 --warmup-epochs 3 --model-ema --model-ema-decay 0.9966 --epochs 150 --num-classes 20 --pretrained