A Demo of OpenCafe using GitHub
===============================

Steps:

1. Clone this repository.
2. Install this repository using pip (`pip install .` from the root directory
   of the project).
3. Run `cafe-config init` from the command line if you haven't already done
   so.
4. Create a directory named `GitHub` in your .opencafe/configs directory.
5. Copy the `prod.config` file from the root of this project to the new
   directory.
6. From the command line, run `cafe-runner github prod`.
7. Check the `.opencafe/logs/github/prod.config` directory. There should be
   a directory whose name is a date time stamp of when the tests were run.
   This directory should contain the logs for the tests that were executed.