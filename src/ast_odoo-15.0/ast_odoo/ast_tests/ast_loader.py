Module(
    body=[
        Import(
            names=[alias(name='importlib', asname=None)],
        ),
        Import(
            names=[alias(name='inspect', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='unittest', asname=None)],
        ),
        ImportFrom(
            module=None,
            names=[alias(name='tools', asname=None)],
            level=2,
        ),
        ImportFrom(
            module='common',
            names=[
                alias(name='TagsSelector', asname=None),
                alias(name='OdooSuite', asname=None),
            ],
            level=1,
        ),
        ImportFrom(
            module='runner',
            names=[alias(name='OdooTestResult', asname=None)],
            level=1,
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
        FunctionDef(
            name='get_test_modules',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='module', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a list of module for the addons potentially containing tests to\n    feed unittest.TestLoader.loadTestsFromModule() ', kind=None),
                ),
                Assign(
                    targets=[Name(id='results', ctx=Store())],
                    value=Call(
                        func=Name(id='_get_tests_modules', ctx=Load()),
                        args=[
                            Constant(value='odoo.addons', kind=None),
                            Name(id='module', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='importlib', ctx=Load()),
                                    attr='import_module',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='odoo.upgrade.%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='module', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='ImportError', ctx=Load()),
                            name=None,
                            body=[Pass()],
                        ),
                    ],
                    orelse=[
                        AugAssign(
                            target=Name(id='results', ctx=Store()),
                            op=Add(),
                            value=Call(
                                func=Name(id='_get_tests_modules', ctx=Load()),
                                args=[
                                    Constant(value='odoo.upgrade', kind=None),
                                    Name(id='module', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    finalbody=[],
                ),
                Return(
                    value=Name(id='results', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_get_tests_modules',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='path', annotation=None, type_comment=None),
                    arg(arg='module', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='modpath', ctx=Store())],
                    value=BinOp(
                        left=Constant(value='%s.%s', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Name(id='path', ctx=Load()),
                                Name(id='module', ctx=Load()),
                            ],
                            ctx=Load(),
                        ),
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='mod', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='importlib', ctx=Load()),
                                    attr='import_module',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='.tests', kind=None),
                                    Name(id='modpath', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='ImportError', ctx=Load()),
                            name='e',
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    BinOp(
                                                        left=Name(id='modpath', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value='.tests', kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='msg',
                                                        ctx=Load(),
                                                    ),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='No module named', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=List(elts=[], ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='exception',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Can not `import %s`.', kind=None),
                                            Name(id='module', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                        ),
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name='e',
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='exception',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Can not `import %s`.', kind=None),
                                            Name(id='module', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                If(
                    test=BoolOp(
                        op=Or(),
                        values=[
                            Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='mod', ctx=Load()),
                                    Constant(value='fast_suite', kind=None),
                                ],
                                keywords=[],
                            ),
                            Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='mod', ctx=Load()),
                                    Constant(value='checks', kind=None),
                                ],
                                keywords=[],
                            ),
                        ],
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
                                    Constant(value='Found deprecated fast_suite or checks attribute in test module %s. These have no effect in or after version 8.0.', kind=None),
                                    Attribute(
                                        value=Name(id='mod', ctx=Load()),
                                        attr='__name__',
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
                    targets=[Name(id='result', ctx=Store())],
                    value=ListComp(
                        elt=Name(id='mod_obj', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Tuple(
                                    elts=[
                                        Name(id='name', ctx=Store()),
                                        Name(id='mod_obj', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                                iter=Call(
                                    func=Attribute(
                                        value=Name(id='inspect', ctx=Load()),
                                        attr='getmembers',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='mod', ctx=Load()),
                                        Attribute(
                                            value=Name(id='inspect', ctx=Load()),
                                            attr='ismodule',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ifs=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='name', ctx=Load()),
                                            attr='startswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='test_', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                is_async=0,
                            ),
                        ],
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
        FunctionDef(
            name='make_suite',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='module_names', annotation=None, type_comment=None),
                    arg(arg='position', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='at_install', kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Creates a test suite for all the tests in the specified modules,\n    filtered by the provided ``position`` and the current test tags\n\n    :param list[str] module_names: modules to load tests from\n    :param str position: "at_install" or "post_install"\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='config_tags', ctx=Store())],
                    value=Call(
                        func=Name(id='TagsSelector', ctx=Load()),
                        args=[
                            Subscript(
                                value=Attribute(
                                    value=Name(id='tools', ctx=Load()),
                                    attr='config',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_tags', kind=None),
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='position_tag', ctx=Store())],
                    value=Call(
                        func=Name(id='TagsSelector', ctx=Load()),
                        args=[Name(id='position', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tests', ctx=Store())],
                    value=GeneratorExp(
                        elt=Name(id='t', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Name(id='module_name', ctx=Store()),
                                iter=Name(id='module_names', ctx=Load()),
                                ifs=[],
                                is_async=0,
                            ),
                            comprehension(
                                target=Name(id='m', ctx=Store()),
                                iter=Call(
                                    func=Name(id='get_test_modules', ctx=Load()),
                                    args=[Name(id='module_name', ctx=Load())],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                            comprehension(
                                target=Name(id='t', ctx=Store()),
                                iter=Call(
                                    func=Name(id='unwrap_suite', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='unittest', ctx=Load()),
                                                        attr='TestLoader',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='loadTestsFromModule',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='m', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ifs=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='position_tag', ctx=Load()),
                                                    attr='check',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='t', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='config_tags', ctx=Load()),
                                                    attr='check',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='t', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                is_async=0,
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='OdooSuite', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[Name(id='tests', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='t', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='test_sequence',
                                                ctx=Load(),
                                            ),
                                        ),
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
            name='run_suite',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='suite', annotation=None, type_comment=None),
                    arg(arg='module_name', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                ImportFrom(
                    module='modules',
                    names=[alias(name='module', asname=None)],
                    level=2,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='module', ctx=Load()),
                            attr='current_test',
                            ctx=Store(),
                        ),
                    ],
                    value=Name(id='module_name', ctx=Load()),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='currentThread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='testing',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='results', ctx=Store())],
                    value=Call(
                        func=Name(id='OdooTestResult', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Name(id='suite', ctx=Load()),
                        args=[Name(id='results', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='currentThread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='testing',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[
                        Attribute(
                            value=Name(id='module', ctx=Load()),
                            attr='current_test',
                            ctx=Store(),
                        ),
                    ],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='results', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='unwrap_suite',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='test', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value="\n    Attempts to unpack testsuites (holding suites or cases) in order to\n    generate a single stream of terminals (either test cases or customized\n    test suites). These can then be checked for run/skip attributes\n    individually.\n\n    An alternative would be to use a variant of @unittest.skipIf with a state\n    flag of some sort e.g. @unittest.skipIf(common.runstate != 'at_install'),\n    but then things become weird with post_install as tests should *not* run\n    by default there\n    ", kind=None),
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='test', ctx=Load()),
                            Attribute(
                                value=Name(id='unittest', ctx=Load()),
                                attr='TestCase',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Yield(
                                value=Name(id='test', ctx=Load()),
                            ),
                        ),
                        Return(value=None),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='subtests', ctx=Store())],
                    value=Call(
                        func=Name(id='list', ctx=Load()),
                        args=[Name(id='test', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='subtests', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Expr(
                            value=Yield(
                                value=Name(id='test', ctx=Load()),
                            ),
                        ),
                        Return(value=None),
                    ],
                    orelse=[],
                ),
                For(
                    target=Name(id='item', ctx=Store()),
                    iter=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='itertools', ctx=Load()),
                                attr='chain',
                                ctx=Load(),
                            ),
                            attr='from_iterable',
                            ctx=Load(),
                        ),
                        args=[
                            GeneratorExp(
                                elt=Call(
                                    func=Name(id='unwrap_suite', ctx=Load()),
                                    args=[Name(id='t', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='t', ctx=Store()),
                                        iter=Name(id='subtests', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Yield(
                                value=Name(id='item', ctx=Load()),
                            ),
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
    ],
    type_ignores=[],
)
