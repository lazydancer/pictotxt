# pictotxt 

[![Build Status](https://travis-ci.org/SpaceVim/SpaceVim.svg?branch=master)](https://travis-ci.org/lazydancer/pictotxt)

## About

**pictotxt** is a a python script which takes an image and outputs text in the form of the input image

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

Input an image

![step1](https://raw.githubusercontent.com/lazydancer/pictotxt/master/examples/step1.png)

Take the imported image and converting it to character sized images. 

![step2](https://raw.githubusercontent.com/lazydancer/pictotxt/master/examples/step2.png)

Split of the font to get individual images of each character

![step3](https://raw.githubusercontent.com/lazydancer/pictotxt/master/examples/step3.png)

For each mini-image from the imported image, it is compared to each character till the closest value is found. It is found using the following objective function

![step4](https://raw.githubusercontent.com/lazydancer/pictotxt/master/examples/step4.png)

We get the final image as text

<img src="https://raw.githubusercontent.com/lazydancer/pictotxt/master/examples/step5.png" width="366">

