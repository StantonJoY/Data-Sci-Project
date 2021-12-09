Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='_prepare_data',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='data', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Compare(
                        left=Call(
                            func=Attribute(
                                value=Name(id='data', ctx=Load()),
                                attr='get',
                                ctx=Load(),
                            ),
                            args=[Constant(value='active_model', kind=None)],
                            keywords=[],
                        ),
                        ops=[Eq()],
                        comparators=[Constant(value='product.template', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='quantity_by_product', ctx=Store())],
                            value=DictComp(
                                key=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Name(id='env', ctx=Load()),
                                                    slice=Constant(value='product.template', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='with_context',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='display_default_code',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                        ),
                                        attr='browse',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[Name(id='p', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                value=Name(id='q', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='p', ctx=Store()),
                                                Name(id='q', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='data', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='quantity_by_product', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='items',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='data', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='active_model', kind=None)],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='product.product', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='quantity_by_product', ctx=Store())],
                                    value=DictComp(
                                        key=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='env', ctx=Load()),
                                                            slice=Constant(value='product.product', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='display_default_code',
                                                            value=Constant(value=False, kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Name(id='int', ctx=Load()),
                                                    args=[Name(id='p', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        value=Name(id='q', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='p', ctx=Store()),
                                                        Name(id='q', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='data', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='quantity_by_product', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Product model not defined, Please contact your administrator.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                        ),
                    ],
                ),
                Assign(
                    targets=[Name(id='layout_wizard', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='product.label.layout', kind=None),
                                ctx=Load(),
                            ),
                            attr='browse',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='layout_wizard', kind=None)],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='layout_wizard', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Dict(keys=[], values=[]),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Dict(
                        keys=[
                            Constant(value='quantity', kind=None),
                            Constant(value='rows', kind=None),
                            Constant(value='columns', kind=None),
                            Constant(value='page_numbers', kind=None),
                            Constant(value='price_included', kind=None),
                            Constant(value='extra_html', kind=None),
                        ],
                        values=[
                            Name(id='quantity_by_product', ctx=Load()),
                            Attribute(
                                value=Name(id='layout_wizard', ctx=Load()),
                                attr='rows',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='layout_wizard', ctx=Load()),
                                attr='columns',
                                ctx=Load(),
                            ),
                            BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='quantity_by_product', ctx=Load()),
                                                        attr='values',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                    op=FloorDiv(),
                                    right=BinOp(
                                        left=Attribute(
                                            value=Name(id='layout_wizard', ctx=Load()),
                                            attr='rows',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Attribute(
                                            value=Name(id='layout_wizard', ctx=Load()),
                                            attr='columns',
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=1, kind=None),
                            ),
                            Call(
                                func=Attribute(
                                    value=Name(id='data', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='price_included', kind=None)],
                                keywords=[],
                            ),
                            Attribute(
                                value=Name(id='layout_wizard', ctx=Load()),
                                attr='extra_html',
                                ctx=Load(),
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='ReportProductTemplateLabel',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='report.product.report_producttemplatelabel', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Product Label Report', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_report_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='docids', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='_prepare_data', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    Name(id='data', ctx=Load()),
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
            name='ReportProductTemplateLabelDymo',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='report.product.report_producttemplatelabel_dymo', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Product Label Report', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_report_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='docids', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='_prepare_data', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    Name(id='data', ctx=Load()),
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
