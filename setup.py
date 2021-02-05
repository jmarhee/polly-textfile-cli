from setuptools import setup
setup(name='polly-textfile-cli',
version='0.1.1',
description='Command Line Client to render TTS for long textfiles using AWS Polly',
url='https://github.com/jmarhee/polly-textfile-cli',
author='jmarhee',
author_email='jmarhee@interiorae.com',
license='MIT',
packages=['polly_textfile_cli'],
python_requires='>=3.8',
entry_points = {
	'console_scripts': ['polly-textfile=polly_textfile_cli.main:main']
},
install_requires=[
	"boto3"
],
zip_safe=False)
