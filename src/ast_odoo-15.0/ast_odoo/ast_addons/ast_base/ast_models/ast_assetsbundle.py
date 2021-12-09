Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='subprocess',
            names=[
                alias(name='Popen', asname=None),
                alias(name='PIPE', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='hashlib', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='textwrap', asname=None)],
        ),
        Import(
            names=[alias(name='uuid', asname=None)],
        ),
        Import(
            names=[alias(name='psycopg2', asname=None)],
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='sass', asname='libsass')],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='libsass', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='SUPERUSER_ID', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules.module',
            names=[alias(name='get_resource_path', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='func', asname=None),
                alias(name='misc', asname=None),
                alias(name='transpile_javascript', asname=None),
                alias(name='is_odoo_module', asname=None),
                alias(name='SourceMapGenerator', asname=None),
                alias(name='profiler', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='html_escape', asname='escape')],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.pycompat',
            names=[alias(name='to_text', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='CompileError',
            bases=[Name(id='RuntimeError', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        FunctionDef(
            name='rjsmin',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='script', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Minify js with a clever regex.\n    Taken from http://opensource.perlig.de/rjsmin (version 1.1.0)\n    Apache License, Version 2.0 ', kind=None),
                ),
                FunctionDef(
                    name='subber',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='match', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Substitution callback ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='match', ctx=Load()),
                                    attr='groups',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Name(id='groups', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='groups', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Subscript(
                                                value=Name(id='groups', ctx=Load()),
                                                slice=Constant(value=3, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Subscript(
                                                    value=Name(id='groups', ctx=Load()),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Constant(value='\n', kind=None),
                                            ),
                                        ],
                                    ),
                                    Subscript(
                                        value=Name(id='groups', ctx=Load()),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Subscript(
                                                value=Name(id='groups', ctx=Load()),
                                                slice=Constant(value=5, kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='%s%s%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Subscript(
                                                                            value=Name(id='groups', ctx=Load()),
                                                                            slice=Constant(value=4, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        Constant(value='\n', kind=None),
                                                                    ],
                                                                ),
                                                                Constant(value='', kind=None),
                                                            ],
                                                        ),
                                                        Subscript(
                                                            value=Name(id='groups', ctx=Load()),
                                                            slice=Constant(value=5, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                BoolOp(
                                                                    op=And(),
                                                                    values=[
                                                                        Subscript(
                                                                            value=Name(id='groups', ctx=Load()),
                                                                            slice=Constant(value=6, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        Constant(value='\n', kind=None),
                                                                    ],
                                                                ),
                                                                Constant(value='', kind=None),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Subscript(
                                                value=Name(id='groups', ctx=Load()),
                                                slice=Constant(value=7, kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value='\n', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Subscript(
                                                value=Name(id='groups', ctx=Load()),
                                                slice=Constant(value=8, kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=' ', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Subscript(
                                                value=Name(id='groups', ctx=Load()),
                                                slice=Constant(value=9, kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=' ', kind=None),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Subscript(
                                                value=Name(id='groups', ctx=Load()),
                                                slice=Constant(value=10, kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=' ', kind=None),
                                        ],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='result', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='([^\\047"\\140/\\000-\\040]+)|((?:(?:\\047[^\\047\\\\\\r\\n]*(?:\\\\(?:[^\\r\\n]|\\r?\\n|\\r)[^\\047\\\\\\r\\n]*)*\\047)|(?:"[^"\\\\\\r\\n]*(?:\\\\(?:[^\\r\\n]|\\r?\\n|\\r)[^"\\\\\\r\\n]*)*")|(?:\\140[^\\140\\\\]*(?:\\\\(?:[^\\r\\n]|\\r?\\n|\\r)[^\\140\\\\]*)*\\140))[^\\047"\\140/\\000-\\040]*)|(?<=[(,=:\\[!&|?{};\\r\\n+*-])(?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/))*(?:(?:(?://[^\\r\\n]*)?[\\r\\n])(?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/))*)*((?:/(?![\\r\\n/*])[^/\\\\\\[\\r\\n]*(?:(?:\\\\[^\\r\\n]|(?:\\[[^\\\\\\]\\r\\n]*(?:\\\\[^\\r\\n][^\\\\\\]\\r\\n]*)*\\]))[^/\\\\\\[\\r\\n]*)*/))((?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/))*(?:(?:(?://[^\\r\\n]*)?[\\r\\n])(?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/))*)+(?=[^\\000-\\040&)+,.:;=?\\]|}-]))?|(?<=[\\000-#%-,./:-@\\[-^\\140{-~-]return)(?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/))*(?:((?:(?://[^\\r\\n]*)?[\\r\\n]))(?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/))*)*((?:/(?![\\r\\n/*])[^/\\\\\\[\\r\\n]*(?:(?:\\\\[^\\r\\n]|(?:\\[[^\\\\\\]\\r\\n]*(?:\\\\[^\\r\\n][^\\\\\\]\\r\\n]*)*\\]))[^/\\\\\\[\\r\\n]*)*/))((?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/))*(?:(?:(?://[^\\r\\n]*)?[\\r\\n])(?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/))*)+(?=[^\\000-\\040&)+,.:;=?\\]|}-]))?|(?<=[^\\000-!#%&(*,./:-@\\[\\\\^{|~])(?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/))*(?:((?:(?://[^\\r\\n]*)?[\\r\\n]))(?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/))*)+(?=[^\\000-\\040"#%-\\047)*,./:-@\\\\-^\\140|-~])|(?<=[^\\000-#%-,./:-@\\[-^\\140{-~-])((?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/)))+(?=[^\\000-#%-,./:-@\\[-^\\140{-~-])|(?<=\\+)((?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/)))+(?=\\+)|(?<=-)((?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/)))+(?=-)|(?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/))+|(?:(?:(?://[^\\r\\n]*)?[\\r\\n])(?:[\\000-\\011\\013\\014\\016-\\040]|(?:/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/))*)+', kind=None),
                                    Name(id='subber', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='\n%s\n', kind=None),
                                        op=Mod(),
                                        right=Name(id='script', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            attr='strip',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='result', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='AssetError',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        ClassDef(
            name='AssetNotFound',
            bases=[Name(id='AssetError', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        ClassDef(
            name='AssetsBundle',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='rx_css_import', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='(@import[^;{]+;?)', kind=None),
                            Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='M',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rx_preprocess_imports', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[Constant(value='(@import\\s?[\'"]([^\'"]+)[\'"](;?))', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rx_css_split', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[Constant(value='\\/\\*\\! ([a-f0-9-]+) \\*\\/', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='TRACKED_BUNDLES', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='web.assets_common', kind=None),
                            Constant(value='web.assets_backend', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='files', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='css', annotation=None, type_comment=None),
                            arg(arg='js', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        :param name: bundle name\n        :param files: files to be added to the bundle\n        :param css: if css is True, the stylesheets files are added to the bundle\n        :param js: if js is True, the javascript files are added to the bundle\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='name', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='env', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                orelse=Name(id='env', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='javascripts',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='stylesheets',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='css_errors',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='files',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='files', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_direction',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='res.lang', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='_lang_get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        BoolOp(
                                            op=Or(),
                                            values=[
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='context',
                                                            ctx=Load(),
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='lang', kind=None)],
                                                    keywords=[],
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='lang',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='direction',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='f', ctx=Store()),
                            iter=Name(id='files', ctx=Load()),
                            body=[
                                If(
                                    test=Name(id='css', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='f', ctx=Load()),
                                                    slice=Constant(value='atype', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='text/sass', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='stylesheets',
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='SassStylesheetAsset', ctx=Load()),
                                                                args=[Name(id='self', ctx=Load())],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='url',
                                                                        value=Subscript(
                                                                            value=Name(id='f', ctx=Load()),
                                                                            slice=Constant(value='url', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='filename',
                                                                        value=Subscript(
                                                                            value=Name(id='f', ctx=Load()),
                                                                            slice=Constant(value='filename', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='inline',
                                                                        value=Subscript(
                                                                            value=Name(id='f', ctx=Load()),
                                                                            slice=Constant(value='content', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='media',
                                                                        value=Subscript(
                                                                            value=Name(id='f', ctx=Load()),
                                                                            slice=Constant(value='media', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='direction',
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='user_direction',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='f', ctx=Load()),
                                                            slice=Constant(value='atype', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='text/scss', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='stylesheets',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='ScssStylesheetAsset', ctx=Load()),
                                                                        args=[Name(id='self', ctx=Load())],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='url',
                                                                                value=Subscript(
                                                                                    value=Name(id='f', ctx=Load()),
                                                                                    slice=Constant(value='url', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='filename',
                                                                                value=Subscript(
                                                                                    value=Name(id='f', ctx=Load()),
                                                                                    slice=Constant(value='filename', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='inline',
                                                                                value=Subscript(
                                                                                    value=Name(id='f', ctx=Load()),
                                                                                    slice=Constant(value='content', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='media',
                                                                                value=Subscript(
                                                                                    value=Name(id='f', ctx=Load()),
                                                                                    slice=Constant(value='media', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='direction',
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='user_direction',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Subscript(
                                                                    value=Name(id='f', ctx=Load()),
                                                                    slice=Constant(value='atype', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='text/less', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='stylesheets',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='LessStylesheetAsset', ctx=Load()),
                                                                                args=[Name(id='self', ctx=Load())],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='url',
                                                                                        value=Subscript(
                                                                                            value=Name(id='f', ctx=Load()),
                                                                                            slice=Constant(value='url', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='filename',
                                                                                        value=Subscript(
                                                                                            value=Name(id='f', ctx=Load()),
                                                                                            slice=Constant(value='filename', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='inline',
                                                                                        value=Subscript(
                                                                                            value=Name(id='f', ctx=Load()),
                                                                                            slice=Constant(value='content', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='media',
                                                                                        value=Subscript(
                                                                                            value=Name(id='f', ctx=Load()),
                                                                                            slice=Constant(value='media', kind=None),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='direction',
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='user_direction',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='f', ctx=Load()),
                                                                            slice=Constant(value='atype', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='text/css', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='stylesheets',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='append',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Name(id='StylesheetAsset', ctx=Load()),
                                                                                        args=[Name(id='self', ctx=Load())],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='url',
                                                                                                value=Subscript(
                                                                                                    value=Name(id='f', ctx=Load()),
                                                                                                    slice=Constant(value='url', kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                            keyword(
                                                                                                arg='filename',
                                                                                                value=Subscript(
                                                                                                    value=Name(id='f', ctx=Load()),
                                                                                                    slice=Constant(value='filename', kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                            keyword(
                                                                                                arg='inline',
                                                                                                value=Subscript(
                                                                                                    value=Name(id='f', ctx=Load()),
                                                                                                    slice=Constant(value='content', kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                            keyword(
                                                                                                arg='media',
                                                                                                value=Subscript(
                                                                                                    value=Name(id='f', ctx=Load()),
                                                                                                    slice=Constant(value='media', kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                            keyword(
                                                                                                arg='direction',
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='user_direction',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='js', ctx=Load()),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='f', ctx=Load()),
                                                    slice=Constant(value='atype', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='text/javascript', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='javascripts',
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='JavascriptAsset', ctx=Load()),
                                                        args=[Name(id='self', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='url',
                                                                value=Subscript(
                                                                    value=Name(id='f', ctx=Load()),
                                                                    slice=Constant(value='url', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='filename',
                                                                value=Subscript(
                                                                    value=Name(id='f', ctx=Load()),
                                                                    slice=Constant(value='filename', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='inline',
                                                                value=Subscript(
                                                                    value=Name(id='f', ctx=Load()),
                                                                    slice=Constant(value='content', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='to_node',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='css', annotation=None, type_comment=None),
                            arg(arg='js', annotation=None, type_comment=None),
                            arg(arg='debug', annotation=None, type_comment=None),
                            arg(arg='async_load', annotation=None, type_comment=None),
                            arg(arg='defer_load', annotation=None, type_comment=None),
                            arg(arg='lazy_load', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        :returns [(tagName, attributes, content)] if the tag is auto close\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='is_debug_assets', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='debug', ctx=Load()),
                                    Compare(
                                        left=Constant(value='assets', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='debug', ctx=Load())],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='css', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='stylesheets',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='css_attachments', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='css',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='is_minified',
                                                        value=UnaryOp(
                                                            op=Not(),
                                                            operand=Name(id='is_debug_assets', ctx=Load()),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='attachment', ctx=Store()),
                                    iter=Name(id='css_attachments', ctx=Load()),
                                    body=[
                                        If(
                                            test=Name(id='is_debug_assets', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='href', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='get_debug_asset_url',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='extra',
                                                                value=IfExp(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='user_direction',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='rtl', kind=None)],
                                                                    ),
                                                                    body=Constant(value='rtl/', kind=None),
                                                                    orelse=Constant(value='', kind=None),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='name',
                                                                value=Attribute(
                                                                    value=Name(id='css_attachments', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='extension',
                                                                value=Constant(value='', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='href', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='attachment', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='attr', ctx=Store())],
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='text/css', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='rel', kind=None),
                                                                    Constant(value='stylesheet', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='href', kind=None),
                                                                    Name(id='href', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='data-asset-bundle', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='data-asset-version', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='version',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='link', kind=None),
                                                            Name(id='attr', ctx=Load()),
                                                            Constant(value=None, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='css_errors',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Constant(value='\n', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='css_errors',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='JavascriptAsset', ctx=Load()),
                                                                args=[Name(id='self', ctx=Load())],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='inline',
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='dialog_message',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='msg', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='to_node',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='StylesheetAsset', ctx=Load()),
                                                                args=[Name(id='self', ctx=Load())],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='url',
                                                                        value=Constant(value='/web/static/lib/bootstrap/css/bootstrap.css', kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='to_node',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='js', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='javascripts',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='js_attachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='js',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='is_minified',
                                                value=UnaryOp(
                                                    op=Not(),
                                                    operand=Name(id='is_debug_assets', ctx=Load()),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='src', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='is_debug_assets', ctx=Load()),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='get_debug_asset_url',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='name',
                                                    value=Attribute(
                                                        value=Name(id='js_attachment', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='extension',
                                                    value=Constant(value='', kind=None),
                                                ),
                                            ],
                                        ),
                                        orelse=Attribute(
                                            value=Subscript(
                                                value=Name(id='js_attachment', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='url',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attr', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Constant(value='async', kind=None),
                                                            IfExp(
                                                                test=Name(id='async_load', ctx=Load()),
                                                                body=Constant(value='async', kind=None),
                                                                orelse=Constant(value=None, kind=None),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='defer', kind=None),
                                                            IfExp(
                                                                test=BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Name(id='defer_load', ctx=Load()),
                                                                        Name(id='lazy_load', ctx=Load()),
                                                                    ],
                                                                ),
                                                                body=Constant(value='defer', kind=None),
                                                                orelse=Constant(value=None, kind=None),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='text/javascript', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            IfExp(
                                                                test=Name(id='lazy_load', ctx=Load()),
                                                                body=Constant(value='data-src', kind=None),
                                                                orelse=Constant(value='src', kind=None),
                                                            ),
                                                            Name(id='src', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='data-asset-bundle', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='data-asset-version', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='version',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='script', kind=None),
                                                    Name(id='attr', ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='last_modified',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Returns last modified date of linked files', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='itertools', ctx=Load()),
                                            attr='chain',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='asset', ctx=Load()),
                                                    attr='last_modified',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='asset', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='javascripts',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            GeneratorExp(
                                                elt=Attribute(
                                                    value=Name(id='asset', ctx=Load()),
                                                    attr='last_modified',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='asset', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='stylesheets',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='func', ctx=Load()),
                            attr='lazy_property',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='version',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='checksum',
                                    ctx=Load(),
                                ),
                                slice=Slice(
                                    lower=Constant(value=0, kind=None),
                                    upper=Constant(value=7, kind=None),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='func', ctx=Load()),
                            attr='lazy_property',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='checksum',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Not really a full checksum.\n        We compute a SHA512/256 on the rendered bundle + max linked files last_modified date\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='check', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s%s', kind='u'),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='dumps',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='files',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='sort_keys',
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='last_modified',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='hashlib', ctx=Load()),
                                                attr='sha512',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='check', ctx=Load()),
                                                        attr='encode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='utf-8', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='hexdigest',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Slice(
                                    lower=None,
                                    upper=Constant(value=64, kind=None),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='func', ctx=Load()),
                            attr='lazy_property',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_asset_template_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value='/web/assets/{id}-{unique}/{extra}{name}{sep}{extension}', kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_asset_url_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='id', annotation=None, type_comment=None),
                            arg(arg='unique', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='sep', annotation=None, type_comment=None),
                            arg(arg='extension', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='id', kind=None),
                                    Constant(value='unique', kind=None),
                                    Constant(value='extra', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='sep', kind=None),
                                    Constant(value='extension', kind=None),
                                ],
                                values=[
                                    Name(id='id', ctx=Load()),
                                    Name(id='unique', ctx=Load()),
                                    Name(id='extra', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Name(id='sep', ctx=Load()),
                                    Name(id='extension', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_asset_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='id', annotation=None, type_comment=None),
                            arg(arg='unique', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='sep', annotation=None, type_comment=None),
                            arg(arg='extension', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='%', kind=None),
                            Constant(value='%', kind=None),
                            Constant(value='', kind=None),
                            Constant(value='%', kind=None),
                            Constant(value='%', kind=None),
                            Constant(value='%', kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_asset_template_url',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_get_asset_url_values',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='id',
                                                    value=Name(id='id', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='unique',
                                                    value=Name(id='unique', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='extra',
                                                    value=Name(id='extra', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='name',
                                                    value=Name(id='name', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='sep',
                                                    value=Name(id='sep', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='extension',
                                                    value=Name(id='extension', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_debug_asset_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='extension', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='', kind=None),
                            Constant(value='%', kind=None),
                            Constant(value='%', kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=JoinedStr(
                                values=[
                                    Constant(value='/web/assets/debug/', kind=None),
                                    FormattedValue(
                                        value=Name(id='extra', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    FormattedValue(
                                        value=Name(id='name', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    FormattedValue(
                                        value=Name(id='extension', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clean_attachments',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='extension', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Takes care of deleting any outdated ir.attachment records associated to a bundle before\n        saving a fresh one.\n\n        When `extension` is js we need to check that we are deleting a different version (and not *any*\n        version) because, as one of the creates in `save_attachment` can trigger a rollback, the\n        call to `clean_attachments ` is made at the end of the method in order to avoid the rollback\n        of an ir.attachment unlink (because we cannot rollback a removal on the filestore), thus we\n        must exclude the current bundle.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ira', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.attachment', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_asset_url',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='extra',
                                        value=BinOp(
                                            left=Constant(value='%s', kind=None),
                                            op=Mod(),
                                            right=IfExp(
                                                test=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Name(id='extension', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[
                                                                List(
                                                                    elts=[
                                                                        Constant(value='css', kind=None),
                                                                        Constant(value='min.css', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='user_direction',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='rtl', kind=None)],
                                                        ),
                                                    ],
                                                ),
                                                body=Constant(value='rtl/', kind=None),
                                                orelse=Constant(value='', kind=None),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='sep',
                                        value=Constant(value='', kind=None),
                                    ),
                                    keyword(
                                        arg='extension',
                                        value=BinOp(
                                            left=Constant(value='.%s', kind=None),
                                            op=Mod(),
                                            right=Name(id='extension', ctx=Load()),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='url', kind=None),
                                            Constant(value='=like', kind=None),
                                            Name(id='url', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='!', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='url', kind=None),
                                            Constant(value='=like', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_asset_url',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='unique',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='version',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attachments', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ira', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='attachments', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='attachments', ctx=Load()),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.qweb', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='clear_caches',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_attachments',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='extension', annotation=None, type_comment=None),
                            arg(arg='ignore_version', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Return the ir.attachment records for a given bundle. This method takes care of mitigating\n        an issue happening when parallel transactions generate the same bundle: while the file is not\n        duplicated on the filestore (as it is stored according to its hash), there are multiple\n        ir.attachment records referencing the same version of a bundle. As we don't want to source\n        multiple time the same bundle in our `to_html` function, we group our ir.attachment records\n        by file name and only return the one with the max id for each group.\n\n        :param extension: file extension (js, min.js, css)\n        :param ignore_version: if ignore_version, the url contains a version => web/assets/%-%/name.extension\n                                (the second '%' corresponds to the version),\n                               else: the url contains a version equal to that of the self.version\n                                => web/assets/%-self.version/name.extension.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='unique', ctx=Store())],
                            value=IfExp(
                                test=Name(id='ignore_version', ctx=Load()),
                                body=Constant(value='%', kind=None),
                                orelse=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='version',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url_pattern', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_asset_url',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='unique',
                                        value=Name(id='unique', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='extra',
                                        value=BinOp(
                                            left=Constant(value='%s', kind=None),
                                            op=Mod(),
                                            right=IfExp(
                                                test=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Name(id='extension', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[
                                                                List(
                                                                    elts=[
                                                                        Constant(value='css', kind=None),
                                                                        Constant(value='min.css', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='user_direction',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='rtl', kind=None)],
                                                        ),
                                                    ],
                                                ),
                                                body=Constant(value='rtl/', kind=None),
                                                orelse=Constant(value='', kind=None),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='sep',
                                        value=Constant(value='', kind=None),
                                    ),
                                    keyword(
                                        arg='extension',
                                        value=BinOp(
                                            left=Constant(value='.%s', kind=None),
                                            op=Mod(),
                                            right=Name(id='extension', ctx=Load()),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\n             SELECT max(id)\n               FROM ir_attachment\n              WHERE create_uid = %s\n                AND url like %s\n           GROUP BY name\n           ORDER BY name\n         ', kind=None),
                                    List(
                                        elts=[
                                            Name(id='SUPERUSER_ID', ctx=Load()),
                                            Name(id='url_pattern', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='attachment_ids', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='r', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='fetchall',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.attachment', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='attachment_ids', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='save_attachment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='extension', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Record the given bundle in an ir.attachment and delete\n        all other ir.attachments referring to this bundle (with the same name and extension).\n\n        :param extension: extension of the bundle to be recorded\n        :param content: bundle content to be recorded\n\n        :return the ir.attachment records for a given bundle.\n        ', kind=None),
                        ),
                        Assert(
                            test=Compare(
                                left=Name(id='extension', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='js', kind=None),
                                            Constant(value='min.js', kind=None),
                                            Constant(value='js.map', kind=None),
                                            Constant(value='css', kind=None),
                                            Constant(value='min.css', kind=None),
                                            Constant(value='css.map', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='ira', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.attachment', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fname', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s.%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        Name(id='extension', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mimetype', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='extension', ctx=Load()),
                                    ops=[In()],
                                    comparators=[
                                        List(
                                            elts=[
                                                Constant(value='css', kind=None),
                                                Constant(value='min.css', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                body=Constant(value='text/css', kind=None),
                                orelse=IfExp(
                                    test=Compare(
                                        left=Name(id='extension', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='js.map', kind=None),
                                                    Constant(value='css.map', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=Constant(value='application/json', kind=None),
                                    orelse=Constant(value='application/javascript', kind=None),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='mimetype', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='public', kind=None),
                                    Constant(value='raw', kind=None),
                                ],
                                values=[
                                    Name(id='fname', ctx=Load()),
                                    Name(id='mimetype', ctx=Load()),
                                    Constant(value='ir.ui.view', kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value='binary', kind=None),
                                    Constant(value=True, kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='content', ctx=Load()),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf8', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ira', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='SUPERUSER_ID', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_asset_url',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='id',
                                        value=Attribute(
                                            value=Name(id='attachment', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='unique',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='version',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='extra',
                                        value=BinOp(
                                            left=Constant(value='%s', kind=None),
                                            op=Mod(),
                                            right=IfExp(
                                                test=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Name(id='extension', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[
                                                                List(
                                                                    elts=[
                                                                        Constant(value='css', kind=None),
                                                                        Constant(value='min.css', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='user_direction',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='rtl', kind=None)],
                                                        ),
                                                    ],
                                                ),
                                                body=Constant(value='rtl/', kind=None),
                                                orelse=Constant(value='', kind=None),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='name',
                                        value=Name(id='fname', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='sep',
                                        value=Constant(value='', kind=None),
                                    ),
                                    keyword(
                                        arg='extension',
                                        value=Constant(value='', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='url', kind=None)],
                                values=[Name(id='url', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attachment', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='context',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='commit_assetsbundle', kind=None)],
                                    keywords=[],
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=True, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='commit',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='clean_attachments',
                                    ctx=Load(),
                                ),
                                args=[Name(id='extension', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Constant(value='bus.bus', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='TRACKED_BUNDLES',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='bus.bus', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_sendone',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='broadcast', kind=None),
                                            Constant(value='bundle_changed', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='version', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='version',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Asset Changed: bundle: %s -- version: %s', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='version',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='attachment', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='js',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='is_minified', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='extension', ctx=Store())],
                            value=IfExp(
                                test=Name(id='is_minified', ctx=Load()),
                                body=Constant(value='min.js', kind=None),
                                orelse=Constant(value='js', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attachments', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_attachments',
                                    ctx=Load(),
                                ),
                                args=[Name(id='extension', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='attachments', ctx=Load()),
                            ),
                            body=[
                                If(
                                    test=Name(id='is_minified', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Constant(value=';\n', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Call(
                                                            func=Attribute(
                                                                value=Name(id='asset', ctx=Load()),
                                                                attr='minify',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='asset', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='javascripts',
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='save_attachment',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='extension', ctx=Load()),
                                                    Name(id='content', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='js_with_sourcemap',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Subscript(
                                value=Name(id='attachments', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='js_with_sourcemap',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Create the ir.attachment representing the not-minified content of the bundleJS\n        and create/modify the ir.attachment representing the linked sourcemap.\n\n        :return ir.attachment representing the un-minified content of the bundleJS\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sourcemap_attachment', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_attachments',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='js.map', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='save_attachment',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='js.map', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='generator', ctx=Store())],
                            value=Call(
                                func=Name(id='SourceMapGenerator', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='source_root',
                                        value=BinOp(
                                            left=Call(
                                                func=Attribute(
                                                    value=Constant(value='/', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    ListComp(
                                                        elt=Constant(value='..', kind=None),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='i', ctx=Store()),
                                                                iter=Call(
                                                                    func=Name(id='range', ctx=Load()),
                                                                    args=[
                                                                        Constant(value=0, kind=None),
                                                                        BinOp(
                                                                            left=Call(
                                                                                func=Name(id='len', ctx=Load()),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='get_debug_asset_url',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[],
                                                                                                keywords=[
                                                                                                    keyword(
                                                                                                        arg='name',
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='name',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            attr='split',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='/', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            op=Sub(),
                                                                            right=Constant(value=2, kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            op=Add(),
                                            right=Constant(value='/', kind=None),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content_bundle_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content_line_count', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='line_header', ctx=Store())],
                            value=Constant(value=6, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='asset', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='javascripts',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='asset', ctx=Load()),
                                        attr='is_transpiled',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='generator', ctx=Load()),
                                                    attr='add_source',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='asset', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='asset', ctx=Load()),
                                                        attr='_content',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='content_line_count', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='start_offset',
                                                        value=BinOp(
                                                            left=Name(id='line_header', ctx=Load()),
                                                            op=Add(),
                                                            right=Constant(value=3, kind=None),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='generator', ctx=Load()),
                                                    attr='add_source',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='asset', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='asset', ctx=Load()),
                                                        attr='content',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='content_line_count', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='start_offset',
                                                        value=Name(id='line_header', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='content_bundle_list', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='asset', ctx=Load()),
                                                    attr='with_header',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='asset', ctx=Load()),
                                                        attr='content',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='minimal',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='content_line_count', ctx=Store()),
                                    op=Add(),
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='asset', ctx=Load()),
                                                            attr='content',
                                                            ctx=Load(),
                                                        ),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='\n', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Name(id='line_header', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content_bundle', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Call(
                                        func=Attribute(
                                            value=Constant(value=';\n', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='content_bundle_list', ctx=Load())],
                                        keywords=[],
                                    ),
                                    op=Add(),
                                    right=Constant(value='\n//# sourceMappingURL=', kind=None),
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='sourcemap_attachment', ctx=Load()),
                                    attr='url',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='js_attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='save_attachment',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='js', kind=None),
                                    Name(id='content_bundle', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='generator', ctx=Load()),
                                    attr='_file',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='js_attachment', ctx=Load()),
                                attr='url',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sourcemap_attachment', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='raw', kind=None)],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='generator', ctx=Load()),
                                                    attr='get_content',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='js_attachment', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='css',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='is_minified', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='extension', ctx=Store())],
                            value=IfExp(
                                test=Name(id='is_minified', ctx=Load()),
                                body=Constant(value='min.css', kind=None),
                                orelse=Constant(value='css', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attachments', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_attachments',
                                    ctx=Load(),
                                ),
                                args=[Name(id='extension', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='attachments', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='css', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='preprocess_css',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='css_errors',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_attachments',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='extension', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='ignore_version',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='matches', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='css', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='rx_css_import',
                                                ctx=Load(),
                                            ),
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='matchobj', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='matches', ctx=Load()),
                                                                attr='append',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='matchobj', ctx=Load()),
                                                                        attr='group',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value=0, kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Constant(value='', kind=None),
                                                    ],
                                                ),
                                            ),
                                            Name(id='css', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='is_minified', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='matches', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='css', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='css', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Constant(value='\n', kind='u'),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='matches', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='save_attachment',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='extension', ctx=Load()),
                                                    Name(id='css', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='attachments', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_attachments',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='extension', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='css_with_sourcemap',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Constant(value='\n', kind='u'),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='matches', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='attachments', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='css_with_sourcemap',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='content_import_rules', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Create the ir.attachment representing the not-minified content of the bundleCSS\n        and create/modify the ir.attachment representing the linked sourcemap.\n\n        :param content_import_rules: string containing all the @import rules to put at the beginning of the bundle\n        :return ir.attachment representing the un-minified content of the bundleCSS\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sourcemap_attachment', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_attachments',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='css.map', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='save_attachment',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='css.map', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='debug_asset_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_debug_asset_url',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='name',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='extra',
                                        value=IfExp(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_direction',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='rtl', kind=None)],
                                            ),
                                            body=Constant(value='rtl/', kind=None),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='generator', ctx=Store())],
                            value=Call(
                                func=Name(id='SourceMapGenerator', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='source_root',
                                        value=BinOp(
                                            left=Call(
                                                func=Attribute(
                                                    value=Constant(value='/', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    ListComp(
                                                        elt=Constant(value='..', kind=None),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='i', ctx=Store()),
                                                                iter=Call(
                                                                    func=Name(id='range', ctx=Load()),
                                                                    args=[
                                                                        Constant(value=0, kind=None),
                                                                        BinOp(
                                                                            left=Call(
                                                                                func=Name(id='len', ctx=Load()),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='debug_asset_url', ctx=Load()),
                                                                                            attr='split',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='/', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            op=Sub(),
                                                                            right=Constant(value=2, kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            op=Add(),
                                            right=Constant(value='/', kind=None),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content_bundle_list', ctx=Store())],
                            value=List(
                                elts=[Name(id='content_import_rules', ctx=Load())],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content_line_count', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='content_import_rules', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='\n', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='asset', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='stylesheets',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='asset', ctx=Load()),
                                        attr='content',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='asset', ctx=Load()),
                                                    attr='with_header',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='asset', ctx=Load()),
                                                        attr='content',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='asset', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='generator', ctx=Load()),
                                                            attr='add_source',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='asset', ctx=Load()),
                                                                attr='url',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='content', ctx=Load()),
                                                            Name(id='content_line_count', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='sub',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='rx_css_import',
                                                        ctx=Load(),
                                                    ),
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='matchobj', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=JoinedStr(
                                                            values=[
                                                                Constant(value='/* ', kind=None),
                                                                FormattedValue(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='matchobj', ctx=Load()),
                                                                            attr='group',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value=0, kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                                Constant(value=' */', kind=None),
                                                            ],
                                                        ),
                                                    ),
                                                    Name(id='content', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='content_bundle_list', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='content', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='content_line_count', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='content', ctx=Load()),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='\n', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content_bundle', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Constant(value='\n', kind=None),
                                        attr='join',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='content_bundle_list', ctx=Load())],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=JoinedStr(
                                    values=[
                                        Constant(value='\n//*# sourceMappingURL=', kind=None),
                                        FormattedValue(
                                            value=Attribute(
                                                value=Name(id='sourcemap_attachment', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                            conversion=-1,
                                            format_spec=None,
                                        ),
                                        Constant(value=' */', kind=None),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='css_attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='save_attachment',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='css', kind=None),
                                    Name(id='content_bundle', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='generator', ctx=Load()),
                                    attr='_file',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='css_attachment', ctx=Load()),
                                attr='url',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sourcemap_attachment', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='raw', kind=None)],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='generator', ctx=Load()),
                                                    attr='get_content',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='css_attachment', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='dialog_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Returns a JS script which shows a warning to the user on page load.\n        TODO: should be refactored to be a base js file whose code is extended\n              by related apps (web/website).\n        ', kind=None),
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='\n            (function (message) {\n                \'use strict\';\n\n                if (window.__assetsBundleErrorSeen) {\n                    return;\n                }\n                window.__assetsBundleErrorSeen = true;\n\n                if (document.readyState !== \'loading\') {\n                    onDOMContentLoaded();\n                } else {\n                    window.addEventListener(\'DOMContentLoaded\', () => onDOMContentLoaded());\n                }\n\n                async function onDOMContentLoaded() {\n                    var odoo = window.top.odoo;\n                    if (!odoo || !odoo.define) {\n                        useAlert();\n                        return;\n                    }\n\n                    // Wait for potential JS loading\n                    await new Promise(resolve => {\n                        const noLazyTimeout = setTimeout(() => resolve(), 10); // 10 since need to wait for promise resolutions of odoo.define\n                        odoo.define(\'AssetsBundle.PotentialLazyLoading\', function (require) {\n                            \'use strict\';\n\n                            const lazyloader = require(\'web.public.lazyloader\');\n\n                            clearTimeout(noLazyTimeout);\n                            lazyloader.allScriptsLoaded.then(() => resolve());\n                        });\n                    });\n\n                    var alertTimeout = setTimeout(useAlert, 10); // 10 since need to wait for promise resolutions of odoo.define\n                    odoo.define(\'AssetsBundle.ErrorMessage\', function (require) {\n                        \'use strict\';\n\n                        require(\'web.dom_ready\');\n                        var core = require(\'web.core\');\n                        var Dialog = require(\'web.Dialog\');\n\n                        var _t = core._t;\n\n                        clearTimeout(alertTimeout);\n                        new Dialog(null, {\n                            title: _t("Style error"),\n                            $content: $(\'<div/>\')\n                                .append($(\'<p/>\', {text: _t("The style compilation failed, see the error below. Your recent actions may be the cause, please try reverting the changes you made.")}))\n                                .append($(\'<pre/>\', {html: message})),\n                        }).open();\n                    });\n                }\n\n                function useAlert() {\n                    window.alert(message);\n                }\n            })("%s");\n        ', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='message', ctx=Load()),
                                                attr='replace',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='"', kind=None),
                                                Constant(value='\\"', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='replace',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='\n', kind=None),
                                        Constant(value='&NewLine;', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_assets_domain_for_already_processed_css',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='assets', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Method to compute the attachments' domain to search the already process assets (css).\n        This method was created to be overridden.\n        ", kind=None),
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='url', kind=None),
                                            Constant(value='in', kind=None),
                                            Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='assets', ctx=Load()),
                                                            attr='keys',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_css_preprocessed',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='preprocessed', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attachments', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='asset_types', ctx=Store())],
                            value=List(
                                elts=[
                                    Name(id='SassStylesheetAsset', ctx=Load()),
                                    Name(id='ScssStylesheetAsset', ctx=Load()),
                                    Name(id='LessStylesheetAsset', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_direction',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='rtl', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='asset_types', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='StylesheetAsset', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='atype', ctx=Store()),
                            iter=Name(id='asset_types', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='outdated', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='assets', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='asset', ctx=Load()),
                                                            attr='html_url',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='asset', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='asset', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='stylesheets',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[
                                                            Call(
                                                                func=Name(id='isinstance', ctx=Load()),
                                                                args=[
                                                                    Name(id='asset', ctx=Load()),
                                                                    Name(id='atype', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='assets', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='assets_domain', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_assets_domain_for_already_processed_css',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='assets', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='attachments', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.attachment', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='assets_domain', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='attachment', ctx=Store()),
                                            iter=Name(id='attachments', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='asset', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='assets', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='attachment', ctx=Load()),
                                                            attr='url',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='asset', ctx=Load()),
                                                            attr='last_modified',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[
                                                            Subscript(
                                                                value=Name(id='attachment', ctx=Load()),
                                                                slice=Constant(value='__last_update', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='outdated', ctx=Store())],
                                                            value=Constant(value=True, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Break(),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='asset', ctx=Load()),
                                                            attr='_content',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Is()],
                                                        comparators=[Constant(value=None, kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='asset', ctx=Load()),
                                                                    attr='_content',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='attachment', ctx=Load()),
                                                                                attr='raw',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=b'', kind=None),
                                                                        ],
                                                                    ),
                                                                    attr='decode',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='utf8', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    UnaryOp(
                                                                        op=Not(),
                                                                        operand=Attribute(
                                                                            value=Name(id='asset', ctx=Load()),
                                                                            attr='_content',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='attachment', ctx=Load()),
                                                                            attr='file_size',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Gt()],
                                                                        comparators=[Constant(value=0, kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='asset', ctx=Load()),
                                                                            attr='_content',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value=None, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Attribute(
                                                                value=Name(id='asset', ctx=Load()),
                                                                attr='_content',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Is()],
                                                            comparators=[Constant(value=None, kind=None)],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='asset', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='assets', ctx=Load()),
                                                                        attr='values',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='outdated', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Name(id='outdated', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='preprocessed', ctx=Store())],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='preprocessed', ctx=Load()),
                                    Name(id='attachments', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='preprocess_css',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='debug', annotation=None, type_comment=None),
                            arg(arg='old_attachments', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n            Checks if the bundle contains any sass/less content, then compiles it to css.\n            If user language direction is Right to Left then consider css files to call run_rtlcss,\n            css files are also stored in ir.attachment after processing done by rtlcss.\n            Returns the bundle's flat css.\n        ", kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='stylesheets',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='compiled', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='atype', ctx=Store()),
                                    iter=Tuple(
                                        elts=[
                                            Name(id='SassStylesheetAsset', ctx=Load()),
                                            Name(id='ScssStylesheetAsset', ctx=Load()),
                                            Name(id='LessStylesheetAsset', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='assets', ctx=Store())],
                                            value=ListComp(
                                                elt=Name(id='asset', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='asset', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='stylesheets',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[
                                                            Call(
                                                                func=Name(id='isinstance', ctx=Load()),
                                                                args=[
                                                                    Name(id='asset', ctx=Load()),
                                                                    Name(id='atype', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='assets', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='source', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Constant(value='\n', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            ListComp(
                                                                elt=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='asset', ctx=Load()),
                                                                        attr='get_source',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='asset', ctx=Store()),
                                                                        iter=Name(id='assets', ctx=Load()),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='compiled', ctx=Store()),
                                                    op=Add(),
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='compile_css',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Name(id='assets', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='compile',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='source', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user_direction',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='rtl', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='stylesheet_assets', ctx=Store())],
                                            value=ListComp(
                                                elt=Name(id='asset', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='asset', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='stylesheets',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Call(
                                                                    func=Name(id='isinstance', ctx=Load()),
                                                                    args=[
                                                                        Name(id='asset', ctx=Load()),
                                                                        Tuple(
                                                                            elts=[
                                                                                Name(id='SassStylesheetAsset', ctx=Load()),
                                                                                Name(id='ScssStylesheetAsset', ctx=Load()),
                                                                                Name(id='LessStylesheetAsset', ctx=Load()),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='compiled', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Constant(value='\n', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    ListComp(
                                                        elt=Call(
                                                            func=Attribute(
                                                                value=Name(id='asset', ctx=Load()),
                                                                attr='get_source',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='asset', ctx=Store()),
                                                                iter=Name(id='stylesheet_assets', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='compiled', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='run_rtlcss',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='compiled', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='css_errors',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Name(id='old_attachments', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='old_attachments', ctx=Load()),
                                                    attr='unlink',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='old_attachments', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='fragments', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='rx_css_split',
                                                ctx=Load(),
                                            ),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='compiled', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='at_rules', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fragments', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='at_rules', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='stylesheets',
                                                        ctx=Load(),
                                                    ),
                                                    attr='insert',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=0, kind=None),
                                                    Call(
                                                        func=Name(id='StylesheetAsset', ctx=Load()),
                                                        args=[Name(id='self', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='inline',
                                                                value=Name(id='at_rules', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                While(
                                    test=Name(id='fragments', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='asset_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fragments', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='asset', ctx=Store())],
                                            value=Call(
                                                func=Name(id='next', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Name(id='asset', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='asset', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='stylesheets',
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='asset', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='asset_id', ctx=Load())],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='asset', ctx=Load()),
                                                    attr='_content',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fragments', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=0, kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='\n', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='asset', ctx=Load()),
                                                attr='minify',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='asset', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='stylesheets',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='compile_css',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='compiler', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Sanitizes @import rules, remove duplicates @import rules, then compile', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='imports', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='handle_compile_error',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='e', annotation=None, type_comment=None),
                                    arg(arg='source', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='error', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_preprocessor_error',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='e', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='source',
                                                value=Name(id='source', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='error', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='css_errors',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='error', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='sanitize',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='matchobj', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ref', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='matchobj', ctx=Load()),
                                            attr='group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=2, kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='line', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='@import "%s"%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='ref', ctx=Load()),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='matchobj', ctx=Load()),
                                                        attr='group',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=3, kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='.', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='ref', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Name(id='line', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='imports', ctx=Load())],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='ref', ctx=Load()),
                                                        attr='startswith',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='.', kind=None),
                                                                Constant(value='/', kind=None),
                                                                Constant(value='~', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='imports', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='line', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Name(id='line', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='msg', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value="Local import '%s' is forbidden for security reasons. Please remove all @import {your_file} imports in your custom files. In Odoo you have to import all files in the assets, and not through the @import statement.", kind=None),
                                        op=Mod(),
                                        right=Name(id='ref', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='msg', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='css_errors',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='msg', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='rx_preprocess_imports',
                                        ctx=Load(),
                                    ),
                                    Name(id='sanitize', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='compiled', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='compiled', ctx=Store())],
                                    value=Call(
                                        func=Name(id='compiler', ctx=Load()),
                                        args=[Name(id='source', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='CompileError', ctx=Load()),
                                    name='e',
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='handle_compile_error', ctx=Load()),
                                                args=[Name(id='e', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='source',
                                                        value=Name(id='source', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='compiled', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='compiled', ctx=Load()),
                                    attr='strip',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='compiled', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(appearance: (\\w+);)', kind=None),
                                    Constant(value='-webkit-appearance: \\2; -moz-appearance: \\2; \\1', kind=None),
                                    Name(id='compiled', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='compiled', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(display: ((?:inline-)?)flex((?: ?!important)?);)', kind=None),
                                    Constant(value='display: -webkit-\\2box\\3; display: -webkit-\\2flex\\3; \\1', kind=None),
                                    Name(id='compiled', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='compiled', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(justify-content: flex-(\\w+)((?: ?!important)?);)', kind=None),
                                    Constant(value='-webkit-box-pack: \\2\\3; \\1', kind=None),
                                    Name(id='compiled', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='compiled', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(flex-flow: (\\w+ \\w+);)', kind=None),
                                    Constant(value='-webkit-flex-flow: \\2; \\1', kind=None),
                                    Name(id='compiled', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='compiled', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(flex-direction: (column);)', kind=None),
                                    Constant(value='-webkit-box-orient: vertical; -webkit-box-direction: normal; -webkit-flex-direction: \\2; \\1', kind=None),
                                    Name(id='compiled', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='compiled', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(flex-wrap: (\\w+);)', kind=None),
                                    Constant(value='-webkit-flex-wrap: \\2; \\1', kind=None),
                                    Name(id='compiled', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='compiled', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(flex: ((\\d)+ \\d+ (?:\\d+|auto));)', kind=None),
                                    Constant(value='-webkit-box-flex: \\3; -webkit-flex: \\2; \\1', kind=None),
                                    Name(id='compiled', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='compiled', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='run_rtlcss',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='rtlcss', ctx=Store())],
                            value=Constant(value='rtlcss', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='nt', kind=None)],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='rtlcss', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='misc', ctx=Load()),
                                                    attr='find_in_path',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='rtlcss.cmd', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='IOError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[Name(id='rtlcss', ctx=Store())],
                                                    value=Constant(value='rtlcss', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='cmd', ctx=Store())],
                            value=List(
                                elts=[
                                    Name(id='rtlcss', ctx=Load()),
                                    Constant(value='-', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='rtlcss', ctx=Store())],
                                    value=Call(
                                        func=Name(id='Popen', ctx=Load()),
                                        args=[Name(id='cmd', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='stdin',
                                                value=Name(id='PIPE', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='stdout',
                                                value=Name(id='PIPE', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='stderr',
                                                value=Name(id='PIPE', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='process', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='Popen', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='rtlcss', kind=None),
                                                                    Constant(value='--version', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='stdout',
                                                                value=Name(id='PIPE', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='stderr',
                                                                value=Name(id='PIPE', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Tuple(
                                                        elts=[
                                                            Name(id='OSError', ctx=Load()),
                                                            Name(id='IOError', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    name=None,
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='warning',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='You need https://rtlcss.com/ to convert css file to right to left compatiblity. Use: npm install -g rtlcss', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Return(
                                                            value=Name(id='source', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='Could not execute command %r', kind=None),
                                                op=Mod(),
                                                right=Subscript(
                                                    value=Name(id='cmd', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='msg', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='css_errors',
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='msg', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Constant(value='', kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rtlcss', ctx=Load()),
                                    attr='communicate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='input',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='source', ctx=Load()),
                                                attr='encode',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='utf-8', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='rtlcss', ctx=Load()),
                                attr='returncode',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='cmd_output', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='misc', ctx=Load()),
                                                    attr='ustr',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='result', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='cmd_output', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='cmd_output', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='Process exited with return code %d\n', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='rtlcss', ctx=Load()),
                                                    attr='returncode',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='error', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_rtlcss_error',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='cmd_output', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='source',
                                                value=Name(id='source', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='error', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='css_errors',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='error', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value='', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='rtlcss_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf8', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='rtlcss_result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_preprocessor_error',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stderr', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Improve and remove sensitive information from sass/less compilator error messages', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='error', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='misc', ctx=Load()),
                                                        attr='ustr',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='stderr', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='Load paths', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='  Use --trace for backtrace.', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='Cannot load compass', kind=None),
                                ops=[In()],
                                comparators=[Name(id='error', ctx=Load())],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='error', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='Maybe you should install the compass gem using this extra argument:\n\n    $ sudo gem install compass --pre\n', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        AugAssign(
                            target=Name(id='error', ctx=Store()),
                            op=Add(),
                            value=BinOp(
                                left=Constant(value="This error occured while compiling the bundle '%s' containing:", kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                            ),
                        ),
                        For(
                            target=Name(id='asset', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='stylesheets',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='asset', ctx=Load()),
                                            Name(id='PreprocessedCSS', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='error', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Constant(value='\n    - %s', kind=None),
                                                op=Mod(),
                                                right=IfExp(
                                                    test=Attribute(
                                                        value=Name(id='asset', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                    body=Attribute(
                                                        value=Name(id='asset', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                    orelse=Constant(value='<inline sass>', kind=None),
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='error', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_rtlcss_error',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stderr', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Improve and remove sensitive information from sass/less compilator error messages', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='error', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='misc', ctx=Load()),
                                                        attr='ustr',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='stderr', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='Load paths', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='  Use --trace for backtrace.', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='error', ctx=Store()),
                            op=Add(),
                            value=BinOp(
                                left=Constant(value="This error occured while compiling the bundle '%s' containing:", kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                            ),
                        ),
                        Return(
                            value=Name(id='error', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='WebAsset',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='html_url_format', ctx=Store())],
                    value=Constant(value='%s', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_content', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_filename', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_ir_attach', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_id', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                            arg(arg='inline', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='bundle',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='bundle', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='inline',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='inline', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_filename',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='filename', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='url', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='html_url_args',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='url', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='inline', ctx=Load()),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='url', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value="An asset should either be inlined or url linked, defined in bundle '%s'", kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='bundle', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='id',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_id',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='uuid', ctx=Load()),
                                                    attr='uuid4',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='func', ctx=Load()),
                            attr='lazy_property',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='name',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=IfExp(
                                test=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='inline',
                                    ctx=Load(),
                                ),
                                body=Constant(value='<inline asset>', kind=None),
                                orelse=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='url',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value="%s defined in bundle '%s'", kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='name', ctx=Load()),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='bundle',
                                                ctx=Load(),
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='func', ctx=Load()),
                            attr='lazy_property',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='html_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='html_url_format',
                                    ctx=Load(),
                                ),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='html_url_args',
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='stat',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=Or(),
                                    values=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='inline',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_filename',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_ir_attach',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=GeneratorExp(
                                        elt=Name(id='segment', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='segment', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='url',
                                                            ctx=Load(),
                                                        ),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='/', kind=None)],
                                                    keywords=[],
                                                ),
                                                ifs=[Name(id='segment', ctx=Load())],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_filename',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='get_resource_path', ctx=Load()),
                                        args=[
                                            Starred(
                                                value=Name(id='path', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_filename',
                                        ctx=Load(),
                                    ),
                                    body=[Return(value=None)],
                                    orelse=[],
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='attach', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='bundle',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.attachment', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='get_serve_attachment',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_ir_attach',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='attach', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='AssetNotFound', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Could not find %s', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='to_node',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='last_modified',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stat',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_filename',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='fromtimestamp',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='getmtime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_filename',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_ir_attach',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Return(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_ir_attach',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='__last_update', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=1970, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='func', ctx=Load()),
                            attr='lazy_property',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='content',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_content',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_content',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='inline',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_fetch_content',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_content',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_fetch_content',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Fetch content from file or database', kind=None),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stat',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_filename',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Name(id='open', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_filename',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='rb', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='fp', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='fp', ctx=Load()),
                                                                    attr='read',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='utf-8', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='base64', ctx=Load()),
                                                            attr='b64decode',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_ir_attach',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='datas', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='decode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='utf-8', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='UnicodeDecodeError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='AssetError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='%s is not utf-8 encoded.', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='IOError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='AssetNotFound', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='File %s does not exist.', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=None,
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='AssetError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Could not get content for %s.', kind=None),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='minify',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='content',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='with_header',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='content', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='content', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='content',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=JoinedStr(
                                values=[
                                    Constant(value='\n/* ', kind=None),
                                    FormattedValue(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=' */\n', kind=None),
                                    FormattedValue(
                                        value=Name(id='content', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='JavascriptAsset',
            bases=[Name(id='WebAsset', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bundle', annotation=None, type_comment=None),
                            arg(arg='inline', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bundle', ctx=Load()),
                                    Name(id='inline', ctx=Load()),
                                    Name(id='url', ctx=Load()),
                                    Name(id='filename', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='is_transpiled',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='is_odoo_module', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='content',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_converted_content',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='content',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id='super', ctx=Load()),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='content',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='is_transpiled',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_converted_content',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_converted_content',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='transpile_javascript', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='content', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_converted_content',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='content', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='minify',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='with_header',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='rjsmin', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='content',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_fetch_content',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='JavascriptAsset', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_fetch_content',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AssetError', ctx=Load()),
                                    name='e',
                                    body=[
                                        Return(
                                            value=BinOp(
                                                left=Constant(value='console.error(%s);', kind='u'),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='json', ctx=Load()),
                                                        attr='dumps',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Name(id='to_text', ctx=Load()),
                                                            args=[Name(id='e', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='to_node',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='url',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value='script', kind=None),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='text/javascript', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='src', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='html_url',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='data-asset-bundle', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='bundle',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='data-asset-version', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='bundle',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='version',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=None, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value='script', kind=None),
                                            Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='text/javascript', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='charset', kind=None),
                                                                    Constant(value='utf-8', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='data-asset-bundle', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='bundle',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='data-asset-version', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='bundle',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='version',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='with_header',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='with_header',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='minimal', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Name(id='minimal', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='with_header',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='content', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=List(
                                elts=[
                                    JoinedStr(
                                        values=[
                                            Constant(value='Filepath: ', kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='url',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                    JoinedStr(
                                        values=[
                                            Constant(value='Bundle: ', kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='bundle',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                    JoinedStr(
                                        values=[
                                            Constant(value='Lines: ', kind=None),
                                            FormattedValue(
                                                value=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='content', ctx=Load()),
                                                                attr='splitlines',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='length', ctx=Store())],
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='map', ctx=Load()),
                                        args=[
                                            Name(id='len', ctx=Load()),
                                            Name(id='lines', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='\n', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='', kind=None),
                                            BinOp(
                                                left=Constant(value='/', kind=None),
                                                op=Add(),
                                                right=BinOp(
                                                    left=Constant(value='*', kind=None),
                                                    op=Mult(),
                                                    right=BinOp(
                                                        left=Name(id='length', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=5, kind=None),
                                                    ),
                                                ),
                                            ),
                                            Starred(
                                                value=GeneratorExp(
                                                    elt=JoinedStr(
                                                        values=[
                                                            Constant(value='*  ', kind=None),
                                                            FormattedValue(
                                                                value=Name(id='line', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=JoinedStr(
                                                                    values=[
                                                                        Constant(value='<', kind=None),
                                                                        FormattedValue(
                                                                            value=Name(id='length', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            Constant(value='  *', kind=None),
                                                        ],
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='line', ctx=Store()),
                                                            iter=Name(id='lines', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=BinOp(
                                                    left=Constant(value='*', kind=None),
                                                    op=Mult(),
                                                    right=BinOp(
                                                        left=Name(id='length', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=5, kind=None),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Constant(value='/', kind=None),
                                            ),
                                            Name(id='content', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='StylesheetAsset',
            bases=[Name(id='WebAsset', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='rx_import', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='@import\\s+(\'|")(?!\'|"|/|https?://)', kind=None),
                            Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='U',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rx_url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='url\\s*\\(\\s*(\'|"|)(?!\'|"|/|https?://|data:)', kind=None),
                            Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='U',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rx_sourceMap', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='(/\\*# sourceMappingURL=.*)', kind=None),
                            Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='U',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rx_charset', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='(@charset "[^"]+";)', kind=None),
                            Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='U',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='media',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='media', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='direction',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kw', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='direction', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StylesheetAsset', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kw', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='direction',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='rtl', kind=None)],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='url',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='html_url_args',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                            attr='rsplit',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='.', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='html_url_format',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='%%s/%s/%s.%%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Constant(value='rtl', kind=None),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='bundle',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='html_url_args',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='tuple', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='html_url_args',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='content',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id='super', ctx=Load()),
                                    args=[
                                        Name(id='StylesheetAsset', ctx=Load()),
                                        Name(id='self', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                attr='content',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='media',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='content', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='@media %s { %s }', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='media',
                                                    ctx=Load(),
                                                ),
                                                Name(id='content', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='content', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_fetch_content',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='StylesheetAsset', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_fetch_content',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='web_dir', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='dirname',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='rx_import',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='rx_import',
                                                        ctx=Load(),
                                                    ),
                                                    attr='sub',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='@import \\1%s/', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[Name(id='web_dir', ctx=Load())],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Name(id='content', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='rx_url',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='rx_url',
                                                        ctx=Load(),
                                                    ),
                                                    attr='sub',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='url(\\1%s/', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[Name(id='web_dir', ctx=Load())],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Name(id='content', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='rx_charset',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='rx_charset',
                                                        ctx=Load(),
                                                    ),
                                                    attr='sub',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='', kind=None),
                                                    Name(id='content', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='content', ctx=Load()),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AssetError', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='bundle',
                                                            ctx=Load(),
                                                        ),
                                                        attr='css_errors',
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Constant(value='', kind=None),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_source',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='inline',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_fetch_content',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='/*! %s */\n%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        Name(id='content', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='minify',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='rx_sourceMap',
                                        ctx=Load(),
                                    ),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='content',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='/\\*.*?\\*/', kind=None),
                                    Constant(value='', kind=None),
                                    Name(id='content', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='flags',
                                        value=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='S',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\\s+', kind=None),
                                    Constant(value=' ', kind=None),
                                    Name(id='content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=' *([{}]) *', kind=None),
                                    Constant(value='\\1', kind=None),
                                    Name(id='content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='with_header',
                                    ctx=Load(),
                                ),
                                args=[Name(id='content', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='to_node',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='url',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='attr', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='text/css', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='rel', kind=None),
                                                            Constant(value='stylesheet', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='href', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='html_url',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='media', kind=None),
                                                            IfExp(
                                                                test=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='media',
                                                                    ctx=Load(),
                                                                ),
                                                                body=Call(
                                                                    func=Name(id='escape', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Name(id='to_text', ctx=Load()),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='media',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                orelse=Constant(value=None, kind=None),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='data-asset-bundle', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='bundle',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='data-asset-version', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='bundle',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='version',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value='link', kind=None),
                                            Name(id='attr', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='attr', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='text/css', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='media', kind=None),
                                                            IfExp(
                                                                test=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='media',
                                                                    ctx=Load(),
                                                                ),
                                                                body=Call(
                                                                    func=Name(id='escape', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Name(id='to_text', ctx=Load()),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='media',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                orelse=Constant(value=None, kind=None),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='data-asset-bundle', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='bundle',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='data-asset-version', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='bundle',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='version',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value='style', kind=None),
                                            Name(id='attr', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='with_header',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='PreprocessedCSS',
            bases=[Name(id='StylesheetAsset', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='rx_import', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PreprocessedCSS', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kw', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='html_url_args',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                            attr='rsplit',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='html_url_format',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Constant(value='%%s/%s%s/%%s.css', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        IfExp(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='direction',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='rtl', kind=None)],
                                            ),
                                            body=Constant(value='rtl/', kind=None),
                                            orelse=Constant(value='', kind=None),
                                        ),
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='bundle',
                                                ctx=Load(),
                                            ),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_command',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Name(id='NotImplementedError', ctx=Load()),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='compile',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='command', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='get_command',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='compiler', ctx=Store())],
                                    value=Call(
                                        func=Name(id='Popen', ctx=Load()),
                                        args=[Name(id='command', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='stdin',
                                                value=Name(id='PIPE', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='stdout',
                                                value=Name(id='PIPE', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='stderr',
                                                value=Name(id='PIPE', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='CompileError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Could not execute command %r', kind=None),
                                                        op=Mod(),
                                                        right=Subscript(
                                                            value=Name(id='command', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='out', ctx=Store()),
                                        Name(id='err', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='compiler', ctx=Load()),
                                    attr='communicate',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='input',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='source', ctx=Load()),
                                                attr='encode',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='utf-8', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='compiler', ctx=Load()),
                                attr='returncode',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='cmd_output', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='misc', ctx=Load()),
                                                attr='ustr',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='out', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='misc', ctx=Load()),
                                                attr='ustr',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='err', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='cmd_output', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='cmd_output', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='Process exited with return code %d\n', kind='u'),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='compiler', ctx=Load()),
                                                    attr='returncode',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='CompileError', ctx=Load()),
                                        args=[Name(id='cmd_output', ctx=Load())],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='out', ctx=Load()),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf8', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='SassStylesheetAsset',
            bases=[Name(id='PreprocessedCSS', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='rx_indent', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='^( +|\\t+)', kind=None),
                            Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='M',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='indent', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reindent', ctx=Store())],
                    value=Constant(value='    ', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='minify',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='with_header',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_source',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='textwrap', ctx=Load()),
                                    attr='dedent',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='inline',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_fetch_content',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='fix_indent',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='m', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ind', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='m', ctx=Load()),
                                            attr='group',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='indent',
                                            ctx=Load(),
                                        ),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='indent',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='ind', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='indent',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='reindent',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='StopIteration', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ind', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='indent',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='reindent',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='rx_indent',
                                                ctx=Load(),
                                            ),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='fix_indent', ctx=Load()),
                                            Name(id='content', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='StopIteration', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='/*! %s */\n%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        Name(id='content', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_command',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='sass', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='find_in_path',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='sass', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='IOError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='sass', ctx=Store())],
                                            value=Constant(value='sass', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Name(id='sass', ctx=Load()),
                                    Constant(value='--stdin', kind=None),
                                    Constant(value='-t', kind=None),
                                    Constant(value='compressed', kind=None),
                                    Constant(value='--unix-newlines', kind=None),
                                    Constant(value='--compass', kind=None),
                                    Constant(value='-r', kind=None),
                                    Constant(value='bootstrap-sass', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ScssStylesheetAsset',
            bases=[Name(id='PreprocessedCSS', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='bootstrap_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='get_resource_path', ctx=Load()),
                                args=[
                                    Constant(value='web', kind=None),
                                    Constant(value='static', kind=None),
                                    Constant(value='lib', kind=None),
                                    Constant(value='bootstrap', kind=None),
                                    Constant(value='scss', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='precision', ctx=Store())],
                    value=Constant(value=8, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='output_style', ctx=Store())],
                    value=Constant(value='expanded', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='compile',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='source', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='libsass', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='ScssStylesheetAsset', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='compile',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='source', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='profiler', ctx=Load()),
                                            attr='force_hook',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='libsass', ctx=Load()),
                                            attr='compile',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='string',
                                                value=Name(id='source', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='include_paths',
                                                value=List(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='bootstrap_path',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='output_style',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='output_style',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='precision',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='precision',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='libsass', ctx=Load()),
                                        attr='CompileError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='CompileError', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_command',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='sassc', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='misc', ctx=Load()),
                                            attr='find_in_path',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='sassc', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='IOError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='sassc', ctx=Store())],
                                            value=Constant(value='sassc', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Name(id='sassc', ctx=Load()),
                                    Constant(value='--stdin', kind=None),
                                    Constant(value='--precision', kind=None),
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='precision',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='--load-path', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='bootstrap_path',
                                        ctx=Load(),
                                    ),
                                    Constant(value='-t', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='output_style',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='LessStylesheetAsset',
            bases=[Name(id='PreprocessedCSS', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='get_command',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='nt', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='lessc', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='misc', ctx=Load()),
                                                    attr='find_in_path',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='lessc.cmd', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='lessc', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='misc', ctx=Load()),
                                                    attr='find_in_path',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='lessc', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='IOError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='lessc', ctx=Store())],
                                            value=Constant(value='lessc', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='lesspath', ctx=Store())],
                            value=Call(
                                func=Name(id='get_resource_path', ctx=Load()),
                                args=[
                                    Constant(value='web', kind=None),
                                    Constant(value='static', kind=None),
                                    Constant(value='lib', kind=None),
                                    Constant(value='bootstrap', kind=None),
                                    Constant(value='less', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Name(id='lessc', ctx=Load()),
                                    Constant(value='-', kind=None),
                                    Constant(value='--no-js', kind=None),
                                    Constant(value='--no-color', kind=None),
                                    BinOp(
                                        left=Constant(value='--include-path=%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='lesspath', ctx=Load()),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
