---
# Onboarding Project

This project serves as an introduction to making
- changes in git 
- pull requests in Stash

---

## What Do?

You must submit a pull request which passes the unit tests for the project. You can verify that your changes have accomplished this before making your PR by doing the following:
1. Set up virtualenv
    1. `virtualenv . && source bin/activate`
2. See what tests have to pass
    1. `python run_tests.py`
3. Create a branch for your work. This should be named after a JIRA task
    1. `j-new PLOPS-999`
4. Make your changes
    1. `???`
5. See if your tests pass
    1. `python run_tests.py`
6. If they've passed:
    * then GOTO 7
    * else GOTO 4
7. Make a pull request
    1. `j-review`
8. Verify that the build was successful
9. Have a libation, you did it!
