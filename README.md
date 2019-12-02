# Advent of Code 2019

Created by [Eric Wastl](http://was.tl/), [Advent of Code](https://adventofcode.com/2019/about) is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as a speed contest, interview prep, company training, university coursework, practice problems, or to challenge each other.

You don't need a computer science background to participate - just a little programming knowledge and some problem solving skills will get you pretty far. Nor do you need a fancy computer; every problem has a solution that completes in at most 15 seconds on ten-year-old hardware.

## System

This project was created on a Macbook running MacOS Mojave.

## Software Requirements
This project uses [Python](https://www.python.org/about/) 3.8 and [Anaconda](https://www.anaconda.com/distribution/#macos) 4.7.12.

### `ac2019-env` conda environment

This project relies on you using the [`environment.yml`](environment.yml) file to recreate the `ac2019-env` [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html). 

To activate `ac2019-env` in your local environment, please run the following commands:

```bash
# create the ac2019-env conda environment
# note: this make take anywhere from 1-5 minutes
conda env create -f environment.yml

# activate the ac2019-env conda environment
conda activate ac2019-env
```
