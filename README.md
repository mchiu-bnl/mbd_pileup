# mbd_pileup
Train ML models to ID pileup events using MBD data

## Models and/or ML Frameworks
The models used and their original source code if it exists are

Autogluon (using a variety of models:  

## Directions
You will likely have to install all the dependencies below.  Autogluon only works with certain versions of python, with python 3.12 being the most recent supported (as of 8/7/25).  Note that you may have to modify your PYTHONPATH so that it is not pointing to modules from a different version of python.

It's always recommended to use virtual environments, [venv](https://docs.python.org/3/tutorial/venv.html).  A recent better alternative is to use [UV](https://docs.astral.sh/uv/).

Once you have installed all the dependencies, then you will need the training and test data (csv format).  They are too large for git.

Once you have the training data, test the training code with

<code>python run_autogluon.py</code>

If it works, you should run this under condor with

<code>./submit.sh python run_autogluon.py</code>

The final output should be a set of predictions for each possible event, and saved in a csv file. 
 
## Instructions for using UV to install python modules on SDCC

First install [UV](https://docs.astral.sh/uv/) using

`curl -LsSf https://astral.sh/uv/install.sh | sh`

Next set up a UV virtual environment that uses python 3.12:

`uv install python3.12`

`uv init            # create uv project`

`uv venv .venv     # create virtual environment`

Activate the virtual environment:

`source .venv/bin/activate`

Install the dependencies, eg,

`uv pip install autogluon`

Install whatever modules are needed.

If you run out of disk quota on your home disk, you can move the ~/.cache and ~/.local directories to a work disk, and make symlinks back to your home disk:

mv ~/.cache /sphenix/user/[my_username]/
ln -s /sphenix/user/[my_username]/.cache ~/.cache

### Dependencies
- Python 3.12
- numpy
- pandas
- sklearn
- autogluon

