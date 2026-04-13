1. 재귀

2. 2sat (근데 scc를 안 쓰는)

a와 b가 연결되어 있지 않다면, 반드시 다른 곳에 있어야 함.

따라서 $(a \vee b)\wedge((\sim a)\vee (\sim b))\dots $의 2sat 식을 세울 수 있음.
