$f(x)=ax^2+bx+c$

$DP_0=0$

$DP_i=max_{j<=i}\{DP_{j-1}+f(sum_{ji})\}
\\ =max_{j<i}\{DP_{j}+f(sum_{i}-sum_{j})\}$

$f(x-k)-f(x)=-2akx+ak^2-bk$ 이므로

$DP_{j}+f(sum_{i}-sum_{j})$에 대한 최댓값을 구할 때는

$q=DP_j+ak^2-bk\;(k=sum_{j})$에 대한 전처리 이후
$p=-2akx\; (x=sum_{i})$에 대해

$y=px+q$의 $cht$를 적용하면 된다.
