Module(
    body=[
        Import(
            names=[alias(name='textwrap', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[
                alias(name='etree', asname=None),
                alias(name='html', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='lxml.builder',
            names=[alias(name='E', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='BaseCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.web_editor.models.ir_qweb',
            names=[alias(name='html_to_text', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestHTMLToText',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_rawstring',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foobar', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='foobar', kind=None)],
                                                keywords=[],
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
                    name='test_br',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo\nbar', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='foo', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='br',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='bar', kind=None),
                                                ],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo\n\nbar\nbaz', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='foo', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='br',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='br',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='bar', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='br',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                keywords=[],
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
                    name='test_p',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo\n\nbar\n\nbaz', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='foo', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='p',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='bar', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='p',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='foo', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo\n\nbar', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='foo', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='p',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='bar', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo\n\nbar', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='p',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='foo', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='bar', kind=None),
                                                ],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo\n\nbar\n\nbaz', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='p',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='foo', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='p',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='bar', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='p',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='baz', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
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
                    name='test_div',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo\nbar\nbaz', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='foo', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='div',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='bar', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='div',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='foo', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo\nbar', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='foo', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='div',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='bar', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo\nbar', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='div',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='foo', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='bar', kind=None),
                                                ],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo\nbar\nbaz', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='foo', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='div',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='bar', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='div',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='baz', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
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
                    name='test_other_block',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo\nbar\nbaz', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='foo', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='section',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='bar', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                keywords=[],
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
                    name='test_inline',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foobarbaz', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='foo', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='span',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='bar', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                keywords=[],
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
                    name='test_whitespace',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo bar\nbaz', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='foo\nbar', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='br',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                keywords=[],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='foo bar\nbaz', kind=None),
                                    Call(
                                        func=Name(id='html_to_text', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='div',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='E', ctx=Load()),
                                                                    attr='span',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='foo', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Constant(value=' bar', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                keywords=[],
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
        ClassDef(
            name='TestConvertBack',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                                            Name(id='TestConvertBack', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
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
                                    attr='env',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='context',
                                        value=Dict(
                                            keys=[Constant(value='inherit_branding', kind=None)],
                                            values=[Constant(value=True, kind=None)],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='field_rountrip_result',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='expected', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Constant(value='web_editor.converter.test', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Name(id='field', ctx=Load())],
                                        values=[Name(id='value', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='t', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='t', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='e', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='span', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='t', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='e', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='field_value', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='record.%s', kind=None),
                                op=Mod(),
                                right=Name(id='field', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='e', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='t-field', kind=None),
                                    Name(id='field_value', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='rendered', ctx=Store())],
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
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='t', ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='record', kind=None)],
                                        values=[Name(id='record', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='element', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rendered', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='parser',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='html', ctx=Load()),
                                                attr='HTMLParser',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='encoding',
                                                    value=Constant(value='utf-8', kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='ir.qweb.field.', kind=None),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='element', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='data-oe-type', kind=None),
                                        Constant(value='', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='converter', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='model', ctx=Load()),
                                    ops=[In()],
                                    comparators=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                body=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='model', ctx=Load()),
                                    ctx=Load(),
                                ),
                                orelse=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='ir.qweb.field', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='value_back', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='converter', ctx=Load()),
                                    attr='from_html',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='model', ctx=Load()),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_fields',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='field', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    Name(id='element', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='isinstance', ctx=Load()),
                                args=[
                                    Name(id='expected', ctx=Load()),
                                    Name(id='bytes', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='expected', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expected', ctx=Load()),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='utf-8', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
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
                                    Name(id='value_back', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
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
                    name='field_roundtrip',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='field_rountrip_result',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='field', ctx=Load()),
                                    Name(id='value', ctx=Load()),
                                    Name(id='value', ctx=Load()),
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
                    name='test_integer',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='field_roundtrip',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='integer', kind=None),
                                    Constant(value=42, kind=None),
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
                    name='test_float',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='field_roundtrip',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='float', kind=None),
                                    Constant(value=42.56789, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='field_roundtrip',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='float', kind=None),
                                    Constant(value=324542.56789, kind=None),
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
                    name='test_numeric',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='field_roundtrip',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='numeric', kind=None),
                                    Constant(value=42.77, kind=None),
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
                    name='test_char',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='field_roundtrip',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='char', kind=None),
                                    Constant(value='foo bar', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='field_roundtrip',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='char', kind=None),
                                    Constant(value='ⒸⓄⓇⒼⒺ', kind=None),
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
                    name='test_selection_str',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='field_roundtrip',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='selection_str', kind=None),
                                    Constant(value='B', kind=None),
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
                    name='test_text',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='field_roundtrip',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='text', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='textwrap', ctx=Load()),
                                            attr='dedent',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value="            You must obey the dance commander\n            Givin' out the order for fun\n            You must obey the dance commander\n            You know that he's the only one\n            Who gives the orders here,\n            Alright\n            Who gives the orders here,\n            Alright\n\n            It would be awesome\n            If we could dance-a\n            It would be awesome, yeah\n            Let's take the chance-a\n            It would be awesome, yeah\n            Let's start the show\n            Because you never know\n            You never know\n            You never know until you go", kind=None)],
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
                    name='test_m2o',
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
                            value=Constant(value=' the M2O field conversion (from html) is markedly different from\n        others as it directly writes into the m2o and returns nothing at all.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field', ctx=Store())],
                            value=Constant(value='many2one', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subrec1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='web_editor.converter.test.sub', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Foo', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='subrec2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='web_editor.converter.test.sub', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Bar', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='record', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='web_editor.converter.test', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Name(id='field', ctx=Load())],
                                        values=[
                                            Attribute(
                                                value=Name(id='subrec1', ctx=Load()),
                                                attr='id',
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
                            targets=[Name(id='t', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='t', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='e', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='span', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='t', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='e', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='field_value', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='record.%s', kind=None),
                                op=Mod(),
                                right=Name(id='field', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='e', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='t-field', kind=None),
                                    Name(id='field_value', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='rendered', ctx=Store())],
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
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='t', ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='record', kind=None)],
                                        values=[Name(id='record', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='element', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rendered', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='parser',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='html', ctx=Load()),
                                                attr='HTMLParser',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='encoding',
                                                    value=Constant(value='utf-8', kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='element', ctx=Load()),
                                    attr='set',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='data-oe-many2one-id', kind=None),
                                    Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='subrec2', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='element', ctx=Load()),
                                    attr='text',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='New content', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='ir.qweb.field.', kind=None),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='element', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='data-oe-type', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='converter', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='model', ctx=Load()),
                                    ops=[In()],
                                    comparators=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                body=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='model', ctx=Load()),
                                    ctx=Load(),
                                ),
                                orelse=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='ir.qweb.field', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='value_back', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='converter', ctx=Load()),
                                    attr='from_html',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='web_editor.converter.test', kind=None),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_fields',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='field', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    Name(id='element', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='value_back', ctx=Load()),
                                    Constant(value='the m2o converter should return None to avoid spurious or useless writes on the parent record', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='subrec1', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Foo', kind=None),
                                    Constant(value="element edition can't change directly the m2o record", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='many2one',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Bar', kind=None),
                                    Constant(value='element edition should have been change the m2o id', kind=None),
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
    ],
    type_ignores=[],
)
