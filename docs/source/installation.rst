
.. attention::

   Don't have a virtual environment with pip? You probably should! ``pyenv`` is your friend. Google it.

.. _installation:

============
Installation
============

**sphinx_charts** is available on pypi so installation into your virtual environment is dead simple:

.. code-block:: python

   pip install sphinx_charts

Now, add ``sphinx_charts`` to your extensions in ``conf.py`` and you'll be ready to go:

.. code-block:: python

   extensions = [
       ...
       'sphinx_charts.charts'
       ...
   ]
