# Bioinformatics

## Part 1 
*how random 2-breaks differ with min swap solution*

**distance** - min swaps to recover sorted array

**swap number** - count of random swaps to mix an array

n = *100*
swaps = *100*

![alt text](https://github.com/Timoniche/BioInf/blob/main/plots/size100swaps100)

n = *100*
swaps = *500*

![alt text](https://github.com/Timoniche/BioInf/blob/main/plots/size100swaps500)

n = *1000*
swaps = *1000*

![alt text](https://github.com/Timoniche/BioInf/blob/main/plots/size1000swaps1000)

n = *10000*
swaps = *10000*

![alt text](https://github.com/Timoniche/BioInf/blob/main/plots/size10000swaps10000)

## Part 2
*Cooler API*

https://github.com/open2c/cooler

https://github.com/open2c/cooler-binder

data in this project:

`wget ftp://cooler.csail.mit.edu/coolers/hg19/Rao2014-IMR90-MboI-allreps-filtered.500kb.cool
`
Plots:

range k = *1..10*

**E**(k)

![alt text](https://github.com/Timoniche/BioInf/blob/main/plots/chr1_EX_k_1_10)

**D**(k)

![alt text](https://github.com/Timoniche/BioInf/blob/main/plots/chr1_DX_k_1_10)

**SIGMA**(k)

![alt text](https://github.com/Timoniche/BioInf/blob/main/plots/chr1_SIGMA_k_1_10)

range k = *10..25*

**E**(k)

![alt text](https://github.com/Timoniche/BioInf/blob/main/plots/chr1_EX_k_10_25)

**D**(k)

![alt text](https://github.com/Timoniche/BioInf/blob/main/plots/chr1_DX_k_10_25)

**SIGMA**(k)

![alt text](https://github.com/Timoniche/BioInf/blob/main/plots/chr1_SIGMA_k_10_25)

## Part 3

https://github.com/Timoniche/BioInf/blob/main/interview_hic_problem.pdf

**3.1** Параметризовать эту кривую, то есть записать ее уравнение в виде (x(t), y(t)) 
(или написать скрипт, который рисует такую кривую).

![](https://github.com/Timoniche/BioInf/blob/main/solutions/gif_task3.gif)

*getting the relation:*

![alt text](https://github.com/Timoniche/BioInf/blob/main/solutions/archimedean.jpg)

*solution of the equation (using wolfram):*

![alt text](https://github.com/Timoniche/BioInf/blob/main/solutions/solution_max_t.png)

**3.2** Разбить хромосому на 1000 равных бинов по 500 Kb , и 
построить матрицу расстояний между центрами бинов.

*getting bin centers:*

![alt text](https://github.com/Timoniche/BioInf/blob/main/solutions/bin_centers.jpg)

*getting contact matrix*

https://github.com/Timoniche/BioInf/blob/main/log/part3.log



