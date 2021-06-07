### A Pluto.jl notebook ###
# v0.14.7

using Markdown
using InteractiveUtils

# ╔═╡ c648f884-c769-11eb-3dfb-6f3a0468a19f
begin
  using Pkg
  Pkg.activate(Base.Filesystem.homedir() * "/.config/julia/projects/oft")
  using Plots
  using LinearAlgebra
end

# ╔═╡ 0cb4615d-52c0-4307-bc0f-4f08cda3d2b5
md"""
# 緣由
因爲本身工作上被指派到一個跟偏微分方程有關的任務, 於是我複習起一些以前學過的微分方程的知識.
想到幾年前有一篇叫做 NeuralODE 的論文, 雖然跟分派的任務大概沒什麼關係, 但是想說利用空閒
時間一併讀看看. Adjoint method 一詞我就是第一次在那篇論文裏讀到; 本身雖然是數學系畢業的,
但是讀的時候完全不懂那是什麼樣的一個方法, 所以覺得很不好意思. 於是就上網找找相關的解說,
發現似乎在應用的領域, 特別是氣象學裏, 這似乎是一個很多人使用的一種計算方式, 但是從開始
尋覓對於這個 adjoint method 的理解至今大約有一個禮拜的時間了, 我還是不是很清楚這個東西.

這個 notebook 的目的在於

01. 記錄下自己的理解
02. 讓別人更容易看到並幫助解決自己的問題
03. 將來有更正確的理解再往下繼續寫
"""

# ╔═╡ f3595c26-409f-4d8d-80bb-1bb0de4d59e1
md"""
## 文章
以下是少數的幾篇我讀過的文章:

- [Notes on Adjoint Methods for 18.335, _Steven G. Johnson_](https://math.mit.edu/~stevenj/18.336/adjoint.pdf)
- [What Is an Adjoint Model?, _Ronald M. Errico_](http://twister.caps.ou.edu/OBAN2019/Errico_BAMS_1997.pdf)

Johnson 先生的文章是我第一個選擇讀的, 因爲它看起來似乎比較平易近人. 不過我大致讀過一次以後, 發現自己還是不太懂這一切到底在搞什麼, 於是該天晚上我轉而去讀 Errico 先生的文章. 我自己的經驗是 Errico 先生的文章寫得落落長, 但是不容易抓到作者到底要講什麼; 而 Johnson 先生的文章算式比較多, 但是還是有點隱晦. 

諷刺的是, 我是在讀 Errico 覺得很睏, 很無趣的時候, 突然意識到 Neural Network 的簡單, 具體的例子在 Johnson 的文章裏應該對應到哪些函數, 哪些式子.
"""


# ╔═╡ 9dce273d-8e85-498e-af84-59f077499eeb
md"""
Johnson 先生把對於能應用 adjoint method 的問題歸結如下:
> 首先我們有一個向量 $p \in \mathbb{R}^{n_{p}}$ 可以想成是 Neural Network 的參數 ($p$ for "_**p**arameters_")
>
> 隨之, 我們有一個向量 $x \in \mathbb{R}^{n_{x}}$ 以及 一個 $x$ 和 $p$ 共同滿足的等式 $f(x, p) = 0\,,$ 其中 $f: \mathbb{R}^{n_{x}} \times \mathbb{R}^{n_{p}} \to \mathbb{R}^{n_{x}}\,.$
> (這個等式是我們之後要解 $x = x(p)$ 用的, 所以值域的維度要等於 $x$ 所在空間的維度.)
>
> 最後是我們要解決的問題: 給一實值 (i.e. real-valued) 函數
> $g:\mathbb{R}^{n_{x}} \times \mathbb{R}^{n_{p}} \to \mathbb{R}\,,$
> 試着找出這個函數的最小值 $g(x, p)$ 其中 $x$, $p$ 滿足 $f(x, p) = 0\,.$


**附註.** Johnson 先生的文章比較像是上課用的講義, 寫得很快, 沒有很清楚, 以上算是加入我自己的整理和理解後的樣子, 希望沒有失真/正確性.
"""

# ╔═╡ Cell order:
# ╟─0cb4615d-52c0-4307-bc0f-4f08cda3d2b5
# ╠═c648f884-c769-11eb-3dfb-6f3a0468a19f
# ╟─f3595c26-409f-4d8d-80bb-1bb0de4d59e1
# ╟─9dce273d-8e85-498e-af84-59f077499eeb
