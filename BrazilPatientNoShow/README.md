# BrazilPatientNoShow

## 综述

​	在巴西Espirito Santo州首府Vitória市，20%的病人预约医生后没能就诊。病人们的失约每年为该市的公共卫生系统造成2000万美元的亏损。这份报告将探索一份由该市的数据分析志愿者提供的10万+行数据集，尝试总结规律，以找到背后的原因。

​	在对数据集有了初步的认识之后，我们将通过3个方向上8个具体问题的问题进行研究，分别涵盖病人，预约后等待日期和街区。随后，在这些问题的引导之下，我们根据需求进行了数据的整理和清洗，并进行了探索性的数据分析。最后，我们构筑了逻辑回归，决策树，但我们的模型准确率尚低，不足以运用。我们同时使用了并利用autosklearn构建复合模型，但疑似因为样本分布不均衡的问题，导致这一模型的F1分数很低。

​	我们发现了如下规律，以供后续研究进一步探索：1）病人们的等待时间越长，失约率越高；2）收到短信的用户失约率较高，但短信与病患等待时间有线性关系，这也意味着短信作为预防失约机制理论上还有提升的空间。总的来说，我们在探索中的提取变量不能很好的解答病人失约的问题，利用这些变量构建的机器学习存在高偏差的现象。对这一现象进一步的探索还需要对变量之间的关系进行进一步的挖掘和研究。



## Repo文件说明

- 项目主文件：
  - [巴西病人-20190321.ipynb](https://github.com/willliu1995/BrazilPatientNoShow/blob/master/%E5%B7%B4%E8%A5%BF%E7%97%85%E4%BA%BA-20190321.ipynb)：报告主体
  - [巴西病人-预测2.ipynb](https://github.com/willliu1995/BrazilPatientNoShow/blob/master/%E5%B7%B4%E8%A5%BF%E7%97%85%E4%BA%BA-%E9%A2%84%E6%B5%8B2.ipynb)：尝试使用机器学习预测病人失约情况（效果不好）
  - [tree.pdf.pdf](https://github.com/willliu1995/BrazilPatientNoShow/blob/master/tree.pdf.pdf)：预测文件生成的决策树
  - [auto-sklearn](https://github.com/willliu1995/BrazilPatientNoShow/tree/master/auto-sklearn)：尝试使用autosklearn构建复合模型（然而效果更不好）
- 数据集：
  - [noshowappointments-kagglev2-may-2016.csv](https://github.com/willliu1995/BrazilPatientNoShow/blob/master/noshowappointments-kagglev2-may-2016.csv) ：原始数据文件
  - [noshowappointments-kagglev2-may-2016-utf-8-C.xlsx](https://github.com/willliu1995/BrazilPatientNoShow/blob/master/noshowappointments-kagglev2-may-2016-utf-8-C.xlsx)： 使用UTF-8模式读物的数据文件
  - [noshowappointments-kagglev2-may-2016_clean.csv](https://github.com/willliu1995/BrazilPatientNoShow/blob/master/noshowappointments-kagglev2-may-2016_clean.csv)： 经过数据清洗的数据，仅包含部分衍生变量