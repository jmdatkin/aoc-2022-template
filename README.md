# Advent of Code 2022 Starter Template
Puzzle starter code for the [Advent of Code 2022](https://adventofcode.com/2022/).

This template is meant to simplify the process of parsing values from the text input provided by Advent of Code and similar competitive coding sites.

## Usage

The `lines` function contained in the `input` module parses the lines of a text file and applies a custom mapping function:

```python
def lines(filename, cb)
```

The first parameter specifies a file path to read from.
The second parameter targets a function which will receive as its first parameter each successive line of input, and which returns a mapped value derived from the text input.

`lines` returns an array containing the mapped values of every line of text.


### Example:
Consider an input formatted as following, where we want to extract the values:
```
82-82,8-83
6-98,6-93
56-77,55-82
51-68,51-61
4-90,3-67
29-30,29-97
42-88,13-87
17-95,33-96
11-56,12-56
16-90,89-94
74-79,78-80
20-82,19-87
4-86,5-85
...
```

A useful callback function might be:
```python
def cb(line):
    return [k for k in [j.split('-') for j in line.split(',')]]
```

This callback function parses a line of input into a 2D array holding pairs of values:

```python
[
    [
        [82,82], [8,83]
    ],
    [
        [6,98], [6,93]
    ],
    ...
]
```

Enjoy, and happy coding! 😎