Module(
    body=[
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
            names=[alias(name='traceback', asname=None)],
        ),
        Import(
            names=[alias(name='unicodedata', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.exceptions', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.routing', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.urls', asname=None)],
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='slugify', asname='slugify_lib')],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='slugify_lib', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                ),
            ],
            orelse=[],
            finalbody=[],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='registry', asname=None),
                alias(name='exceptions', asname=None),
                alias(name='tools', asname=None),
                alias(name='http', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models',
            names=[alias(name='ir_http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_http',
            names=[alias(name='RequestUID', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.qweb',
            names=[alias(name='QWebException', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='config', asname=None),
                alias(name='ustr', asname=None),
                alias(name='pycompat', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='geoipresolver',
            names=[alias(name='GeoIPResolver', asname=None)],
            level=2,
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
        Assign(
            targets=[
                Attribute(
                    value=Name(id='odoo', ctx=Load()),
                    attr='_geoip_resolver',
                    ctx=Store(),
                ),
            ],
            value=Constant(value=None, kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='_guess_mimetype',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='ext', annotation=None, type_comment=None),
                    arg(arg='default', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value='text/html', kind=None),
                ],
            ),
            body=[
                Assign(
                    targets=[Name(id='exts', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='.css', kind=None),
                            Constant(value='.less', kind=None),
                            Constant(value='.scss', kind=None),
                            Constant(value='.js', kind=None),
                            Constant(value='.xml', kind=None),
                            Constant(value='.csv', kind=None),
                            Constant(value='.html', kind=None),
                        ],
                        values=[
                            Constant(value='text/css', kind=None),
                            Constant(value='text/less', kind=None),
                            Constant(value='text/scss', kind=None),
                            Constant(value='text/javascript', kind=None),
                            Constant(value='text/xml', kind=None),
                            Constant(value='text/csv', kind=None),
                            Constant(value='text/html', kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=BoolOp(
                        op=Or(),
                        values=[
                            BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='ext', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=False, kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='exts', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='default', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            Name(id='exts', ctx=Load()),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='slugify_one',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='s', annotation=None, type_comment=None),
                    arg(arg='max_length', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=0, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Transform a string to a slug that can be used in a url path.\n        This method will first try to do the job with python-slugify if present.\n        Otherwise it will process string by stripping leading and ending spaces,\n        converting unicode chars to ascii, lowering all chars and replacing spaces\n        and underscore with hyphen "-".\n        :param s: str\n        :param max_length: int\n        :rtype: str\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='s', ctx=Store())],
                    value=Call(
                        func=Name(id='ustr', ctx=Load()),
                        args=[Name(id='s', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='slugify_lib', ctx=Load()),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='slugify_lib', ctx=Load()),
                                            attr='slugify',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='s', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='max_length',
                                                value=Name(id='max_length', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='TypeError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='uni', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='unicodedata', ctx=Load()),
                                            attr='normalize',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='NFKD', kind=None),
                                            Name(id='s', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='encode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ascii', kind=None),
                                    Constant(value='ignore', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='decode',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ascii', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='slug_str', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='[\\W_]', kind=None),
                                            Constant(value=' ', kind=None),
                                            Name(id='uni', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='strip',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='lower',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='slug_str', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='sub',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='[-\\s]+', kind=None),
                            Constant(value='-', kind=None),
                            Name(id='slug_str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=IfExp(
                        test=Compare(
                            left=Name(id='max_length', ctx=Load()),
                            ops=[Gt()],
                            comparators=[Constant(value=0, kind=None)],
                        ),
                        body=Subscript(
                            value=Name(id='slug_str', ctx=Load()),
                            slice=Slice(
                                lower=None,
                                upper=Name(id='max_length', ctx=Load()),
                                step=None,
                            ),
                            ctx=Load(),
                        ),
                        orelse=Name(id='slug_str', ctx=Load()),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='slugify',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='s', annotation=None, type_comment=None),
                    arg(arg='max_length', annotation=None, type_comment=None),
                    arg(arg='path', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=0, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='path', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='slugify_one', ctx=Load()),
                                args=[Name(id='s', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='max_length',
                                        value=Name(id='max_length', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='u', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='s', ctx=Load()),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='slugify_one', ctx=Load()),
                                            args=[Name(id='u', ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='max_length',
                                                    value=Name(id='max_length', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='res', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='slugify_one', ctx=Load()),
                                                        args=[Name(id='u', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='max_length',
                                                                value=Name(id='max_length', ctx=Load()),
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
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='path_no_ext', ctx=Store()),
                                        Name(id='ext', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='splitext',
                                    ctx=Load(),
                                ),
                                args=[Name(id='s', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='ext', ctx=Load()),
                                    Compare(
                                        left=Name(id='ext', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Call(
                                                func=Name(id='_guess_mimetype', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='slugify_one', ctx=Load()),
                                            args=[Name(id='path_no_ext', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Name(id='ext', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='/', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='res', ctx=Load())],
                                keywords=[],
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
            name='slug',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='value', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='value', ctx=Load()),
                            Attribute(
                                value=Name(id='models', ctx=Load()),
                                attr='BaseModel',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='value', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value='Cannot slug non-existent record %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='value', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='identifier', ctx=Store()),
                                        Name(id='name', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Attribute(
                                        value=Name(id='value', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Name(id='value', ctx=Load()),
                                                    Constant(value='seo_name', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='value', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='identifier', ctx=Store()),
                                        Name(id='name', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='value', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                ),
                Assign(
                    targets=[Name(id='slugname', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='slugify', ctx=Load()),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='name', ctx=Load()),
                                                    Constant(value='', kind=None),
                                                ],
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
                            attr='strip',
                            ctx=Load(),
                        ),
                        args=[Constant(value='-', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='slugname', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='str', ctx=Load()),
                                args=[Name(id='identifier', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=BinOp(
                        left=Constant(value='%s-%d', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Name(id='slugname', ctx=Load()),
                                Name(id='identifier', ctx=Load()),
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
        Assign(
            targets=[Name(id='_UNSLUG_RE', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='(?:(\\w{1,2}|\\w[A-Za-z0-9-_]+?\\w)-)?(-?\\d+)(?=$|/)', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='unslug',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='s', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='Extract slug and id from a string.\n        Always return un 2-tuple (str|None, int|None)\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='m', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='_UNSLUG_RE', ctx=Load()),
                            attr='match',
                            ctx=Load(),
                        ),
                        args=[Name(id='s', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='m', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Call(
                                func=Attribute(
                                    value=Name(id='m', ctx=Load()),
                                    attr='group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=1, kind=None)],
                                keywords=[],
                            ),
                            Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='m', ctx=Load()),
                                            attr='group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=2, kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
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
            name='unslug_url',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='s', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' From /blog/my-super-blog-1" to "blog/1" ', kind=None),
                ),
                Assign(
                    targets=[Name(id='parts', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='s', ctx=Load()),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value='/', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='parts', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='unslug_val', ctx=Store())],
                            value=Call(
                                func=Name(id='unslug', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='parts', ctx=Load()),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Subscript(
                                value=Name(id='unslug_val', ctx=Load()),
                                slice=Constant(value=1, kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='parts', ctx=Load()),
                                            slice=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='unslug_val', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='/', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='parts', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='s', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='url_lang',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='path_or_uri', annotation=None, type_comment=None),
                    arg(arg='lang_code', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=" Given a relative URL, make it absolute and add the required lang or\n        remove useless lang.\n        Nothing will be done for absolute URL.\n        If there is only one language installed, the lang will not be handled\n        unless forced with `lang` parameter.\n\n        :param lang_code: Must be the lang `code`. It could also be something\n                          else, such as `'[lang]'` (used for url_return).\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='Lang', ctx=Store())],
                    value=Subscript(
                        value=Attribute(
                            value=Name(id='request', ctx=Load()),
                            attr='env',
                            ctx=Load(),
                        ),
                        slice=Constant(value='res.lang', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='location', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='to_text',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path_or_uri', ctx=Load())],
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
                Assign(
                    targets=[Name(id='force_lang', ctx=Store())],
                    value=Compare(
                        left=Name(id='lang_code', ctx=Load()),
                        ops=[IsNot()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='werkzeug', ctx=Load()),
                                attr='urls',
                                ctx=Load(),
                            ),
                            attr='url_parse',
                            ctx=Load(),
                        ),
                        args=[Name(id='location', ctx=Load())],
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
                                    value=Name(id='url', ctx=Load()),
                                    attr='netloc',
                                    ctx=Load(),
                                ),
                            ),
                            UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='url', ctx=Load()),
                                    attr='scheme',
                                    ctx=Load(),
                                ),
                            ),
                            BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='url', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    Name(id='force_lang', ctx=Load()),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='location', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='urls',
                                        ctx=Load(),
                                    ),
                                    attr='url_join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    Name(id='location', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lang_url_codes', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='url_code', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='_', ctx=Store()),
                                                Name(id='url_code', ctx=Store()),
                                                Starred(
                                                    value=Name(id='_', ctx=Store()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='Lang', ctx=Load()),
                                                attr='get_available',
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
                        Assign(
                            targets=[Name(id='lang_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='to_text',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='lang_code', ctx=Load()),
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='lang', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lang_url_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Lang', ctx=Load()),
                                    attr='_lang_code_to_urlcode',
                                    ctx=Load(),
                                ),
                                args=[Name(id='lang_code', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lang_url_code', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='lang_url_code', ctx=Load()),
                                    ops=[In()],
                                    comparators=[Name(id='lang_url_codes', ctx=Load())],
                                ),
                                body=Name(id='lang_url_code', ctx=Load()),
                                orelse=Name(id='lang_code', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='lang_url_codes', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            Name(id='force_lang', ctx=Load()),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='is_multilang_url', ctx=Load()),
                                        args=[
                                            Name(id='location', ctx=Load()),
                                            Name(id='lang_url_codes', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='loc', ctx=Store()),
                                                Name(id='sep', ctx=Store()),
                                                Name(id='qs', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='location', ctx=Load()),
                                            attr='partition',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='?', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ps', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='loc', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind='u')],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='default_lg', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.http', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get_default_lang',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='ps', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='lang_url_codes', ctx=Load())],
                                    ),
                                    body=[
                                        If(
                                            test=Name(id='force_lang', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='ps', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='lang_url_code', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='ps', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='default_lg', ctx=Load()),
                                                                attr='url_code',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='ps', ctx=Load()),
                                                                    attr='pop',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=1, kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='lang_url_code', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='default_lg', ctx=Load()),
                                                                attr='url_code',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='force_lang', ctx=Load()),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ps', ctx=Load()),
                                                            attr='insert',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value=1, kind=None),
                                                            Name(id='lang_url_code', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='ps', ctx=Load()),
                                            slice=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ps', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='location', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Constant(value='/', kind='u'),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='ps', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='/', kind='u'),
                                                ],
                                            ),
                                            op=Add(),
                                            right=Name(id='sep', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='qs', ctx=Load()),
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
                    value=Name(id='location', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='url_for',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='url_from', annotation=None, type_comment=None),
                    arg(arg='lang_code', annotation=None, type_comment=None),
                    arg(arg='no_rewrite', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=" Return the url with the rewriting applied.\n        Nothing will be done for absolute URL, or short URL from 1 char.\n\n        :param url_from: The URL to convert.\n        :param lang_code: Must be the lang `code`. It could also be something\n                          else, such as `'[lang]'` (used for url_return).\n        :param no_rewrite: don't try to match route with website.rewrite.\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='new_url', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='routing', ctx=Store())],
                    value=Call(
                        func=Name(id='getattr', ctx=Load()),
                        args=[
                            Name(id='request', ctx=Load()),
                            Constant(value='website_routing', kind=None),
                            Constant(value=None, kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Attribute(
                                value=Call(
                                    func=Name(id='getattr', ctx=Load()),
                                    args=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='ir.http', kind=None),
                                            ctx=Load(),
                                        ),
                                        Constant(value='_rewrite_len', kind=None),
                                        Dict(keys=[], values=[]),
                                    ],
                                    keywords=[],
                                ),
                                attr='get',
                                ctx=Load(),
                            ),
                            args=[Name(id='routing', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='no_rewrite', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[
                        Tuple(
                            elts=[
                                Name(id='path', ctx=Store()),
                                Name(id='_', ctx=Store()),
                                Name(id='qs', ctx=Store()),
                            ],
                            ctx=Store(),
                        ),
                    ],
                    value=Call(
                        func=Attribute(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='url_from', ctx=Load()),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            attr='partition',
                            ctx=Load(),
                        ),
                        args=[Constant(value='?', kind=None)],
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
                                operand=Name(id='no_rewrite', ctx=Load()),
                            ),
                            Name(id='path', ctx=Load()),
                            BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='path', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='path', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind=None)],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Constant(value='/static/', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='path', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='path', ctx=Load()),
                                                attr='startswith',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='/web/', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='new_url', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='url_rewrite',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_url', ctx=Store())],
                            value=IfExp(
                                test=UnaryOp(
                                    op=Not(),
                                    operand=Name(id='qs', ctx=Load()),
                                ),
                                body=Name(id='new_url', ctx=Load()),
                                orelse=BinOp(
                                    left=Name(id='new_url', ctx=Load()),
                                    op=Add(),
                                    right=BinOp(
                                        left=Constant(value='?%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='qs', ctx=Load()),
                                    ),
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='url_lang', ctx=Load()),
                        args=[
                            BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='new_url', ctx=Load()),
                                    Name(id='url_from', ctx=Load()),
                                ],
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='lang_code',
                                value=Name(id='lang_code', ctx=Load()),
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
            name='is_multilang_url',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='local_url', annotation=None, type_comment=None),
                    arg(arg='lang_url_codes', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=" Check if the given URL content is supposed to be translated.\n        To be considered as translatable, the URL should either:\n        1. Match a POST (non-GET actually) controller that is `website=True` and\n           either `multilang` specified to True or if not specified, with `type='http'`.\n        2. If not matching 1., everything not under /static/ or /web/ will be translatable\n    ", kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='lang_url_codes', ctx=Load()),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lang_url_codes', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='url_code', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='_', ctx=Store()),
                                                Name(id='url_code', ctx=Store()),
                                                Starred(
                                                    value=Name(id='_', ctx=Store()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='res.lang', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='get_available',
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
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='spath', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='local_url', ctx=Load()),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value='/', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Subscript(
                            value=Name(id='spath', ctx=Load()),
                            slice=Constant(value=1, kind=None),
                            ctx=Load(),
                        ),
                        ops=[In()],
                        comparators=[Name(id='lang_url_codes', ctx=Load())],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='spath', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=1, kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='local_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='/', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='spath', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='local_url', ctx=Load()),
                                        attr='partition',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='#', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value='?', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='path', ctx=Store())],
                    value=Subscript(
                        value=Name(id='url', ctx=Load()),
                        slice=Constant(value=0, kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            Compare(
                                left=Constant(value='/static/', kind=None),
                                ops=[In()],
                                comparators=[Name(id='path', ctx=Load())],
                            ),
                            Call(
                                func=Attribute(
                                    value=Name(id='path', ctx=Load()),
                                    attr='startswith',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/web/', kind=None)],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='query_string', ctx=Store())],
                    value=IfExp(
                        test=Compare(
                            left=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='url', ctx=Load())],
                                keywords=[],
                            ),
                            ops=[Gt()],
                            comparators=[Constant(value=1, kind=None)],
                        ),
                        body=Subscript(
                            value=Name(id='url', ctx=Load()),
                            slice=Constant(value=1, kind=None),
                            ctx=Load(),
                        ),
                        orelse=Constant(value=None, kind=None),
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='_', ctx=Store()),
                                        Name(id='func', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='url_rewrite',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='query_args',
                                        value=Name(id='query_string', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='func', ctx=Load()),
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='func', ctx=Load()),
                                                        attr='routing',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='website', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='func', ctx=Load()),
                                                        attr='routing',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='multilang', kind=None),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='func', ctx=Load()),
                                                                attr='routing',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='type', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='http', kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name='exception',
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='exception', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Constant(value=False, kind=None),
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
        ClassDef(
            name='ModelConverter',
            bases=[
                Attribute(
                    value=Name(id='ir_http', ctx=Load()),
                    attr='ModelConverter',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url_map', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value='[]', kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ModelConverter', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='url_map', ctx=Load()),
                                    Name(id='model', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='domain',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='domain', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='regex',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='_UNSLUG_RE', ctx=Load()),
                                attr='pattern',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='to_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='slug', ctx=Load()),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='to_python',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='matching', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='match',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='regex',
                                        ctx=Load(),
                                    ),
                                    Name(id='value', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='_uid', ctx=Store())],
                            value=Call(
                                func=Name(id='RequestUID', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='value',
                                        value=Name(id='value', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='match',
                                        value=Name(id='matching', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='converter',
                                        value=Name(id='self', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record_id', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='matching', ctx=Load()),
                                            attr='group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=2, kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='env', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='api', ctx=Load()),
                                    attr='Environment',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    Name(id='_uid', ctx=Load()),
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='record_id', ctx=Load()),
                                ops=[Lt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='env', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='model',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='record_id', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='exists',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='record_id', ctx=Store())],
                                            value=Call(
                                                func=Name(id='abs', ctx=Load()),
                                                args=[Name(id='record_id', ctx=Load())],
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
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='model',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='_converter_value',
                                                value=Name(id='value', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='record_id', ctx=Load())],
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
            name='IrHttp',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[Constant(value='ir.http', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rerouting_limit', ctx=Store())],
                    value=Constant(value=10, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_converters',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Get the converters list for custom url pattern werkzeug need to\n            match Rule. This override adds the website ones.\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='IrHttp', ctx=Load()),
                                                    Name(id='cls', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_get_converters',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Name(id='ModelConverter', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_default_lang',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lang_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.default', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner', kind=None),
                                    Constant(value='lang', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='lang_code', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.lang', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_lang_get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='lang_code', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_frontend_session_info',
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
                            targets=[Name(id='session_info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrHttp', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_frontend_session_info',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='IrHttpModel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='modules', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrHttpModel', ctx=Load()),
                                    attr='get_translation_frontend_modules',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='user_context', ctx=Store())],
                            value=IfExp(
                                test=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='get_context',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                orelse=Dict(keys=[], values=[]),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='user_context', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='lang', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='translation_hash', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get_web_translations_hash',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='modules', ctx=Load()),
                                    Name(id='lang', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='session_info', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='translationURL', kind=None),
                                            Constant(value='cache_hashes', kind=None),
                                        ],
                                        values=[
                                            Constant(value='/website/translations', kind=None),
                                            Dict(
                                                keys=[Constant(value='translations', kind=None)],
                                                values=[Name(id='translation_hash', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='session_info', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_translation_frontend_modules',
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
                            targets=[Name(id='Modules', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.module.module', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='extra_modules_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_translation_frontend_modules_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='extra_modules_name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_translation_frontend_modules_name',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='extra_modules_domain', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='new', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Modules', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='expression', ctx=Load()),
                                                            attr='AND',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Name(id='extra_modules_domain', ctx=Load()),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='state', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Constant(value='installed', kind=None),
                                                                                ],
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
                                                ],
                                                keywords=[],
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='name', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='extra_modules_name', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='new', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='extra_modules_name', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_translation_frontend_modules_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return a domain to list the domain adding web-translations and\n            dynamic resources that may be used frontend views\n        ', kind=None),
                        ),
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_translation_frontend_modules_name',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return a list of module name where web-translations and\n            dynamic resources may be used in frontend views\n        ', kind=None),
                        ),
                        Return(
                            value=List(
                                elts=[Constant(value='web', kind=None)],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='bots', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Constant(value='bot|crawl|slurp|spider|curl|wget|facebookexternalhit', kind=None),
                            attr='split',
                            ctx=Load(),
                        ),
                        args=[Constant(value='|', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_a_bot',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='user_agent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='environ',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='HTTP_USER_AGENT', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='lower',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='bot', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[Name(id='user_agent', ctx=Load())],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='bot', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='bots',
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
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='UnicodeDecodeError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Name(id='bot', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='user_agent', ctx=Load()),
                                                                        attr='encode',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Constant(value='ascii', kind=None),
                                                                        Constant(value='ignore', kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='bot', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='bots',
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
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_frontend_langs',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=ListComp(
                                elt=Name(id='code', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='code', ctx=Store()),
                                                Name(id='_', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='res.lang', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='get_installed',
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
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_nearest_lang',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='lang_code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Try to find a similar lang. Eg: fr_BE and fr_FR\n            :param lang_code: the lang `code` (en_US)\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='lang_code', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='short_match', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='short', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='lang_code', ctx=Load()),
                                        attr='partition',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='_', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='code', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_get_frontend_langs',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='code', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(id='lang_code', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='code', ctx=Load()),
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
                                                operand=Name(id='short_match', ctx=Load()),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='short', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='short_match', ctx=Store())],
                                            value=Name(id='code', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='short_match', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_geoip_setup_resolver',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='_geoip_resolver',
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='geofile', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='config', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='geoip_database', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='_geoip_resolver',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='GeoIPResolver', ctx=Load()),
                                                    attr='open',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='geofile', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Cannot load GeoIP: %s', kind=None),
                                                    Call(
                                                        func=Name(id='ustr', ctx=Load()),
                                                        args=[Name(id='e', ctx=Load())],
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
                            finalbody=[],
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_geoip_resolve',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Constant(value='geoip', kind=None),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='record', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='_geoip_resolver',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='remote_addr',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='record', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='odoo', ctx=Load()),
                                                                attr='_geoip_resolver',
                                                                ctx=Load(),
                                                            ),
                                                            attr='resolve',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='httprequest',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='remote_addr',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='geoip', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='record', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_dispatch_parameters',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='func', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Lang', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.lang', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='routing_iteration',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='context', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='is_a_bot', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='is_a_bot',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='lang_codes', ctx=Store())],
                                    value=ListComp(
                                        elt=Name(id='code', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='code', ctx=Store()),
                                                        Starred(
                                                            value=Name(id='_', ctx=Store()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='Lang', ctx=Load()),
                                                        attr='get_available',
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
                                Assign(
                                    targets=[Name(id='nearest_lang', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='func', ctx=Load()),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='get_nearest_lang',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='Lang', ctx=Load()),
                                                            attr='_lang_get_code',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='path', ctx=Load()),
                                                                slice=Constant(value=1, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='cook_lang', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='cookies',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='frontend_lang', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='cook_lang', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='cook_lang', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='lang_codes', ctx=Load())],
                                            ),
                                            Name(id='cook_lang', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='nearest_lang', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='lang', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Lang', ctx=Load()),
                                                    attr='_lang_get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='nearest_lang', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='nearest_ctx_lg', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='is_a_bot', ctx=Load()),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='get_nearest_lang',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='request', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='context',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='lang', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='nearest_ctx_lg', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='nearest_ctx_lg', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='lang_codes', ctx=Load())],
                                                    ),
                                                    Name(id='nearest_ctx_lg', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='preferred_lang', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Lang', ctx=Load()),
                                                    attr='_lang_get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='cook_lang', ctx=Load()),
                                                            Name(id='nearest_ctx_lg', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='lang', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='preferred_lang', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='_get_default_lang',
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
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='lang',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='lang', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='context', ctx=Load()),
                                            slice=Constant(value='lang', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lang', ctx=Load()),
                                            attr='_get_cached',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='code', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='context',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='context', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_dispatch',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Before executing the endpoint method, add website params on request, such as\n                - current website (record)\n                - multilang support (set on cookies)\n                - geoip dict data are added in the session\n            Then follow the parent dispatching.\n            Reminder :  Do not use `request.env` before authentication phase, otherwise the env\n                        set on request will be created with uid=None (and it is a lazy property)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='routing_iteration',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Call(
                                    func=Name(id='getattr', ctx=Load()),
                                    args=[
                                        Name(id='request', ctx=Load()),
                                        Constant(value='routing_iteration', kind=None),
                                        Constant(value=0, kind=None),
                                    ],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='func', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='routing_error', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                            attr='method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='GET', kind=None)],
                                    ),
                                    Compare(
                                        left=Constant(value='//', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='new_url', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='httprequest',
                                                            ctx=Load(),
                                                        ),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='//', kind=None),
                                                    Constant(value='/', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            op=Add(),
                                            right=Constant(value='?', kind=None),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='httprequest',
                                                        ctx=Load(),
                                                    ),
                                                    attr='query_string',
                                                    ctx=Load(),
                                                ),
                                                attr='decode',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='utf-8', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='new_url', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='code',
                                                value=Constant(value=301, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='rule', ctx=Store()),
                                                Name(id='arguments', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='_match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='func', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='rule', ctx=Load()),
                                        attr='endpoint',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='is_frontend',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='func', ctx=Load()),
                                                attr='routing',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='website', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='werkzeug', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='NotFound',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Assign(
                                            targets=[Name(id='path_components', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='httprequest',
                                                            ctx=Load(),
                                                        ),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='is_frontend',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='path_components', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ops=[Lt()],
                                                        comparators=[Constant(value=3, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='path_components', ctx=Load()),
                                                            slice=Constant(value=2, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='static', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Constant(value='.', kind=None),
                                                        ops=[NotIn()],
                                                        comparators=[
                                                            Subscript(
                                                                value=Name(id='path_components', ctx=Load()),
                                                                slice=UnaryOp(
                                                                    op=USub(),
                                                                    operand=Constant(value=1, kind=None),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='routing_error', ctx=Store())],
                                            value=Name(id='e', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='is_frontend_multilang',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='func', ctx=Load()),
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='func', ctx=Load()),
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='is_frontend',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='func', ctx=Load()),
                                                        attr='routing',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='multilang', kind=None),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='func', ctx=Load()),
                                                                attr='routing',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='type', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='http', kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                If(
                                    test=Name(id='func', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='_authenticate',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='func', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='uid',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Is()],
                                                        comparators=[Constant(value=None, kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='is_frontend',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='_auth_method_public',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
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
                                    name='e',
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='_handle_exception',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='e', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_geoip_setup_resolver',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_geoip_resolve',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='request', ctx=Load()),
                                attr='is_frontend',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='_add_dispatch_parameters',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='func', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='default_lg_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='_get_default_lang',
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
                                            value=Name(id='request', ctx=Load()),
                                            attr='routing_iteration',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='is_a_bot', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='is_a_bot',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='nearest_lang', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='func', ctx=Load()),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='get_nearest_lang',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='res.lang', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_lang_get_code',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='path', ctx=Load()),
                                                                        slice=Constant(value=1, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='url_lg', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='nearest_lang', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='path', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='wrong_url_lg', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='url_lg', ctx=Load()),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='url_lg', ctx=Load()),
                                                                ops=[NotEq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='lang',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='url_code',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Compare(
                                                                left=Name(id='url_lg', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='default_lg_id', ctx=Load()),
                                                                        attr='url_code',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='missing_url_lg', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='url_lg', ctx=Load()),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='is_frontend_multilang',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='lang',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='default_lg_id', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='httprequest',
                                                                ctx=Load(),
                                                            ),
                                                            attr='method',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='POST', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='wrong_url_lg', ctx=Load()),
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='missing_url_lg', ctx=Load()),
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='is_a_bot', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                If(
                                                    test=Name(id='url_lg', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='path', ctx=Load()),
                                                                    attr='pop',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=1, kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='lang',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='default_lg_id', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='path', ctx=Load()),
                                                                    attr='insert',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value=1, kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='lang',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='url_code',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='path', ctx=Store())],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Constant(value='/', kind=None),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='path', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='/', kind=None),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='routing_error', ctx=Store())],
                                                    value=Constant(value=None, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='redirect', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='redirect',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=BinOp(
                                                                    left=Name(id='path', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Constant(value='?', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='request', ctx=Load()),
                                                                                attr='httprequest',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='query_string',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='decode',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='utf-8', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='redirect', ctx=Load()),
                                                            attr='set_cookie',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='frontend_lang', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='lang',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='code',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Return(
                                                    value=Name(id='redirect', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Name(id='url_lg', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='uid',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=None, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='request', ctx=Load()),
                                                                        attr='httprequest',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='path',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    BinOp(
                                                                        left=Constant(value='/%s/', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='url_lg', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='path', ctx=Store())],
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='request', ctx=Load()),
                                                                                attr='httprequest',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='path',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Slice(
                                                                            lower=None,
                                                                            upper=UnaryOp(
                                                                                op=USub(),
                                                                                operand=Constant(value=1, kind=None),
                                                                            ),
                                                                            step=None,
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='httprequest',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='query_string',
                                                                        ctx=Load(),
                                                                    ),
                                                                    body=[
                                                                        AugAssign(
                                                                            target=Name(id='path', ctx=Store()),
                                                                            op=Add(),
                                                                            value=BinOp(
                                                                                left=Constant(value='?', kind=None),
                                                                                op=Add(),
                                                                                right=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='request', ctx=Load()),
                                                                                                attr='httprequest',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='query_string',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='decode',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='utf-8', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Return(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='redirect',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='path', ctx=Load())],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='code',
                                                                                value=Constant(value=301, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='path', ctx=Load()),
                                                                    attr='pop',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=1, kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='routing_error', ctx=Store())],
                                                            value=Constant(value=None, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Return(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='reroute',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Constant(value='/', kind=None),
                                                                                    attr='join',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='path', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            Constant(value='/', kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='missing_url_lg', ctx=Load()),
                                                                    Name(id='is_a_bot', ctx=Load()),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='lang',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Name(id='default_lg_id', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='context',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Name(id='dict', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='request', ctx=Load()),
                                                                                attr='context',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='lang',
                                                                                value=Attribute(
                                                                                    value=Name(id='default_lg_id', ctx=Load()),
                                                                                    attr='code',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='lang',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='default_lg_id', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='context', ctx=Store())],
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='context',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='context', ctx=Load()),
                                                    slice=Constant(value='edit_translations', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='context',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='context', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='routing_error', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='_handle_exception',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='routing_error', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrHttp', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_dispatch',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cook_lang', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='cookies',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='frontend_lang', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='is_frontend',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Name(id='cook_lang', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='lang',
                                                    ctx=Load(),
                                                ),
                                                attr='code',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='result', ctx=Load()),
                                            Constant(value='set_cookie', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='set_cookie',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='frontend_lang', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='lang',
                                                    ctx=Load(),
                                                ),
                                                attr='code',
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
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_redirect',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='location', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=303, kind=None)],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='request', ctx=Load()),
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='request', ctx=Load()),
                                            Constant(value='is_frontend', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='location', ctx=Store())],
                                    value=Call(
                                        func=Name(id='url_for', ctx=Load()),
                                        args=[Name(id='location', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='location', ctx=Load()),
                                    Name(id='code', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='reroute',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
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
                                operand=Call(
                                    func=Name(id='hasattr', ctx=Load()),
                                    args=[
                                        Name(id='request', ctx=Load()),
                                        Constant(value='rerouting', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='rerouting',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='path', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='rerouting',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[Constant(value='Rerouting loop is forbidden', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='rerouting',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='rerouting',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='rerouting_limit',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[Constant(value='Rerouting limit exceeded', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='environ',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='PATH_INFO', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='path', ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='key', ctx=Store()),
                            iter=Tuple(
                                elts=[
                                    Constant(value='path', kind=None),
                                    Constant(value='full_path', kind=None),
                                    Constant(value='url', kind=None),
                                    Constant(value='base_url', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='__dict__',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='key', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_dispatch',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_postprocess_args',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='arguments', annotation=None, type_comment=None),
                            arg(arg='rule', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrHttp', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_postprocess_args',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='arguments', ctx=Load()),
                                    Name(id='rule', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='_', ctx=Store()),
                                                Name(id='path', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rule', ctx=Load()),
                                            attr='build',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='arguments', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assert(
                                    test=Compare(
                                        left=Name(id='path', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    msg=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='MissingError',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='_handle_exception',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='werkzeug', ctx=Load()),
                                                                attr='exceptions',
                                                                ctx=Load(),
                                                            ),
                                                            attr='NotFound',
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
                                ),
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='_handle_exception',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='e', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='request', ctx=Load()),
                                            Constant(value='is_frontend_multilang', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                            attr='method',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='GET', kind=None),
                                                    Constant(value='HEAD', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='generated_path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='urls',
                                                ctx=Load(),
                                            ),
                                            attr='url_unquote_plus',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='current_path', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='werkzeug', ctx=Load()),
                                                attr='urls',
                                                ctx=Load(),
                                            ),
                                            attr='url_unquote_plus',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='generated_path', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Name(id='current_path', ctx=Load())],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='lang',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='_get_default_lang',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='path', ctx=Store())],
                                                    value=BinOp(
                                                        left=BinOp(
                                                            left=Constant(value='/', kind=None),
                                                            op=Add(),
                                                            right=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='lang',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='url_code',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='path', ctx=Load()),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='httprequest',
                                                    ctx=Load(),
                                                ),
                                                attr='query_string',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='path', ctx=Store()),
                                                    op=Add(),
                                                    value=BinOp(
                                                        left=Constant(value='?', kind=None),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='request', ctx=Load()),
                                                                        attr='httprequest',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='query_string',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='decode',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='utf-8', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='redirect',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='path', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='code',
                                                        value=Constant(value=301, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_exception_code_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return a tuple with the error code following by the values matching the exception', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Constant(value=500, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='exception',
                                        value=Name(id='exception', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='traceback',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='traceback', ctx=Load()),
                                                attr='format_exc',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='exception', ctx=Load()),
                                    Attribute(
                                        value=Name(id='exceptions', ctx=Load()),
                                        attr='UserError',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='error_message', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='exception', ctx=Load()),
                                            attr='args',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='code', ctx=Store())],
                                    value=Constant(value=400, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='exception', ctx=Load()),
                                            Attribute(
                                                value=Name(id='exceptions', ctx=Load()),
                                                attr='AccessError',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='code', ctx=Store())],
                                            value=Constant(value=403, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='exception', ctx=Load()),
                                            Name(id='QWebException', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='qweb_exception',
                                                        value=Name(id='exception', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='type', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='exception', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='exceptions', ctx=Load()),
                                                        attr='AccessError',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='code', ctx=Store())],
                                                    value=Constant(value=403, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='exception', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='werkzeug', ctx=Load()),
                                                            attr='exceptions',
                                                            ctx=Load(),
                                                        ),
                                                        attr='HTTPException',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='code', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='exception', ctx=Load()),
                                                        attr='code',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='status_message',
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='werkzeug', ctx=Load()),
                                                        attr='http',
                                                        ctx=Load(),
                                                    ),
                                                    attr='HTTP_STATUS_CODES',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='code', ctx=Load()),
                                                Constant(value='', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='status_code',
                                        value=Name(id='code', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='code', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_values_500_error',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='view', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='ir.ui.view', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_error_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='code', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='ir.ui.view', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_render_template',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='http_routing.%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='code', ctx=Load()),
                                            ),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_handle_exception',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='is_frontend_request', ctx=Store())],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='request', ctx=Load()),
                                            Constant(value='is_frontend', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
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
                                operand=Name(id='is_frontend_request', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='IrHttp', ctx=Load()),
                                                    Name(id='cls', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_handle_exception',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='exception', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='IrHttp', ctx=Load()),
                                                    Name(id='cls', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_handle_exception',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='exception', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='response', ctx=Load()),
                                            Name(id='Exception', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='exception', ctx=Store())],
                                            value=Name(id='response', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Name(id='response', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='werkzeug', kind=None),
                                                ops=[In()],
                                                comparators=[
                                                    Subscript(
                                                        value=Name(id='config', ctx=Load()),
                                                        slice=Constant(value='dev_mode', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Name(id='e', ctx=Load()),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='exception', ctx=Store())],
                                            value=Name(id='e', ctx=Load()),
                                            type_comment=None,
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
                                        Name(id='code', ctx=Store()),
                                        Name(id='values', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_get_exception_code_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='exception', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='code', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='exception', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='_auth_method_public',
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='rollback',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='registry', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='cr',
                                                            ctx=Load(),
                                                        ),
                                                        attr='dbname',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='cr', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='api', ctx=Load()),
                                            attr='Environment',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='uid',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='code', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=500, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='500 Internal Server Error:\n\n%s', kind=None),
                                                    Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='traceback', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='_get_values_500_error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='env', ctx=Load()),
                                                    Name(id='values', ctx=Load()),
                                                    Name(id='exception', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='code', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value=403, kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='403 Forbidden:\n\n%s', kind=None),
                                                            Subscript(
                                                                value=Name(id='values', ctx=Load()),
                                                                slice=Constant(value='traceback', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='code', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=400, kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='warning',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='400 Bad Request:\n\n%s', kind=None),
                                                                    Subscript(
                                                                        value=Name(id='values', ctx=Load()),
                                                                        slice=Constant(value='traceback', kind=None),
                                                                        ctx=Load(),
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
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='code', ctx=Store()),
                                                        Name(id='html', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='_get_error_html',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='env', ctx=Load()),
                                                    Name(id='code', ctx=Load()),
                                                    Name(id='values', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='code', ctx=Store()),
                                                                Name(id='html', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Tuple(
                                                        elts=[
                                                            Constant(value=418, kind=None),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='env', ctx=Load()),
                                                                        slice=Constant(value='ir.ui.view', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_render_template',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='http_routing.http_error', kind=None),
                                                                    Name(id='values', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='werkzeug', ctx=Load()),
                                        attr='wrappers',
                                        ctx=Load(),
                                    ),
                                    attr='Response',
                                    ctx=Load(),
                                ),
                                args=[Name(id='html', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='status',
                                        value=Name(id='code', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='content_type',
                                        value=Constant(value='text/html;charset=utf-8', kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='url_rewrite',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='query_args', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='new_url', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='router', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='http', ctx=Load()),
                                                attr='root',
                                                ctx=Load(),
                                            ),
                                            attr='get_db_router',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='db',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='bind',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='endpoint', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='endpoint', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='router', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='method',
                                                value=Constant(value='POST', kind=None),
                                            ),
                                            keyword(
                                                arg='query_args',
                                                value=Name(id='query_args', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='werkzeug', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='MethodNotAllowed',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='endpoint', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='router', ctx=Load()),
                                                    attr='match',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='path', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='method',
                                                        value=Constant(value='GET', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='query_args',
                                                        value=Name(id='query_args', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='werkzeug', ctx=Load()),
                                            attr='routing',
                                            ctx=Load(),
                                        ),
                                        attr='RequestRedirect',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Assign(
                                            targets=[Name(id='new_url', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='new_url',
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=Constant(value=7, kind=None),
                                                    upper=None,
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='_', ctx=Store()),
                                                        Name(id='endpoint', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='url_rewrite',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='new_url', ctx=Load()),
                                                    Name(id='query_args', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='endpoint', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='endpoint', ctx=Load()),
                                                    List(
                                                        elts=[Name(id='endpoint', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Attribute(
                                        value=Attribute(
                                            value=Name(id='werkzeug', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='NotFound',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[Name(id='new_url', ctx=Store())],
                                            value=Name(id='path', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='new_url', ctx=Load()),
                                            Name(id='path', ctx=Load()),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='endpoint', ctx=Load()),
                                            Subscript(
                                                value=Name(id='endpoint', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='tools', ctx=Load()),
                                attr='ormcache',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='path', kind=None),
                                Constant(value='query_args', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
