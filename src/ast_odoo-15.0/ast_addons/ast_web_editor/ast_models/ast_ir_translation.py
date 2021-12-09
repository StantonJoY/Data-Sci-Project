Module(
    body=[
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[
                alias(name='encode', asname=None),
                alias(name='xml_translate', asname=None),
                alias(name='html_translate', asname=None),
            ],
            level=0,
        ),
        FunctionDef(
            name='edit_translation_mapping',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='data', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='data', ctx=Store())],
                    value=Call(
                        func=Name(id='dict', ctx=Load()),
                        args=[Name(id='data', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='model',
                                value=Subscript(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='data', ctx=Load()),
                                                slice=Constant(value='name', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='partition',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=',', kind=None)],
                                        keywords=[],
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='value',
                                value=BoolOp(
                                    op=Or(),
                                    values=[
                                        Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='value', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='src', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=BinOp(
                        left=Constant(value='<span data-oe-model="%(model)s" data-oe-translation-id="%(id)s" data-oe-translation-state="%(state)s">%(value)s</span>', kind=None),
                        op=Mod(),
                        right=Name(id='data', ctx=Load()),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='IrTranslation',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.translation', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_terms_mapping',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='edit_translations', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='insert_missing',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field', ctx=Load()),
                                            Name(id='records', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Name(id='edit_translation_mapping', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrTranslation', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_terms_mapping',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='field', ctx=Load()),
                                    Name(id='records', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='save_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
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
                            value=Constant(value=' Convert the HTML fragment ``value`` to XML if necessary, and write\n        it as the value of translation ``self``.\n        ', kind=None),
                        ),
                        Assert(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='self', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='model_terms', kind=None)],
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='mname', ctx=Store()),
                                        Name(id='fname', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=',', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
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
                                        slice=Name(id='mname', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='_fields',
                                    ctx=Load(),
                                ),
                                slice=Name(id='fname', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='translate',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Name(id='xml_translate', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='div', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='<div>%s</div>', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='encode', ctx=Load()),
                                            args=[Name(id='value', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='root', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='div', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
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
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='etree', ctx=Load()),
                                                attr='tostring',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='root', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='encoding',
                                                    value=Constant(value='utf-8', kind=None),
                                                ),
                                            ],
                                        ),
                                        slice=Slice(
                                            lower=Constant(value=5, kind=None),
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=6, kind=None),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='translate',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='html_translate', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='div', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='<div>%s</div>', kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Name(id='encode', ctx=Load()),
                                                    args=[Name(id='value', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='root', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='fromstring',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='div', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='etree', ctx=Load()),
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
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='etree', ctx=Load()),
                                                        attr='tostring',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Subscript(
                                                            value=Subscript(
                                                                value=Name(id='root', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='encoding',
                                                            value=Constant(value='utf-8', kind=None),
                                                        ),
                                                        keyword(
                                                            arg='method',
                                                            value=Constant(value='html', kind=None),
                                                        ),
                                                    ],
                                                ),
                                                slice=Slice(
                                                    lower=Constant(value=5, kind=None),
                                                    upper=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=6, kind=None),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='value', kind=None)],
                                        values=[Name(id='value', ctx=Load())],
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
