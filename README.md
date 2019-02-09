# Variable corelation

[value_functions.py](value_functions.py) will keep a list of signal
altering functions to be used for expressing correlations among
variables in the vector.

Just now it contains a discrete factor, with progressive growth
arbitrarily setup. And an example square function.

The *CriteriaVector* class will use whatever function matrix to update
its variable vector, given a delta for a single variable.


## Installation

    $ virtualenv -p python3 venv3
	$ source venv3/bin/activate
	(venv3) $ pip install pytest
	
## Tests

Read test for API usage.

Run test thusly:

    $ python -m pytest
