$S=\{A, B, C\}$ 의 수열을 3등분할 때 점수가 최소가 되는 나누기 순서를 구해보자.

$a$: $A$와 $B$사이를 나눈다.

$b$: $B$와 $C$사이를 나눈다.

$\;$

1. $b \circ a=A(B+C)+BC=AB+BC+CA$

2. $a \circ b: (A+B)C+AB=AB+BC+CA$

결과적으로 수열을 나누는 동작(연산)은 교환법칙이 성립한다.

즉, 수열을 나누는 순서에 상관없이 나눠진 부분수열의 곱을 합하면 점수를 얻는다.

$\;$

$\quad A=\bigcap{T_i}$

$\;$

$\begin{align}
\quad score :
&\sum{sum(T_i)sum(T_j)\; (i!=j)}
\\
\\ &=(sum(A)^2-\sum sum(T_i)^2 )/2\end{align}$

DP[i][k]: 0~i까지 수열을 k등분했을 때 최소의 sum(T_i**2)값

$ $

$(S_i-S_j)^2+DP[j][k]=S_i^2-2S_iS_j+(DP[j][k]+S_j^2)$
