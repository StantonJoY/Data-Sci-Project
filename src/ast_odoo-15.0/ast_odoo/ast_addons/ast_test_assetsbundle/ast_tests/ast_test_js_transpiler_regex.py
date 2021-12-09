Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='URL_RE', asname=None),
                alias(name='ODOO_MODULE_RE', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestJsTranspiler',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_correct_ODOO_MODULE_RE',
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
                            targets=[Name(id='cases', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='// @odoo-module', kind=None),
                                    Constant(value='//@odoo-module', kind=None),
                                    Constant(value='/* @odoo-module', kind=None),
                                    Constant(value='/** @odoo-module', kind=None),
                                    Constant(value='/*@odoo-module', kind=None),
                                    Constant(value='/**@odoo-module', kind=None),
                                    Constant(value='// @odoo-module alias=web.test', kind=None),
                                    Constant(value='/* @odoo-module  alias=web.test', kind=None),
                                    Constant(value='/** @odoo-module  alias=web.test', kind=None),
                                    Constant(value='/** @odoo-module  alias=web.test**/', kind=None),
                                    Constant(value='/* @odoo-module  alias=web.test ', kind=None),
                                    Constant(value='/* @odoo-module alias=web.test default=false', kind=None),
                                    Constant(value='/* @odoo-module alias=web.test default=false ', kind=None),
                                    Constant(value='/* @odoo-module alias=web.test default=false**/', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='case', ctx=Store()),
                            iter=Name(id='cases', ctx=Load()),
                            body=[
                                Assert(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='ODOO_MODULE_RE', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='case', ctx=Load())],
                                        keywords=[],
                                    ),
                                    msg=BinOp(
                                        left=Constant(value='URL_RE is failing... >%s<', kind=None),
                                        op=Mod(),
                                        right=Name(id='case', ctx=Load()),
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='alias', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='case', ctx=Load())],
                                    ),
                                    body=[
                                        Assert(
                                            test=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='ODOO_MODULE_RE', ctx=Load()),
                                                                    attr='match',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='case', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='groupdict',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='alias', kind=None)],
                                                keywords=[],
                                            ),
                                            msg=BinOp(
                                                left=Constant(value='URL_RE is failing for alias... >%s<', kind=None),
                                                op=Mod(),
                                                right=Name(id='case', ctx=Load()),
                                            ),
                                        ),
                                        Assert(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='ODOO_MODULE_RE', ctx=Load()),
                                                                        attr='match',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='case', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                attr='groupdict',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='alias', kind=None)],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='web.test', kind=None)],
                                            ),
                                            msg=BinOp(
                                                left=Constant(value='URL_RE does not get the right alias for ... >%s<', kind=None),
                                                op=Mod(),
                                                right=Name(id='case', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='default', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='case', ctx=Load())],
                                    ),
                                    body=[
                                        Assert(
                                            test=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='ODOO_MODULE_RE', ctx=Load()),
                                                                    attr='match',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='case', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='groupdict',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='default', kind=None)],
                                                keywords=[],
                                            ),
                                            msg=BinOp(
                                                left=Constant(value='URL_RE is failing for default... >%s<', kind=None),
                                                op=Mod(),
                                                right=Name(id='case', ctx=Load()),
                                            ),
                                        ),
                                        Assert(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='ODOO_MODULE_RE', ctx=Load()),
                                                                        attr='match',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='case', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                attr='groupdict',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='default', kind=None)],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='false', kind=None)],
                                            ),
                                            msg=BinOp(
                                                left=Constant(value='URL_RE does not get the right default for ... >%s<', kind=None),
                                                op=Mod(),
                                                right=Name(id='case', ctx=Load()),
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
                    name='test_incorrect_ODOO_MODULE_RE',
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
                            targets=[Name(id='cases', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='/* @odoo-module alias = web.test ', kind=None),
                                    Constant(value='/* @odoo-module alias= web.test', kind=None),
                                    Constant(value='/* @odoo-module alias = web.test default=false', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='case', ctx=Store()),
                            iter=Name(id='cases', ctx=Load()),
                            body=[
                                Assert(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='ODOO_MODULE_RE', ctx=Load()),
                                                                attr='match',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='case', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='groupdict',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='alias', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    msg=BinOp(
                                        left=Constant(value="URL_RE should fail because of too much spaces but didn't... >%s<", kind=None),
                                        op=Mod(),
                                        right=Name(id='case', ctx=Load()),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cases', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='// @odoo-modulealias=web.test', kind=None),
                                    Constant(value='/* @odoo-module alias=web.testdefault=false', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='case', ctx=Store()),
                            iter=Name(id='cases', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Constant(value='alias', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='case', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Constant(value='default', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='case', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assert(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='ODOO_MODULE_RE', ctx=Load()),
                                                                                attr='match',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='case', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='groupdict',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='alias', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='ODOO_MODULE_RE', ctx=Load()),
                                                                                attr='match',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='case', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='groupdict',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='default', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            msg=BinOp(
                                                left=Constant(value='URL_RE should fail for alias and default... >%s<', kind=None),
                                                op=Mod(),
                                                right=Name(id='case', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='alias', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='case', ctx=Load())],
                                            ),
                                            body=[
                                                Assert(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='ODOO_MODULE_RE', ctx=Load()),
                                                                                attr='match',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='case', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='groupdict',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='alias', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    msg=BinOp(
                                                        left=Constant(value='URL_RE should fail for alias... >%s<', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='case', ctx=Load()),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
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
                    name='test_correct_URL_RE',
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
                            targets=[Name(id='cases', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='web/static/src/js/file.js', kind=None),
                                    Constant(value='/web/static/src/js/file.js', kind=None),
                                    Constant(value='/web/other/static/src/js/file.js', kind=None),
                                    Constant(value='/web/other/static/src/file.js', kind=None),
                                    Constant(value='/web/other/static/tests/file.js', kind=None),
                                    Constant(value='/web/other/static/src/another/and/file.js', kind=None),
                                    Constant(value='/web/other-o/static/src/another/and/file.js', kind=None),
                                    Constant(value='/web-o/other-o/static/src/another/and/file.js', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='case', ctx=Store()),
                            iter=Name(id='cases', ctx=Load()),
                            body=[
                                Assert(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='URL_RE', ctx=Load()),
                                            attr='fullmatch',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='case', ctx=Load())],
                                        keywords=[],
                                    ),
                                    msg=BinOp(
                                        left=Constant(value='URL RE failed... %s', kind=None),
                                        op=Mod(),
                                        right=Name(id='case', ctx=Load()),
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
                FunctionDef(
                    name='test_incorrect_URL_RE',
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
                            targets=[Name(id='cases', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='web/static/js/src/file.js', kind=None),
                                    Constant(value='web/static/js/file.js', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='case', ctx=Store()),
                            iter=Name(id='cases', ctx=Load()),
                            body=[
                                Assert(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='URL_RE', ctx=Load()),
                                                attr='fullmatch',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='case', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    msg=BinOp(
                                        left=Constant(value='URL RE should have failed... %s', kind=None),
                                        op=Mod(),
                                        right=Name(id='case', ctx=Load()),
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
