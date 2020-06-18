from setuptools import setup

with open("rkb_probability/README.md", "r") as fh:
    long_description = fh.read()

setup(name='rkb_probability',
      version='1.6',
      packages=['rkb_probability'],
      author = 'Raj Kumar Barmon',
      author_email = 'apu.rajkumar1@gmail.com',
      description='Gaussian and Bionomial distributions',
      long_description=long_description,
      long_description_content_type="text/markdown",
      zip_safe=False)
