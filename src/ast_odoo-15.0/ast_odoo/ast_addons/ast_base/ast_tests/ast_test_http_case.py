Module(
    body=[
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='HttpCase', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='mute_logger', asname=None),
                alias(name='logging', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestHttpCase',
            bases=[Name(id='HttpCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_console_error_string',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AssertionError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='error_catcher', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='code', ctx=Store())],
                                    value=Constant(value="console.error('test error','message')", kind=None),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='patch', ctx=Load()),
                                                args=[Constant(value='odoo.tests.common.ChromeBrowser.take_screenshot', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='return_value',
                                                        value=Constant(value=None, kind=None),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='browser_js',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='url_path',
                                                        value=Constant(value='about:blank', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='code',
                                                        value=Name(id='code', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='error_catcher', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='splitlines',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='test error message', kind=None),
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
                    name='test_console_error_object',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AssertionError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='error_catcher', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='code', ctx=Store())],
                                    value=Constant(value="console.error(TypeError('test error message'))", kind=None),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='patch', ctx=Load()),
                                                args=[Constant(value='odoo.tests.common.ChromeBrowser.take_screenshot', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='return_value',
                                                        value=Constant(value=None, kind=None),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='browser_js',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='url_path',
                                                        value=Constant(value='about:blank', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='code',
                                                        value=Name(id='code', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='error_catcher', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='splitlines',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=Constant(value=3, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='TypeError: test error message', kind=None),
                                            Constant(value='    at <anonymous>:1:15', kind=None),
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
                FunctionDef(
                    name='test_console_log_object',
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
                            targets=[Name(id='logger', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logging', ctx=Load()),
                                    attr='getLogger',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='odoo', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='level', ctx=Store())],
                            value=Attribute(
                                value=Name(id='logger', ctx=Load()),
                                attr='level',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logger', ctx=Load()),
                                    attr='setLevel',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='INFO',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='addCleanup',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='logger', ctx=Load()),
                                        attr='setLevel',
                                        ctx=Load(),
                                    ),
                                    Name(id='level', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertLogs',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='log_catcher', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='code', ctx=Store())],
                                    value=Constant(value="console.log({custom:{1:'test', 2:'a'}, value:1, description:'dummy'});console.log('test successful');", kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='browser_js',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='url_path',
                                                value=Constant(value='about:blank', kind=None),
                                            ),
                                            keyword(
                                                arg='code',
                                                value=Name(id='code', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='console_log_count', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='log', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='log_catcher', ctx=Load()),
                                attr='output',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='.browser:', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='log', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='text', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='log', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='.browser:', kind=None),
                                                        Constant(value=1, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='text', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='test successful', kind=None)],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='text', ctx=Load()),
                                                    Constant(value="Object(custom=Object, value=1, description='dummy')", kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='console_log_count', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='console_log_count', ctx=Load()),
                                    Constant(value=1, kind=None),
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='-at_install', kind=None),
                        Constant(value='post_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
