mock.patch('package.module.Classname')

mock.patch('package.module.Classname', return_value='ping')

mock.patch('package.module.Classname', side_effect='pong')

@mock.patch('package.module.Classname', return_value='echo')
def test_example(self, m):

@mock.patch('package.module.Classname', return_value='echo')
class TestExample:
    def test_example(self, m):

with @mock.patch('package.module.Classname', return_value='echo') as m:

