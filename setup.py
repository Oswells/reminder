from setuptools import setup, find_packages



if __name__ == '__main__':
    version = '0.0.4'
    setup(
        name='emailreminder',
        version=version,
        description = 'A decorator',
        long_description = 'Use http post requests to send a email to remind you that your program has been break up or finished normally.',
        install_requires=[
            'requests',
        ],
        author='Junjie Zhang',
        author_email='zjunjie@hust.edu.cn',
        license='Apache License 2.0',
        packages=find_packages(),
        url='https://github.com/Oswells/reminder.git'
    )

