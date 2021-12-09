Module(
    body=[
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[
                alias(name='quote', asname=None),
                alias(name='unquote', asname=None),
                alias(name='xml_translate', asname=None),
                alias(name='html_translate', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='TransactionCase', asname=None),
                alias(name='BaseCase', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='psycopg2',
            names=[alias(name='IntegrityError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TranslationToolsTestCase',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='assertItemsEqual',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='a', annotation=None, type_comment=None),
                            arg(arg='b', annotation=None, type_comment=None),
                            arg(arg='msg', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
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
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[Name(id='a', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[Name(id='b', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='msg', ctx=Load()),
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
                    name='test_quote_unquote',
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
                        FunctionDef(
                            name='test_string',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='str', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='quoted', ctx=Store())],
                                    value=Call(
                                        func=Name(id='quote', ctx=Load()),
                                        args=[Name(id='str', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='unquoted', ctx=Store())],
                                    value=Call(
                                        func=Name(id='unquote', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='', kind=None),
                                                    attr='join',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='quoted', ctx=Load()),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='"\n"', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
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
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='str', ctx=Load()),
                                            Name(id='unquoted', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='test_string', ctx=Load()),
                                args=[Constant(value='test \nall kinds\n \n o\r\n         \\\\ nope\n\n"\n         ', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRaises',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='AssertionError', ctx=Load()),
                                    Name(id='quote', ctx=Load()),
                                    Constant(value='test \nall kinds\n\no\r\n         \\\\nope\n\n"\n         ', kind=None),
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
                    name='test_translate_xml_base',
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
                            value=Constant(value=' Test xml_translate() without formatting elements. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<form string="Form stuff">\n                        <h1>Blah blah blah</h1>\n                        Put some more text here\n                        <field name="foo"/>\n                    </form>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='Form stuff', kind=None),
                                            Constant(value='Blah blah blah', kind=None),
                                            Constant(value='Put some more text here', kind=None),
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
                    name='test_translate_xml_text',
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
                            value=Constant(value=' Test xml_translate() on plain text. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='Blah blah blah', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[Name(id='source', ctx=Load())],
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
                    name='test_translate_xml_unicode',
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
                            value=Constant(value=' Test xml_translate() on plain text with unicode characters. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='Un heureux évènement', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[Name(id='source', ctx=Load())],
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
                    name='test_translate_xml_text_entity',
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
                            value=Constant(value=' Test xml_translate() on plain text with HTML escaped entities. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='Blah&amp;nbsp;blah&amp;nbsp;blah', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[Name(id='source', ctx=Load())],
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
                    name='test_translate_xml_inline1',
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
                            value=Constant(value=' Test xml_translate() with formatting elements. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<form string="Form stuff">\n                        <h1>Blah <i>blah</i> blah</h1>\n                        Put some <b>more text</b> here\n                        <field name="foo"/>\n                    </form>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='Form stuff', kind=None),
                                            Constant(value='Blah <i>blah</i> blah', kind=None),
                                            Constant(value='Put some <b>more text</b> here', kind=None),
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
                    name='test_translate_xml_inline2',
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
                            value=Constant(value=' Test xml_translate() with formatting elements embedding other elements. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<form string="Form stuff">\n                        <b><h1>Blah <i>blah</i> blah</h1></b>\n                        Put <em>some <b>more text</b></em> here\n                        <field name="foo"/>\n                    </form>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='Form stuff', kind=None),
                                            Constant(value='Blah <i>blah</i> blah', kind=None),
                                            Constant(value='Put <em>some <b>more text</b></em> here', kind=None),
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
                    name='test_translate_xml_inline3',
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
                            value=Constant(value=' Test xml_translate() with formatting elements without actual text. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<form string="Form stuff">\n                        <div>\n                            <span class="before"/>\n                            <h1>Blah blah blah</h1>\n                            <span class="after">\n                                <i class="hack"/>\n                            </span>\n                        </div>\n                    </form>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='Form stuff', kind=None),
                                            Constant(value='Blah blah blah', kind=None),
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
                    name='test_translate_xml_inline4',
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
                            value=Constant(value=' Test xml_translate() with inline elements with translated attrs only. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<form string="Form stuff">\n                        <div>\n                            <label for="stuff"/>\n                            <span class="fa fa-globe" title="Title stuff"/>\n                        </div>\n                    </form>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='Form stuff', kind=None),
                                            Constant(value='<span class="fa fa-globe" title="Title stuff"/>', kind=None),
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
                    name='test_translate_xml_inline5',
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
                            value=Constant(value=' Test xml_translate() with inline elements with empty translated attrs only. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<form string="Form stuff">\n                        <div>\n                            <label for="stuff"/>\n                            <span class="fa fa-globe" title=""/>\n                        </div>\n                    </form>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[Constant(value='Form stuff', kind=None)],
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
                    name='test_translate_xml_t',
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
                            value=Constant(value=' Test xml_translate() with t-* attributes. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<t t-name="stuff">\n                        stuff before\n                        <span t-field="o.name"/>\n                        stuff after\n                    </t>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='stuff before', kind=None),
                                            Constant(value='stuff after', kind=None),
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
                    name='test_translate_xml_off',
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
                            value=Constant(value=' Test xml_translate() with attribute translate="off". ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<div>\n                        stuff before\n                        <div t-translation="off">Do not translate this</div>\n                        stuff after\n                    </div>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[
                                            Constant(value='stuff before', kind=None),
                                            Constant(value='stuff after', kind=None),
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
                    name='test_translate_xml_attribute',
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
                            value=Constant(value=' Test xml_translate() with <attribute> elements. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<field name="foo" position="attributes">\n                        <attribute name="string">Translate this</attribute>\n                        <attribute name="option">Do not translate this</attribute>\n                    </field>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[Constant(value='Translate this', kind=None)],
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
                    name='test_translate_xml_a',
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
                            value=Constant(value=' Test xml_translate() with <a> elements. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<t t-name="stuff">\n                        <ul class="nav navbar-nav">\n                            <li class="nav-item">\n                                <a class="nav-link oe_menu_leaf" href="/web#menu_id=42&amp;action=54">\n                                    <span class="oe_menu_text">Blah</span>\n                                </a>\n                            </li>\n                        </ul>\n                    </t>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[Constant(value='<span class="oe_menu_text">Blah</span>', kind=None)],
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
                    name='test_translate_xml_with_namespace',
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
                            value=Constant(value=' Test xml_translate() on elements with namespaces. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='terms', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<Invoice xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">\n                        <cbc:UBLVersionID t-esc="version_id"/>\n                        <t t-foreach="[1, 2, 3, 4]" t-as="value">\n                            Oasis <cac:Test t-esc="value"/>\n                        </t>\n                    </Invoice>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='terms', ctx=Load()),
                                        attr='append',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertItemsEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='terms', ctx=Load()),
                                    List(
                                        elts=[Constant(value='Oasis', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='term', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Name(id='term', ctx=Load()),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
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
                    name='test_translate_xml_invalid_translations',
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
                            value=Constant(value=' Test xml_translate() with invalid translations. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<form string="Form stuff">\n                        <h1>Blah <i>blah</i> blah</h1>\n                        Put some <b>more text</b> here\n                        <field name="foo"/>\n                    </form>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='translations', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='Put some <b>more text</b> here', kind=None)],
                                values=[Constant(value='Mettre <b>plus de texte</i> ici', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expect', ctx=Store())],
                            value=Constant(value='<form string="Form stuff">\n                        <h1>Blah <i>blah</i> blah</h1>\n                        Mettre <b>plus de texte ici\n                        </b><field name="foo"/>\n                    </form>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='translations', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='expect', ctx=Load()),
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
                    name='test_translate_html',
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
                            value=Constant(value=' Test html_translate(). ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<blockquote>A <h2>B</h2> C</blockquote>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='html_translate', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='term', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Name(id='term', ctx=Load()),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
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
                    name='test_translate_html_i',
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
                            value=Constant(value=' Test xml_translate() and html_translate() with <i> elements. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=Constant(value='<p>A <i class="fa-check"></i> B</p>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='xml_translate', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='term', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Name(id='term', ctx=Load()),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Constant(value='<p>A <i class="fa-check"/> B</p>', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='html_translate', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='term', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Name(id='term', ctx=Load()),
                                    ),
                                    Name(id='source', ctx=Load()),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='source', ctx=Load()),
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
            name='TestTranslation',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
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
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='fr_FR', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.module_base', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_update_translations',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='fr_FR', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='customers',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner.category', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Customers', kind=None)],
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
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='type', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='module', kind=None),
                                            Constant(value='lang', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='value', kind=None),
                                            Constant(value='state', kind=None),
                                        ],
                                        values=[
                                            Constant(value='model', kind=None),
                                            Constant(value='res.partner.category,name', kind=None),
                                            Constant(value='base', kind=None),
                                            Constant(value='fr_FR', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='customers',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Clients', kind=None),
                                            Constant(value='translated', kind=None),
                                        ],
                                    ),
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
                    name='test_101_create_translated_record',
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
                            targets=[Name(id='category', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='customers',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
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
                                    Attribute(
                                        value=Name(id='category', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Customers', kind=None),
                                    Constant(value='Error in basic name_get', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='category_fr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='category', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='lang', kind=None)],
                                        values=[Constant(value='fr_FR', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='category_fr', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Clients', kind=None),
                                    Constant(value='Translation not found', kind=None),
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
                    name='test_102_duplicate_record',
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
                            targets=[Name(id='category', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='customers',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='lang', kind=None)],
                                                values=[Constant(value='fr_FR', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='category_no', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='category', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
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
                                    Attribute(
                                        value=Name(id='category_no', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Customers', kind=None),
                                    Constant(value='Duplication did not set untranslated value', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='category_fr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='category', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='lang', kind=None)],
                                        values=[Constant(value='fr_FR', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='category_fr', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Clients', kind=None),
                                    Constant(value='Did not found translation for initial value', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translation_fr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='res.partner.category,name', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='category', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='fr_FR', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='translation_fr', ctx=Load()),
                                        attr='src',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Customers', kind=None),
                                    Constant(value='Did not set English version as source', kind=None),
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
                    name='test_103_duplicate_record_fr',
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
                            targets=[Name(id='category', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='customers',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='lang', kind=None)],
                                                values=[Constant(value='fr_FR', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Clients (copie)', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='category_no', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='category', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
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
                                    Attribute(
                                        value=Name(id='category_no', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Clients (copie)', kind=None),
                                    Constant(value='Duplication should set untranslated value', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='category_fr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='category', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='lang', kind=None)],
                                        values=[Constant(value='fr_FR', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='category_fr', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Clients (copie)', kind=None),
                                    Constant(value='Did not used default value for translated value', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translation_fr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='res.partner.category,name', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='category', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='fr_FR', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='translation_fr', ctx=Load()),
                                        attr='src',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Clients (copie)', kind=None),
                                    Constant(value='Did not set new name as source', kind=None),
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
                    name='test_104_orderby_translated_field',
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
                            value=Constant(value=' Test search ordered by a translated field. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='padawans', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner.category', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Padawans', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='padawans_fr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='padawans', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='lang',
                                        value=Constant(value='fr_FR', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='padawans_fr', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Apprentis', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='categories', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='padawans_fr', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='customers',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='padawans', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
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
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='name', kind=None),
                                    ),
                                ],
                            ),
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
                                    Attribute(
                                        value=Name(id='categories', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='padawans', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='customers',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='Search ordered by translated name should return Padawans (Apprentis) before Customers (Clients)', kind=None),
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
                    name='test_105_duplicated_translation',
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
                            value=Constant(value=' Test synchronizing translations with duplicated source ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='padawans', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner.category', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Padawan', kind=None)],
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='type', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='module', kind=None),
                                            Constant(value='lang', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='value', kind=None),
                                            Constant(value='state', kind=None),
                                        ],
                                        values=[
                                            Constant(value='model', kind=None),
                                            Constant(value='res.partner.category,name', kind=None),
                                            Constant(value='base', kind=None),
                                            Constant(value='fr_FR', kind=None),
                                            Attribute(
                                                value=Name(id='padawans', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Apprenti', kind=None),
                                            Constant(value='translated', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='padawans', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Padawans', kind=None)],
                                    ),
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
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='IntegrityError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='mute_logger', ctx=Load()),
                                        args=[Constant(value='odoo.sql_db', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
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
                                                    attr='savepoint',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
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
                                                        slice=Constant(value='ir.translation', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='module', kind=None),
                                                            Constant(value='lang', kind=None),
                                                            Constant(value='res_id', kind=None),
                                                            Constant(value='value', kind=None),
                                                            Constant(value='state', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='model', kind=None),
                                                            Constant(value='res.partner.category,name', kind=None),
                                                            Constant(value='base', kind=None),
                                                            Constant(value='fr_FR', kind=None),
                                                            Attribute(
                                                                value=Name(id='padawans', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='Apprentis', kind=None),
                                                            Constant(value='translated', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='translate_fields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner.category', kind=None),
                                    Attribute(
                                        value=Name(id='padawans', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='name', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='padawans', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='res.partner.category,name', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='fr_FR', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='translations', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                    Constant(value='Translations were not duplicated after `translate_fields` call', kind=None),
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
                                        value=Name(id='translations', ctx=Load()),
                                        attr='value',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Apprenti', kind=None),
                                    Constant(value='The first translation must stay', kind=None),
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
                    name='test_106_en_us_translation',
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
                            value=Constant(value=' Test synchronizing translations with duplicated source ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='cheese', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner.category', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Cheese', kind=None)],
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='translate_fields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.partner.category', kind=None),
                                    Attribute(
                                        value=Name(id='cheese', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='name', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='res.partner.category,name', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='cheese', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='lang', kind=None),
                                    ),
                                ],
                            ),
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='translations', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='translations', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='src', kind=None),
                                                    Constant(value='value', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='en_US', kind=None),
                                                    Constant(value='Cheese', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='src', kind=None),
                                                    Constant(value='value', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='fr_FR', kind=None),
                                                    Constant(value='Cheese', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Name(id='translations', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='value',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='The Cheese', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Name(id='translations', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='value',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Fromage', kind=None),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='cheese', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Constant(value=None, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Cheese', kind=None),
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
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='cheese', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Constant(value='fr_FR', kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Fromage', kind=None),
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
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='cheese', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Constant(value='en_US', kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='The Cheese', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cheese', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cheese', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='en_US', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Delicious Cheese', kind=None)],
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='cheese', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Constant(value=None, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Delicious Cheese', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='translations', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='src', kind=None),
                                                    Constant(value='value', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='en_US', kind=None),
                                                    Constant(value='Delicious Cheese', kind=None),
                                                    Constant(value='Delicious Cheese', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='src', kind=None),
                                                    Constant(value='value', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='fr_FR', kind=None),
                                                    Constant(value='Delicious Cheese', kind=None),
                                                    Constant(value='Fromage', kind=None),
                                                ],
                                            ),
                                        ],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='cheese', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Constant(value=None, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Delicious Cheese', kind=None),
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
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='cheese', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Constant(value='fr_FR', kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Fromage', kind=None),
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
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='cheese', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Constant(value='en_US', kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Delicious Cheese', kind=None),
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
                    name='test_107_duplicate_record_en',
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
                            targets=[Name(id='category', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='customers',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='lang', kind=None)],
                                                values=[Constant(value='en_US', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='category_no', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='category', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
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
                                    Attribute(
                                        value=Name(id='category_no', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Customers', kind=None),
                                    Constant(value='Duplication did not set untranslated value', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='category_fr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='category', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='lang', kind=None)],
                                        values=[Constant(value='fr_FR', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='category_fr', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Clients', kind=None),
                                    Constant(value='Did not found translation for initial value', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translation_fr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='res.partner.category,name', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='category', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='fr_FR', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='translation_fr', ctx=Load()),
                                        attr='src',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Customers', kind=None),
                                    Constant(value='Did not set English version as source', kind=None),
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
            name='TestTranslationWrite',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='category',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.partner.category', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Reblochon', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_01_en',
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
                            targets=[Name(id='langs', ctx=Store())],
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
                                    attr='get_installed',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='en_US', kind=None),
                                                    Constant(value='English (US)', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='langs', ctx=Load()),
                                    Constant(value='Test did not started with expected languages', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='en_US', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='English Name', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='name', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='name', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='English Name', kind=None),
                                    Constant(value='Reference field not updated', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='res.partner.category,name', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='category',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='en_US', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='translations', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='No English translation should be created when writing in English', kind=None),
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
                    name='test_02_en_translated',
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
                            targets=[Name(id='langs', ctx=Store())],
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
                                    attr='get_installed',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='en_US', kind=None),
                                                    Constant(value='English (US)', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='langs', ctx=Load()),
                                    Constant(value='Test did not started with expected languages', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translation', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='type', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='lang', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='src', kind=None),
                                            Constant(value='value', kind=None),
                                            Constant(value='state', kind=None),
                                        ],
                                        values=[
                                            Constant(value='model', kind=None),
                                            Constant(value='res.partner.category,name', kind=None),
                                            Constant(value='en_US', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='category',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Reblochon', kind=None),
                                            Constant(value='Translated Name', kind=None),
                                            Constant(value='translated', kind=None),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='en_US', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='English Name', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translation_value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='translation', ctx=Load()),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='value', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='translation_value', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='value', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='English Name', kind=None),
                                    Constant(value='Existing translation was not updated', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='source_name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='name', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='source_name', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='English Name', kind=None),
                                    Constant(value='Reference field not updated', kind=None),
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
                    name='test_03_fr_single',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='fr_FR', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
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
                                                        slice=Constant(value='res.partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_test',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='lang', kind=None)],
                                        values=[Constant(value='fr_FR', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.lang_en', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='active',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='langs', ctx=Store())],
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
                                    attr='get_installed',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='fr_FR', kind=None),
                                                    Constant(value='French / Français', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='langs', ctx=Load()),
                                    Constant(value='Test did not started with expected languages', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='fr_FR', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='French Name', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='source_name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='name', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='source_name', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='name', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='French Name', kind=None),
                                    Constant(value='Reference field not updated', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='res.partner.category,name', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='category',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='fr_FR', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='translations', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='No French translation should be created when writing in French', kind=None),
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
                    name='test_04_fr_multi',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='fr_FR', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='langs', ctx=Store())],
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
                                    attr='get_installed',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='en_US', kind=None),
                                                    Constant(value='English (US)', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='fr_FR', kind=None),
                                                    Constant(value='French / Français', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='langs', ctx=Load()),
                                    Constant(value='Test did not started with expected languages', kind=None),
                                ],
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
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='type', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='lang', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='src', kind=None),
                                            Constant(value='value', kind=None),
                                            Constant(value='state', kind=None),
                                        ],
                                        values=[
                                            Constant(value='model', kind=None),
                                            Constant(value='res.partner.category,name', kind=None),
                                            Constant(value='en_US', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='category',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Reblochon', kind=None),
                                            Constant(value='Translated Name', kind=None),
                                            Constant(value='translated', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='fr_FR', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='French Name', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='en_US', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='English Name', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='res.partner.category,name', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='category',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='lang', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='translations', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='src', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='lang', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='English Name', kind=None),
                                                    Constant(value='English Name', kind=None),
                                                    Constant(value='en_US', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='src', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='lang', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='English Name', kind=None),
                                                    Constant(value='French Name', kind=None),
                                                    Constant(value='fr_FR', kind=None),
                                                ],
                                            ),
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
                    name='test_04_fr_multi_no_en',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='fr_FR', kind=None)],
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
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='es_ES', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
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
                                                        slice=Constant(value='res.partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_test',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='lang', kind=None)],
                                        values=[Constant(value='fr_FR', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.lang_en', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='active',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='langs', ctx=Store())],
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
                                    attr='get_installed',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='fr_FR', kind=None),
                                                    Constant(value='French / Français', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='es_ES', kind=None),
                                                    Constant(value='Spanish / Español', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='langs', ctx=Load()),
                                    Constant(value='Test did not start with the expected languages', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='fr_FR', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='French Name', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='es_ES', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Spanish Name', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='None Name', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='res.partner.category,name', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='category',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='lang', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertRecordValues',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='translations', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='src', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='lang', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='None Name', kind=None),
                                                    Constant(value='Spanish Name', kind=None),
                                                    Constant(value='es_ES', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='src', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='lang', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='None Name', kind=None),
                                                    Constant(value='French Name', kind=None),
                                                    Constant(value='fr_FR', kind=None),
                                                ],
                                            ),
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
                    name='test_05_remove_multi_empty_string',
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
                                    attr='_test_05_remove_multi',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_05_remove_multi_false',
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
                                    attr='_test_05_remove_multi',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=False, kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_test_05_remove_multi',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='empty_value', annotation=None, type_comment=None),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='fr_FR', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='langs', ctx=Store())],
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
                                    attr='get_installed',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='en_US', kind=None),
                                                    Constant(value='English (US)', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='fr_FR', kind=None),
                                                    Constant(value='French / Français', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Name(id='langs', ctx=Load()),
                                    Constant(value='Test did not started with expected languages', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='belgium', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='base.be', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='belgium', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='en_US', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='vat_label', kind=None)],
                                        values=[Constant(value='VAT', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='belgium', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='fr_FR', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='vat_label', kind=None)],
                                        values=[Constant(value='TVA', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='res.country,vat_label', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='belgium', ctx=Load()),
                                                        attr='id',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='translations', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='Translations are not created', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='belgium', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='fr_FR', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='vat_label', kind=None)],
                                        values=[Name(id='empty_value', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='belgium', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Constant(value='fr_FR', kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='vat_label',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Value was not reset', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='belgium', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Constant(value='en_US', kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='vat_label',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Value was not reset in other languages', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='belgium', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Constant(value=None, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='vat_label',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Value was not reset on the field model', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='res.country,vat_label', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='belgium', ctx=Load()),
                                                        attr='id',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='translations', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='Translations were not removed', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='belgium', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='fr_FR', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='vat_label', kind=None)],
                                        values=[Constant(value='TVA', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='belgium', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='en_US', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='vat_label', kind=None)],
                                        values=[Constant(value='VAT', kind=None)],
                                    ),
                                ],
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
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='translate_fields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='res.country', kind=None),
                                    Attribute(
                                        value=Name(id='belgium', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='vat_label', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='en_translation', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='res.country,vat_label', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='belgium', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='lang', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='en_US', kind=None),
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
                                    value=Name(id='en_translation', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Constant(value='', kind=None)],
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
                                    Constant(value='TVA', kind=None),
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='belgium', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Constant(value='fr_FR', kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='vat_label',
                                        ctx=Load(),
                                    ),
                                    Constant(value='French translation was not kept', kind=None),
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
                                    Constant(value='VAT', kind=None),
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='belgium', ctx=Load()),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='lang',
                                                    value=Constant(value='en_US', kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='vat_label',
                                        ctx=Load(),
                                    ),
                                    Constant(value='Did not fallback to source when reset', kind=None),
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
                    name='test_field_selection',
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
                            value=Constant(value=' Test translations of field selections. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_fields',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='state', kind=None),
                                ctx=Load(),
                            ),
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
                                    ListComp(
                                        elt=Name(id='key', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='key', ctx=Store()),
                                                        Name(id='_', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='selection',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='manual', kind=None),
                                            Constant(value='base', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ir_field', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.model', kind=None),
                                    Constant(value='state', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ir_field', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ir_field', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='lang',
                                        value=Constant(value='fr_FR', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='ir_field', ctx=Load()),
                                            attr='selection_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Custo', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='ir_field', ctx=Load()),
                                            attr='selection_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Pas touche!', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='fg', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='fields_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='state', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='fg', ctx=Load()),
                                            slice=Constant(value='state', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='selection', kind=None),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='selection',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='fg', ctx=Store())],
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
                                                slice=Constant(value='ir.model', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Constant(value='fr_FR', kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='fields_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='state', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='fg', ctx=Load()),
                                            slice=Constant(value='state', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='selection', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='manual', kind=None),
                                                    Constant(value='Custo', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='base', kind=None),
                                                    Constant(value='Pas touche!', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
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
                    name='test_fields_view_get',
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
                            value=Constant(value=' Test translations of field descriptions in fields_view_get(). ', kind=None),
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
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='fr_FR', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ir_model_field', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='ir.model', kind=None),
                                    Constant(value='name', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='LABEL', ctx=Store())],
                            value=Constant(value='Description du Modèle', kind=None),
                            type_comment=None,
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
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='type', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='lang', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='src', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='model', kind=None),
                                            Constant(value='ir.model.fields,field_description', kind=None),
                                            Constant(value='fr_FR', kind=None),
                                            Attribute(
                                                value=Name(id='ir_model_field', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='Name', kind=None),
                                            Name(id='LABEL', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='lang',
                                        value=Constant(value='fr_FR', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='info', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model', ctx=Load()),
                                    attr='fields_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='name', kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='info', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='string', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='LABEL', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='info', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='model', ctx=Load()),
                                        attr='fields_view_get',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value='fields', kind=None),
                                ctx=Load(),
                            ),
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
                                        value=Subscript(
                                            value=Name(id='info', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='string', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='LABEL', ctx=Load()),
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
            name='TestXMLTranslation',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
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
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='fr_FR', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.lang', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_activate_lang',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='nl_NL', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.module_base', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_update_translations',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='fr_FR', kind=None),
                                            Constant(value='nl_NL', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
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
                    name='create_view',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='archf', annotation=None, type_comment=None),
                            arg(arg='terms', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='view', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='res.partner', kind=None),
                                            BinOp(
                                                left=Name(id='archf', ctx=Load()),
                                                op=Mod(),
                                                right=Name(id='terms', ctx=Load()),
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
                                    value=Name(id='view', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='lang', ctx=Store()),
                                    Name(id='trans_terms', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='src', ctx=Store()),
                                            Name(id='val', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='zip', ctx=Load()),
                                        args=[
                                            Name(id='terms', ctx=Load()),
                                            Name(id='trans_terms', ctx=Load()),
                                        ],
                                        keywords=[],
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
                                                        slice=Constant(value='ir.translation', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='lang', kind=None),
                                                            Constant(value='res_id', kind=None),
                                                            Constant(value='src', kind=None),
                                                            Constant(value='value', kind=None),
                                                            Constant(value='state', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='model_terms', kind=None),
                                                            Constant(value='ir.ui.view,arch_db', kind=None),
                                                            Name(id='lang', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='view', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='src', ctx=Load()),
                                                            Name(id='val', ctx=Load()),
                                                            Constant(value='translated', kind=None),
                                                        ],
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
                            value=Name(id='view', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_copy',
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
                            value=Constant(value=' Create a simple view, fill in translations, and copy it. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='archf', ctx=Store())],
                            value=Constant(value='<form string="%s"><div>%s</div><div>%s</div></form>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='terms_en', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value='Knife', kind=None),
                                    Constant(value='Fork', kind=None),
                                    Constant(value='Spoon', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='terms_fr', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value='Couteau', kind=None),
                                    Constant(value='Fourchette', kind=None),
                                    Constant(value='Cuiller', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view0', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_view',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='archf', ctx=Load()),
                                    Name(id='terms_en', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='fr_FR',
                                        value=Name(id='terms_fr', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='env_en', ctx=Store())],
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
                                        value=Dict(keys=[], values=[]),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='env_fr', ctx=Store())],
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
                                            keys=[Constant(value='lang', kind=None)],
                                            values=[Constant(value='fr_FR', kind=None)],
                                        ),
                                    ),
                                ],
                            ),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view0', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_en', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_en', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view0', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_fr', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_fr', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='view0', ctx=Load()),
                                            attr='with_env',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='env_en', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view1', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_en', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_en', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view1', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_fr', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_fr', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='view2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='view0', ctx=Load()),
                                            attr='with_env',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='env_fr', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view2', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_en', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_en', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view2', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_fr', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_fr', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='patch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Name(id='type', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='ir.ui.view', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    Constant(value='translate', kind=None),
                                    Name(id='html_translate', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='view3', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='view0', ctx=Load()),
                                            attr='with_env',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='env_fr', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view3', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_en', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_en', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view3', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_fr', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_fr', ctx=Load()),
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
                    name='test_spaces',
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
                            value=Constant(value=' Create translations where value has surrounding spaces. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='archf', ctx=Store())],
                            value=Constant(value='<form string="%s"><div>%s</div><div>%s</div></form>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='terms_en', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value='Knife', kind=None),
                                    Constant(value='Fork', kind=None),
                                    Constant(value='Spoon', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='terms_fr', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value=' Couteau', kind=None),
                                    Constant(value='Fourchette ', kind=None),
                                    Constant(value=' Cuiller ', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_view',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='archf', ctx=Load()),
                                    Name(id='terms_en', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='fr_FR',
                                        value=Name(id='terms_fr', ctx=Load()),
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
                    name='test_sync',
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
                            value=Constant(value=' Check translations after minor change in source terms. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='archf', ctx=Store())],
                            value=Constant(value='<form string="X">%s</form>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='terms_en', ctx=Store())],
                            value=Tuple(
                                elts=[Constant(value='Bread and cheeze', kind=None)],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='terms_fr', ctx=Store())],
                            value=Tuple(
                                elts=[Constant(value='Pain et fromage', kind=None)],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='terms_nl', ctx=Store())],
                            value=Tuple(
                                elts=[Constant(value='Brood and kaas', kind=None)],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_view',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='archf', ctx=Load()),
                                    Name(id='terms_en', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='en_US',
                                        value=Name(id='terms_en', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='fr_FR',
                                        value=Name(id='terms_fr', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='nl_NL',
                                        value=Name(id='terms_nl', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='env_nolang', ctx=Store())],
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
                                        value=Dict(keys=[], values=[]),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='env_en', ctx=Store())],
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
                                            keys=[Constant(value='lang', kind=None)],
                                            values=[Constant(value='en_US', kind=None)],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='env_fr', ctx=Store())],
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
                                            keys=[Constant(value='lang', kind=None)],
                                            values=[Constant(value='fr_FR', kind=None)],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='env_nl', ctx=Store())],
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
                                            keys=[Constant(value='lang', kind=None)],
                                            values=[Constant(value='nl_NL', kind=None)],
                                        ),
                                    ),
                                ],
                            ),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_nolang', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_en', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_en', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_en', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_fr', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_fr', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_nl', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_nl', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='terms_en', ctx=Store())],
                            value=Tuple(
                                elts=[Constant(value='Bread and cheese', kind=None)],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='view', ctx=Load()),
                                            attr='with_env',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='env_en', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='arch_db', kind=None)],
                                        values=[
                                            BinOp(
                                                left=Name(id='archf', ctx=Load()),
                                                op=Mod(),
                                                right=Name(id='terms_en', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_nolang', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_en', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_en', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_en', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_fr', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_fr', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_nl', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_nl', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='view', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_view',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='archf', ctx=Load()),
                                    Name(id='terms_fr', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='en_US',
                                        value=Name(id='terms_en', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='fr_FR',
                                        value=Name(id='terms_fr', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='nl_NL',
                                        value=Name(id='terms_nl', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_terms_fr', ctx=Store())],
                            value=Tuple(
                                elts=[Constant(value='Pains et fromage', kind=None)],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='view', ctx=Load()),
                                            attr='with_env',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='env_fr', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='arch_db', kind=None)],
                                        values=[
                                            BinOp(
                                                left=Name(id='archf', ctx=Load()),
                                                op=Mod(),
                                                right=Name(id='new_terms_fr', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_nolang', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='new_terms_fr', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_en', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_en', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_fr', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='new_terms_fr', ctx=Load()),
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
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='with_env',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='env_nl', ctx=Load())],
                                            keywords=[],
                                        ),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Name(id='archf', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='terms_nl', ctx=Load()),
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
                    name='test_sync_update',
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
                            value=Constant(value=' Check translations after major changes in source terms. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='archf', ctx=Store())],
                            value=Constant(value='<form string="X"><div>%s</div><div>%s</div></form>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='terms_src', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value='Subtotal', kind=None),
                                    Constant(value='Subtotal:', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='terms_en', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Constant(value='', kind=None),
                                    Constant(value='Sub total:', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_view',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='archf', ctx=Load()),
                                    Name(id='terms_src', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='en_US',
                                        value=Name(id='terms_en', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='translations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='model_terms', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='ir.ui.view,arch_db', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='view', ctx=Load()),
                                                        attr='id',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='translations', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='new_arch', ctx=Store())],
                            value=BinOp(
                                left=Name(id='archf', ctx=Load()),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Constant(value='Subtotal', kind=None),
                                        Constant(value='Subtotal:<br/>', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='view', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='arch_db', kind=None)],
                                        values=[Name(id='new_arch', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='translations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.translation', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='type', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='model_terms', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='ir.ui.view,arch_db', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='view', ctx=Load()),
                                                        attr='id',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='translations', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
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
                    name='test_cache_consistency',
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
                            targets=[Name(id='view', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test_translate_xml_cache_invalidation', kind=None),
                                            Constant(value='res.partner', kind=None),
                                            Constant(value='<form><b>content</b></form>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view_fr', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='view', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='lang', kind=None)],
                                        values=[Constant(value='fr_FR', kind=None)],
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
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<b>', kind=None),
                                    Attribute(
                                        value=Name(id='view', ctx=Load()),
                                        attr='arch_db',
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
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<b>', kind=None),
                                    Attribute(
                                        value=Name(id='view_fr', ctx=Load()),
                                        attr='arch_db',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='view', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='arch_db', kind=None)],
                                        values=[Constant(value='<form><i>content</i></form>', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<i>', kind=None),
                                    Attribute(
                                        value=Name(id='view', ctx=Load()),
                                        attr='arch_db',
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
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<i>', kind=None),
                                    Attribute(
                                        value=Name(id='view_fr', ctx=Load()),
                                        attr='arch_db',
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
    ],
    type_ignores=[],
)
