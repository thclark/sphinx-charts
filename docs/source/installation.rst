

.. _installation:

============
Installation
============

**sphinx_charts** is available on pypi so installation into your virtual environment is dead simple:

.. code-block:: python

   poetry add sphinx_charts

.. attention::

   Still using ``pip``? ``poetry`` will be a short learning curve but saves you lots of dependency pain. It's your friend. Google it.

Now, add ``sphinx_charts`` to your extensions in ``conf.py`` and you'll be ready to go:

.. code-block:: python

   extensions = [
       ...
       'sphinx_charts.charts'
       ...
   ]
