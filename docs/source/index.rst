Add badges and labels like this:

.. ATTENTION::
    This library is in very early stages. Like the idea of it? Please
    `star us on GitHub <https://github.com/{{github_username}}/{{repo_name}}>`_ and contribute via the
    `issues board <https://github.com/{{github_username}}/{{repo_name}}/issues>`_ and
    `roadmap <https://github.com/{{github_username}}/{{repo_name}}/projects/1>`_.

.. image:: https://codecov.io/gh/{{codecov_username}}/sphinx_charts/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/{{codecov_username}}/sphinx_charts
  :alt: Code coverage
  :align: right
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
  :target: https://github.com/ambv/black
  :alt: Code Style
  :align: right

=============
Sphinx Charts
=============

.. epigraph::
   *"Sphinx Charts" ~ Interactive charts, graphs and figures in Sphinx, using plot.ly and D3*


.. chart:: charts/validation_perry_marusic_12a.json

    They look $\lambda$ freaking glorious 😍. This one even has latex labels and a log axis. Have you tried exporting (hover over the chart for a control panel)? That gives you an actual ``SVG``, not just a screenshot 🤯.

.. chart:: charts/test_mandelbrot_plot.json

    Don't even get me started. Benoit Mandelbrot? ❤️throb.


.. _reason_for_being:

Raison d'etre
=============

Because I wanted to render validation reports (for wind turbine power curves among many other things!)
into sphinx and have the graphs set up so they can be interacted with, because it's not 1995 any more and
``PNG`` files just don't cut it for doing proper science.


.. _related awesome stuff:

Related Awesome Stuff
=====================

Check out `cpplot <https://github.com/thclark/cpplot>`_ to plot charts like these from C++.

Use `cpplot viewer <https://cpplot.herokuapp.com>`_ to quickly check your figure JSON
(or find its source code `here <https://github.com/thclark/cpplot-viewer>`).


.. _contents:

Contents
========

.. toctree::
   :maxdepth: 2

   self
   installation
   quick_start
   example_chapter
   license
   version_history
