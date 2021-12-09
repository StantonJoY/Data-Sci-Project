Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='os.path', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='traceback', asname=None)],
        ),
        Import(
            names=[alias(name='builtins', asname=None)],
        ),
        Import(
            names=[alias(name='token', asname=None)],
        ),
        Import(
            names=[alias(name='tokenize', asname=None)],
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        ImportFrom(
            module='markupsafe',
            names=[
                alias(name='Markup', asname=None),
                alias(name='escape', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='collections.abc',
            names=[
                alias(name='Sized', asname=None),
                alias(name='Mapping', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='itertools',
            names=[
                alias(name='count', asname=None),
                alias(name='chain', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='textwrap',
            names=[
                alias(name='dedent', asname=None),
                alias(name='indent', asname='_indent'),
            ],
            level=0,
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='psycopg2.extensions',
            names=[alias(name='TransactionRollbackError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='pycompat', asname=None),
                alias(name='freehash', asname=None),
            ],
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
        Assign(
            targets=[Name(id='SUPPORTED_DEBUGGERS', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='pdb', kind=None),
                    Constant(value='ipdb', kind=None),
                    Constant(value='pudb', kind=None),
                    Constant(value='wdb', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='token', ctx=Load()),
                    attr='QWEB',
                    ctx=Store(),
                ),
            ],
            value=BinOp(
                left=Attribute(
                    value=Name(id='token', ctx=Load()),
                    attr='NT_OFFSET',
                    ctx=Load(),
                ),
                op=Sub(),
                right=Constant(value=1, kind=None),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Subscript(
                    value=Attribute(
                        value=Name(id='token', ctx=Load()),
                        attr='tok_name',
                        ctx=Load(),
                    ),
                    slice=Attribute(
                        value=Name(id='token', ctx=Load()),
                        attr='QWEB',
                        ctx=Load(),
                    ),
                    ctx=Store(),
                ),
            ],
            value=Constant(value='QWEB', kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='QWebCodeFound',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Exception raised when a qweb compilation encounter dynamic content if the\n    option `raise_on_code` is True.\n    ', kind=None),
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='QWebException',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='qweb', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='error', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
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
                                    attr='error',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='error', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='template', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Call(
                                    func=Attribute(
                                        value=Name(id='options', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='dev_mode', kind=None)],
                                    keywords=[],
                                ),
                                body=Name(id='code', ctx=Load()),
                                orelse=Constant(value=None, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='path',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='path', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='html',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='template', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Name(id='path', ctx=Load()),
                                    Compare(
                                        left=Constant(value=':', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='path', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='element', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='qweb', ctx=Load()),
                                                attr='_get_template',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='template', ctx=Load()),
                                                Name(id='options', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='nodes', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='element', ctx=Load()),
                                                    attr='getroottree',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='xpath',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='nodes', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='node', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='nodes', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='node', ctx=Load()),
                                                    slice=Slice(lower=None, upper=None, step=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='node', ctx=Load()),
                                                    attr='text',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='html',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='tostring',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='node', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='encoding',
                                                        value=Constant(value='unicode', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='stack',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='traceback', ctx=Load()),
                                    attr='format_exc',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='message',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='message', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='error',
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='message',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='%s\n%s: %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='message',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        attr='__class__',
                                                        ctx=Load(),
                                                    ),
                                                    attr='__name__',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='message',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='%s\nTemplate: %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='message',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
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
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='path',
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='message',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='%s\nPath: %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='message',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='path',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='html',
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='message',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Constant(value='%s\nNode: %s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='message',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='html',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='QWebException', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[Name(id='message', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__str__',
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
                            targets=[Name(id='message', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='%s\n%s\n%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='error',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stack',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='message',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='code',
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s\nCompiled code:\n%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='message', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
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
                            value=Name(id='message', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__repr__',
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
                                func=Name(id='str', ctx=Load()),
                                args=[Name(id='self', ctx=Load())],
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
            name='frozendict',
            bases=[Name(id='dict', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' An implementation of an immutable dictionary. ', kind=None),
                ),
                FunctionDef(
                    name='__delitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                        ],
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
                                args=[Constant(value="'__delitem__' not supported on frozendict", kind=None)],
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
                    name='__setitem__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='val', annotation=None, type_comment=None),
                        ],
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
                                args=[Constant(value="'__setitem__' not supported on frozendict", kind=None)],
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
                    name='clear',
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
                                args=[Constant(value="'clear' not supported on frozendict", kind=None)],
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
                    name='pop',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[Constant(value="'pop' not supported on frozendict", kind=None)],
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
                    name='popitem',
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
                                args=[Constant(value="'popitem' not supported on frozendict", kind=None)],
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
                    name='setdefault',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[Constant(value="'setdefault' not supported on frozendict", kind=None)],
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
                    name='update',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[Constant(value="'update' not supported on frozendict", kind=None)],
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
                    name='__hash__',
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
                                func=Name(id='hash', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='frozenset', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Tuple(
                                                    elts=[
                                                        Name(id='key', ctx=Load()),
                                                        Call(
                                                            func=Name(id='freehash', ctx=Load()),
                                                            args=[Name(id='val', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='key', ctx=Store()),
                                                                Name(id='val', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='items',
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
        Assign(
            targets=[Name(id='unsafe_eval', ctx=Store())],
            value=Name(id='eval', ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_FORMAT_REGEX', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='(?:#\\{(.+?)\\})|(?:\\{\\{(.+?)\\}\\})', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_VARNAME_REGEX', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='\\W', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='QWeb',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=Tuple(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_void_elements', ctx=Store())],
                    value=Call(
                        func=Name(id='frozenset', ctx=Load()),
                        args=[
                            List(
                                elts=[
                                    Constant(value='area', kind=None),
                                    Constant(value='base', kind=None),
                                    Constant(value='br', kind=None),
                                    Constant(value='col', kind=None),
                                    Constant(value='embed', kind=None),
                                    Constant(value='hr', kind=None),
                                    Constant(value='img', kind=None),
                                    Constant(value='input', kind=None),
                                    Constant(value='keygen', kind=None),
                                    Constant(value='link', kind=None),
                                    Constant(value='menuitem', kind=None),
                                    Constant(value='meta', kind=None),
                                    Constant(value='param', kind=None),
                                    Constant(value='source', kind=None),
                                    Constant(value='track', kind=None),
                                    Constant(value='wbr', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_name_gen', ctx=Store())],
                    value=Call(
                        func=Name(id='count', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_available_objects', ctx=Store())],
                    value=DictComp(
                        key=Name(id='k', ctx=Load()),
                        value=Name(id='v', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Tuple(
                                    elts=[
                                        Name(id='k', ctx=Store()),
                                        Name(id='v', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                                iter=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='vars', ctx=Load()),
                                            args=[Name(id='builtins', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='items',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ifs=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='k', ctx=Load()),
                                                attr='startswith',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='_', kind=None)],
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
                Assign(
                    targets=[Name(id='_allowed_keyword', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='False', kind=None),
                            Constant(value='None', kind=None),
                            Constant(value='True', kind=None),
                            Constant(value='and', kind=None),
                            Constant(value='as', kind=None),
                            Constant(value='elif', kind=None),
                            Constant(value='else', kind=None),
                            Constant(value='for', kind=None),
                            Constant(value='if', kind=None),
                            Constant(value='in', kind=None),
                            Constant(value='is', kind=None),
                            Constant(value='not', kind=None),
                            Constant(value='or', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_render',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='options', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' render(template, values, **options)\n\n        Render the template specified by the given name.\n\n        :param template: template identifier, name or etree (see ``_get_template``)\n        :param dict values: template values to be used for rendering\n        :param options: used to compile the template (the dict available for the rendering is frozen)\n            * ``load`` (function) overrides the load method (returns: (template, ref))\n\n        :returns: str as Markup\n        :rtype: markupsafe.Markup\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='values', ctx=Load()),
                                    Compare(
                                        left=Constant(value=0, kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[Constant(value='values[0] should be unset when call the _render method and only set into the template.', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='render_template', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='template', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendering', ctx=Store())],
                            value=Call(
                                func=Name(id='render_template', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='values', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rendering', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='Markup', ctx=Load()),
                                args=[Name(id='result', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Compile the given template into a rendering function (generator)::\n\n            render(qweb, values)\n\n        where ``qweb`` is a QWeb instance and ``values`` are the values to render.\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='options', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='options', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='element', ctx=Store()),
                                        Name(id='document', ctx=Store()),
                                        Name(id='ref', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_template',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='template', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='ref', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ref', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='element', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='t-name', kind=None),
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='document', ctx=Load())],
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
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='ref', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='ref', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='ref_xml', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='document', ctx=Load()),
                                        Name(id='str', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                body=Name(id='document', ctx=Load()),
                                orelse=Call(
                                    func=Name(id='str', ctx=Load()),
                                    args=[
                                        Name(id='document', ctx=Load()),
                                        Constant(value='utf-8', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='_options', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[Name(id='options', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='options', ctx=Store())],
                            value=Call(
                                func=Name(id='frozendict', ctx=Load()),
                                args=[Name(id='options', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='_options', ctx=Load()),
                                    slice=Constant(value='template', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='template', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='_options', ctx=Load()),
                                    slice=Constant(value='root', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='element', ctx=Load()),
                                    attr='getroottree',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='_options', ctx=Load()),
                                    slice=Constant(value='last_path_node', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='options', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='nsmap', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='_options', ctx=Load()),
                                            slice=Constant(value='nsmap', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='def_name', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='ref', ctx=Load()),
                                        Name(id='int', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                body=JoinedStr(
                                    values=[
                                        Constant(value='template_', kind=None),
                                        FormattedValue(
                                            value=Name(id='ref', ctx=Load()),
                                            conversion=-1,
                                            format_spec=None,
                                        ),
                                    ],
                                ),
                                orelse=Constant(value='template', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='_options', ctx=Load()),
                                            slice=Constant(value='_text_concat', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_appendText',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='', kind=None),
                                            Name(id='_options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='code_lines', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=List(
                                                elts=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='def ', kind=None),
                                                            FormattedValue(
                                                                value=Name(id='def_name', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='(self, values, log):', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_node',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='element', ctx=Load()),
                                                    Name(id='_options', ctx=Load()),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_flushText',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='_options', ctx=Load()),
                                                Constant(value=1, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='QWebException', ctx=Load()),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Name(id='e', ctx=Load()),
                                            cause=None,
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='QWebCodeFound', ctx=Load()),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Name(id='e', ctx=Load()),
                                            cause=None,
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='QWebException', ctx=Load()),
                                                args=[
                                                    Constant(value='Error when compiling xml template', kind=None),
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='error',
                                                        value=Name(id='e', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='template',
                                                        value=Name(id='template', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='path',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='_options', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='last_path_node', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='code', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='\n', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='code_lines', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='QWebException', ctx=Load()),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Name(id='e', ctx=Load()),
                                            cause=None,
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Assign(
                                            targets=[Name(id='code', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Constant(value='\n', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='map', ctx=Load()),
                                                        args=[
                                                            Name(id='str', ctx=Load()),
                                                            Name(id='code_lines', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='QWebException', ctx=Load()),
                                                args=[
                                                    Constant(value='Error when compiling xml template', kind=None),
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='error',
                                                        value=Name(id='e', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='template',
                                                        value=Name(id='template', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='code',
                                                        value=Name(id='code', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='compiled', ctx=Store())],
                                    value=Call(
                                        func=Name(id='compile', ctx=Load()),
                                        args=[
                                            Name(id='code', ctx=Load()),
                                            JoinedStr(
                                                values=[
                                                    Constant(value='<', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='def_name', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='>', kind=None),
                                                ],
                                            ),
                                            Constant(value='exec', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='globals_dict', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_prepare_globals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(keys=[], values=[]),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='globals_dict', ctx=Load()),
                                            slice=Constant(value='__builtins__', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='globals_dict', ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='unsafe_eval', ctx=Load()),
                                        args=[
                                            Name(id='compiled', ctx=Load()),
                                            Name(id='globals_dict', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='compiled_fn', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='globals_dict', ctx=Load()),
                                        slice=Name(id='def_name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='QWebException', ctx=Load()),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Name(id='e', ctx=Load()),
                                            cause=None,
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='QWebException', ctx=Load()),
                                                args=[
                                                    Constant(value='Error when compiling xml template', kind=None),
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='error',
                                                        value=Name(id='e', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='template',
                                                        value=Name(id='template', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='code',
                                                        value=Name(id='code', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        FunctionDef(
                            name='render_template',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='self', annotation=None, type_comment=None),
                                    arg(arg='values', annotation=None, type_comment=None),
                                ],
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
                                            targets=[Name(id='log', ctx=Store())],
                                            value=Dict(
                                                keys=[Constant(value='last_path_node', kind=None)],
                                                values=[Constant(value=None, kind=None)],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_prepare_values',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='values', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=YieldFrom(
                                                value=Call(
                                                    func=Name(id='compiled_fn', ctx=Load()),
                                                    args=[
                                                        Name(id='self', ctx=Load()),
                                                        Name(id='values', ctx=Load()),
                                                        Name(id='log', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Name(id='QWebException', ctx=Load()),
                                                    Name(id='TransactionRollbackError', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Name(id='e', ctx=Load()),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='QWebException', ctx=Load()),
                                                        args=[
                                                            Constant(value='Error when render the template', kind=None),
                                                            Name(id='self', ctx=Load()),
                                                            Name(id='options', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='error',
                                                                value=Name(id='e', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='template',
                                                                value=Name(id='template', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='path',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='log', ctx=Load()),
                                                                        attr='get',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='last_path_node', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='code',
                                                                value=Name(id='code', ctx=Load()),
                                                            ),
                                                        ],
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
                        Return(
                            value=Name(id='render_template', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_template',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Retrieve the given template, and return it as a tuple ``(etree,\n        xml, ref)``, where ``element`` is an etree, ``document`` is the\n        string document that contains ``element``, and ``ref`` if the uniq\n        reference of the template (id, t-name or template).\n\n        :param template: template identifier, name or etree\n        :param options: used to compile the template (the dict available for\n            the rendering is frozen)\n            ``load`` (function) overrides the load method\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ref', ctx=Store())],
                            value=Name(id='template', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='template', ctx=Load()),
                                    Attribute(
                                        value=Name(id='etree', ctx=Load()),
                                        attr='_Element',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='element', ctx=Store())],
                                    value=Name(id='template', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='document', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='tostring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='template', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Name(id='element', ctx=Load()),
                                            Name(id='document', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='template', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='t-name', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='loaded', ctx=Store())],
                                            value=Call(
                                                func=Call(
                                                    func=Attribute(
                                                        value=Name(id='options', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='load', kind=None),
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_load',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                args=[
                                                    Name(id='template', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='loaded', ctx=Load()),
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValueError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value="Can not load template '%s'", kind=None),
                                                                op=Mod(),
                                                                right=Name(id='template', ctx=Load()),
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
                                                        Name(id='document', ctx=Store()),
                                                        Name(id='ref', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='loaded', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='QWebException', ctx=Load()),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Name(id='e', ctx=Load()),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Assign(
                                                    targets=[Name(id='template', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='options', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='caller_template', kind=None),
                                                            Name(id='template', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='QWebException', ctx=Load()),
                                                        args=[
                                                            Constant(value='load could not load template', kind=None),
                                                            Name(id='self', ctx=Load()),
                                                            Name(id='options', ctx=Load()),
                                                            Name(id='e', ctx=Load()),
                                                            Name(id='template', ctx=Load()),
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
                        ),
                        If(
                            test=Compare(
                                left=Name(id='document', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='QWebException', ctx=Load()),
                                        args=[
                                            Constant(value='Template not found', kind=None),
                                            Name(id='self', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='template',
                                                value=Name(id='template', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='document', ctx=Load()),
                                    Attribute(
                                        value=Name(id='etree', ctx=Load()),
                                        attr='_Element',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='element', ctx=Store())],
                                    value=Name(id='document', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='document', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='tostring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='document', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='encoding',
                                                value=Constant(value='utf-8', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='document', ctx=Load()),
                                                                attr='strip',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        attr='startswith',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='<', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='os', ctx=Load()),
                                                        attr='path',
                                                        ctx=Load(),
                                                    ),
                                                    attr='exists',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='document', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='element', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='etree', ctx=Load()),
                                                            attr='parse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='document', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='getroot',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='element', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='fromstring',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='document', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        For(
                            target=Name(id='node', ctx=Store()),
                            iter=Name(id='element', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='node', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='t-name', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='template', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Name(id='node', ctx=Load()),
                                                    Name(id='document', ctx=Load()),
                                                    Name(id='ref', ctx=Load()),
                                                ],
                                                ctx=Load(),
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
                            value=Tuple(
                                elts=[
                                    Name(id='element', ctx=Load()),
                                    Name(id='document', ctx=Load()),
                                    Name(id='ref', ctx=Load()),
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
                    name='_load',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Load a given template and return a tuple ``(xml, ref)``` ', kind=None),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='template', ctx=Load()),
                                    Constant(value=None, kind=None),
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
                    name='_prepare_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Prepare the context that will sent to the compiled and evaluated\n        function.\n\n        :param values: template values to be used for rendering\n        :param options: frozen dict of compilation parameters.\n        ', kind=None),
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_globals',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='globals_dict', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Prepare the global context that will sent to eval the qweb generated\n        code.\n\n        :param globals_dict: template global values use in compiled code\n        :param options: frozen dict of compilation parameters.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='globals_dict', ctx=Load()),
                                    slice=Constant(value='Sized', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='Sized', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='globals_dict', ctx=Load()),
                                    slice=Constant(value='Mapping', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='Mapping', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='globals_dict', ctx=Load()),
                                    slice=Constant(value='Markup', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='Markup', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='globals_dict', ctx=Load()),
                                    slice=Constant(value='escape', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='escape', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='globals_dict', ctx=Load()),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='type', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='globals_dict', ctx=Load()),
                                    slice=Constant(value='compile_options', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='options', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='globals_dict', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_available_objects',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='globals_dict', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_appendText',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='text', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Add an item (converts to a string) to the list.\n            This will be concatenated and added during a call to the\n            `_flushText` method. This makes it possible to return only one\n            yield containing all the parts.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='options', ctx=Load()),
                                        slice=Constant(value='_text_concat', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_to_str',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='text', ctx=Load())],
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
                    name='_flushText',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Concatenate all the textual chunks added by the `_appendText`\n            method into a single yield.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='text_concat', ctx=Store())],
                            value=Subscript(
                                value=Name(id='options', ctx=Load()),
                                slice=Constant(value='_text_concat', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='text_concat', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='text', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='text_concat', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='text_concat', ctx=Load()),
                                            attr='clear',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=List(
                                        elts=[
                                            JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=BinOp(
                                                            left=Constant(value='    ', kind=None),
                                                            op=Mult(),
                                                            right=Name(id='indent', ctx=Load()),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='yield ', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[Name(id='text', ctx=Load())],
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
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_indent',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Indent the code to respect the python syntax.', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='_indent', ctx=Load()),
                                args=[
                                    Name(id='code', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='    ', kind=None),
                                        op=Mult(),
                                        right=Name(id='indent', ctx=Load()),
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
                    name='_make_name',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='prefix', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='var', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Generates a unique name.', kind=None),
                        ),
                        Return(
                            value=JoinedStr(
                                values=[
                                    FormattedValue(
                                        value=Name(id='prefix', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value='_', kind=None),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='next', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_name_gen',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
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
                    name='_compile_node',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Compile the given element into python code.\n\n            The t-* attributes (directives) will be converted to a python instruction. If there\n            are no t-* attributes, the element will be considered static.\n\n            Directives are compiled using the order provided by the\n            ``_directives_eval_order`` method (an create the\n            ``options['iter_directives']`` iterator).\n            For compilation, the directives supported are those with a\n            compilation method ``_compile_directive_*``\n\n        :return: list of string\n        ", kind=None),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_static_node',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_static_node',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='raise_on_code', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='QWebCodeFound', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='options', ctx=Load()),
                                        slice=Constant(value='root', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='getpath',
                                    ctx=Load(),
                                ),
                                args=[Name(id='el', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='last_path_node', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Name(id='path', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='last_path_node', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='path', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='log["last_path_node"] = ', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[Name(id='path', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='iter_directives', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='iter', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_directives_eval_order',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=List(
                                            elts=[Constant(value=None, kind=None)],
                                            ctx=Load(),
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
                                    value=Name(id='el', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='t-tag', kind=None),
                                    Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='tag',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=BinOp(
                                    left=Set(
                                        elts=[
                                            Constant(value='t-out', kind=None),
                                            Constant(value='t-esc', kind=None),
                                            Constant(value='t-raw', kind=None),
                                            Constant(value='t-field', kind=None),
                                        ],
                                    ),
                                    op=BitAnd(),
                                    right=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='t-content', kind=None),
                                            Constant(value='True', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='body', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_compile_directives',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='el', ctx=Load()),
                                        Name(id='options', ctx=Load()),
                                        Name(id='indent', ctx=Load()),
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
                    name='_compile_directives',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Compile the given element, following the directives given in the\n        iterator ``options['iter_directives']`` create by `_compile_node``\n        method.\n\n        :return: list of code lines\n        ", kind=None),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_static_node',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='t-tag', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='t-content', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_static_node',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='directive', ctx=Store()),
                            iter=Subscript(
                                value=Name(id='options', ctx=Load()),
                                slice=Constant(value='iter_directives', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=Constant(value='t-', kind=None),
                                            op=Add(),
                                            right=Name(id='directive', ctx=Load()),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_directive',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='el', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                    Name(id='directive', ctx=Load()),
                                                    Name(id='indent', ctx=Load()),
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
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_format',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='expr', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Parses the provided format string and compiles it to a single\n        expression python, uses string with format method.\n        Use format is faster to concat string and values.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='text', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_idx', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='m', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='_FORMAT_REGEX', ctx=Load()),
                                    attr='finditer',
                                    ctx=Load(),
                                ),
                                args=[Name(id='expr', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='literal', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='expr', ctx=Load()),
                                        slice=Slice(
                                            lower=Name(id='base_idx', ctx=Load()),
                                            upper=Call(
                                                func=Attribute(
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='start',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='literal', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='text', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='literal', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='{', kind=None),
                                                            Constant(value='{{', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='}', kind=None),
                                                    Constant(value='}}', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                AugAssign(
                                    target=Name(id='text', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='{}', kind=None),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='self._compile_to_str(', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_compile_expr',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                BoolOp(
                                                                    op=Or(),
                                                                    values=[
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
                                                                            func=Attribute(
                                                                                value=Name(id='m', ctx=Load()),
                                                                                attr='group',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value=2, kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=')', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='base_idx', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='m', ctx=Load()),
                                            attr='end',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='literal', ctx=Store())],
                            value=Subscript(
                                value=Name(id='expr', ctx=Load()),
                                slice=Slice(
                                    lower=Name(id='base_idx', ctx=Load()),
                                    upper=None,
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='literal', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='text', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='literal', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='{', kind=None),
                                                    Constant(value='{{', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='}', kind=None),
                                            Constant(value='}}', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Call(
                                func=Name(id='repr', ctx=Load()),
                                args=[Name(id='text', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='values', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='code', ctx=Store()),
                                    op=Add(),
                                    value=JoinedStr(
                                        values=[
                                            Constant(value='.format(', kind=None),
                                            FormattedValue(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Constant(value=', ', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='values', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=')', kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_expr_tokens',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tokens', annotation=None, type_comment=None),
                            arg(arg='allowed_keys', annotation=None, type_comment=None),
                            arg(arg='raise_on_missing', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Transform the list of token coming into a python instruction in\n            textual form by adding the namepaces for the dynamic values.\n\n            Example: `5 + a + b.c` to be `5 + values.get('a') + values['b'].c`\n            Unknown values are considered to be None, but using `values['b']`\n            gives a clear error message in cases where there is an attribute for\n            example (have a `KeyError: 'b'`, instead of `AttributeError: 'NoneType'\n            object has no attribute 'c'`).\n\n            @returns str\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='index', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='open_bracket_index', ctx=Store())],
                            value=UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bracket_depth', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        While(
                            test=Compare(
                                left=Name(id='index', ctx=Load()),
                                ops=[Lt()],
                                comparators=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='tokens', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='t', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='tokens', ctx=Load()),
                                        slice=Name(id='index', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='t', ctx=Load()),
                                            attr='exact_type',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='token', ctx=Load()),
                                                        attr='LPAR',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='token', ctx=Load()),
                                                        attr='LSQB',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='token', ctx=Load()),
                                                        attr='LBRACE',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='bracket_depth', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='t', ctx=Load()),
                                            attr='exact_type',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='token', ctx=Load()),
                                                        attr='RPAR',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='token', ctx=Load()),
                                                        attr='RSQB',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='token', ctx=Load()),
                                                        attr='RBRACE',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='bracket_depth', ctx=Store()),
                                            op=Sub(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='bracket_depth', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='t', ctx=Load()),
                                                            attr='exact_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='token', ctx=Load()),
                                                                attr='NAME',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='string', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='t', ctx=Load()),
                                                        attr='string',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='string', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='lambda', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='i', ctx=Store())],
                                                            value=BinOp(
                                                                left=Name(id='index', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        While(
                                                            test=Compare(
                                                                left=Name(id='i', ctx=Load()),
                                                                ops=[Lt()],
                                                                comparators=[
                                                                    Call(
                                                                        func=Name(id='len', ctx=Load()),
                                                                        args=[Name(id='tokens', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='t', ctx=Store())],
                                                                    value=Subscript(
                                                                        value=Name(id='tokens', ctx=Load()),
                                                                        slice=Name(id='i', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='t', ctx=Load()),
                                                                            attr='exact_type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='token', ctx=Load()),
                                                                                attr='NAME',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='allowed_keys', ctx=Load()),
                                                                                    attr='append',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='t', ctx=Load()),
                                                                                        attr='string',
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
                                                                                left=Attribute(
                                                                                    value=Name(id='t', ctx=Load()),
                                                                                    attr='exact_type',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[
                                                                                    Attribute(
                                                                                        value=Name(id='token', ctx=Load()),
                                                                                        attr='COMMA',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[Pass()],
                                                                            orelse=[
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='t', ctx=Load()),
                                                                                            attr='exact_type',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
                                                                                            Attribute(
                                                                                                value=Name(id='token', ctx=Load()),
                                                                                                attr='COLON',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[Break()],
                                                                                    orelse=[
                                                                                        If(
                                                                                            test=Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='t', ctx=Load()),
                                                                                                    attr='exact_type',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='token', ctx=Load()),
                                                                                                        attr='EQUAL',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            body=[
                                                                                                Raise(
                                                                                                    exc=Call(
                                                                                                        func=Name(id='NotImplementedError', ctx=Load()),
                                                                                                        args=[Constant(value='Lambda default values are not supported', kind=None)],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    cause=None,
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[
                                                                                                Raise(
                                                                                                    exc=Call(
                                                                                                        func=Name(id='NotImplementedError', ctx=Load()),
                                                                                                        args=[Constant(value='This lambda code style is not implemented.', kind=None)],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    cause=None,
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                AugAssign(
                                                                    target=Name(id='i', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Constant(value=1, kind=None),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='string', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='for', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='i', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Name(id='index', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                While(
                                                                    test=Compare(
                                                                        left=Call(
                                                                            func=Name(id='len', ctx=Load()),
                                                                            args=[Name(id='tokens', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        ops=[Gt()],
                                                                        comparators=[Name(id='i', ctx=Load())],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='t', ctx=Store())],
                                                                            value=Subscript(
                                                                                value=Name(id='tokens', ctx=Load()),
                                                                                slice=Name(id='i', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='t', ctx=Load()),
                                                                                    attr='exact_type',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[
                                                                                    Attribute(
                                                                                        value=Name(id='token', ctx=Load()),
                                                                                        attr='NAME',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='t', ctx=Load()),
                                                                                            attr='string',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='in', kind=None)],
                                                                                    ),
                                                                                    body=[Break()],
                                                                                    orelse=[],
                                                                                ),
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='allowed_keys', ctx=Load()),
                                                                                            attr='append',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='t', ctx=Load()),
                                                                                                attr='string',
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
                                                                                        left=Attribute(
                                                                                            value=Name(id='t', ctx=Load()),
                                                                                            attr='exact_type',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[In()],
                                                                                        comparators=[
                                                                                            List(
                                                                                                elts=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='token', ctx=Load()),
                                                                                                        attr='COMMA',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Name(id='token', ctx=Load()),
                                                                                                        attr='LPAR',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Attribute(
                                                                                                        value=Name(id='token', ctx=Load()),
                                                                                                        attr='RPAR',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    body=[Pass()],
                                                                                    orelse=[
                                                                                        Raise(
                                                                                            exc=Call(
                                                                                                func=Name(id='NotImplementedError', ctx=Load()),
                                                                                                args=[Constant(value='This loop code style is not implemented.', kind=None)],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            cause=None,
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        AugAssign(
                                                                            target=Name(id='i', ctx=Store()),
                                                                            op=Add(),
                                                                            value=Constant(value=1, kind=None),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                AugAssign(
                                    target=Name(id='index', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='index', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='open_bracket_index', ctx=Store())],
                            value=UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bracket_depth', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        While(
                            test=Compare(
                                left=Name(id='index', ctx=Load()),
                                ops=[Lt()],
                                comparators=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='tokens', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='t', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='tokens', ctx=Load()),
                                        slice=Name(id='index', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='string', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='string',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='t', ctx=Load()),
                                            attr='exact_type',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='token', ctx=Load()),
                                                        attr='LPAR',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='token', ctx=Load()),
                                                        attr='LSQB',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='token', ctx=Load()),
                                                        attr='LBRACE',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='bracket_depth', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='open_bracket_index', ctx=Store())],
                                                    value=Name(id='index', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        AugAssign(
                                            target=Name(id='bracket_depth', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='t', ctx=Load()),
                                                    attr='exact_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='token', ctx=Load()),
                                                                attr='RPAR',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='token', ctx=Load()),
                                                                attr='RSQB',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='token', ctx=Load()),
                                                                attr='RBRACE',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='bracket_depth', ctx=Store()),
                                                    op=Sub(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='bracket_depth', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='code', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_compile_expr_tokens',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='tokens', ctx=Load()),
                                                                        slice=Slice(
                                                                            lower=BinOp(
                                                                                left=Name(id='open_bracket_index', ctx=Load()),
                                                                                op=Add(),
                                                                                right=Constant(value=1, kind=None),
                                                                            ),
                                                                            upper=Name(id='index', ctx=Load()),
                                                                            step=None,
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='list', ctx=Load()),
                                                                        args=[Name(id='allowed_keys', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    Name(id='raise_on_missing', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='code', ctx=Store())],
                                                            value=BinOp(
                                                                left=BinOp(
                                                                    left=Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='tokens', ctx=Load()),
                                                                            slice=Name(id='open_bracket_index', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='string',
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Name(id='code', ctx=Load()),
                                                                ),
                                                                op=Add(),
                                                                right=Attribute(
                                                                    value=Name(id='t', ctx=Load()),
                                                                    attr='string',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='tokens', ctx=Load()),
                                                                    slice=Slice(
                                                                        lower=Name(id='open_bracket_index', ctx=Load()),
                                                                        upper=BinOp(
                                                                            left=Name(id='index', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value=1, kind=None),
                                                                        ),
                                                                        step=None,
                                                                    ),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=List(
                                                                elts=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='tokenize', ctx=Load()),
                                                                            attr='TokenInfo',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='token', ctx=Load()),
                                                                                attr='QWEB',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='code', ctx=Load()),
                                                                            Attribute(
                                                                                value=Subscript(
                                                                                    value=Name(id='tokens', ctx=Load()),
                                                                                    slice=Name(id='open_bracket_index', ctx=Load()),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='start',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='t', ctx=Load()),
                                                                                attr='end',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='', kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='index', ctx=Store())],
                                                            value=Name(id='open_bracket_index', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                AugAssign(
                                    target=Name(id='index', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='index', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pos', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='tokens', ctx=Load()),
                                    Attribute(
                                        value=Subscript(
                                            value=Name(id='tokens', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Compare(
                                left=Name(id='index', ctx=Load()),
                                ops=[Lt()],
                                comparators=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='tokens', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='t', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='tokens', ctx=Load()),
                                        slice=Name(id='index', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='string', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='string',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='start',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='pos', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='pos', ctx=Store())],
                                            value=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='t', ctx=Load()),
                                                            attr='start',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='space', ctx=Store())],
                                    value=BinOp(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='start',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Subscript(
                                            value=Name(id='pos', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='space', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value=' ', kind=None),
                                                        op=Mult(),
                                                        right=Name(id='space', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='pos', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='start',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='t', ctx=Load()),
                                            attr='exact_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='token', ctx=Load()),
                                                attr='NAME',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='string', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='lambda', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='code', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='lambda ', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Name(id='index', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                                While(
                                                    test=Compare(
                                                        left=Name(id='index', ctx=Load()),
                                                        ops=[Lt()],
                                                        comparators=[
                                                            Call(
                                                                func=Name(id='len', ctx=Load()),
                                                                args=[Name(id='tokens', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='t', ctx=Store())],
                                                            value=Subscript(
                                                                value=Name(id='tokens', ctx=Load()),
                                                                slice=Name(id='index', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='t', ctx=Load()),
                                                                    attr='exact_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[
                                                                    List(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Name(id='token', ctx=Load()),
                                                                                attr='COMMA',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='token', ctx=Load()),
                                                                                attr='NAME',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='token', ctx=Load()),
                                                                                attr='COLON',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='code', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='t', ctx=Load()),
                                                                                attr='string',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='t', ctx=Load()),
                                                                    attr='exact_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='token', ctx=Load()),
                                                                        attr='COLON',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[Break()],
                                                            orelse=[],
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='index', ctx=Store()),
                                                            op=Add(),
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='t', ctx=Load()),
                                                                attr='end',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Subscript(
                                                                value=Name(id='pos', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='pos', ctx=Store())],
                                                            value=Tuple(
                                                                elts=[
                                                                    Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='t', ctx=Load()),
                                                                            attr='end',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=0, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[Name(id='pos', ctx=Store())],
                                                            value=Attribute(
                                                                value=Name(id='t', ctx=Load()),
                                                                attr='end',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='string', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='allowed_keys', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='code', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='string', ctx=Load())],
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
                                                                        left=BinOp(
                                                                            left=Name(id='index', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value=1, kind=None),
                                                                        ),
                                                                        ops=[Lt()],
                                                                        comparators=[
                                                                            Call(
                                                                                func=Name(id='len', ctx=Load()),
                                                                                args=[Name(id='tokens', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Subscript(
                                                                                value=Name(id='tokens', ctx=Load()),
                                                                                slice=BinOp(
                                                                                    left=Name(id='index', ctx=Load()),
                                                                                    op=Add(),
                                                                                    right=Constant(value=1, kind=None),
                                                                                ),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='exact_type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Name(id='token', ctx=Load()),
                                                                                attr='EQUAL',
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
                                                                            value=Name(id='code', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='string', ctx=Load())],
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
                                                                                left=Name(id='index', ctx=Load()),
                                                                                ops=[Gt()],
                                                                                comparators=[Constant(value=0, kind=None)],
                                                                            ),
                                                                            Subscript(
                                                                                value=Name(id='tokens', ctx=Load()),
                                                                                slice=BinOp(
                                                                                    left=Name(id='index', ctx=Load()),
                                                                                    op=Sub(),
                                                                                    right=Constant(value=1, kind=None),
                                                                                ),
                                                                                ctx=Load(),
                                                                            ),
                                                                            Compare(
                                                                                left=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Name(id='tokens', ctx=Load()),
                                                                                        slice=BinOp(
                                                                                            left=Name(id='index', ctx=Load()),
                                                                                            op=Sub(),
                                                                                            right=Constant(value=1, kind=None),
                                                                                        ),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='exact_type',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[
                                                                                    Attribute(
                                                                                        value=Name(id='token', ctx=Load()),
                                                                                        attr='DOT',
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
                                                                                    value=Name(id='code', ctx=Load()),
                                                                                    attr='append',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='string', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    Name(id='raise_on_missing', ctx=Load()),
                                                                                    BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=BinOp(
                                                                                                    left=Name(id='index', ctx=Load()),
                                                                                                    op=Add(),
                                                                                                    right=Constant(value=1, kind=None),
                                                                                                ),
                                                                                                ops=[Lt()],
                                                                                                comparators=[
                                                                                                    Call(
                                                                                                        func=Name(id='len', ctx=Load()),
                                                                                                        args=[Name(id='tokens', ctx=Load())],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Attribute(
                                                                                                    value=Subscript(
                                                                                                        value=Name(id='tokens', ctx=Load()),
                                                                                                        slice=BinOp(
                                                                                                            left=Name(id='index', ctx=Load()),
                                                                                                            op=Add(),
                                                                                                            right=Constant(value=1, kind=None),
                                                                                                        ),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='exact_type',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[In()],
                                                                                                comparators=[
                                                                                                    List(
                                                                                                        elts=[
                                                                                                            Attribute(
                                                                                                                value=Name(id='token', ctx=Load()),
                                                                                                                attr='DOT',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            Attribute(
                                                                                                                value=Name(id='token', ctx=Load()),
                                                                                                                attr='LPAR',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            Attribute(
                                                                                                                value=Name(id='token', ctx=Load()),
                                                                                                                attr='LSQB',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            Constant(value='qweb', kind=None),
                                                                                                        ],
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='code', ctx=Load()),
                                                                                            attr='append',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            JoinedStr(
                                                                                                values=[
                                                                                                    Constant(value='values[', kind=None),
                                                                                                    FormattedValue(
                                                                                                        value=Call(
                                                                                                            func=Name(id='repr', ctx=Load()),
                                                                                                            args=[Name(id='string', ctx=Load())],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                        conversion=-1,
                                                                                                        format_spec=None,
                                                                                                    ),
                                                                                                    Constant(value=']', kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='code', ctx=Load()),
                                                                                            attr='append',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            JoinedStr(
                                                                                                values=[
                                                                                                    Constant(value='values.get(', kind=None),
                                                                                                    FormattedValue(
                                                                                                        value=Call(
                                                                                                            func=Name(id='repr', ctx=Load()),
                                                                                                            args=[Name(id='string', ctx=Load())],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                        conversion=-1,
                                                                                                        format_spec=None,
                                                                                                    ),
                                                                                                    Constant(value=')', kind=None),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='t', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='tokenize', ctx=Load()),
                                                                attr='ENCODING',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='token', ctx=Load()),
                                                                attr='ENDMARKER',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='token', ctx=Load()),
                                                                attr='DEDENT',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='code', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='string', ctx=Load())],
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
                                            value=Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='end',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='pos', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='pos', ctx=Store())],
                                            value=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='t', ctx=Load()),
                                                            attr='end',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='pos', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='end',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                AugAssign(
                                    target=Name(id='index', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[Name(id='code', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_expr',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='expr', annotation=None, type_comment=None),
                            arg(arg='raise_on_missing', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Transform string coming into a python instruction in textual form by\n        adding the namepaces for the dynamic values.\n        This method tokenize the string and call ``_compile_expr_tokens``\n        method.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='readable', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='expr', ctx=Load()),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='tokens', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='tokenize', ctx=Load()),
                                                    attr='tokenize',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='readable', ctx=Load()),
                                                        attr='readline',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='tokenize', ctx=Load()),
                                        attr='TokenError',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='Can not compile expression: ', kind=None),
                                                            FormattedValue(
                                                                value=Name(id='expr', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                        ],
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
                            targets=[Name(id='expression', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile_expr_tokens',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tokens', ctx=Load()),
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_allowed_keyword',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='list', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_available_objects',
                                                            ctx=Load(),
                                                        ),
                                                        attr='keys',
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
                                keywords=[
                                    keyword(
                                        arg='raise_on_missing',
                                        value=Name(id='raise_on_missing', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=JoinedStr(
                                values=[
                                    Constant(value='(', kind=None),
                                    FormattedValue(
                                        value=Name(id='expression', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                    Constant(value=')', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_bool',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attr', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Convert the statements as a boolean.', kind=None),
                        ),
                        If(
                            test=Name(id='attr', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='attr', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=True, kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=True, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='attr', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='attr', ctx=Load()),
                                            attr='lower',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='attr', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='false', kind=None),
                                                    Constant(value='0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='attr', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='true', kind=None),
                                                            Constant(value='1', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[Name(id='default', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_to_str',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='expr', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Generates a text value (an instance of text_type) from an arbitrary\n            source.\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='pycompat', ctx=Load()),
                                    attr='to_text',
                                    ctx=Load(),
                                ),
                                args=[Name(id='expr', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_directives_eval_order',
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
                            value=Constant(value=' List all supported directives in the order in which they should be\n        evaluated on a given element. For instance, a node bearing both\n        ``foreach`` and ``if`` should see ``foreach`` executed before ``if`` aka\n        .. code-block:: xml\n            <el t-foreach="foo" t-as="bar" t-if="bar">\n        should be equivalent to\n        .. code-block:: xml\n            <t t-foreach="foo" t-as="bar">\n                <t t-if="bar">\n                    <el>\n        then this method should return ``[\'foreach\', \'if\']``.\n        ', kind=None),
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='debug', kind=None),
                                    Constant(value='foreach', kind=None),
                                    Constant(value='if', kind=None),
                                    Constant(value='elif', kind=None),
                                    Constant(value='else', kind=None),
                                    Constant(value='field', kind=None),
                                    Constant(value='esc', kind=None),
                                    Constant(value='raw', kind=None),
                                    Constant(value='out', kind=None),
                                    Constant(value='tag', kind=None),
                                    Constant(value='call', kind=None),
                                    Constant(value='set', kind=None),
                                    Constant(value='content', kind=None),
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
                    name='_is_static_node',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Test whether the given element is purely static, i.e. (there\n        are no t-* attributes), does not require dynamic rendering for its\n        attributes.\n        ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='tag',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='t', kind=None)],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='any', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='att', ctx=Load()),
                                                                    attr='startswith',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='t-', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Compare(
                                                                left=Name(id='att', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[
                                                                    List(
                                                                        elts=[
                                                                            Constant(value='t-tag', kind=None),
                                                                            Constant(value='t-content', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='att', ctx=Store()),
                                                            iter=Attribute(
                                                                value=Name(id='el', ctx=Load()),
                                                                attr='attrib',
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_static_node',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Compile a purely static element into a list of string. ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='el', ctx=Load()),
                                    attr='nsmap',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='unqualified_el_tag', ctx=Store()),
                                        Name(id='el_tag', ctx=Store()),
                                    ],
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='tag',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attrib', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_post_processing_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='tag',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='unqualified_el_tag', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='etree', ctx=Load()),
                                                attr='QName',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='el', ctx=Load()),
                                                    attr='tag',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='localname',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='el_tag', ctx=Store())],
                                    value=Name(id='unqualified_el_tag', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='prefix',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='el_tag', ctx=Store())],
                                            value=JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='prefix',
                                                            ctx=Load(),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=':', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='el_tag', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='attrib', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='ns_prefix', ctx=Store()),
                                            Name(id='ns_definition', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=BinOp(
                                        left=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='nsmap',
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='options', ctx=Load()),
                                                            slice=Constant(value='nsmap', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='ns_prefix', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='attrib', ctx=Load()),
                                                            slice=Constant(value='xmlns', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='ns_definition', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='attrib', ctx=Load()),
                                                            slice=JoinedStr(
                                                                values=[
                                                                    Constant(value='xmlns:', kind=None),
                                                                    FormattedValue(
                                                                        value=Name(id='ns_prefix', ctx=Load()),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                ],
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='ns_definition', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ns', ctx=Store())],
                                    value=Call(
                                        func=Name(id='chain', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='options', ctx=Load()),
                                                        slice=Constant(value='nsmap', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='items',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='nsmap',
                                                        ctx=Load(),
                                                    ),
                                                    attr='items',
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
                                Assign(
                                    targets=[Name(id='nsprefixmap', ctx=Store())],
                                    value=DictComp(
                                        key=Name(id='v', ctx=Load()),
                                        value=Name(id='k', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='k', ctx=Store()),
                                                        Name(id='v', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Name(id='ns', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='key', ctx=Store()),
                                            Name(id='value', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='attrib_qname', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='QName',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='key', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='attrib_qname', ctx=Load()),
                                                attr='namespace',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='attrib', ctx=Load()),
                                                            slice=JoinedStr(
                                                                values=[
                                                                    FormattedValue(
                                                                        value=Subscript(
                                                                            value=Name(id='nsprefixmap', ctx=Load()),
                                                                            slice=Attribute(
                                                                                value=Name(id='attrib_qname', ctx=Load()),
                                                                                attr='namespace',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ctx=Load(),
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value=':', kind=None),
                                                                    FormattedValue(
                                                                        value=Attribute(
                                                                            value=Name(id='attrib_qname', ctx=Load()),
                                                                            attr='localname',
                                                                            ctx=Load(),
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                ],
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='attrib', ctx=Load()),
                                                            slice=Name(id='key', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attrib', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_post_processing_att',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='tag',
                                                ctx=Load(),
                                            ),
                                            Name(id='attrib', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='original_nsmap', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='nsmap', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='unqualified_el_tag', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='t', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='attributes', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=JoinedStr(
                                                    values=[
                                                        Constant(value=' ', kind=None),
                                                        FormattedValue(
                                                            value=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='name', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                        Constant(value='="', kind=None),
                                                        FormattedValue(
                                                            value=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='escape', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='str', ctx=Load()),
                                                                                args=[Name(id='value', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                        Constant(value='"', kind=None),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='name', ctx=Store()),
                                                                Name(id='value', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='attrib', ctx=Load()),
                                                                attr='items',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Name(id='value', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                        args=[
                                                                            Name(id='value', ctx=Load()),
                                                                            Name(id='str', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_appendText',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='<', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='el_tag', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    FormattedValue(
                                                        value=Name(id='attributes', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='unqualified_el_tag', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_void_elements',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_appendText',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='/>', kind=None),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_appendText',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='>', kind=None),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='el', ctx=Load()),
                                attr='nsmap',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='nsmap', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='nsmap',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_directive_content',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='nsmap', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='original_nsmap', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_directive_content',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='unqualified_el_tag', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='t', kind=None)],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='unqualified_el_tag', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_void_elements',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_appendText',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='</', kind=None),
                                                            FormattedValue(
                                                                value=Name(id='el_tag', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='>', kind=None),
                                                        ],
                                                    ),
                                                    Name(id='options', ctx=Load()),
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
                        Return(
                            value=Name(id='body', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_attributes',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Generates the part of the code that post-process the attributes\n        (this is ``attrs`` in the compiled code) during rendering time.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_flushText',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='body', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='dedent', ctx=Load()),
                                                        args=[Constant(value='\n            attrs = self._post_processing_att(tagName, attrs, compile_options)\n            for name, value in attrs.items():\n                if value or isinstance(value, str):\n                    yield f\' {str(escape(str(name)))}="{str(escape(str(value)))}"\'\n        ', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='body', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_static_attributes',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Compile the static and dynamc attributes of the given element.\n\n        We do not support namespaced dynamic attributes.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='nsprefixmap', ctx=Store())],
                            value=DictComp(
                                key=Name(id='v', ctx=Load()),
                                value=Name(id='k', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='k', ctx=Store()),
                                                Name(id='v', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Name(id='chain', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='options', ctx=Load()),
                                                            slice=Constant(value='nsmap', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='nsmap',
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
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
                            targets=[Name(id='code', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='key', ctx=Load()),
                                                attr='startswith',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='t-', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='attrib_qname', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='QName',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='key', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='attrib_qname', ctx=Load()),
                                                attr='namespace',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='key', ctx=Store())],
                                                    value=JoinedStr(
                                                        values=[
                                                            FormattedValue(
                                                                value=Subscript(
                                                                    value=Name(id='nsprefixmap', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='attrib_qname', ctx=Load()),
                                                                        attr='namespace',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value=':', kind=None),
                                                            FormattedValue(
                                                                value=Attribute(
                                                                    value=Name(id='attrib_qname', ctx=Load()),
                                                                    attr='localname',
                                                                    ctx=Load(),
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_indent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            JoinedStr(
                                                                values=[
                                                                    Constant(value='attrs[', kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='repr', ctx=Load()),
                                                                            args=[Name(id='key', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value='] = ', kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='repr', ctx=Load()),
                                                                            args=[Name(id='value', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                ],
                                                            ),
                                                            Name(id='indent', ctx=Load()),
                                                        ],
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
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_dynamic_attributes',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Compile the dynamic attributes of the given element into a list\n        string (this is adding elements to ``attrs`` in the compiled code).\n\n        We do not support namespaced dynamic attributes.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='name', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='name', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='t-attf-', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_indent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            JoinedStr(
                                                                values=[
                                                                    Constant(value='attrs[', kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='repr', ctx=Load()),
                                                                            args=[
                                                                                Subscript(
                                                                                    value=Name(id='name', ctx=Load()),
                                                                                    slice=Slice(
                                                                                        lower=Constant(value=7, kind=None),
                                                                                        upper=None,
                                                                                        step=None,
                                                                                    ),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value='] = ', kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='_compile_format',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='value', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                ],
                                                            ),
                                                            Name(id='indent', ctx=Load()),
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
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='name', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='t-att-', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='code', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_indent',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    JoinedStr(
                                                                        values=[
                                                                            Constant(value='attrs[', kind=None),
                                                                            FormattedValue(
                                                                                value=Call(
                                                                                    func=Name(id='repr', ctx=Load()),
                                                                                    args=[
                                                                                        Subscript(
                                                                                            value=Name(id='name', ctx=Load()),
                                                                                            slice=Slice(
                                                                                                lower=Constant(value=6, kind=None),
                                                                                                upper=None,
                                                                                                step=None,
                                                                                            ),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value='] = ', kind=None),
                                                                            FormattedValue(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='_compile_expr',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Name(id='value', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Name(id='indent', ctx=Load()),
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
                                                    test=Compare(
                                                        left=Name(id='name', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='t-att', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='code', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_indent',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='dedent', ctx=Load()),
                                                                                args=[
                                                                                    JoinedStr(
                                                                                        values=[
                                                                                            Constant(value='\n                    atts_value = ', kind=None),
                                                                                            FormattedValue(
                                                                                                value=Call(
                                                                                                    func=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='_compile_expr',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    args=[Name(id='value', ctx=Load())],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                                conversion=-1,
                                                                                                format_spec=None,
                                                                                            ),
                                                                                            Constant(value='\n                    if isinstance(atts_value, dict):\n                        attrs.update(atts_value)\n                    elif isinstance(atts_value, (list, tuple)) and not isinstance(atts_value[0], (list, tuple)):\n                        attrs.update([atts_value])\n                    elif isinstance(atts_value, (list, tuple)):\n                        attrs.update(dict(atts_value))\n                    ', kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            Name(id='indent', ctx=Load()),
                                                                        ],
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
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_all_attributes',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                            arg(arg='attr_already_created', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Compile the attributes (static and dynamic) of the given elements\n        into a list of str.\n        (this compiled The code will create the ``attrs`` in the compiled code).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=BoolOp(
                                            op=Or(),
                                            values=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='name', ctx=Load()),
                                                        attr='startswith',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='t-att', kind=None)],
                                                    keywords=[],
                                                ),
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Call(
                                                        func=Attribute(
                                                            value=Name(id='name', ctx=Load()),
                                                            attr='startswith',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='t-', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='name', ctx=Store()),
                                                        Name(id='value', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='attrib',
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
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
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='attr_already_created', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='attr_already_created', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_indent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='attrs = {}', kind=None),
                                                            Name(id='indent', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_static_attributes',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='el', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_dynamic_attributes',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='el', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='attr_already_created', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='tagName = ', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='el', ctx=Load()),
                                                                            attr='tag',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_attributes',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='options', ctx=Load()),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_tag_open',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                            arg(arg='attr_already_created', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Compile the opening tag of the given element into a list of string. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='extra_attrib', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='el', ctx=Load()),
                                    attr='nsmap',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='unqualified_el_tag', ctx=Store()),
                                        Name(id='el_tag', ctx=Store()),
                                    ],
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='tag',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='unqualified_el_tag', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='etree', ctx=Load()),
                                                attr='QName',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='el', ctx=Load()),
                                                    attr='tag',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='localname',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='el_tag', ctx=Store())],
                                    value=Name(id='unqualified_el_tag', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='prefix',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='el_tag', ctx=Store())],
                                            value=JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='prefix',
                                                            ctx=Load(),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=':', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='el_tag', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='ns_prefix', ctx=Store()),
                                            Name(id='ns_definition', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=BinOp(
                                        left=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='nsmap',
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='options', ctx=Load()),
                                                            slice=Constant(value='nsmap', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='ns_prefix', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='extra_attrib', ctx=Load()),
                                                            slice=Constant(value='xmlns', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='ns_definition', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='extra_attrib', ctx=Load()),
                                                            slice=JoinedStr(
                                                                values=[
                                                                    Constant(value='xmlns:', kind=None),
                                                                    FormattedValue(
                                                                        value=Name(id='ns_prefix', ctx=Load()),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                ],
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='ns_definition', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='unqualified_el_tag', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='t', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='attributes', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=JoinedStr(
                                                    values=[
                                                        Constant(value=' ', kind=None),
                                                        FormattedValue(
                                                            value=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='name', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                        Constant(value='="', kind=None),
                                                        FormattedValue(
                                                            value=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='escape', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='_compile_to_str',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='value', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            conversion=-1,
                                                            format_spec=None,
                                                        ),
                                                        Constant(value='"', kind=None),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='name', ctx=Store()),
                                                                Name(id='value', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='extra_attrib', ctx=Load()),
                                                                attr='items',
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
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_appendText',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='<{}{}', kind=None),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='el_tag', ctx=Load()),
                                                    Name(id='attributes', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_all_attributes',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='el', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                    Name(id='indent', ctx=Load()),
                                                    Name(id='attr_already_created', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='unqualified_el_tag', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_void_elements',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_appendText',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='/>', kind=None),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_appendText',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='>', kind=None),
                                                    Name(id='options', ctx=Load()),
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
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_tag_close',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Compile the closing tag of the given element into a list of string. ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='el', ctx=Load()),
                                    attr='nsmap',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='unqualified_el_tag', ctx=Store()),
                                        Name(id='el_tag', ctx=Store()),
                                    ],
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='tag',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='unqualified_el_tag', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='etree', ctx=Load()),
                                                attr='QName',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='el', ctx=Load()),
                                                    attr='tag',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='localname',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='el_tag', ctx=Store())],
                                    value=Name(id='unqualified_el_tag', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='prefix',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='el_tag', ctx=Store())],
                                            value=JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='prefix',
                                                            ctx=Load(),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=':', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='el_tag', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='unqualified_el_tag', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='t', kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='el_tag', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_void_elements',
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='_appendText',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='</', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='el_tag', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='>', kind=None),
                                                ],
                                            ),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='directive', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='compile_handler', ctx=Store())],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    JoinedStr(
                                        values=[
                                            Constant(value='_compile_directive_', kind=None),
                                            FormattedValue(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='directive', ctx=Load()),
                                                        attr='replace',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='-', kind=None),
                                                        Constant(value='_', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='compile_handler', ctx=Load()),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
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
                    name='_compile_directive_debug',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Compile `t-debug` expressions into a python code as a list of\n        strings.\n\n        The code will contains the call to the debugger chosen from the valid\n        list.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='debugger', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='t-debug', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='dev_mode', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='self._debug_trace(', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[Name(id='debugger', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value=', compile_options)', kind=None),
                                                        ],
                                                    ),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='warning',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='@t-debug in template is only available in qweb dev mode options', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_directives',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive_options',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        compile t-options and add to the dict the t-options-xxx values\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='varname', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='t_options_varname', kind=None),
                                    Constant(value='t_options', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dict_arg', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='key', ctx=Store()),
                            iter=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='key', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='t-options-', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='key', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='option_name', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='key', ctx=Load()),
                                                slice=Slice(
                                                    lower=Constant(value=10, kind=None),
                                                    upper=None,
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='dict_arg', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[Name(id='option_name', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value=':', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_compile_expr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='value', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
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
                            targets=[Name(id='t_options', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='t-options', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='t_options', ctx=Load()),
                                    Name(id='dict_arg', ctx=Load()),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            FormattedValue(
                                                                value=Name(id='varname', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value=' = {**', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_compile_expr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='t_options', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value=', ', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Constant(value=', ', kind=None),
                                                                        attr='join',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='dict_arg', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='}', kind=None),
                                                        ],
                                                    ),
                                                    Name(id='indent', ctx=Load()),
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
                                    test=Name(id='dict_arg', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_indent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            JoinedStr(
                                                                values=[
                                                                    FormattedValue(
                                                                        value=Name(id='varname', ctx=Load()),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value=' = {', kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Constant(value=', ', kind=None),
                                                                                attr='join',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='dict_arg', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value='}', kind=None),
                                                                ],
                                                            ),
                                                            Name(id='indent', ctx=Load()),
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
                                            test=Name(id='t_options', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='code', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_indent',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    JoinedStr(
                                                                        values=[
                                                                            FormattedValue(
                                                                                value=Name(id='varname', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' = ', kind=None),
                                                                            FormattedValue(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='_compile_expr',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Name(id='t_options', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Name(id='indent', ctx=Load()),
                                                                ],
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
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive_tag',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Compile the element tag into a python code as a list of strings.\n\n        The code will contains the opening tag, namespace, static and dynamic\n        attributes and closing tag.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='t-tag', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile_tag_open',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='el', ctx=Load()),
                                attr='nsmap',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_directives',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='el', ctx=Load()),
                                                    Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[Name(id='options', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='nsmap',
                                                                value=Attribute(
                                                                    value=Name(id='el', ctx=Load()),
                                                                    attr='nsmap',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_directives',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='el', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_tag_close',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive_set',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Compile `t-set` expressions into a python code as a list of\n        strings.\n\n        There are 3 kinds of `t-set`:\n        * `t-value` containing python code;\n        * `t-valuef` containing strings to format;\n        * whose value is the content of the tag (being Markup safe).\n\n        The code will contain the assignment of the dynamically generated value.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='varname', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='t-set', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_flushText',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='t-value', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='varname', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='0', kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[Constant(value='t-set="0" should not contains t-value or t-valuef', kind=None)],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='expr', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='t-value', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='None', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='expr', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_expr',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='expr', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Constant(value='t-valuef', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Name(id='varname', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='0', kind=None)],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValueError', ctx=Load()),
                                                        args=[Constant(value='t-set="0" should not contains t-value or t-valuef', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='exprf', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='t-valuef', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='expr', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_format',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='exprf', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='def_name', ctx=Store())],
                                            value=JoinedStr(
                                                values=[
                                                    Constant(value='qweb_t_set_', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='re', ctx=Load()),
                                                                attr='sub',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='_VARNAME_REGEX', ctx=Load()),
                                                                Constant(value='_', kind=None),
                                                                Subscript(
                                                                    value=Name(id='options', ctx=Load()),
                                                                    slice=Constant(value='last_path_node', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_compile_directive_content',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='el', ctx=Load()),
                                                        Name(id='options', ctx=Load()),
                                                        BinOp(
                                                            left=Name(id='indent', ctx=Load()),
                                                            op=Add(),
                                                            right=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_flushText',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='options', ctx=Load()),
                                                        BinOp(
                                                            left=Name(id='indent', ctx=Load()),
                                                            op=Add(),
                                                            right=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='content', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='code', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_indent',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    JoinedStr(
                                                                        values=[
                                                                            Constant(value='def ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='def_name', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value='():', kind=None),
                                                                        ],
                                                                    ),
                                                                    Name(id='indent', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='code', ctx=Load()),
                                                            attr='extend',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='content', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='expr', ctx=Store())],
                                                    value=JoinedStr(
                                                        values=[
                                                            Constant(value="Markup(''.join(", kind=None),
                                                            FormattedValue(
                                                                value=Name(id='def_name', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='()))', kind=None),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='expr', ctx=Store())],
                                                    value=Constant(value="''", kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='values[', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[Name(id='varname', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='] = ', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='expr', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive_content',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Compiles the content of the element (is the technical `t-content`\n        directive created by QWeb) into a python code as a list of\n        strings.\n\n        The code will contains the text content of the node or the compliled\n        code from the recursive call of ``_compile_node``.\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='el', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_appendText',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='text',
                                                ctx=Load(),
                                            ),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='el', ctx=Load()),
                                    attr='getchildren',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='item', ctx=Store()),
                                    iter=Name(id='el', ctx=Load()),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='isinstance', ctx=Load()),
                                                    args=[
                                                        Name(id='item', ctx=Load()),
                                                        Attribute(
                                                            value=Name(id='etree', ctx=Load()),
                                                            attr='_Comment',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='body', ctx=Load()),
                                                            attr='extend',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_compile_node',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='item', ctx=Load()),
                                                                    Name(id='options', ctx=Load()),
                                                                    Name(id='indent', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='item', ctx=Load()),
                                                    attr='tail',
                                                    ctx=Load(),
                                                ),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_appendText',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='item', ctx=Load()),
                                                                attr='tail',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='options', ctx=Load()),
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
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='body', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive_else',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Compile `t-else` expressions into a python code as a list of strings.\n\n        This method is linked with the `t-if` directive.\n        The code will contain the compiled code of the element (without `else`\n        python part).\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='attrib',
                                            ctx=Load(),
                                        ),
                                        attr='pop',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='t-else', kind=None)],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='_t_skip_else_', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='options', ctx=Load()),
                                        attr='pop',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='t_if', kind=None),
                                        Constant(value=None, kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[Constant(value='t-else directive must be preceded by t-if directive', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='compiled', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile_directives',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='t-else', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='_t_skip_else_', kind=None),
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
                    name='_compile_directive_elif',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Compile `t-eif` expressions into a python code as a list of strings.\n\n        This method is linked with the `t-if` directive.\n        The code will contain the compiled code of the element (without `else`\n        python part).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='_elif', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='el', ctx=Load()),
                                    attr='attrib',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='t-elif', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='_elif', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='_t_skip_else_', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='t-elif', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='options', ctx=Load()),
                                        attr='pop',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='t_if', kind=None),
                                        Constant(value=None, kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[Constant(value='t-elif directive must be preceded by t-if directive', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='compiled', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile_directive_if',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='t-elif', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='_t_skip_else_', kind=None),
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
                    name='_compile_directive_if',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Compile `t-if` expressions into a python code as a list of strings.\n\n        The code will contain the condition `if`, `else` and `elif` part that\n        wrap the rest of the compiled code of this element.\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='t-elif', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='expr', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='t-elif', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='expr', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='t-if', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_flushText',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content_if', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_compile_directives',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='el', ctx=Load()),
                                        Name(id='options', ctx=Load()),
                                        BinOp(
                                            left=Name(id='indent', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_flushText',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='options', ctx=Load()),
                                        BinOp(
                                            left=Name(id='indent', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='orelse', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='next_el', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='el', ctx=Load()),
                                    attr='getnext',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='comments_to_remove', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        While(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='next_el', ctx=Load()),
                                    Attribute(
                                        value=Name(id='etree', ctx=Load()),
                                        attr='_Comment',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='comments_to_remove', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='next_el', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='next_el', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='next_el', ctx=Load()),
                                            attr='getnext',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                                    Compare(
                                        left=Name(id='next_el', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    BinOp(
                                        left=Set(
                                            elts=[
                                                Constant(value='t-else', kind=None),
                                                Constant(value='t-elif', kind=None),
                                            ],
                                        ),
                                        op=BitAnd(),
                                        right=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='next_el', ctx=Load()),
                                                    attr='attrib',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='parent', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='getparent',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='comment', ctx=Store()),
                                    iter=Name(id='comments_to_remove', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='parent', ctx=Load()),
                                                    attr='remove',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='comment', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='tail',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='tail',
                                                            ctx=Load(),
                                                        ),
                                                        attr='isspace',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[Constant(value='Unexpected non-whitespace characters between t-if and t-else directives', kind=None)],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='tail',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='orelse', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_compile_node',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='next_el', ctx=Load()),
                                                Call(
                                                    func=Name(id='dict', ctx=Load()),
                                                    args=[Name(id='options', ctx=Load())],
                                                    keywords=[
                                                        keyword(
                                                            arg='t_if',
                                                            value=Constant(value=True, kind=None),
                                                        ),
                                                    ],
                                                ),
                                                BinOp(
                                                    left=Name(id='indent', ctx=Load()),
                                                    op=Add(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_flushText',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='options', ctx=Load()),
                                                BinOp(
                                                    left=Name(id='indent', ctx=Load()),
                                                    op=Add(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='if ', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_compile_expr',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='expr', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=':', kind=None),
                                                ],
                                            ),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='content_if', ctx=Load()),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_indent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='pass', kind=None),
                                                            BinOp(
                                                                left=Name(id='indent', ctx=Load()),
                                                                op=Add(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='orelse', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='else:', kind=None),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='orelse', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive_foreach',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Compile `t-foreach` expressions into a python code as a list of\n        strings.\n\n        `t-as` is used to define the key name.\n        `t-foreach` compiled value can be an iterable, an dictionary or a\n        number.\n\n        The code will contain loop `for` that wrap the rest of the compiled\n        code of this element.\n        Some key into values dictionary are create automatically:\n            *_size, *_index, *_value, *_first, *_last, *_odd, *_even, *_parity\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='expr_foreach', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='t-foreach', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expr_as', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='t-as', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_flushText',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content_foreach', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_compile_directives',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='el', ctx=Load()),
                                        Name(id='options', ctx=Load()),
                                        BinOp(
                                            left=Name(id='indent', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_flushText',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='options', ctx=Load()),
                                        BinOp(
                                            left=Name(id='indent', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='t_foreach', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_name',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='t_foreach', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='size', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_name',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='size', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='has_value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_make_name',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='has_value', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='expr_foreach', ctx=Load()),
                                    attr='isdigit',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='dedent', ctx=Load()),
                                                                args=[
                                                                    JoinedStr(
                                                                        values=[
                                                                            Constant(value='\n                values[', kind=None),
                                                                            FormattedValue(
                                                                                value=Call(
                                                                                    func=Name(id='repr', ctx=Load()),
                                                                                    args=[
                                                                                        BinOp(
                                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                                            op=Add(),
                                                                                            right=Constant(value='_size', kind=None),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value='] = ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='size', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' = ', kind=None),
                                                                            FormattedValue(
                                                                                value=Call(
                                                                                    func=Name(id='int', ctx=Load()),
                                                                                    args=[Name(id='expr_foreach', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value='\n                ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='t_foreach', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' = range(', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='size', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=')\n                ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='has_value', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' = False\n            ', kind=None),
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
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='dedent', ctx=Load()),
                                                                args=[
                                                                    JoinedStr(
                                                                        values=[
                                                                            Constant(value='\n                ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='t_foreach', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' = ', kind=None),
                                                                            FormattedValue(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='_compile_expr',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Name(id='expr_foreach', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' or []\n                if isinstance(', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='t_foreach', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=', Sized):\n                    values[', kind=None),
                                                                            FormattedValue(
                                                                                value=Call(
                                                                                    func=Name(id='repr', ctx=Load()),
                                                                                    args=[
                                                                                        BinOp(
                                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                                            op=Add(),
                                                                                            right=Constant(value='_size', kind=None),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value='] = ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='size', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' = len(', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='t_foreach', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=')\n                elif type(', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='t_foreach', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=') == int:\n                    values[', kind=None),
                                                                            FormattedValue(
                                                                                value=Call(
                                                                                    func=Name(id='repr', ctx=Load()),
                                                                                    args=[
                                                                                        BinOp(
                                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                                            op=Add(),
                                                                                            right=Constant(value='_size', kind=None),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value='] = ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='size', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' = ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='t_foreach', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value='\n                    ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='t_foreach', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' = range(', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='size', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=')\n                else:\n                    ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='size', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' = None\n                ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='has_value', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' = False\n                if isinstance(', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='t_foreach', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=', Mapping):\n                    ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='t_foreach', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' = ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='t_foreach', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value='.items()\n                    ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='has_value', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=' = True\n            ', kind=None),
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
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='dedent', ctx=Load()),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='\n                for index, item in enumerate(', kind=None),
                                                            FormattedValue(
                                                                value=Name(id='t_foreach', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='):\n                    values[', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='_index', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='] = index\n                    if ', kind=None),
                                                            FormattedValue(
                                                                value=Name(id='has_value', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value=':\n                        values[', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[Name(id='expr_as', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='], values[', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='_value', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='] = item\n                    else:\n                        values[', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[Name(id='expr_as', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='] = values[', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='_value', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='] = item\n                    values[', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='_first', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='] = values[', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='_index', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='] == 0\n                    if ', kind=None),
                                                            FormattedValue(
                                                                value=Name(id='size', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value=' is not None:\n                        values[', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='_last', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='] = index + 1 == ', kind=None),
                                                            FormattedValue(
                                                                value=Name(id='size', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='\n                    values[', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='_odd', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='] = index % 2\n                    values[', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='_even', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='] = not values[', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='_odd', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value=']\n                    values[', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='_parity', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value="] = 'odd' if values[", kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='expr_as', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='_odd', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value="] else 'even'\n            ", kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='log["last_path_node"] = ', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Subscript(
                                                                            value=Name(id='options', ctx=Load()),
                                                                            slice=Constant(value='root', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='getpath',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='el', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=' ', kind=None),
                                                ],
                                            ),
                                            BinOp(
                                                left=Name(id='indent', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='content_foreach', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='continue', kind=None),
                                                    BinOp(
                                                        left=Name(id='indent', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive_out',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Compile `t-out` expressions into a python code as a list of\n        strings.\n\n        The output can have some rendering option with `t-options-widget` or\n        `t-options={'widget': ...}. The compiled code will call ``_get_widget``\n        method at rendering time.\n\n        The code will contain evalution and rendering of the compiled value. If\n        the compiled value is None or False, the tag is not added to the render\n        (Except if the widget forces rendering or there is default content.).\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ttype', ctx=Store())],
                            value=Constant(value='t-out', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='t-out', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='expr', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ttype', ctx=Store())],
                                    value=Constant(value='t-esc', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='expr', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='t-esc', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='expr', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='ttype', ctx=Store())],
                                            value=Constant(value='t-raw', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='expr', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='t-raw', kind=None)],
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
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_flushText',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='t_options_varname', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='t_out_t_options', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code_options', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile_directive',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    Constant(value='options', kind=None),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[Name(id='code_options', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='expr', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='0', kind=None)],
                            ),
                            body=[
                                If(
                                    test=Name(id='code_options', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_indent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value="content = Markup(''.join(values.get('0', [])))", kind=None),
                                                            Name(id='indent', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_compile_tag_open',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='el', ctx=Load()),
                                                            Name(id='options', ctx=Load()),
                                                            Name(id='indent', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_flushText',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='options', ctx=Load()),
                                                            Name(id='indent', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_indent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value="yield from values.get('0', [])", kind=None),
                                                            Name(id='indent', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_compile_tag_close',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='el', ctx=Load()),
                                                            Name(id='options', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Name(id='code', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='content = ', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='_compile_expr',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='expr', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='code_options', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='attrs, content, force_display = self._get_widget(content, ', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[Name(id='expr', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value=', ', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Name(id='repr', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='el', ctx=Load()),
                                                                            attr='tag',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value=', t_out_t_options, compile_options, values)', kind=None),
                                                        ],
                                                    ),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='force_display = None', kind=None),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='ttype', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='t-raw', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_indent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='dedent', ctx=Load()),
                                                                args=[Constant(value='\n                    if content is not None and content is not False:\n                        content = Markup(content)\n                ', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Name(id='indent', ctx=Load()),
                                                        ],
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_widget_value',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='without_attributes',
                                                value=UnaryOp(
                                                    op=Not(),
                                                    operand=Name(id='code_options', ctx=Load()),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive_esc',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='dev_mode', kind=None)],
                                keywords=[],
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
                                            Constant(value='Found deprecated directive @t-esc=%r in template %r. Replace by @t-out', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='el', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='t-esc', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='ref', kind=None),
                                                    Constant(value='<unknown>', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile_directive_out',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
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
                    name='_compile_directive_raw',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
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
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Found deprecated directive @t-raw=%r in template %r. Replace by @t-out, and explicitely wrap content in `Markup` if necessary (which likely is not the case)', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='t-raw', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='ref', kind=None),
                                            Constant(value='<unknown>', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile_directive_out',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
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
                    name='_compile_directive_field',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Compile `t-field` expressions into a python code as a list of\n        strings.\n\n        The compiled code will call ``_get_field`` method at rendering time\n        using the type of value supplied by the field. This behavior can be\n        changed with `t-options-widget` or `t-options={'widget': ...}.\n\n        The code will contain evalution and rendering of the compiled value\n        value from the record field. If the compiled value is None or False,\n        the tag is not added to the render\n        (Except if the widget forces rendering or there is default content.).\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tagName', ctx=Store())],
                            value=Attribute(
                                value=Name(id='el', ctx=Load()),
                                attr='tag',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Name(id='tagName', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='table', kind=None),
                                            Constant(value='tbody', kind=None),
                                            Constant(value='thead', kind=None),
                                            Constant(value='tfoot', kind=None),
                                            Constant(value='tr', kind=None),
                                            Constant(value='td', kind=None),
                                            Constant(value='li', kind=None),
                                            Constant(value='ul', kind=None),
                                            Constant(value='ol', kind=None),
                                            Constant(value='dl', kind=None),
                                            Constant(value='dt', kind=None),
                                            Constant(value='dd', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=BinOp(
                                left=Constant(value='RTE widgets do not work correctly on %r elements', kind=None),
                                op=Mod(),
                                right=Name(id='tagName', ctx=Load()),
                            ),
                        ),
                        Assert(
                            test=Compare(
                                left=Name(id='tagName', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Constant(value='t', kind=None)],
                            ),
                            msg=Constant(value='t-field can not be used on a t element, provide an actual HTML node', kind=None),
                        ),
                        Assert(
                            test=Compare(
                                left=Constant(value='.', kind=None),
                                ops=[In()],
                                comparators=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='el', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='t-field', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            msg=Constant(value="t-field must have at least a dot like 'record.field_name'", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='expression', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='t-field', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='record', ctx=Store()),
                                        Name(id='field_name', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
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
                            targets=[Name(id='code', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='t_options_varname', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='t_field_t_options', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code_options', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_directive',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                            Constant(value='options', kind=None),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='t_field_t_options = {}', kind=None),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[Name(id='code_options', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='attrs, content, force_display = self._get_field(', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_compile_expr',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='record', ctx=Load())],
                                                            keywords=[
                                                                keyword(
                                                                    arg='raise_on_missing',
                                                                    value=Constant(value=True, kind=None),
                                                                ),
                                                            ],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=', ', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[Name(id='field_name', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=', ', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[Name(id='expression', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=', ', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[Name(id='tagName', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=', t_field_t_options, compile_options, values)', kind=None),
                                                ],
                                            ),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='content = self._compile_to_str(content)', kind=None),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_widget_value',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_widget_value',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                            arg(arg='without_attributes', annotation=None, type_comment=None),
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
                        Expr(
                            value=Constant(value='Take care of part of the compilation of `t-out` and `t-field` (and\n        the technical directive `t-tag). This is the part that takes care of\n        whether or not created the tags and the default content of the element.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='t-tag', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_flushText',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='if content is not None and content is not False:', kind=None),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_tag_open',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                            BinOp(
                                                left=Name(id='indent', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='without_attributes', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_flushText',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='options', ctx=Load()),
                                            BinOp(
                                                left=Name(id='indent', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='yield str(escape(content))', kind=None),
                                            BinOp(
                                                left=Name(id='indent', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_tag_close',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_flushText',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='options', ctx=Load()),
                                            BinOp(
                                                left=Name(id='indent', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='default_body', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile_directive_content',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    BinOp(
                                        left=Name(id='indent', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='default_body', ctx=Load()),
                                    Subscript(
                                        value=Name(id='options', ctx=Load()),
                                        slice=Constant(value='_text_concat', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='_text_concat', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='_text_concat', kind=None),
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
                                            value=Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='_text_concat', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='clear',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='else:', kind=None),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_tag_open',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='el', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='indent', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='without_attributes', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='default_body', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='_text_concat', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='_text_concat', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_tag_close',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='el', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_flushText',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='options', ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='indent', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=1, kind=None),
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
                                Assign(
                                    targets=[Name(id='content', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_tag_open',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='el', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='indent', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='without_attributes', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            op=Add(),
                                            right=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compile_tag_close',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='el', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_flushText',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='options', ctx=Load()),
                                                BinOp(
                                                    left=Name(id='indent', ctx=Load()),
                                                    op=Add(),
                                                    right=Constant(value=2, kind=None),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='content', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_indent',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='elif force_display:', kind=None),
                                                            Name(id='indent', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='content', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compile_directive_call',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='el', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='indent', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Compile `t-call` expressions into a python code as a list of\n        strings.\n\n        `t-call` allow formating string dynamic at rendering time.\n        Can use `t-options` used to call and render the sub-template at\n        rendering time.\n        The sub-template is called with a copy of the rendering values\n        dictionary. The dictionary contains the key 0 coming from the\n        compilation of the contents of this element\n\n        The code will contain the call of the template and a function from the\n        compilation of the content of this element.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='expr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='t-call', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='el', ctx=Load()),
                                        attr='attrib',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='t-call-options', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='el', ctx=Load()),
                                                attr='attrib',
                                                ctx=Load(),
                                            ),
                                            attr='set',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='t-options', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='el', ctx=Load()),
                                                        attr='attrib',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='t-call-options', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='nsmap', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='nsmap', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_flushText',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='options', ctx=Load()),
                                    Name(id='indent', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='t_options_varname', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='t_call_t_options', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='code_options', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_compile_directive',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                            Constant(value='options', kind=None),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='t_call_t_options = {}', kind=None),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[Name(id='code_options', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='def_name', ctx=Store())],
                            value=Constant(value='t_call_content', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile_directive_content',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='el', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    BinOp(
                                        left=Name(id='indent', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='content', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='_text_concat', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_appendText',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='', kind=None),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='content', ctx=Load()),
                                    attr='extend',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_flushText',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='options', ctx=Load()),
                                            BinOp(
                                                left=Name(id='indent', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='content', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='def ', kind=None),
                                                            FormattedValue(
                                                                value=Name(id='def_name', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='(self, values, log):', kind=None),
                                                        ],
                                                    ),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='content', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='t_call_values = values.copy()', kind=None),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value="t_call_values['0'] = Markup(''.join(", kind=None),
                                                            FormattedValue(
                                                                value=Name(id='def_name', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='(self, t_call_values, log)))', kind=None),
                                                        ],
                                                    ),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='t_call_values = values.copy()', kind=None),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value="t_call_values['0'] = Markup()", kind=None),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='code', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='dedent', ctx=Load()),
                                                        args=[
                                                            JoinedStr(
                                                                values=[
                                                                    Constant(value="\n            t_call_options = compile_options.copy()\n            t_call_options.update({'caller_template': ", kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='repr', ctx=Load()),
                                                                            args=[
                                                                                Call(
                                                                                    func=Name(id='str', ctx=Load()),
                                                                                    args=[
                                                                                        Call(
                                                                                            func=Attribute(
                                                                                                value=Name(id='options', ctx=Load()),
                                                                                                attr='get',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Constant(value='template', kind=None)],
                                                                                            keywords=[],
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value=", 'last_path_node': ", kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='repr', ctx=Load()),
                                                                            args=[
                                                                                Call(
                                                                                    func=Name(id='str', ctx=Load()),
                                                                                    args=[
                                                                                        Call(
                                                                                            func=Attribute(
                                                                                                value=Subscript(
                                                                                                    value=Name(id='options', ctx=Load()),
                                                                                                    slice=Constant(value='root', kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='getpath',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            args=[Name(id='el', ctx=Load())],
                                                                                            keywords=[],
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value=' })\n            ', kind=None),
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
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='nsmap', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='nsmap', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='key', ctx=Store()),
                                            Name(id='value', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='nsmap', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='key', ctx=Load()),
                                                    Name(id='str', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='nsmap', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            JoinedStr(
                                                                values=[
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='repr', ctx=Load()),
                                                                            args=[Name(id='key', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value=':', kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='repr', ctx=Load()),
                                                                            args=[Name(id='value', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='nsmap', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            JoinedStr(
                                                                values=[
                                                                    Constant(value='None:', kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='repr', ctx=Load()),
                                                                            args=[Name(id='value', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
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
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='t_call_options.update(nsmap={', kind=None),
                                                            FormattedValue(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Constant(value=', ', kind=None),
                                                                        attr='join',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='nsmap', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='})', kind=None),
                                                        ],
                                                    ),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='template', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compile_format',
                                    ctx=Load(),
                                ),
                                args=[Name(id='expr', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='code_options', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='t_call_options.update(t_call_t_options)', kind=None),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='dedent', ctx=Load()),
                                                                args=[
                                                                    JoinedStr(
                                                                        values=[
                                                                            Constant(value="\n                if compile_options.get('lang') != t_call_options.get('lang'):\n                    self_lang = self.with_context(lang=t_call_options.get('lang'))\n                    yield from self_lang._compile(", kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='template', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=', t_call_options)(self_lang, t_call_values)\n                else:\n                    yield from self._compile(', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='template', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value=', t_call_options)(self, t_call_values)\n                ', kind=None),
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
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='code', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_indent',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='yield from self._compile(', kind=None),
                                                            FormattedValue(
                                                                value=Name(id='template', ctx=Load()),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value=', t_call_options)(self, t_call_values)', kind=None),
                                                        ],
                                                    ),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='code', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_post_processing_att',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tagName', annotation=None, type_comment=None),
                            arg(arg='atts', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Method called at compile time for the static node and called at\n            runing time for the dynamic attributes.\n\n            This method may be overwrited to filter or modify the attributes\n            (during compilation for static node or after they compilation in\n            the case of dynamic elements).\n\n            @returns dict\n        ', kind=None),
                        ),
                        Return(
                            value=Name(id='atts', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_field',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='expression', annotation=None, type_comment=None),
                            arg(arg='tagName', annotation=None, type_comment=None),
                            arg(arg='field_options', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Method called at compile time to return the field value.\n\n        :returns: tuple:\n            * dict: attributes\n            * string or None: content\n            * boolean: force_display display the tag if the content and default_content are None\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_widget',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Name(id='field_name', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='expression', ctx=Load()),
                                    Name(id='tagName', ctx=Load()),
                                    Name(id='field_options', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                    Name(id='values', ctx=Load()),
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
                    name='_get_widget',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='expression', annotation=None, type_comment=None),
                            arg(arg='tagName', annotation=None, type_comment=None),
                            arg(arg='field_options', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Method called at compile time to return the widget value.\n\n        :returns: tuple:\n            * dict: attributes\n            * string or None: content\n            * boolean: force_display display the tag if the content and default_content are None\n        ', kind=None),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Dict(keys=[], values=[]),
                                    Name(id='value', ctx=Load()),
                                    Constant(value=False, kind=None),
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
                    name='_debug_trace',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='debugger', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Method called at compile time to load debugger.', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='debugger', ctx=Load()),
                                ops=[In()],
                                comparators=[Name(id='SUPPORTED_DEBUGGERS', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='__import__', ctx=Load()),
                                                args=[Name(id='debugger', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='set_trace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='QWebException', ctx=Load()),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='unsupported t-debug value: ', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='debugger', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                            Name(id='self', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
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
    ],
    type_ignores=[],
)
