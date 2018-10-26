from distutils.core import setup
setup(name='appcli',
      description='setup.py config sample',
      version='1.0',
      author='Ronglu Cao',
      author_email='caoronglu@gmail.com',
      url='https://www.example.com',
      py_modules=['appcli'],
      install_requires=['click'],
      entry_points = {
          "console_scripts": ['appcli=appcli:cli']
      }
)
