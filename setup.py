from distutils.core import setup
setup(
  name = 'validemail',
  py_modules=('validemail',),
  install_requires=['dnspython'],
  version = '1.2',
  description = 'alidemail verifies if an email address is valid and really exists.',
  author = 'Oleg Borodai',
  author_email = 'oleg@borodai.com',
  url = 'https://github.com/oleg-borodai/validate_email',
  download_url = 'https://github.com/oleg-borodai/validate_email/archive/1.2.tar.gz',
  keywords = ['email', 'validation', 'dnspython'],
  classifiers = [],
)