A Demo of OpenCafe using GitHub
===============================

This demo is meant to be a quickstart for those interested in a working demo
of an OpenCase-based test suite. For more detailed documentation, visit our
documentation site at http://opencafe.readthedocs.io.

Steps:

1. Clone this repository.
2. Install this repository using pip (``pip install .`` from the root directory
   of the project).
3. Run ``cafe-config init`` from the command line if you haven't already done
   so.
4. Create a directory named ``GitHub`` in your ``.opencafe/configs`` directory.
   The ``.opencafe`` directory was created by the previous command either in
   the root of your virtual environment if you have a virtualenv active.
   If not, it was created in the home directory of the current user.
5. Copy the ``prod.config`` file from the root of this project to the new
   directory.
6. From the command line, run ``cafe-runner github prod --result xml --result-directory .``
7. Check that the current directory now contains a file named `results.xml`.
   This is a JUnit XML formatted result file that is consumable by Jenkins or
   other CI system that parses JUnit XML results.
8. Check the ``.opencafe/logs/github/prod.config`` directory. There should be
   a directory whose name is a date time stamp of when the tests were run.
   This directory should contain the detailed logs for the tests that were
   executed.