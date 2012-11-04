from setuptools import setup

__author__ = 'virifi129@gmail.com'

setup(
    name='Smali Lexer',
    version='0.0.1',
    description=__doc__,
    author=__author__,
    packages=['smali_lexer'],
    entry_points='''[pygments.lexers]
smalilexer = smali_lexer:SmaliLexer
'''
)
