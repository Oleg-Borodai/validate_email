from setuptools import setup, find_packages

setup(name='validemail',
      version = '1.0',
      download_url = 'git@github.com:oleg-borodai/validate_email.git',
      py_modules = ('validemail',),
      author = 'Oleg Borodai',
      author_email = 'oleg@borodai.com',
      description = 'validemail verifies if an email address is valid and really exists.',
      long_description=open('README.rst').read(),
      keywords = 'email validation verification mx verify',
      url = 'https://github.com/oleg-borodai/validate_email',
      license = 'LGPL',
    )
