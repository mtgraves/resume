import unittest
import xmlrunner
import os
import coverage

# clear out old test results
if not os.path.exists(os.path.join('docs', 'testreports')):
    os.mkdir(os.path.join('docs', 'testreports'))
base_test_result_path = os.path.join('docs', 'testreports')
for f in os.listdir(base_test_result_path):
    os.remove(os.path.join(base_test_result_path,f))

# set up coverage
cov = coverage.Coverage()
cov.start()

# run tests
loader = unittest.TestLoader()
suite = loader.discover('scripts/tests')
runner = xmlrunner.XMLTestRunner(output='docs/testreports')
runner.run(suite)

cov.stop()
cov.save()