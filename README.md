# Visual Secret Sharing

Given three black and white images $A$, $B$ and $C$ , the algorithm creates three new versions of them, $\tilde{A}$, $\tilde{B}$ and $\tilde{C}$, which resemble the original corresponding images. Whoever has access to $\tilde{A}$ and $\tilde{B}$ simultaneously may easily compute $\tilde{C}$. Yet, If someone has only access to one of them, say $\tilde{A}$, he has absolutely no way to find out what's in image $\tilde{C}$. It is as hard as finding out what's in picture $\tilde{B}$. In this context, we call $\tilde{C}$  "the secret", and we call $\tilde{A}$ and $\tilde{B}$  "the shares".

Formally, the algorithm takes three black and white input pictures of size $w\times h$. It returns three new images $\tilde{A}$, $\tilde{B}$ and $\tilde{C}$, such that for every $X\in\{A,B,C\}$:

1. $\tilde{X}$ is of size $2w \times 2h$.

2. $\tilde{X}$ resembles $X$, and may expose information regarding $X$.

3. For every $Y\in\{A,B,C\}\backslash\{X\}$, $\tilde{X}$ does not expose any information regarding $Y$.

4. There's a deterministic computation we can apply on $\tilde{A}$ and $\tilde{B}$  to get $\tilde{C}$ as a result. The $(i,j)$ pixel of $\tilde{C}$ has the following property:
   $$
   \tilde{C}_{i,j}=
   \begin{cases}
   	\text{white}	&	\text{if } \tilde{A}_{i,j}=\text{white} \text{ and } \tilde{B}_{i,j}=\text{white} \\
   	\text{black}	&	\text{otherwise}
   \end{cases}.
   $$

![Demonstration](https://github.com/idodoron11/crypto_ex9_visual_secret_sharing/raw/master/demonstration.gif)

## Example

Let's look at the following three input pictures:

| $A$  | ![A](https://raw.githubusercontent.com/idodoron11/crypto_ex9_visual_secret_sharing/master/a.jpg) |
| ---- | ------------------------------------------------------------ |
| $B$  | ![B](https://raw.githubusercontent.com/idodoron11/crypto_ex9_visual_secret_sharing/master/b.jpg) |
| $C$  | ![C](https://raw.githubusercontent.com/idodoron11/crypto_ex9_visual_secret_sharing/master/c.jpg) |

The algorithm transforms them into three new versions:



| $\tilde{A}$ | ![A_tilde](https://raw.githubusercontent.com/idodoron11/crypto_ex9_visual_secret_sharing/master/A.bmp) |
| ----------- | ------------------------------------------------------------ |
| $\tilde{B}$ | ![B_tilde](https://raw.githubusercontent.com/idodoron11/crypto_ex9_visual_secret_sharing/master/B.bmp) |
| $\tilde{C}$ | ![C_tilde](https://raw.githubusercontent.com/idodoron11/crypto_ex9_visual_secret_sharing/master/C.bmp) |

It appears that both $\tilde{A}$ and $\tilde{B}$ resemble $A$ and $B$, and yet each of them independently doesn't compromise the secret $\tilde{C}$. However, if someone has both $\tilde{A}$ and $\tilde{B}$ he may find $\tilde{C}$ quickly:
$$
\tilde{C}_{i,j}=
\begin{cases}
	\text{white}	&	\text{if } \tilde{A}_{i,j}=\text{white} \text{ and } \tilde{B}_{i,j}=\text{white} \\
	\text{black}	&	\text{otherwise}
\end{cases}.
$$
