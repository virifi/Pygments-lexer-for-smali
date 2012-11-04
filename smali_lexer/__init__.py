from pygments.lexer import RegexLexer, bygroups, include, using, this
from pygments.token import *

__all__ = ['SmaliLexer']

class SmaliLexer(RegexLexer):
    name = 'Smali'
    aliases = ['smali']
    filenames = ['*.smali']

    tokens = {
        'root': [
            (r'^#.+$', Comment.Single),
            (r'"(\\\\|\\"|[^"])*"', String),
            # member access
            (r'->', Text),
            # field
            (r'([a-zA-Z0-9_$]+?)(:)(\S+)(\s*)', bygroups(Name.Attribute, Text, using(this), Text)),
            # method
            (r'([a-zA-Z0-9_<>$]+?)(\()(.*?)(\))(.*)', bygroups(Name.Function, Text, using(this), Text, using(this))),
            # register name
            (r'[vp]\d+', Name.Variable),
            # instructions
            (r'const-string(?:/jumbo)*|const(?:/\d+)|invoke-static|'
             r'move-result-object|move-result|move-object|'
             r'sget-object|sput-object|aget-object|aput-object|'
             r'new-instance|new-array|'
             r'invoke-direct(?:/range)*|'
             r'invoke-virtual|'
             r'invoke-interface|'
             r'add-int(/\S+)*|'
             r'array-length|'
             r'throw|monitor-enter|monitor-exit|move-exception|'
             r'return-object|return-void|return', Keyword),
            (r'if-nez|if-ne|if-eqz|if-ge|'
             r'goto', Keyword.Reserved),
            # label
            (r':[a-zA-Z0-9_]+', Keyword.Reserved),

            # directives
            (r'\.?(class|super|source|annotation|end|field|method|'
             r'prologue|parameter|line|registers|local|catchall|catch|restart)\b', Keyword.Declaration),

            # reserved words
            (r'(abstract|const|enum|extends|final|implements|native|private|'
             r'protected|public|static|strictfp|super|synchronized|throws|'
             r'transient|volatile|constructor|varargs|synthetic)\b', Keyword.Reserved),
            (r'system|value', Keyword.Reserved),
            (r'null', Keyword),

            # class name
            (r'\[?(L.+?;)', Name.Class),
            # type name
            (r'\[?[VZBSCIJFD\[]', Name.Class),
            # numbers
            (r'0x[0-9a-f]+', Number.Hex),
            (r'\d+', Number),

            (r'\s', Text),
            (r'.', Text)
        ]
    }
