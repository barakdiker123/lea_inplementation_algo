
# Table of Contents

1.  [Website](#orge41dc35)
2.  [Quickstart](#orga25d2a7)
3.  [Visualizations](#orgb350156)
4.  [Abstract](#org13d4f12)
    1.  [Input](#org731cf12)
    2.  [Goal](#orgdef4cd4)
5.  [Command to test](#org5fa6201)
6.  [Algorithm Local Search Barak&rsquo;s heuristic](#orgaa4b9be)
7.  [Improvements and Significal developmets](#orgcd14632)



<a id="orge41dc35"></a>

# Website

For Reading the docs with beautiful web please visit
[website better graphics](https://barakdiker123.github.io/lea_inplementation_algo/)


<a id="orga25d2a7"></a>

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


<a id="orgb350156"></a>

# Visualizations

for animation creation one can use the following command

    python local_search_algorithm.py --input_path possible_solutions/sol3/input/input.py --output_dir possible_solutions/sol3 --visualize_simple --animation_flag

This will create a new folder in `output` directory called `animation` with GIF


<a id="org13d4f12"></a>

# Abstract

The Project try to solve the following schedule problem

Scheduling with cardinality constraints.


<a id="org731cf12"></a>

## Input

An integer number of (identical) machines m ≥ 2. A set of n jobs J =
{1, 2, . . . , n}, where job j has an integer processing time p<sub>j</sub> > 0. A positive integer
parameter k.


<a id="orgdef4cd4"></a>

## Goal

Find a partition (assignment) of the jobs into subsets, I<sub>1</sub>, I<sub>2</sub>, . . . , I<sub>m</sub>, where
for any 3 ≤ i ≤ m, it holds that |I<sub>i</sub>| ≤ k (a cardinality constraint of k is enforced for
all machines except for possibly the first two machines, that is, every machine whose
index is at least 3 can receive at most k jobs).


<a id="org5fa6201"></a>

# Command to test

    sudo python launcher.py --input_path possible_solutions/lea_inputs/question_3/2l/input/input.py --output_dir possible_solutions/lea_inputs/question_3/2l --visualize_simple --animation_flag


<a id="orgaa4b9be"></a>

# Algorithm Local Search Barak&rsquo;s heuristic

How the Final algorithm works
Given an array of jobs which I&rsquo;ll call processing<sub>arr</sub> , number of machines which will be marked with m , and a maximus job number for machine of greater index of 3 which be be marked as k

The following process will take place

-   Create array of array of size m which named machines
-   Put all the jobs on machine 0 (The first machine)
-   Create PseudoArray of machine jobs of size m which named previous-machines
-   While machines not equals to previous-machines
    -   While a move occured 
        -   from the machine which has the highest **processing time** move the longest possible job to the machine which has the lowest processing time under the problem constraint
    
    -   While a move occured 
        -   from the machine which has the highest **job count** move the longest possible job to the machine which has the lowest **job count** under the problem constraint
    
    -   While a move occured 
        -   from the machine which has the highest **processing time** move the longest possible job to the machine which has the lowest processing time under the problem constraint
    
    -   For all 2 machines and all job in the first machine and all job in second machine exchange the 2 jobs and if the overall processing time has decreased apply the change and exit the loops


<a id="orgcd14632"></a>

# Improvements and Significal developmets

-   At first I have tried to move jobs under constraint until there is not more moves and then exchange once,
    -   This Procedure was not effective
-   I&rsquo;ve tried couple of different combinations of movement and exchanges that were not so great

