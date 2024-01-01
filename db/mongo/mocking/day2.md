---
title: Day 2
author: John Doe
tags: [statistics, math]
date: 2024-12-02
---

## Advent of Code - Day 2

### Problem Description

Santa's elves are working in a gift-wrapping factory. Each gift needs to be 
wrapped with a specific amount of wrapping paper. The dimensions of each gift 
are given as length, width, and height. Additionally, Santa wants to add a 
little extra paper for the ribbon.

To calculate the total amount of wrapping paper needed, you need to find the 
area of the smallest side and add twice the sum of the smallest and 
second-smallest sides. For the ribbon, find the smallest perimeter of any two 
dimensions and add the volume of the gift.

### Input

A list of dimensions for each gift in the format "length x width x height".

### Output

The total amount of wrapping paper needed for all gifts and the total amount 
of ribbon needed.

### Example

Input: 

```text
2x3x4
1x1x10
4x5x6
```

Output:

```
Total Wrapping Paper Needed: 96 square feet
Total Ribbon Needed: 34 feet
```