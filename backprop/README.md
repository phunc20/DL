# 起源與目標
我剛接觸 neural network 的時候是在上班的時候工作上的需要. 但是上班的時間不允許我花太多時間和功夫在理論上,
對於 backprop 或者說對於簡單的 neural network 的微分, 我當時雖然自己有利用閒暇的時間整理, 但一直覺得哪裏
怪怪的, 沒能搞得很清楚. 一直到 2021/01/20 辭職後的幾個月後, 我才真的有空和有幸看出自己被卡住的點在哪裏,
並且提出解決的方法. 因爲這有一點原創性, 和是自己理清出來的, 所以我想大概有一點值得分享的價值, 於是決定
寫成 pdf 放在GitHub 上.

這裏 (`nn_andrew_ng.pdf`), 我用
(Andrew Ng 某個 mooc 裏的簡單的 neural network 的例子)[https://www.coursera.org/lecture/neural-networks-deep-learning/backpropagation-intuition-optional-6dDj7],
是個只有大概兩三層 (i.e. two or three layers) 的一般 neural network, 不是 CNN, 還是什麼其他比較複雜的結構.
不過至少, 第一步我們要瞭解這麼簡單的結構產生出的 backprop, 之後才適合討論更複雜的.

## 修正
抱歉, 我一開始想用中文寫, 但後來發現自己 $\LaTeX$ 實在太弱了, 只好先用英文 (`en_nn_andrew_ng.pdf`),
但是寫完以後, 發現花太多時間了, 所以或許暫時不會有中文的版本.
主要是中文有些常用字我的 xelatex 在 gentoo/artix 上竟然顯示不出來, 只好先作罷了.

## Code
Andrew Ng 的課程是有 code 的, 不過方便起見, 如果有人對於這個簡單的 neural network 的 code 該課程如何呈現有興趣的話,
可以參考下列網址, 或者其他網址, 網路上應該不乏類似的分享, 畢竟是門當初相當受到歡迎的課.
- [https://github.com/phunc20/deeplearning.ai/blob/main/dl/2019/01-neural_networks_deep_learning/03-shallow_neural_networks/02-programming_assignment/Planar%2Bdata%2Bclassification%2Bwith%2Bone%2Bhidden%2Blayer%2Bv5--phunc20.ipynb](https://github.com/phunc20/deeplearning.ai/blob/main/dl/2019/01-neural_networks_deep_learning/03-shallow_neural_networks/02-programming_assignment/Planar%2Bdata%2Bclassification%2Bwith%2Bone%2Bhidden%2Blayer%2Bv5--phunc20.ipynb)
- [https://github.com/phunc20/deeplearning.ai/blob/main/dl/2019/01-neural_networks_deep_learning/03-shallow_neural_networks/02-programming_assignment/my_derived_formulae.ipynb](https://github.com/phunc20/deeplearning.ai/blob/main/dl/2019/01-neural_networks_deep_learning/03-shallow_neural_networks/02-programming_assignment/my_derived_formulae.ipynb)

