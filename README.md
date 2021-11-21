# stochastic-ramsey
## Table of contents
- [ Purpose ](#purpose)
- [Requirements](#req)
- [Usage](#usage)
- [Code structure](#str)

<a name="purpose"></a>
## Purpose
Task was to solve the stochastic infinite-horizon Ramsey growth model via value function iterations algo on a discrete grid of states.

<a name="req"></a>
## Requirements
```bash
pip3 install -r requirements.txt
```

<a name="usage"></a>
## Usage
Just run `main.py` and have fun 😎

<a name="str"></a>
## Code structure
### `markov_ar.py`
Approximates AR(1)-Process by Markov chain

### `bilinear intepolation`
Bilinear intepolation, used for the computation of the policy function

### `policy.py`
Calculates the policy function via bilinear interpolation, used for the calculation of the Euler residuals

### `euler.py`
Computes Euler residuals

### `solver.py`
Computes the policy function for a Stochastic Infinite-Horizon Ramsey Model

### `utility.py`
Contains the one-period utility function of the model

### `consts.py`
File with global constants
