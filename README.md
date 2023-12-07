# k-Cores: Greedy Algorithm

## Overview
This project, centered around the theme of greedy algorithms, delves into the design and implementation of a novel approach for identifying k-cores within a graph. A k-core is defined as a maximal connected subgraph where every vertex possesses a degree of at least k. By leveraging the concept of locally optimal choices, the algorithm aims to efficiently determine these dense subgraphs, reducing the computational complexity of the problem. The README provides a comprehensive guide to the algorithm, its implementation, and a lemma supporting its optimality.

## Part 1: k-Cores Algorithm
The algorithm adeptly discovers all k-cores within a given graph. Rooted in key observations, such as the nested hierarchy of k-cores, the design ensures efficiency and correctness. Input graphs are represented as edge lists, and the program outputs k-cores in a specific, well-defined format.

### Example Usage
```bash
$ ./compile.sh
$ ./run.sh input_graph.txt
Vertices in 1-cores:
0, 1, 2, 3, 4, 5
Vertices in 2-cores:
0, 1, 2
```
## Part 2: Greedy Stays Ahead
In this problem, the quantity being optimized is the size of each k-core, with a focus on maximality. To provide a theoretical foundation for the algorithm's optimality, the README introduces a lemma:

### Lemma
Suppose your algorithm returns the k-cores X = (x1, x2, ..., xn−1), and there exist optimal k-cores Opt = (y1, y2, ..., yn−1), where xi, yi are sets of vertices in i-cores. For all i < n, yi ⊆ xi. In simpler terms, the vertices in the algorithm's k-cores are subgraphs of the vertices in the optimal k-cores.

#### Example
Given the above graph, the optimal k-cores are Opt = ({v0, v1, v2, v3, v4, v5}, {v0, v1, v2}, ∅, ∅, ∅), ordered from the 1-core to the 5-core.

**report.pdf:** Pseudocode for an efficient, greedy algorithm to find k-cores, along with proof of the lemma given in Part 2 and analysis of complexity for the pseudocode.
