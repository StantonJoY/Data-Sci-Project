Module(
    body=[
        Import(
            names=[alias(name='functools', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='Controller', asname=None),
                alias(name='route', asname=None),
                alias(name='request', asname=None),
                alias(name='Response', asname=None),
            ],
            level=0,
        ),
        FunctionDef(
            name='webservice',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='f', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                FunctionDef(
                    name='wrap',
                    args=arguments(
                        posonlyargs=[],
                        args=[],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='f', ctx=Load()),
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
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name='e',
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='Response', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='response',
                                                        value=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='e', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='status',
                                                        value=Constant(value=500, kind=None),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='functools', ctx=Load()),
                                attr='wraps',
                                ctx=Load(),
                            ),
                            args=[Name(id='f', ctx=Load())],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Name(id='wrap', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='ImportModule',
            bases=[Name(id='Controller', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='check_user',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='uid', annotation=None, type_comment=None),
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
                                left=Name(id='uid', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='uid', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='is_admin', ctx=Store())],
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='uid', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='_is_admin',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='is_admin', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AccessError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Only administrators can upload a module', kind=None)],
                                                keywords=[],
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
                    name='login_upload',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                            arg(arg='db', annotation=None, type_comment=None),
                            arg(arg='force', annotation=None, type_comment=None),
                            arg(arg='mod_file', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='', kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='db', ctx=Load()),
                                    Compare(
                                        left=Name(id='db', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='db',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value="Could not select database '%s'", kind=None),
                                                    Name(id='db', ctx=Load()),
                                                ],
                                                keywords=[],
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
                            targets=[Name(id='uid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='authenticate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                    Name(id='login', ctx=Load()),
                                    Name(id='password', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_user',
                                    ctx=Load(),
                                ),
                                args=[Name(id='uid', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='force', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='force', ctx=Load()),
                                    ops=[Eq()],
                                    comparators=[Constant(value='1', kind=None)],
                                ),
                                body=Constant(value=True, kind=None),
                                orelse=Constant(value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
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
                                        attr='import_zipfile',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='mod_file', ctx=Load())],
                                    keywords=[
                                        keyword(
                                            arg='force',
                                            value=Name(id='force', ctx=Load()),
                                        ),
                                    ],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[Constant(value='/base_import_module/login_upload', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='csrf',
                                    value=Constant(value=False, kind=None),
                                ),
                                keyword(
                                    arg='save_session',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                        Name(id='webservice', ctx=Load()),
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
