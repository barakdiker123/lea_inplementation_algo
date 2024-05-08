
# Table of Contents

1.  [Website](#org2ea9f56)
2.  [Quickstart](#org53a3b7d)
3.  [Abstract](#orge876f3a)
    1.  [Input](#org7f1b0ea)
    2.  [Goal](#orgc97be5e)



<a id="org2ea9f56"></a>

# Website

For Reading the docs with beautiful web please visit
[website better graphics](https://barakdiker123.github.io/lea_inplementation_algo/)


<a id="org53a3b7d"></a>

# Quickstart

In order to run the program one should clone the repo and run the following command

    python local_search_algorithm.py --input_path test/input/input.py --output_dir test_dir

the `input_path` should point to a python file for example input.py
and should have the following content

    m = 6
    k = 5
    processing_arr = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5]

if one get stuck he can read the docs via the command

    python  local_search_algorithm.py --help

One should note that the final solution to the problem is in the `output_dir` under the name `output_score.txt` ,

also there is more output contents


<a id="orge876f3a"></a>

# Abstract

The Project try to solve the following schedule problem

Scheduling with cardinality constraints.


<a id="org7f1b0ea"></a>

## Input

An integer number of (identical) machines m ≥ 2. A set of n jobs J =
{1, 2, . . . , n}, where job j has an integer processing time p<sub>j</sub> > 0. A positive integer
parameter k.


<a id="orgc97be5e"></a>

## Goal

Find a partition (assignment) of the jobs into subsets, I<sub>1</sub>, I<sub>2</sub>, . . . , I<sub>m</sub>, where
for any 3 ≤ i ≤ m, it holds that |I<sub>i</sub>| ≤ k (a cardinality constraint of k is enforced for
all machines except for possibly the first two machines, that is, every machine whose
index is at least 3 can receive at most k jobs).

