# Hyperparameter-Optimization

## Google Vizer
https://github.com/google/vizier
### User
>for inference

Configuration type
* double
* inter
* dicrete
* categorical
* bool
* conditional search space : 調整 tree 架構的 configuration

Algorithm
![image](https://hackmd.io/_uploads/Syafdl0Sp.png)

### Developer
>for training

寫一個調整設定的物件
![image](https://hackmd.io/_uploads/rJv7jeAra.png)

## HEBO
https://www.bing.com/search?q=hebo+github&qs=SC&pq=hebogithub&sc=1-10&cvid=4897F8DD7E7646238A43370A3489E959&FORM=QBRE&sp=1&ghc=1&lq=0

opt.suggest(n_suggestions=1)
>吐出 dataframe

opt.observe(rec, obj(rec))
>rec : suggestion
>obj(rec) : nd.array

Results
![image](https://hackmd.io/_uploads/ry-dZRNUp.png)
>9 設定，每個設定超過 200 種組合

100 次以內收斂

技術補充
>https://zhuanlan.zhihu.com/p/374415112

## BO
https://github.com/bayesian-optimization/BayesianOptimization

![image](https://hackmd.io/_uploads/SyRDwGIIp.png)


![image](https://hackmd.io/_uploads/HJXwPM88T.png)

![image](https://hackmd.io/_uploads/H1NYPMI8p.png)
