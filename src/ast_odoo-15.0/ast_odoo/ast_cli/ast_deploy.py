Module(
    body=[
        ImportFrom(
            module='__future__',
            names=[alias(name='print_function', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='argparse', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='tempfile', asname=None)],
        ),
        Import(
            names=[alias(name='zipfile', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[alias(name='Command', asname=None)],
            level=1,
        ),
        ClassDef(
            name='Deploy',
            bases=[Name(id='Command', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Deploy a module on an Odoo instance', kind=None),
                ),
                FunctionDef(
                    name='__init__',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Deploy', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='session',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='requests', ctx=Load()),
                                    attr='session',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='deploy_module',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='module_path', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                            arg(arg='db', annotation=None, type_comment=None),
                            arg(arg='force', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='', kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='url', ctx=Load()),
                                    attr='rstrip',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='module_file', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='zip_module',
                                    ctx=Load(),
                                ),
                                args=[Name(id='module_path', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='login_upload_module',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='module_file', ctx=Load()),
                                            Name(id='url', ctx=Load()),
                                            Name(id='login', ctx=Load()),
                                            Name(id='password', ctx=Load()),
                                            Name(id='db', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='force',
                                                value=Name(id='force', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='remove',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='module_file', ctx=Load())],
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
                    name='login_upload_module',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='module_file', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='login', annotation=None, type_comment=None),
                            arg(arg='password', annotation=None, type_comment=None),
                            arg(arg='db', annotation=None, type_comment=None),
                            arg(arg='force', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='print', ctx=Load()),
                                args=[Constant(value='Uploading module file...', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='endpoint', ctx=Store())],
                            value=BinOp(
                                left=Name(id='url', ctx=Load()),
                                op=Add(),
                                right=Constant(value='/base_import_module/login_upload', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='post_data', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='login', kind=None),
                                    Constant(value='password', kind=None),
                                    Constant(value='db', kind=None),
                                    Constant(value='force', kind=None),
                                ],
                                values=[
                                    Name(id='login', ctx=Load()),
                                    Name(id='password', ctx=Load()),
                                    Name(id='db', ctx=Load()),
                                    IfExp(
                                        test=Name(id='force', ctx=Load()),
                                        body=Constant(value='1', kind=None),
                                        orelse=Constant(value='', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='open', ctx=Load()),
                                        args=[
                                            Name(id='module_file', ctx=Load()),
                                            Constant(value='rb', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='f', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            attr='post',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='endpoint', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='files',
                                                value=Dict(
                                                    keys=[Constant(value='mod_file', kind=None)],
                                                    values=[Name(id='f', ctx=Load())],
                                                ),
                                            ),
                                            keyword(
                                                arg='data',
                                                value=Name(id='post_data', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='status_code',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=404, kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value="The server '%s' does not have the 'base_import_module' installed or is not up-to-date.", kind=None),
                                                op=Mod(),
                                                right=Name(id='url', ctx=Load()),
                                            ),
                                        ],
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
                                    value=Name(id='res', ctx=Load()),
                                    attr='raise_for_status',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='res', ctx=Load()),
                                attr='text',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='zip_module',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    attr='abspath',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        attr='isdir',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='path', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value="Could not find module directory '%s'", kind=None),
                                                op=Mod(),
                                                right=Name(id='path', ctx=Load()),
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
                                        Name(id='container', ctx=Store()),
                                        Name(id='module_name', ctx=Store()),
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
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='temp', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tempfile', ctx=Load()),
                                    attr='mktemp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='suffix',
                                        value=Constant(value='.zip', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='print', ctx=Load()),
                                        args=[Constant(value='Zipping module directory...', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='zipfile', ctx=Load()),
                                                    attr='ZipFile',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='temp', ctx=Load()),
                                                    Constant(value='w', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='zfile', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='root', ctx=Store()),
                                                    Name(id='dirs', ctx=Store()),
                                                    Name(id='files', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='walk',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='path', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=[
                                                For(
                                                    target=Name(id='file', ctx=Store()),
                                                    iter=Name(id='files', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='file_path', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='os', ctx=Load()),
                                                                        attr='path',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='root', ctx=Load()),
                                                                    Name(id='file', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='zfile', ctx=Load()),
                                                                    attr='write',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='file_path', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='file_path', ctx=Load()),
                                                                                    attr='split',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='container', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            attr='pop',
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
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Name(id='temp', ctx=Load()),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='os', ctx=Load()),
                                                    attr='remove',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='temp', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(exc=None, cause=None),
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
                    name='run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cmdargs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='parser', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='argparse', ctx=Load()),
                                    attr='ArgumentParser',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='prog',
                                        value=BinOp(
                                            left=Constant(value='%s deploy', kind=None),
                                            op=Mod(),
                                            right=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='sys', ctx=Load()),
                                                                attr='argv',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='sep',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='description',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='__doc__',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='path', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Path of the module to deploy', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='url', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='nargs',
                                        value=Constant(value='?', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Url of the server (default=http://localhost:8069)', kind=None),
                                    ),
                                    keyword(
                                        arg='default',
                                        value=Constant(value='http://localhost:8069', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--db', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='db', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Database to use if server does not use db-filter.', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--login', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='login', kind=None),
                                    ),
                                    keyword(
                                        arg='default',
                                        value=Constant(value='admin', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Login (default=admin)', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--password', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='dest',
                                        value=Constant(value='password', kind=None),
                                    ),
                                    keyword(
                                        arg='default',
                                        value=Constant(value='admin', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Password (default=admin)', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--verify-ssl', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store_true', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Verify SSL certificate', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='add_argument',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='--force', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='action',
                                        value=Constant(value='store_true', kind=None),
                                    ),
                                    keyword(
                                        arg='help',
                                        value=Constant(value='Force init even if module is already installed. (will update `noupdate="1"` records)', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='cmdargs', ctx=Load()),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='sys', ctx=Load()),
                                            attr='exit',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='parser', ctx=Load()),
                                                    attr='print_help',
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
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='parser', ctx=Load()),
                                    attr='parse_args',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='args',
                                        value=Name(id='cmdargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='args', ctx=Load()),
                                    attr='verify_ssl',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='session',
                                                ctx=Load(),
                                            ),
                                            attr='verify',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='args', ctx=Load()),
                                                    attr='url',
                                                    ctx=Load(),
                                                ),
                                                attr='startswith',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='http://', kind=None),
                                                        Constant(value='https://', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='args', ctx=Load()),
                                                    attr='url',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value='https://%s', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='args', ctx=Load()),
                                                    attr='url',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='deploy_module',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='url',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='login',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='password',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='args', ctx=Load()),
                                                attr='db',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='force',
                                                value=Attribute(
                                                    value=Name(id='args', ctx=Load()),
                                                    attr='force',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='print', ctx=Load()),
                                        args=[Name(id='result', ctx=Load())],
                                        keywords=[],
                                    ),
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
                                                    value=Name(id='sys', ctx=Load()),
                                                    attr='exit',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='ERROR: %s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='e', ctx=Load()),
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
