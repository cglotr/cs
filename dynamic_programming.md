# Dynamic programming
## Summary
It can be seen as a recursion with caching. That is, we cache the results of recursive calls in a
table for later use. Instead of doing the recursive calls all over again, we can just do table look
ups to get the results we wanted.

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
the table, thus avoiding costy recomputation.

Usually applicable to **optimization problems**, where a problem might have many solutions and we
want to get to any solution with the optimal value.

## Requirements for any optimization problem to be applicable to DP
### Exhibit optimal sub-structure
A problem has optimal sub-structure when the optimal solution to the problem contain within it,
optimal solutions to sub-problems. For example, `f(n) = f(n - 1) + f(n - 2)`.
### Overlapping sub-problems
This is where the speed up comes from. When a problem has overlapping sub-problems, we can store the
result when we first compute it in a table. By looking up the solution for subsequent overlapping
sub-problems, we are reducing the cost of computing the given sub-problem to `O(1)` time.
