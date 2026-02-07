## Pytest Library
Install pytest library 
`pip install -U pytest`
* run `pytest` in folder where test_sample.py is.

## Pytest can integrate with various tools and plugins
* for additional functionalities, such as coverage reports, continuous integration, and more. Plugins can be installed via pip and used to extend capabilities of Pytest.
## File name standards
* Running pytest without mentioning a filename will run all files of format test_*.py or *_test.py in the current directory and subdirectories. 
* Pytest automatically identifies those files as test files. We can make pytest run other filenames by explicitly mentioning them.
* The function tesequality is not executed because pytest will not consider it as a test since its name is not of the format test*.
* Pytest allows us to use markers on test functions. Markers are used to set various features/attributes to test functions. Pytest provides many inbuilt markers such as xfail, skip and parametrize. Apart from that, users can create their own marker names. Markers are applied on the tests using the syntax given below −
@pytest.mark.<markername>
* run group of tests with `pytest -m <markername> -v`

## Parallel testing 
`pip install pytest-xdist`
* run `pytest -n 3` will create 3 workers