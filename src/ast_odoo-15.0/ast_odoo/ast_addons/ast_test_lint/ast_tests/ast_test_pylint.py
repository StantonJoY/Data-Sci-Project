Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Try(
            body=[
                Import(
                    names=[alias(name='pylint', asname=None)],
                ),
            ],
            handlers=[
                ExceptHandler(
                    type=Name(id='ImportError', ctx=Load()),
                    name=None,
                    body=[
                        Assign(
                            targets=[Name(id='pylint', ctx=Store())],
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
            names=[alias(name='subprocess', asname=None)],
        ),
        ImportFrom(
            module='distutils.version',
            names=[alias(name='LooseVersion', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        ImportFrom(
            module='os.path',
            names=[alias(name='join', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.modules',
            names=[
                alias(name='get_modules', asname=None),
                alias(name='get_module_path', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='HERE', ctx=Store())],
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
                    Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='realpath',
                            ctx=Load(),
                        ),
                        args=[Name(id='__file__', ctx=Load())],
                        keywords=[],
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
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
            name='TestPyLint',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='ENABLED_CODES', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='used-before-assignment', kind=None),
                            Constant(value='undefined-variable', kind=None),
                            Constant(value='eval-used', kind=None),
                            Constant(value='unreachable', kind=None),
                            Constant(value='function-redefined', kind=None),
                            Constant(value='sql-injection', kind=None),
                            Constant(value='gettext-variable', kind=None),
                            Constant(value='raise-unlink-override', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='BAD_FUNCTIONS', ctx=Store())],
                    value=List(
                        elts=[Constant(value='input', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='BAD_MODULES', ctx=Store())],
                    value=BinOp(
                        left=List(
                            elts=[
                                Constant(value='csv', kind=None),
                                Constant(value='urllib', kind=None),
                                Constant(value='cgi', kind=None),
                            ],
                            ctx=Load(),
                        ),
                        op=Add(),
                        right=Call(
                            func=Name(id='list', ctx=Load()),
                            args=[
                                Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='SUPPORTED_DEBUGGER',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_skip_test',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='reason', annotation=None, type_comment=None),
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
                                args=[Name(id='reason', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='skipTest',
                                    ctx=Load(),
                                ),
                                args=[Name(id='reason', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_pylint',
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
                                left=Name(id='pylint', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_skip_test',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='please install pylint', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='required_pylint_version', ctx=Store())],
                            value=Call(
                                func=Name(id='LooseVersion', ctx=Load()),
                                args=[Constant(value='1.6.4', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='version_info',
                                    ctx=Load(),
                                ),
                                ops=[GtE()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value=3, kind=None),
                                            Constant(value=6, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='required_pylint_version', ctx=Store())],
                                    value=Call(
                                        func=Name(id='LooseVersion', ctx=Load()),
                                        args=[Constant(value='1.7.0', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='LooseVersion', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='pylint', ctx=Load()),
                                                Constant(value='__version__', kind=None),
                                                Constant(value='0.0.1', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Lt()],
                                comparators=[Name(id='required_pylint_version', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_skip_test',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='please upgrade pylint to >= %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='required_pylint_version', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='paths', ctx=Store())],
                            value=List(
                                elts=[
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='config',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='root_path', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='module', ctx=Store()),
                            iter=Call(
                                func=Name(id='get_modules', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='module_path', ctx=Store())],
                                    value=Call(
                                        func=Name(id='get_module_path', ctx=Load()),
                                        args=[Name(id='module', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='module_path', ctx=Load()),
                                                attr='startswith',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Name(id='join', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='tools', ctx=Load()),
                                                                attr='config',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='root_path', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value='addons', kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='paths', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='module_path', ctx=Load())],
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
                            targets=[Name(id='options', ctx=Store())],
                            value=List(
                                elts=[
                                    BinOp(
                                        left=Constant(value='--rcfile=%s', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='devnull',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Constant(value='--disable=all', kind=None),
                                    BinOp(
                                        left=Constant(value='--enable=%s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Constant(value=',', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ENABLED_CODES',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    Constant(value='--reports=n', kind=None),
                                    Constant(value="--msg-template='{msg} ({msg_id}) at {path}:{line}'", kind=None),
                                    Constant(value='--load-plugins=pylint.extensions.bad_builtin,_odoo_checker_sql_injection,_odoo_checker_gettext,_odoo_checker_unlink_override', kind=None),
                                    BinOp(
                                        left=Constant(value='--bad-functions=%s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Constant(value=',', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='BAD_FUNCTIONS',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    BinOp(
                                        left=Constant(value='--deprecated-modules=%s', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Constant(value=',', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='BAD_MODULES',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pypath', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='HERE', ctx=Load()),
                                    op=Add(),
                                    right=Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='pathsep',
                                        ctx=Load(),
                                    ),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='environ',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='PYTHONPATH', kind=None),
                                        Constant(value='', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='env', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='os', ctx=Load()),
                                        attr='environ',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='PYTHONPATH',
                                        value=Name(id='pypath', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='pylint_bin', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tools', ctx=Load()),
                                            attr='which',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='pylint', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='process', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='subprocess', ctx=Load()),
                                            attr='Popen',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=List(
                                                        elts=[Name(id='pylint_bin', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                    op=Add(),
                                                    right=Name(id='options', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='paths', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='stdout',
                                                value=Attribute(
                                                    value=Name(id='subprocess', ctx=Load()),
                                                    attr='PIPE',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='stderr',
                                                value=Attribute(
                                                    value=Name(id='subprocess', ctx=Load()),
                                                    attr='PIPE',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='env',
                                                value=Name(id='env', ctx=Load()),
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
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_skip_test',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='pylint executable not found in the path', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
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
                                            value=Name(id='process', ctx=Load()),
                                            attr='communicate',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='process', ctx=Load()),
                                        attr='returncode',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='fail',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='pylint test failed:\n', kind=None),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=BinOp(
                                                                            left=BinOp(
                                                                                left=BinOp(
                                                                                    left=Constant(value=b'\n', kind=None),
                                                                                    op=Add(),
                                                                                    right=Name(id='out', ctx=Load()),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=b'\n', kind=None),
                                                                            ),
                                                                            op=Add(),
                                                                            right=Name(id='err', ctx=Load()),
                                                                        ),
                                                                        attr='decode',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='utf-8', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='strip',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
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
