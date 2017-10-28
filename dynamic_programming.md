# Dynamic programming
## Summary
It can be seen as a recursion with caching. That is, we cache the results of recursive calls in a
table for later use. Instead of doing the recursive calls all over again, we can just do table
lookups to get the results we wanted.

Dynamic programming (DP) solves a problem by utilizing solutions to sub-problems of the original
problem. The type of problem that is solvable with DP is usually optimization problems that have
optimal sub-structures. We solve sub-problems of a problem either via a bottom-up or top-down
approach and record the results in a table, thus avoiding recomputing the sub-problems again.

## Key points
Solve a problem by utilizing/combining solutions to sub-problems.

The sub-problems used to compute the solution to the original problem overlap - that is,
sub-problems share sub-sub-problems.

DP only computes the solution to each of the common sub-sub-problems once by storing the result in a
table. The next time DP encounters the common sub-sub-problem, it will just look up the result from
the table, thus avoiding costly recomputation.

Usually applicable to **optimization problems**, where a problem might have many solutions and we
want to get to any solution with the optimal value.

## Requirements for any optimization problem to be applicable to DP
### Exhibit optimal sub-structure
A problem has optimal sub-structure when the optimal solution to the problem contains within it,
optimal solutions to sub-problems. For example, `f(n) = f(n - 1) + f(n - 2)`.
### Overlapping sub-problems
This is where the speedup comes from. When a problem has overlapping sub-problems, we can store the
result when we first compute it in a table. By looking up the solution for subsequent overlapping
sub-problems, we are reducing the cost of computing the given sub-problem to `O(1)` time.

## Practical step-by-step
### Figuring out the recurrence
The recursive formula is crucial to defining the table. But, coming up with a recursive formula to a
given problem is not trivial. Instead, try reverse engineering. Assume that table dp[i] works and
try to figure out the definitions of i and dp[i] that work. If it seems to be impossible, move up to
dp[i][j] and try to figure out what each of the components should mean. If it is still not viable,
move up again and so on.

### Choosing the choice
For any given table cell to fill, we usually have to choose the optimal value among several possible
choices. The table correctness relies on the choices we make to be correct. Do a few examples, to
come up with the correct way to choose them.

### Building up the table
First, start with filling up the base case for the table. This is easy if you have well-defined
recurrence formula.

Second, iterate the table from bottom-up. This is easy if your table is one-dimensional, but it can
get trickier with more dimensions. Make sure to build up the table so, for each f(n), the table has
all the information it needs to correctly compute the optimal solution for f(n).

### Returning the result
When the table construction is complete, we can now get our final result. If the table is built
correctly, the final result is guaranteed to be optimal.

## Mastery
Some tips on mastery:
- Practice a lot. Theory alone won't get you anywhere. Practice will develop the intuition which is
crucial when trying to solve a DP problem.
- Do both **bottom-up** (tabulation) method and **top-down** (memoized recursion) approach on each
practice problem.
- Build the intuition to figure out the **recurrence formula**.

## Video resource
- [Longest Common Subsequence](https://www.youtube.com/watch?v=tYzNrCul5OU)

## Practice problems
1. [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/description/)
2. [DP: Coin Change](https://www.hackerrank.com/challenges/ctci-coin-change/problem)
3. [712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/)
4. [343. Integer Break](https://leetcode.com/problems/integer-break/description/)
5. [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/description/)
