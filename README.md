# pictotxt 

[![Build Status](https://travis-ci.org/SpaceVim/SpaceVim.svg?branch=master)](https://travis-ci.org/lazydancer/pictotxt)

## About

**pictotxt** is a python script which converts an image to text

![pictotxt](https://raw.githubusercontent.com/lazydancer/pictotxt/master/examples/movie.gif)

## How to use

Requirements:
- Python Image Library (PIL)
- Numpy

```
git clone git@github.com:lazydancer/pictotxt.git
cd pictotxt
pip install -r requirements
python src/pictotxt.py examples/octocat.png
```

The result will be printed on your console/terminal

## How it works

Input:

![step1](https://raw.githubusercontent.com/lazydancer/pictotxt/master/examples/step1.png)

The imported image is split up into 'character sized' images. 

![step2](https://raw.githubusercontent.com/lazydancer/pictotxt/master/examples/step2.png)

Split of the font to get individual images of each character

![step3](https://raw.githubusercontent.com/lazydancer/pictotxt/master/examples/step3.png)

For each mini-image from the imported image, compare it with all the characters and find the best match with the following function

![step4](https://raw.githubusercontent.com/lazydancer/pictotxt/master/examples/step4.png)

Result:

<img src="https://raw.githubusercontent.com/lazydancer/pictotxt/master/examples/step5.png" width="366">

