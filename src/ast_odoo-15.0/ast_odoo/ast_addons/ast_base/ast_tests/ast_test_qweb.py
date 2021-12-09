Module(
    body=[
        Import(
            names=[alias(name='collections', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='os.path', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='markupsafe', asname=None)],
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
            module='odoo.modules',
            names=[alias(name='get_module_resource', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.qweb',
            names=[alias(name='QWebException', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='misc', asname=None),
                alias(name='mute_logger', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.json',
            names=[alias(name='scriptsafe', asname='json_scriptsafe')],
            level=0,
        ),
        Assign(
            targets=[Name(id='unsafe_eval', ctx=Store())],
            value=Name(id='eval', ctx=Load()),
            type_comment=None,
        ),
        ClassDef(
            name='TestQWebTField',
            bases=[Name(id='TransactionCase', ctx=Load())],
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
                                            Name(id='TestQWebTField', ctx=Load()),
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
                                    attr='env_branding',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='engine',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env_branding',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.qweb', kind=None),
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
                    name='test_trivial',
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
                            targets=[Name(id='field', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='span', kind=None),
                                    Dict(
                                        keys=[Constant(value='t-field', kind=None)],
                                        values=[Constant(value='company.name', kind='u')],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='My Test Company', kind=None)],
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='engine',
                                        ctx=Load(),
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='field', ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='company', kind=None)],
                                        values=[Name(id='company', ctx=Load())],
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='result', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='<span data-oe-model="res.company" data-oe-id="%d" data-oe-field="name" data-oe-type="char" data-oe-expression="company.name">%s</span>', kind='u'),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='company', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value='My Test Company', kind='u'),
                                                    ],
                                                    ctx=Load(),
                                                ),
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
                    name='test_i18n',
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
                            targets=[Name(id='field', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='span', kind=None),
                                    Dict(
                                        keys=[Constant(value='t-field', kind=None)],
                                        values=[Constant(value='company.name', kind='u')],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='s', ctx=Store())],
                            value=Constant(value='Testing «ταБЬℓσ»: 1<2 & 4+1>3, now 20% off!', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.company', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Name(id='s', ctx=Load())],
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='engine',
                                        ctx=Load(),
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='field', ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='company', kind=None)],
                                        values=[Name(id='company', ctx=Load())],
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='result', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='<span data-oe-model="res.company" data-oe-id="%d" data-oe-field="name" data-oe-type="char" data-oe-expression="company.name">%s</span>', kind='u'),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='company', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='misc', ctx=Load()),
                                                                attr='html_escape',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='s', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
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
                    name='test_reject_crummy_tags',
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
                            targets=[Name(id='field', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='td', kind=None),
                                    Dict(
                                        keys=[Constant(value='t-field', kind=None)],
                                        values=[Constant(value='company.name', kind='u')],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaisesRegex',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='QWebException', ctx=Load()),
                                            Constant(value='^RTE widgets do not work correctly', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='engine',
                                                ctx=Load(),
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field', ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='company', kind=None)],
                                                values=[Constant(value=None, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_reject_t_tag',
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
                            targets=[Name(id='field', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='Element',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='t', kind=None),
                                    Dict(
                                        keys=[Constant(value='t-field', kind=None)],
                                        values=[Constant(value='company.name', kind='u')],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaisesRegex',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='QWebException', ctx=Load()),
                                            Constant(value='^t-field can not be used on a t element', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='engine',
                                                ctx=Load(),
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field', ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='company', kind=None)],
                                                values=[Constant(value=None, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_render_t_options',
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
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy"><root><span t-esc="5" t-options="{\'widget\': \'char\'}" t-options-widget="\'float\'" t-options-precision="4"/></root></t>\n            ', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='text', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='etree', ctx=Load()),
                                                attr='fromstring',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='view1', ctx=Load()),
                                                        attr='_render',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='find',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='span', kind=None)],
                                    keywords=[],
                                ),
                                attr='text',
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
                                    Name(id='text', ctx=Load()),
                                    Constant(value='5.0000', kind='u'),
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
                    name='test_xss_breakout',
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy">\n                    <root>\n                        <script type="application/javascript">\n                            var s = <t t-esc="json.dumps({\'key\': malicious})"/>;\n                        </script>\n                    </root>\n                </t>\n            ', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendered', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='view', ctx=Load()),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='malicious', kind=None)],
                                        values=[Constant(value='1</script><script>alert("pwned")</script><script>', kind=None)],
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
                                    Constant(value='alert', kind=None),
                                    Name(id='rendered', ctx=Load()),
                                    BinOp(
                                        left=Constant(value="%r doesn't seem to be rendered", kind=None),
                                        op=Mod(),
                                        right=Name(id='rendered', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='doc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rendered', ctx=Load())],
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
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='doc', ctx=Load()),
                                                    attr='xpath',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='//script', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
            decorator_list=[],
        ),
        ClassDef(
            name='TestQWebNS',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_render_static_xml_with_namespace',
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
                            value=Constant(value=' Test the rendering on a namespaced view with no static content. The resulting string should be untouched.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='\n            <root>\n                <h:table xmlns:h="http://www.example.org/table">\n                    <h:tr>\n                        <h:td xmlns:h="http://www.w3.org/TD/html4/">Apples</h:td>\n                        <h:td>Bananas</h:td>\n                    </h:tr>\n                </h:table>\n                <f:table xmlns:f="http://www.example.org/furniture">\n                    <f:width>80</f:width>\n                </f:table>\n            </root>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            BinOp(
                                                left=Constant(value='\n                <t t-name="base.dummy">%s</t>\n            ', kind=None),
                                                op=Mod(),
                                                right=Name(id='expected_result', ctx=Load()),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='view1', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='expected_result', ctx=Load())],
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
                    name='test_render_static_xml_with_namespace_2',
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
                            value=Constant(value=' Test the rendering on a namespaced view with no static content. The resulting string should be untouched.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='\n            <html xmlns="http://www.w3.org/HTML/1998/html4" xmlns:xdc="http://www.xml.com/books">\n                <head>\n                    <title>Book Review</title>\n                </head>\n                <body>\n                    <xdc:bookreview>\n                        <xdc:title>XML: A Primer</xdc:title>\n                        <table>\n                            <tr align="center">\n                                <td>Author</td><td>Price</td>\n                                <td>Pages</td><td>Date</td>\n                            </tr>\n                            <tr align="left">\n                                <td><xdc:author>Simon St. Laurent</xdc:author></td>\n                                <td><xdc:price>31.98</xdc:price></td>\n                                <td><xdc:pages>352</xdc:pages></td>\n                                <td><xdc:date>1998/01</xdc:date></td>\n                            </tr>\n                        </table>\n                    </xdc:bookreview>\n                </body>\n            </html>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            BinOp(
                                                left=Constant(value='\n                <t t-name="base.dummy">%s</t>\n            ', kind=None),
                                                op=Mod(),
                                                right=Name(id='expected_result', ctx=Load()),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='view1', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='expected_result', ctx=Load())],
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
                    name='test_render_static_xml_with_useless_distributed_namespace',
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
                            value=Constant(value=' Test that redundant namespaces are stripped upon rendering.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy">\n                    <root>\n                        <h:table xmlns:h="http://www.example.org/table">\n                            <h:tr xmlns:h="http://www.example.org/table">\n                                <h:td xmlns:h="http://www.w3.org/TD/html4/">Apples</h:td>\n                                <h:td xmlns:h="http://www.example.org/table">Bananas</h:td>\n                            </h:tr>\n                        </h:table>\n                    </root>\n                </t>\n            ', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n            <root>\n                <h:table xmlns:h="http://www.example.org/table">\n                    <h:tr>\n                        <h:td xmlns:h="http://www.w3.org/TD/html4/">Apples</h:td>\n                        <h:td>Bananas</h:td>\n                    </h:tr>\n                </h:table>\n            </root>\n        ', kind='u')],
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='view1', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_render_static_xml_with_namespace_3',
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
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='\n            <cfdi:Comprobante xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd"></cfdi:Comprobante>\n        ', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            BinOp(
                                                left=Constant(value='\n                <t t-name="base.dummy">%s</t>\n            ', kind='u'),
                                                op=Mod(),
                                                right=Name(id='expected_result', ctx=Load()),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='view1', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='expected_result', ctx=Load())],
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
                    name='test_render_static_xml_with_namespace_dynamic',
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
                            value=Constant(value=' Test the rendering on a namespaced view with dynamic URI (need default namespace uri).\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tempate', ctx=Store())],
                            value=Constant(value='\n            <root xmlns:h="https://default.namespace.url/h">\n                <h:table t-att="{\'xmlns:h\': h1}">\n                    <h:tr>\n                        <h:td t-att="{\'xmlns:h\': h2}">Apples</h:td>\n                        <h:td>Bananas</h:td>\n                    </h:tr>\n                </h:table>\n            </root>\n        ', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='\n            <root xmlns:h="https://default.namespace.url/h">\n                <h:table xmlns:h="%(h1)s">\n                    <h:tr>\n                        <h:td xmlns:h="%(h2)s">Apples</h:td>\n                        <h:td>Bananas</h:td>\n                    </h:tr>\n                </h:table>\n            </root>\n        ', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='h1',
                                        value=Constant(value='http://www.example.org/table', kind=None),
                                    ),
                                    keyword(
                                        arg='h2',
                                        value=Constant(value='http://www.w3.org/TD/html4/', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            BinOp(
                                                left=Constant(value='\n                <t t-name="base.dummy">%s</t>\n            ', kind='u'),
                                                op=Mod(),
                                                right=Name(id='tempate', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendering', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='view1', ctx=Load()),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='engine',
                                        value=Constant(value='ir.qweb', kind=None),
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rendering', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='expected_result', ctx=Load()),
                                                op=Mod(),
                                                right=Name(id='values', ctx=Load()),
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
                    name='test_render_static_xml_with_namespace_dynamic_2',
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
                            value=Constant(value=' Test the rendering on a namespaced view with dynamic URI (need default namespace uri).\n        Default URIs must be differents.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='tempate', ctx=Store())],
                            value=Constant(value='\n            <root xmlns:f="https://default.namespace.url/f" xmlns:h="https://default.namespace.url/h" >\n                <h:table t-att="{\'xmlns:h\': h1}">\n                    <h:tr>\n                        <h:td t-att="{\'xmlns:h\': h2}">Apples</h:td>\n                        <h:td>Bananas</h:td>\n                    </h:tr>\n                </h:table>\n                <f:table t-att="{\'xmlns:f\': f}">\n                    <f:width>80</f:width>\n                </f:table>\n            </root>\n        ', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Constant(value='\n            <root xmlns:f="https://default.namespace.url/f" xmlns:h="https://default.namespace.url/h">\n                <h:table xmlns:h="%(h1)s">\n                    <h:tr>\n                        <h:td xmlns:h="%(h2)s">Apples</h:td>\n                        <h:td>Bananas</h:td>\n                    </h:tr>\n                </h:table>\n                <f:table xmlns:f="%(f)s">\n                    <f:width>80</f:width>\n                </f:table>\n            </root>\n        ', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='h1',
                                        value=Constant(value='http://www.example.org/table', kind=None),
                                    ),
                                    keyword(
                                        arg='h2',
                                        value=Constant(value='http://www.w3.org/TD/html4/', kind=None),
                                    ),
                                    keyword(
                                        arg='f',
                                        value=Constant(value='http://www.example.org/furniture', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            BinOp(
                                                left=Constant(value='\n                <t t-name="base.dummy">%s</t>\n            ', kind='u'),
                                                op=Mod(),
                                                right=Name(id='tempate', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendering', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='view1', ctx=Load()),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='engine',
                                        value=Constant(value='ir.qweb', kind=None),
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rendering', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='expected_result', ctx=Load()),
                                                op=Mod(),
                                                right=Name(id='values', ctx=Load()),
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
                    name='test_render_dynamic_xml_with_namespace_t_esc',
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
                            value=Constant(value=' Test that rendering a template containing a node having both an ns declaration and a t-esc attribute correctly\n        handles the t-esc attribute and keep the ns declaration.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy">\n                    <Invoice xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" t-esc="\'test\'"/>\n                </t>\n            ', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='<Invoice xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2">test</Invoice>', kind='u')],
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='view1', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_render_dynamic_xml_with_namespace_t_esc_with_useless_distributed_namespace',
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
                            value=Constant(value=' Test that rendering a template containing a node having both an ns declaration and a t-esc attribute correctly\n        handles the t-esc attribute and keep the ns declaration, and distribute correctly the ns declaration to its children.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy">\n                    <Invoice xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" t-attf-test="test">\n                        <cac:Test xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2">blabla</cac:Test>\n                    </Invoice>\n                </t>\n            ', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n            <Invoice xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" test="test">\n                <cac:Test>blabla</cac:Test>\n            </Invoice>\n        ', kind='u')],
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='view1', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_render_dynamic_xml_with_namespace_t_attf',
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
                            value=Constant(value=' Test that rendering a template containing a node having both an ns declaration and a t-attf attribute correctly\n        handles the t-attf attribute and keep the ns declaration.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy">\n                    <root>\n                        <h:table xmlns:h="http://www.example.org/table">\n                            <h:tr>\n                                <h:td xmlns:h="http://www.w3.org/TD/html4/">Apples</h:td>\n                                <h:td>Bananas</h:td>\n                            </h:tr>\n                        </h:table>\n                        <f:table xmlns:f="http://www.example.org/furniture">\n                            <f:width t-attf-test="1">80</f:width>\n                        </f:table>\n                    </root>\n                </t>\n            ', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n            <root>\n                <h:table xmlns:h="http://www.example.org/table">\n                    <h:tr>\n                        <h:td xmlns:h="http://www.w3.org/TD/html4/">Apples</h:td>\n                        <h:td>Bananas</h:td>\n                    </h:tr>\n                </h:table>\n                <f:table xmlns:f="http://www.example.org/furniture">\n                    <f:width test="1">80</f:width>\n                </f:table>\n            </root>\n        ', kind='u')],
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='view1', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_render_dynamic_xml_with_namespace_t_attf_with_useless_distributed_namespace',
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
                            value=Constant(value=' Test that rendering a template containing a node having both an ns declaration and a t-attf attribute correctly\n        handles the t-attf attribute and that redundant namespaces are stripped upon rendering.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy">\n                <root>\n                    <h:table xmlns:h="http://www.example.org/table">\n                        <h:tr>\n                            <h:td xmlns:h="http://www.w3.org/TD/html4/">Apples</h:td>\n                            <h:td>Bananas</h:td>\n                        </h:tr>\n                    </h:table>\n                    <f:table xmlns:f="http://www.example.org/furniture">\n                        <f:width xmlns:f="http://www.example.org/furniture" t-attf-test="1">80</f:width>\n                    </f:table>\n                </root>\n\n                </t>\n            ', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n                <root>\n                    <h:table xmlns:h="http://www.example.org/table">\n                        <h:tr>\n                            <h:td xmlns:h="http://www.w3.org/TD/html4/">Apples</h:td>\n                            <h:td>Bananas</h:td>\n                        </h:tr>\n                    </h:table>\n                    <f:table xmlns:f="http://www.example.org/furniture">\n                        <f:width test="1">80</f:width>\n                    </f:table>\n                </root>\n\n        ', kind='u')],
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='view1', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_render_dynamic_xml_with_namespace_2',
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
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy">\n                    <Invoice xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">\n                        <cbc:UBLVersionID t-esc="version_id"/>\n                        <t t-foreach="[1, 2, 3, 4]" t-as="value">\n                            Oasis <cac:Test t-esc="value"/>\n                        </t>\n                    </Invoice>\n                </t>\n            ', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n            <Invoice xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2">\n                <cbc:UBLVersionID>1.0</cbc:UBLVersionID>\n\n                    Oasis <cac:Test>1</cac:Test>\n\n                    Oasis <cac:Test>2</cac:Test>\n\n                    Oasis <cac:Test>3</cac:Test>\n\n                    Oasis <cac:Test>4</cac:Test>\n\n            </Invoice>\n        ', kind='u')],
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='view1', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='version_id', kind=None)],
                                                        values=[Constant(value=1.0, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_render_static_xml_with_namespaced_attributes',
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
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy">\n                    <cfdi:Comprobante xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd">abc</cfdi:Comprobante>\n                </t>\n            ', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='<cfdi:Comprobante xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd">abc</cfdi:Comprobante>', kind='u')],
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='view1', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_render_dynamic_xml_with_namespaced_attributes',
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
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy">\n                    <cfdi:Comprobante xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd" t-esc="\'abc\'"/>\n                </t>\n            ', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='<cfdi:Comprobante xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd">abc</cfdi:Comprobante>', kind=None)],
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='view1', ctx=Load()),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_render_static_xml_with_t_call',
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
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy">\n                    <cac:fruit xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"\n                               xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">\n                        <cac:table>\n                            <cbc:td>Appel</cbc:td>\n                            <cbc:td>Pineappel</cbc:td>\n                        </cac:table>\n                    </cac:fruit>\n                </t>\n            ', kind='u'),
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="INSERT INTO ir_model_data(name, model, res_id, module)VALUES ('dummy', 'ir.ui.view', %s, 'base')", kind=None),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='view1', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='view2', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy2', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy2">\n                    <root xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2" xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2">\n                        <cac:line t-foreach="[1, 2]" t-as="i" t-call="base.dummy"/>\n                    </root>\n                </t>\n            ', kind='u'),
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
                                    value=Name(id='view2', ctx=Load()),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result_etree', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Name(id='result', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_ns', ctx=Store())],
                            value=Set(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=None, kind=None),
                                            Constant(value='urn:oasis:names:specification:ubl:schema:xsd:Invoice-2', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='cac', kind=None),
                                            Constant(value='urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='cbc', kind=None),
                                            Constant(value='urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2', kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='result_etree', ctx=Load()),
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
                                    Name(id='expected_ns', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='cac_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='result_etree', ctx=Load()),
                                    attr='findall',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='.//cac:line', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='namespaces',
                                        value=Dict(
                                            keys=[Constant(value='cac', kind=None)],
                                            values=[Constant(value='urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2', kind=None)],
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='cac_lines', ctx=Load())],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='count',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Appel', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='count',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"', kind=None)],
                                        keywords=[],
                                    ),
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
                FunctionDef(
                    name='test_render_static_xml_with_extension',
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
                            value=Constant(value=' Test the extension of a view by an xpath expression on a ns prefixed element.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy">\n                    <root>\n                        <h:table xmlns:h="http://www.example.org/table">\n                            <h:tr>\n                                <h:td xmlns:h="http://www.w3.org/TD/html4/">Apples</h:td>\n                                <h:td>Bananas</h:td>\n                            </h:tr>\n                        </h:table>\n                    </root>\n                </t>\n            ', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view2', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='inherit_id', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy_ext', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Attribute(
                                                value=Name(id='view1', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='\n                <xpath expr="//{http://www.example.org/table}table/{http://www.example.org/table}tr">\n                        <h:td xmlns:h="http://www.example.org/table">Oranges</h:td>\n                </xpath>\n            ', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='\n            <root>\n                <h:table xmlns:h="http://www.example.org/table">\n                    <h:tr>\n                        <h:td xmlns:h="http://www.w3.org/TD/html4/">Apples</h:td>\n                        <h:td>Bananas</h:td>\n                        <h:td>Oranges</h:td>\n                    </h:tr>\n                </h:table>\n            </root>\n        ', kind='u')],
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
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='view1', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='check_view_ids',
                                                                value=List(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Name(id='view1', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='view2', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='_render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='expected_result', ctx=Load()),
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
                    name='test_render_dynamic_xml_with_code_error',
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
                            value=Constant(value=' Test that, when rendering a template containing a namespaced node\n            that evaluates code with errors, the proper exception is raised\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy">\n                    <Invoice xmlns:od="http://odoo.com/od">\n                        <od:name t-att-test="\'a\' + 1"/>\n                    </Invoice>\n                </t>\n            ', kind='u'),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=BinOp(
                                        left=Constant(value='', kind=None),
                                        op=Add(),
                                        right=Constant(value=0, kind=None),
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='TypeError', ctx=Load()),
                                    name='e',
                                    body=[
                                        Assign(
                                            targets=[Name(id='error_msg', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='args',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='QWebException', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Name(id='error_msg', ctx=Load()),
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
                                            value=Name(id='view1', ctx=Load()),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_render_t_call_propagates_t_lang',
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
                            targets=[Name(id='current_lang', ctx=Store())],
                            value=Constant(value='en_US', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='other_lang', ctx=Store())],
                            value=Constant(value='fr_FR', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
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
                                args=[Name(id='other_lang', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='lang', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='decimal_point', kind=None),
                                            Constant(value='thousands_sep', kind=None),
                                        ],
                                        values=[
                                            Constant(value='*', kind=None),
                                            Constant(value='/', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='callee', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.callee">\n                    <t t-esc="9000000.00" t-options="{\'widget\': \'float\', \'precision\': 2}" />\n                </t>\n            ', kind='u'),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
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
                                            Constant(value='module', kind=None),
                                            Constant(value='res_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='callee', kind=None),
                                            Constant(value='ir.ui.view', kind=None),
                                            Constant(value='base', kind=None),
                                            Attribute(
                                                value=Name(id='view1', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='view2', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='calling', kind=None),
                                            Constant(value='qweb', kind=None),
                                            BinOp(
                                                left=Constant(value='\n                <t t-name="base.calling">\n                    <t t-call="base.callee" t-lang="\'%s\'" />\n                </t>\n            ', kind='u'),
                                                op=Mod(),
                                                right=Name(id='other_lang', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendered', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='view2', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='lang',
                                                        value=Name(id='current_lang', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='rendered', ctx=Load()),
                                    Constant(value='9/000/000*00', kind=None),
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
                    name='test_render_barcode',
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
                            targets=[Name(id='partner', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='barcode', kind=None),
                                        ],
                                        values=[
                                            Constant(value='bacode_test', kind=None),
                                            Constant(value='test', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
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
                                            Constant(value='type', kind=None),
                                        ],
                                        values=[
                                            Constant(value='a_barcode_view', kind=None),
                                            Constant(value='qweb', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='view', ctx=Load()),
                                    attr='arch',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='<div t-field="partner.barcode" t-options="{\'widget\': \'barcode\', \'width\': 100, \'height\': 30}"/>', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendered', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='view', ctx=Load()),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='values',
                                                value=Dict(
                                                    keys=[Constant(value='partner', kind=None)],
                                                    values=[Name(id='partner', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='strip',
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
                                    attr='assertRegex',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='rendered', ctx=Load()),
                                    Constant(value='<div><img alt="Barcode test" src="data:image/png;base64,\\S+"></div>', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='partner', ctx=Load()),
                                    attr='barcode',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='4012345678901', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='view', ctx=Load()),
                                    attr='arch',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='<div t-field="partner.barcode" t-options="{\'widget\': \'barcode\', \'symbology\': \'EAN13\', \'width\': 100, \'height\': 30, \'img_style\': \'width:100%;\', \'img_alt\': \'Barcode\'}"/>', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ean_rendered', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='view', ctx=Load()),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='values',
                                                value=Dict(
                                                    keys=[Constant(value='partner', kind=None)],
                                                    values=[Name(id='partner', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='strip',
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
                                    attr='assertRegex',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='ean_rendered', ctx=Load()),
                                    Constant(value='<div><img style="width:100%;" alt="Barcode" src="data:image/png;base64,\\S+"></div>', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='view', ctx=Load()),
                                    attr='arch',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='<div t-field="partner.barcode" t-options="{\'widget\': \'barcode\', \'symbology\': \'auto\', \'width\': 100, \'height\': 30, \'img_style\': \'width:100%;\', \'img_alt\': \'Barcode\'}"/>', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='auto_rendered', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='view', ctx=Load()),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='values',
                                                value=Dict(
                                                    keys=[Constant(value='partner', kind=None)],
                                                    values=[Name(id='partner', ctx=Load())],
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='strip',
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
                                    attr='assertRegex',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='auto_rendered', ctx=Load()),
                                    Constant(value='<div><img style="width:100%;" alt="Barcode" src="data:image/png;base64,\\S+"></div>', kind=None),
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
            name='TestQWebBasic',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_compile_expr',
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
                            targets=[Name(id='tests', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='1 +2+ 3', kind=None),
                                            Dict(keys=[], values=[]),
                                            Constant(value=6, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='(((1 +2+ 3)))', kind=None),
                                            Dict(keys=[], values=[]),
                                            Constant(value=6, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='(1) +(2+ (3))', kind=None),
                                            Dict(keys=[], values=[]),
                                            Constant(value=6, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='a == 5', kind=None),
                                            Dict(
                                                keys=[Constant(value='a', kind=None)],
                                                values=[Constant(value=5, kind=None)],
                                            ),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value="{'a': True}", kind=None),
                                            Dict(keys=[], values=[]),
                                            Dict(
                                                keys=[Constant(value='a', kind=None)],
                                                values=[Constant(value=True, kind=None)],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='object.count(1)', kind=None),
                                            Dict(
                                                keys=[Constant(value='object', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Constant(value=1, kind=None),
                                                            Constant(value=2, kind=None),
                                                            Constant(value=1, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=3, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='dict(a=True)', kind=None),
                                            Dict(keys=[], values=[]),
                                            Dict(
                                                keys=[Constant(value='a', kind=None)],
                                                values=[Constant(value=True, kind=None)],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='fn(a=11, b=22) or a', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='fn', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[
                                                                arg(arg='a', annotation=None, type_comment=None),
                                                                arg(arg='b', annotation=None, type_comment=None),
                                                            ],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Constant(value=0, kind=None),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='fn(a=11, b=22) or a', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='fn', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[
                                                                arg(arg='a', annotation=None, type_comment=None),
                                                                arg(arg='b', annotation=None, type_comment=None),
                                                            ],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Name(id='b', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            Constant(value=22, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='(lambda a: a)(5)', kind=None),
                                            Dict(keys=[], values=[]),
                                            Constant(value=5, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='(lambda a: a[0])([5])', kind=None),
                                            Dict(keys=[], values=[]),
                                            Constant(value=5, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value="{'a': lambda a: a[0], 'b': 3}['a']([5])", kind=None),
                                            Dict(keys=[], values=[]),
                                            Constant(value=5, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='list(map(lambda a: a[0], r))', kind=None),
                                            Dict(
                                                keys=[Constant(value='r', kind=None)],
                                                values=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=1, kind=None),
                                                                    Constant(value=11, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=2, kind=None),
                                                                    Constant(value=22, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value="z + (head or 'z')", kind=None),
                                            Dict(
                                                keys=[Constant(value='z', kind=None)],
                                                values=[Constant(value='a', kind=None)],
                                            ),
                                            Constant(value='az', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value="z + (head or 'z')", kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='z', kind=None),
                                                    Constant(value='head', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='b', kind=None),
                                                ],
                                            ),
                                            Constant(value='ab', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='{a:b for a, b in [(1,11), (2, 22)]}', kind=None),
                                            Dict(keys=[], values=[]),
                                            Dict(
                                                keys=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                values=[
                                                    Constant(value=11, kind=None),
                                                    Constant(value=22, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='any({x == 2 for x in [1,2,3]})', kind=None),
                                            Dict(keys=[], values=[]),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='any({x == 5 for x in [1,2,3]})', kind=None),
                                            Dict(keys=[], values=[]),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value="{x:y for x,y in [('a', 11),('b', 22)]}", kind=None),
                                            Dict(keys=[], values=[]),
                                            Dict(
                                                keys=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='b', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=11, kind=None),
                                                    Constant(value=22, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='[(y,x) for x,y in [(1, 11),(2, 22)]]', kind=None),
                                            Dict(keys=[], values=[]),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=11, kind=None),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=22, kind=None),
                                                            Constant(value=2, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='(lambda a: a + 5)(a=x)', kind=None),
                                            Dict(
                                                keys=[Constant(value='x', kind=None)],
                                                values=[Constant(value=10, kind=None)],
                                            ),
                                            Constant(value=15, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sum(x for x in range(4)) + ((x))', kind=None),
                                            Dict(
                                                keys=[Constant(value='x', kind=None)],
                                                values=[Constant(value=10, kind=None)],
                                            ),
                                            Constant(value=16, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='IrQweb', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.qweb', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='expr', ctx=Store()),
                                    Name(id='q_values', ctx=Store()),
                                    Name(id='result', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='tests', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='expr_namespace', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrQweb', ctx=Load()),
                                            attr='_compile_expr',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='expr', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='compiled', ctx=Store())],
                                    value=Call(
                                        func=Name(id='compile', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Constant(value="def test(values):\n  values['result'] = %s", kind=None),
                                                op=Mod(),
                                                right=Name(id='expr_namespace', ctx=Load()),
                                            ),
                                            Constant(value='<test>', kind=None),
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
                                            value=Name(id='IrQweb', ctx=Load()),
                                            attr='_prepare_globals',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(keys=[], values=[]),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='unsafe_eval', ctx=Load()),
                                        args=[
                                            Name(id='compiled', ctx=Load()),
                                            Name(id='globals_dict', ctx=Load()),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='test', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='test', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='test', ctx=Load()),
                                        args=[Name(id='q_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='q_result', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='q_values', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='result',
                                                value=Name(id='result', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertDictEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='q_values', ctx=Load()),
                                            Name(id='q_result', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='Should compile: %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='expr', ctx=Load()),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_compile_expr_security',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-escaping">\n                <div>\n                    <t t-set="o" t-value="(lambda a=open: a)()"/>\n                    <t t-out="o(\'/etc/passwd\').read()"/>\n                </div>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='other', kind=None)],
                                values=[Constant(value='any value', kind=None)],
                            ),
                            type_comment=None,
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
                                        args=[Name(id='Exception', ctx=Load())],
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
                                                slice=Constant(value='ir.qweb', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_foreach_iter_list',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="iter-list">\n                <t t-foreach="[3, 2, 1]" t-as="item">\n                    [<t t-esc="item_index"/>: <t t-esc="item"/> <t t-esc="item_value"/>]</t>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                    [0: 3 3]\n                    [1: 2 2]\n                    [2: 1 1]\n        ', kind='u'),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_foreach_iter_dict',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="iter-dict">\n                <t t-foreach="{\'a\': 3, \'b\': 2, \'c\': 1}" t-as="item">\n                    [<t t-esc="item_index"/>: <t t-esc="item"/> <t t-esc="item_value"/>]</t>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                    [0: a 3]\n                    [1: b 2]\n                    [2: c 1]\n        ', kind='u'),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_att_escaping_1',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-escaping">\n                <div t-att-bibi="json.dumps(bibi)">1</div>\n                <div t-att-toto="toto">2</div>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div bibi="{&#34;a&#34;: &#34;string&#34;, &#34;b&#34;: 1}">1</div>\n                <div toto="a&#39;b&#34;c">2</div>\n            ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='json', kind=None),
                                    Constant(value='bibi', kind=None),
                                    Constant(value='toto', kind=None),
                                ],
                                values=[
                                    Name(id='json_scriptsafe', ctx=Load()),
                                    Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='a',
                                                value=Constant(value='string', kind=None),
                                            ),
                                            keyword(
                                                arg='b',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='a\'b"c', kind=None),
                                ],
                            ),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_att_escaping_2',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-escaping">\n                <t t-set="abc"> <t t-if="add_abc"><t t-out="add_abc"/> <span a="b"> | </span></t><t t-out="efg"/> </t>\n                <div t-att-abc="abc">123</div>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div abc=" &amp;#34;yes&amp;#34; &lt;span a=&#34;b&#34;&gt; | &lt;/span&gt;-efg- ">123</div>\n            ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='add_abc', kind=None),
                                    Constant(value='efg', kind=None),
                                ],
                                values=[
                                    Constant(value='"yes"', kind=None),
                                    Constant(value='-efg-', kind=None),
                                ],
                            ),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_attf_escaping_1',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-escaping">\n                <div t-attf-bibi="a, b &gt; c &gt; #{d}">1</div>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div bibi="a, b &gt; c &gt; a&#39; &gt; b&#34;c">1</div>\n            ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='d', kind=None)],
                                values=[Constant(value='a\' > b"c', kind=None)],
                            ),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_attf_escaping_2',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-escaping">\n                <a t-attf-href="/link/#{ url }/#{other and \'sub\'}">link</a>\n                <a t-attf-href="/link/#{ url }/#{(not other) and \'sub\'}">link2</a>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <a href="/link/odoo/sub">link</a>\n                <a href="/link/odoo/">link2</a>\n            ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='url', kind=None),
                                    Constant(value='other', kind=None),
                                ],
                                values=[
                                    Constant(value='odoo', kind=None),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_attf_escaping_3',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-escaping">\n                <div t-attf-abc="abc #{val} { other }">123</div>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div abc="abc &#34;yes&#34; { other }">123</div>\n            ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='val', kind=None)],
                                values=[Constant(value='"yes"', kind=None)],
                            ),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_set_body_1',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-set">\n                <t t-set="abc"> <span a="b"> [%s] </span> </t>\n                <div t-att-abc="abc % add_abc">123</div>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div abc=" &lt;span a=&#34;b&#34;&gt; [&amp;#34;yes&amp;#34;] &lt;/span&gt; ">123</div>\n            ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='add_abc', kind=None)],
                                values=[Constant(value='"yes"', kind=None)],
                            ),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_set_body_2',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-set">\n                <t t-set="abc"> <span a="b"> toto </span> </t>\n                <div t-att-abc="\'[%s]\' % abc">123</div>\n                <div class="a1" t-out="abc"/>\n                <div class="a2" t-out="\'[%s]\' % abc"/>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div abc="[ &lt;span a=&#34;b&#34;&gt; toto &lt;/span&gt; ]">123</div>\n                <div class="a1"> <span a="b"> toto </span> </div>\n                <div class="a2">[ &lt;span a=&#34;b&#34;&gt; toto &lt;/span&gt; ]</div>\n            ', kind=None),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_out_format_1',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="out-format">\n                <t t-set="final_message">Powered by %s%s</t>\n                <div t-out="final_message % (a, b and (\'-%s\' % b) or \'\')"/>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div>Powered by 1-2</div>\n        ', kind='u'),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='a', kind=None),
                                            Constant(value='b', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_out_format_2',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-set">\n                <t t-set="toto">Toto %s</t>\n                <t t-set="abc"> <span a="b"> [%s , %s] </span> </t>\n                <div t-out="(abc % (add_abc, toto)) % 5">123</div>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div> <span a="b"> [&#34;yes&#34; , Toto 5] </span> </div>\n            ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='add_abc', kind=None)],
                                values=[Constant(value='"yes"', kind=None)],
                            ),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_out_format_3',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-set">\n                <t t-set="toto">Toto %s</t>\n                <t t-set="abc"> <span a="b"> a </span> </t>\n                <div t-out="(toto + abc) % v">123</div>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div>Toto &#34;yes&#34; <span a="b"> a </span> </div>\n            ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='v', kind=None)],
                                values=[Constant(value='"yes"', kind=None)],
                            ),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_out_format_4',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-set">\n                <t t-set="abc"> <span a="b"> a </span> </t>\n                <div t-out="(v + abc)">123</div>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div>&#34;yes&#34; <span a="b"> a </span> </div>\n            ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='v', kind=None)],
                                values=[Constant(value='"yes"', kind=None)],
                            ),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_out_format_5',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-set">\n                <t t-set="abc"> <span a="b"> a </span> </t>\n                <div t-out="(abc + v)">123</div>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div> <span a="b"> a </span> &#34;yes&#34;</div>\n            ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='v', kind=None)],
                                values=[Constant(value='"yes"', kind=None)],
                            ),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_out_format_6',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-set">\n                <t t-set="abc"> <span a="b"> a </span> </t>\n                <div t-out="(abc.strip() + v)">123</div>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div><span a="b"> a </span>&#34;yes&#34;</div>\n            ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='v', kind=None)],
                                values=[Constant(value='"yes"', kind=None)],
                            ),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_out_escape_text',
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
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n                <t t-name="base.dummy"><root><span t-out="text" t-options-widget="\'text\'"/></root></t>\n            ', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='view1', ctx=Load()),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='text', kind=None)],
                                        values=[Constant(value='a\n        b <b>c</b>', kind=None)],
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
                                    Name(id='html', ctx=Load()),
                                    Constant(value='<root><span data-oe-type="text" data-oe-expression="text">a<br>\n        b &lt;b&gt;c&lt;/b&gt;</span></root>', kind=None),
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
                    name='test_out_markup',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="esc-markup">\n                <t t-set="content"><span>toto</span></t>\n                <div t-out="content"/>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div><span>toto</span></div>\n        ', kind=None),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_esc_markup',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="esc-markup">\n                <t t-set="content"><span>toto</span></t>\n                <div t-esc="content"/>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ref', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="esc-markup">\n                <t t-set="content"><span>toto</span></t>\n                <div t-out="content"/>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
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
                                    Attribute(
                                        value=Name(id='ref', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Dict(keys=[], values=[]),
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_if_from_body',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="attr-set">\n                <t t-set="abc"> <span a="b"> a </span> </t>\n                <div t-if="abc">123</div>\n                <div t-if="not abc">456</div>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                <div>123</div>\n            ', kind=None),
                            type_comment=None,
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
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
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_error_message_1',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="test">\n                <section>\n                    <div t-esc="abc + def">\n                        <span>content</span>\n                    </div>\n                </section>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                        args=[Name(id='QWebException', ctx=Load())],
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
                                                slice=Constant(value='ir.qweb', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Try(
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
                                                slice=Constant(value='ir.qweb', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='QWebException', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='<div t-esc="abc + def"/>', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='message',
                                                        ctx=Load(),
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
                FunctionDef(
                    name='test_error_message_2',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="test">\n                <section>\n                    <div t-esc="abc + def + (">\n                        <span>content</span>\n                    </div>\n                </section>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                        args=[Name(id='QWebException', ctx=Load())],
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
                                                slice=Constant(value='ir.qweb', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Try(
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
                                                slice=Constant(value='ir.qweb', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='QWebException', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Can not compile expression', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='message',
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
                                                    Constant(value='<div t-esc="abc + def + ("/>', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='message',
                                                        ctx=Load(),
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
        ImportFrom(
            module='copy',
            names=[alias(name='deepcopy', asname=None)],
            level=0,
        ),
        ClassDef(
            name='FileSystemLoader',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
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
                                    attr='doc',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='parse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='path', ctx=Load())],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__iter__',
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
                        For(
                            target=Name(id='node', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='doc',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='node', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='t-name', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='name', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=Name(id='name', ctx=Load()),
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
                    name='__call__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='node', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='doc',
                                ctx=Load(),
                            ),
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
                                        comparators=[Name(id='name', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='root', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='Element',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='templates', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='root', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='deepcopy', ctx=Load()),
                                                        args=[Name(id='node', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='arch', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='tostring',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='root', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='encoding',
                                                        value=Constant(value='unicode', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Name(id='arch', ctx=Load()),
                                                    Name(id='name', ctx=Load()),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestQWebStaticXml',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='matcher', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='re', ctx=Load()),
                            attr='compile',
                            ctx=Load(),
                        ),
                        args=[Constant(value='^qweb-test-(.*)\\.xml$', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_cases',
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
                            targets=[Name(id='path', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='qweb_test_file_path',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=GeneratorExp(
                                elt=Call(
                                    func=Name(id='cls', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Constant(value='test_qweb_{}', kind=None),
                                                attr='format',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='matcher',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='match',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='f', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='group',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=1, kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='f', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='listdir',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='path', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Compare(
                                                left=Name(id='f', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='qweb-test-extend.xml', kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='cls', ctx=Load()),
                                                        attr='matcher',
                                                        ctx=Load(),
                                                    ),
                                                    attr='match',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='f', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
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
                    name='qweb_test_file_path',
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
                                        func=Name(id='get_module_resource', ctx=Load()),
                                        args=[
                                            Constant(value='web', kind=None),
                                            Constant(value='static', kind=None),
                                            Constant(value='lib', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='qweb2.js', kind=None),
                                        ],
                                        keywords=[],
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
                    name='__getattr__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='item', annotation=None, type_comment=None),
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
                                    func=Attribute(
                                        value=Name(id='item', ctx=Load()),
                                        attr='startswith',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='test_qweb_', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='AttributeError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='No {} on {}', kind=None),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='item', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
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
                            targets=[Name(id='f', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='qweb-test-{}.xml', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='item', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=10, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='qweb_test_file_path',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Lambda(
                                args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                body=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='run_test_file',
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
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='path', ctx=Load()),
                                                Name(id='f', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
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
                    name='run_test_file',
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
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='tz',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='Europe/Brussels', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='doc', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='parse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='path', ctx=Load())],
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
                        Assign(
                            targets=[Name(id='loader', ctx=Store())],
                            value=Call(
                                func=Name(id='FileSystemLoader', ctx=Load()),
                                args=[Name(id='path', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='qweb', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.qweb', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='template', ctx=Store()),
                            iter=Name(id='loader', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='template', ctx=Load()),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='template', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='_', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='param', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='doc', ctx=Load()),
                                            attr='find',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Constant(value='params[@id="{}"]', kind=None),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='template', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='params', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='param', ctx=Load()),
                                            ops=[Is()],
                                            comparators=[Constant(value=None, kind=None)],
                                        ),
                                        body=Dict(keys=[], values=[]),
                                        orelse=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='param', ctx=Load()),
                                                    attr='text',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='object_pairs_hook',
                                                    value=Attribute(
                                                        value=Name(id='collections', ctx=Load()),
                                                        attr='OrderedDict',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='params', ctx=Load()),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='__keep_empty_lines', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='doc', ctx=Load()),
                                                attr='find',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Constant(value='result[@id="{}"]', kind=None),
                                                        attr='format',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='template', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='text',
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
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='qweb', ctx=Load()),
                                                            attr='_render',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='template', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='values',
                                                                value=Name(id='params', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='load',
                                                                value=Name(id='loader', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Name(id='result', ctx=Load()),
                                                                    Constant(value='', kind='u'),
                                                                ],
                                                            ),
                                                            attr='strip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='&quot;', kind=None),
                                                    Constant(value='&#34;', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='template', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[Constant(value='odoo.addons.base.models.qweb', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='load_tests',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='loader', annotation=None, type_comment=None),
                    arg(arg='suite', annotation=None, type_comment=None),
                    arg(arg='_', annotation=None, type_comment=None),
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
                            value=Name(id='suite', ctx=Load()),
                            attr='addTests',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='TestQWebStaticXml', ctx=Load()),
                                    attr='get_cases',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Name(id='suite', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='TestPageSplit',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_split_before',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name=\'test\'>\n            <div>\n                <table>\n                    <tr></tr>\n                    <tr data-pagebreak="before"></tr>\n                    <tr></tr>\n                </table>\n            </div>\n            </t>\n            ', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendered', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
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
                                            Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='id',
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
                        Assign(
                            targets=[Name(id='ref', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='E', ctx=Load()),
                                    attr='div',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='table',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='tr',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='div',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='style', kind=None)],
                                                values=[Constant(value='page-break-after: always', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='E', ctx=Load()),
                                            attr='table',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='tr',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='data-pagebreak', kind=None)],
                                                        values=[Constant(value='before', kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='tr',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                                    attr='assertTreesEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='rendered', ctx=Load()),
                                    Name(id='ref', ctx=Load()),
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
                    name='test_split_after',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name=\'test\'>\n            <div>\n                <table>\n                    <tr></tr>\n                    <tr data-pagebreak="after"></tr>\n                    <tr></tr>\n                </table>\n            </div>\n            </t>\n            ', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendered', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
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
                                            Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='id',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTreesEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='rendered', ctx=Load()),
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
                                                    attr='table',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='tr',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='tr',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='data-pagebreak', kind=None)],
                                                                values=[Constant(value='after', kind=None)],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='div',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='style', kind=None)],
                                                        values=[Constant(value='page-break-after: always', kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='E', ctx=Load()),
                                                    attr='table',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='tr',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
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
                    name='test_dontsplit',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value="<t t-name='test'>\n            <div>\n                <table>\n                    <tr></tr>\n                    <tr></tr>\n                    <tr></tr>\n                </table>\n            </div>\n            </t>\n            ", kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendered', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='html', ctx=Load()),
                                    attr='fromstring',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
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
                                            Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='id',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTreesEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='rendered', ctx=Load()),
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
                                                    attr='table',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='tr',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='tr',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='E', ctx=Load()),
                                                            attr='tr',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestEmptyLines',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='arch', ctx=Store())],
                    value=Constant(value="<t t-name='test'>\n            \n                <div>\n                    \n                </div>\n                \n                \n            </t>", kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_no_empty_lines',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='arch',
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='compile',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='^\\s+\n', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rendered', ctx=Load())],
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
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='compile',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='\n\\s+\n', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rendered', ctx=Load())],
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
                    name='test_keep_empty_lines',
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
                            targets=[Name(id='t', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='arch',
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
                                    Attribute(
                                        value=Name(id='t', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='__keep_empty_lines', kind=None)],
                                        values=[Constant(value=True, kind=None)],
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='compile',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='^\\s+\n', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rendered', ctx=Load())],
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='compile',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='\n\\s+\n', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rendered', ctx=Load())],
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
            name='TestQWebMisc',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_render_comment_tail',
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
                            value=Constant(value=' Test the rendering of a tail text, near a comment.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='view1', ctx=Store())],
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
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='dummy', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='\n            <t>\n                <!-- it is a comment -->\n                <!-- it is another comment -->\n                Text 1\n                <!-- it is still another comment -->\n                Text 2\n                <t>ok</t>\n            </t>\n            ', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='emptyline', ctx=Store())],
                            value=Constant(value='\n                ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='markupsafe', ctx=Load()),
                                    attr='Markup',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=Constant(value='Text 1', kind=None),
                                                    op=Add(),
                                                    right=Name(id='emptyline', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Constant(value='Text 2', kind=None),
                                            ),
                                            op=Add(),
                                            right=Name(id='emptyline', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Constant(value='ok', kind=None),
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
                                        func=Attribute(
                                            value=Name(id='view1', ctx=Load()),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
