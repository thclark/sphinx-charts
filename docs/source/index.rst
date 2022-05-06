.. ATTENTION::
    This library is in very early stages. Like the idea of it? Please
    `star us on GitHub <https://github.com/thclark/sphinx-charts>`_ and contribute via the
    `issues board <https://github.com/thclark/sphinx-charts/issues>`_ and
    `roadmap <https://github.com/thclark/sphinx-charts/projects/1>`_.

=============
Sphinx Charts
=============

.. epigraph::
   *"Sphinx Charts" ~ Interactive charts, graphs and figures in Sphinx, using plot.ly and D3*

.. chart:: charts/test_mandelbrot_plot.json

    Don't even get me started. Benoit Mandelbrot? ❤️throb.

.. chart:: charts/validation_perry_marusic_12a.json

    They look freaking glorious 😍. This one even has latex labels and a log axis. Have you tried exporting (hover over the chart for a control panel)? That gives you an actual ``SVG``, not just a screenshot 🤯.


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
(or find its source code `here <https://github.com/thclark/cpplot-viewer>`_).


.. _contents:

Contents
========

.. toctree::
   :maxdepth: 2

   self
   installation
   quick_start
   subdir_example/subdir_example
   license
   version_history
