Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='float_round', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ReportBomStructure',
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
                    value=Constant(value='report.mrp.report_bom_structure', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='BOM Structure Report', kind=None),
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
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='docs', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='bom_id', ctx=Store()),
                            iter=Name(id='docids', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='bom', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mrp.bom', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='bom_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='variant', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='variant', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='candidates', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='variant', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='product.product', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='variant', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='bom', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='bom', ctx=Load()),
                                                    attr='product_tmpl_id',
                                                    ctx=Load(),
                                                ),
                                                attr='product_variant_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='quantity', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='product_variant_id', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='candidates', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='data', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='data', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='childs', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='doc', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_pdf_line',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='bom_id', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='product_id',
                                                                value=Name(id='product_variant_id', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='qty',
                                                                value=Name(id='quantity', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='child_bom_ids',
                                                                value=Call(
                                                                    func=Name(id='set', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='json', ctx=Load()),
                                                                                attr='loads',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='data', ctx=Load()),
                                                                                        attr='get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='childs', kind=None)],
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
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='doc', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_pdf_line',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='bom_id', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='product_id',
                                                                value=Name(id='product_variant_id', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='qty',
                                                                value=Name(id='quantity', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='unfolded',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='doc', ctx=Load()),
                                                    slice=Constant(value='report_type', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='pdf', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='doc', ctx=Load()),
                                                    slice=Constant(value='report_structure', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='data', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='data', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='report_type', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value='all', kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='docs', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='doc', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='candidates', ctx=Load()),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='data', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='data', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='childs', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='doc', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_pdf_line',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='bom_id', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='qty',
                                                                value=Name(id='quantity', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='child_bom_ids',
                                                                value=Call(
                                                                    func=Name(id='set', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='json', ctx=Load()),
                                                                                attr='loads',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='data', ctx=Load()),
                                                                                        attr='get',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='childs', kind=None)],
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
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='doc', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_pdf_line',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='bom_id', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='qty',
                                                                value=Name(id='quantity', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='unfolded',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='doc', ctx=Load()),
                                                    slice=Constant(value='report_type', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='pdf', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='doc', ctx=Load()),
                                                    slice=Constant(value='report_structure', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='data', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='data', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='report_type', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    Constant(value='all', kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='docs', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='doc', ctx=Load())],
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
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='doc_ids', kind=None),
                                    Constant(value='doc_model', kind=None),
                                    Constant(value='docs', kind=None),
                                ],
                                values=[
                                    Name(id='docids', ctx=Load()),
                                    Constant(value='mrp.bom', kind=None),
                                    Name(id='docs', ctx=Load()),
                                ],
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
                    name='get_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom_id', annotation=None, type_comment=None),
                            arg(arg='searchQty', annotation=None, type_comment=None),
                            arg(arg='searchVariant', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=1, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_report_data',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Name(id='bom_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='searchQty',
                                        value=Name(id='searchQty', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='searchVariant',
                                        value=Name(id='searchVariant', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='lines', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='report_type', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='html', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='lines', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='report_structure', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='all', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='lines', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='has_attachments', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='lines', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='attachments', kind=None),
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Subscript(
                                                    value=Name(id='component', ctx=Load()),
                                                    slice=Constant(value='attachments', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='component', ctx=Store()),
                                                        iter=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='res', ctx=Load()),
                                                                slice=Constant(value='lines', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='components', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='lines', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
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
                                        args=[Constant(value='mrp.report_mrp_bom', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='data', kind=None)],
                                        values=[
                                            Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='lines', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
                    name='get_bom',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom_id', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='line_qty', annotation=None, type_comment=None),
                            arg(arg='line_id', annotation=None, type_comment=None),
                            arg(arg='level', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_bom',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Name(id='bom_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='product_id',
                                        value=Name(id='product_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='line_qty',
                                        value=Name(id='line_qty', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='line_id',
                                        value=Name(id='line_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='level',
                                        value=Name(id='level', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
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
                                        args=[Constant(value='mrp.report_mrp_bom_line', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='data', kind=None)],
                                        values=[Name(id='lines', ctx=Load())],
                                    ),
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
                    name='get_operations',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='bom_id', annotation=None, type_comment=None),
                            arg(arg='qty', annotation=None, type_comment=None),
                            arg(arg='level', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=0, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='bom', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bom_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='product_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_operation_line',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product', ctx=Load()),
                                    Name(id='bom', ctx=Load()),
                                    Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='qty', ctx=Load()),
                                                op=Div(),
                                                right=Attribute(
                                                    value=Name(id='bom', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='rounding_method',
                                                value=Constant(value='UP', kind=None),
                                            ),
                                        ],
                                    ),
                                    Name(id='level', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='bom_id', kind=None),
                                    Constant(value='currency', kind=None),
                                    Constant(value='operations', kind=None),
                                    Constant(value='extra_column_count', kind=None),
                                ],
                                values=[
                                    Name(id='bom_id', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='lines', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_extra_column_count',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
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
                                        args=[Constant(value='mrp.report_mrp_operation_line', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='data', kind=None)],
                                        values=[Name(id='values', ctx=Load())],
                                    ),
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
                    name='get_byproducts',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom_id', annotation=None, type_comment=None),
                            arg(arg='qty', annotation=None, type_comment=None),
                            arg(arg='level', annotation=None, type_comment=None),
                            arg(arg='total', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=0, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='bom', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bom_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='lines', ctx=Store()),
                                        Name(id='dummy', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_byproducts_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bom', ctx=Load()),
                                    Name(id='qty', ctx=Load()),
                                    Name(id='level', ctx=Load()),
                                    Name(id='total', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='bom_id', kind=None),
                                    Constant(value='currency', kind=None),
                                    Constant(value='byproducts', kind=None),
                                ],
                                values=[
                                    Name(id='bom_id', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='lines', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
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
                                        args=[Constant(value='mrp.report_mrp_byproduct_line', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='data', kind=None)],
                                        values=[Name(id='values', ctx=Load())],
                                    ),
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
                    name='_get_report_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom_id', annotation=None, type_comment=None),
                            arg(arg='searchQty', annotation=None, type_comment=None),
                            arg(arg='searchVariant', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bom_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_quantity', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='searchQty', ctx=Load()),
                                    Attribute(
                                        value=Name(id='bom', ctx=Load()),
                                        attr='product_qty',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_product_variants', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_uom_name', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='bom', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='bom_uom_name', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='bom', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='bom', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='variant', ctx=Store()),
                                            iter=Attribute(
                                                value=Attribute(
                                                    value=Name(id='bom', ctx=Load()),
                                                    attr='product_tmpl_id',
                                                    ctx=Load(),
                                                ),
                                                attr='product_variant_ids',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='bom_product_variants', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='variant', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='variant', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_bom',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bom_id', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='product_id',
                                        value=Name(id='searchVariant', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='line_qty',
                                        value=Name(id='bom_quantity', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='level',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='lines', kind=None),
                                    Constant(value='variants', kind=None),
                                    Constant(value='bom_uom_name', kind=None),
                                    Constant(value='bom_qty', kind=None),
                                    Constant(value='is_variant_applied', kind=None),
                                    Constant(value='is_uom_applied', kind=None),
                                    Constant(value='extra_column_count', kind=None),
                                ],
                                values=[
                                    Name(id='lines', ctx=Load()),
                                    Name(id='bom_product_variants', ctx=Load()),
                                    Name(id='bom_uom_name', ctx=Load()),
                                    Name(id='bom_quantity', ctx=Load()),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user_has_groups',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='product.group_product_variant', kind=None)],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='bom_product_variants', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='user_has_groups',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='uom.group_uom', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_extra_column_count',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
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
                    name='_get_bom',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom_id', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='line_qty', annotation=None, type_comment=None),
                            arg(arg='line_id', annotation=None, type_comment=None),
                            arg(arg='level', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='bom', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bom_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='bom', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_quantity', ctx=Store())],
                            value=Name(id='line_qty', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='line_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='current_line', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mrp.bom.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='line_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='bom_quantity', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='current_line', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='line_qty', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='product_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='product.product', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='product_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='bom', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='bom', ctx=Load()),
                                                    attr='product_tmpl_id',
                                                    ctx=Load(),
                                                ),
                                                attr='product_variant_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='product', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='price', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='_compute_price',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='product', ctx=Load()),
                                                            attr='with_company',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='company', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='standard_price',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='bom', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Mult(),
                                        right=Name(id='bom_quantity', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attachments', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mrp.document', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Constant(value='|', kind=None),
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='res_model', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='product.product', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='res_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='product', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='res_model', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='product.template', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='res_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='product', ctx=Load()),
                                                                    attr='product_tmpl_id',
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
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='price', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='product_tmpl_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='_compute_price',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='bom', ctx=Load()),
                                                                attr='product_tmpl_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_company',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='company', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='standard_price',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='bom', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Mult(),
                                        right=Name(id='bom_quantity', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attachments', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='mrp.document', kind=None),
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
                                                            Constant(value='res_model', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='product.template', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='res_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='bom', ctx=Load()),
                                                                    attr='product_tmpl_id',
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
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='operations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_operation_line',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product', ctx=Load()),
                                    Name(id='bom', ctx=Load()),
                                    Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='bom_quantity', ctx=Load()),
                                                op=Div(),
                                                right=Attribute(
                                                    value=Name(id='bom', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='rounding_method',
                                                value=Constant(value='UP', kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='bom', kind=None),
                                    Constant(value='bom_qty', kind=None),
                                    Constant(value='bom_prod_name', kind=None),
                                    Constant(value='currency', kind=None),
                                    Constant(value='product', kind=None),
                                    Constant(value='code', kind=None),
                                    Constant(value='price', kind=None),
                                    Constant(value='total', kind=None),
                                    Constant(value='level', kind=None),
                                    Constant(value='operations', kind=None),
                                    Constant(value='operations_cost', kind=None),
                                    Constant(value='attachments', kind=None),
                                    Constant(value='operations_time', kind=None),
                                ],
                                values=[
                                    Name(id='bom', ctx=Load()),
                                    Name(id='bom_quantity', ctx=Load()),
                                    Attribute(
                                        value=Name(id='product', ctx=Load()),
                                        attr='display_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    Name(id='product', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='bom', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    Name(id='price', ctx=Load()),
                                    Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Subscript(
                                                    value=Name(id='op', ctx=Load()),
                                                    slice=Constant(value='total', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='op', ctx=Store()),
                                                        iter=Name(id='operations', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='level', ctx=Load()),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Name(id='operations', ctx=Load()),
                                    Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Subscript(
                                                    value=Name(id='op', ctx=Load()),
                                                    slice=Constant(value='total', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='op', ctx=Store()),
                                                        iter=Name(id='operations', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='attachments', ctx=Load()),
                                    Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Subscript(
                                                    value=Name(id='op', ctx=Load()),
                                                    slice=Constant(value='duration_expected', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='op', ctx=Store()),
                                                        iter=Name(id='operations', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='components', ctx=Store()),
                                        Name(id='total', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_bom_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bom', ctx=Load()),
                                    Name(id='bom_quantity', ctx=Load()),
                                    Name(id='product', ctx=Load()),
                                    Name(id='line_id', ctx=Load()),
                                    Name(id='level', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Subscript(
                                value=Name(id='lines', ctx=Load()),
                                slice=Constant(value='total', kind=None),
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Name(id='total', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='lines', ctx=Load()),
                                    slice=Constant(value='components', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='components', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='byproducts', ctx=Store()),
                                        Name(id='byproduct_cost_portion', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_byproducts_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bom', ctx=Load()),
                                    Name(id='bom_quantity', ctx=Load()),
                                    Name(id='level', ctx=Load()),
                                    Subscript(
                                        value=Name(id='lines', ctx=Load()),
                                        slice=Constant(value='total', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='lines', ctx=Load()),
                                    slice=Constant(value='byproducts', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='byproducts', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='lines', ctx=Load()),
                                    slice=Constant(value='cost_share', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='float_round', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value=1, kind=None),
                                        op=Sub(),
                                        right=Name(id='byproduct_cost_portion', ctx=Load()),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='precision_rounding',
                                        value=Constant(value=0.0001, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='lines', ctx=Load()),
                                    slice=Constant(value='bom_cost', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Subscript(
                                    value=Name(id='lines', ctx=Load()),
                                    slice=Constant(value='total', kind=None),
                                    ctx=Load(),
                                ),
                                op=Mult(),
                                right=Subscript(
                                    value=Name(id='lines', ctx=Load()),
                                    slice=Constant(value='cost_share', kind=None),
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='lines', ctx=Load()),
                                    slice=Constant(value='byproducts_cost', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='byproduct', ctx=Load()),
                                            slice=Constant(value='bom_cost', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='byproduct', ctx=Store()),
                                                iter=Name(id='byproducts', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='lines', ctx=Load()),
                                    slice=Constant(value='byproducts_total', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='byproduct', ctx=Load()),
                                            slice=Constant(value='product_qty', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='byproduct', ctx=Store()),
                                                iter=Name(id='byproducts', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='lines', ctx=Load()),
                                    slice=Constant(value='extra_column_count', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_extra_column_count',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='lines', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_bom_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom', annotation=None, type_comment=None),
                            arg(arg='bom_quantity', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                            arg(arg='line_id', annotation=None, type_comment=None),
                            arg(arg='level', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='components', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='total', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='bom', ctx=Load()),
                                attr='bom_line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='line_quantity', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Name(id='bom_quantity', ctx=Load()),
                                            op=Div(),
                                            right=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='product_qty',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1.0, kind=None),
                                                ],
                                            ),
                                        ),
                                        op=Mult(),
                                        right=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='_skip_bom_line',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='product', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='bom', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='price', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='_compute_price',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_company',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='company', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='standard_price',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Mult(),
                                        right=Name(id='line_quantity', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='child_bom_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='factor', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='_compute_quantity',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Name(id='line_quantity', ctx=Load()),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='child_bom_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_uom_id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Div(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='child_bom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='sub_total', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_price',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='child_bom_id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='factor', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='byproduct_cost_share', ctx=Store())],
                                            value=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='child_bom_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='byproduct_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='cost_share', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='byproduct_cost_share', ctx=Load()),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='sub_total', ctx=Store()),
                                                    op=Mult(),
                                                    value=Call(
                                                        func=Name(id='float_round', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value=1, kind=None),
                                                                op=Sub(),
                                                                right=BinOp(
                                                                    left=Name(id='byproduct_cost_share', ctx=Load()),
                                                                    op=Div(),
                                                                    right=Constant(value=100, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_rounding',
                                                                value=Constant(value=0.0001, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='sub_total', ctx=Store())],
                                            value=Name(id='price', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='sub_total', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            attr='round',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='sub_total', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='components', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='prod_id', kind=None),
                                                    Constant(value='prod_name', kind=None),
                                                    Constant(value='code', kind=None),
                                                    Constant(value='prod_qty', kind=None),
                                                    Constant(value='prod_uom', kind=None),
                                                    Constant(value='prod_cost', kind=None),
                                                    Constant(value='parent_id', kind=None),
                                                    Constant(value='line_id', kind=None),
                                                    Constant(value='level', kind=None),
                                                    Constant(value='total', kind=None),
                                                    Constant(value='child_bom', kind=None),
                                                    Constant(value='phantom_bom', kind=None),
                                                    Constant(value='attachments', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='child_bom_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='child_bom_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='display_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                    Name(id='line_quantity', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='company', ctx=Load()),
                                                                attr='currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='round',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='price', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='level', ctx=Load()),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                    Name(id='sub_total', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='child_bom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='child_bom_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='child_bom_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='phantom', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='mrp.document', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='|', kind=None),
                                                                    Constant(value='&', kind=None),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='res_model', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value='product.product', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='res_id', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='line', ctx=Load()),
                                                                                    attr='product_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='&', kind=None),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='res_model', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value='product.template', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='res_id', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='line', ctx=Load()),
                                                                                        attr='product_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='product_tmpl_id',
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
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='total', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='sub_total', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='components', ctx=Load()),
                                    Name(id='total', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_byproducts_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom', annotation=None, type_comment=None),
                            arg(arg='bom_quantity', annotation=None, type_comment=None),
                            arg(arg='level', annotation=None, type_comment=None),
                            arg(arg='total', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='byproducts', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='byproduct_cost_portion', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='bom', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='byproduct', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='bom', ctx=Load()),
                                attr='byproduct_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='line_quantity', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Name(id='bom_quantity', ctx=Load()),
                                            op=Div(),
                                            right=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='product_qty',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1.0, kind=None),
                                                ],
                                            ),
                                        ),
                                        op=Mult(),
                                        right=Attribute(
                                            value=Name(id='byproduct', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='cost_share', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='byproduct', ctx=Load()),
                                            attr='cost_share',
                                            ctx=Load(),
                                        ),
                                        op=Div(),
                                        right=Constant(value=100, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='byproduct_cost_portion', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='cost_share', ctx=Load()),
                                ),
                                Assign(
                                    targets=[Name(id='price', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='byproduct', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uom_id',
                                                    ctx=Load(),
                                                ),
                                                attr='_compute_price',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='byproduct', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='with_company',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='company', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='standard_price',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='byproduct', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Mult(),
                                        right=Name(id='line_quantity', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='byproducts', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='product_name', kind=None),
                                                    Constant(value='product_qty', kind=None),
                                                    Constant(value='product_uom', kind=None),
                                                    Constant(value='product_cost', kind=None),
                                                    Constant(value='parent_id', kind=None),
                                                    Constant(value='level', kind=None),
                                                    Constant(value='bom_cost', kind=None),
                                                    Constant(value='cost_share', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='byproduct', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='byproduct', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='line_quantity', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='byproduct', ctx=Load()),
                                                            attr='product_uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='company', ctx=Load()),
                                                                attr='currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='round',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='price', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='level', ctx=Load()),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='company', ctx=Load()),
                                                                attr='currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='round',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='total', ctx=Load()),
                                                                op=Mult(),
                                                                right=Name(id='cost_share', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Name(id='cost_share', ctx=Load()),
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
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='byproducts', ctx=Load()),
                                    Name(id='byproduct_cost_portion', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_operation_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                            arg(arg='bom', annotation=None, type_comment=None),
                            arg(arg='qty', annotation=None, type_comment=None),
                            arg(arg='level', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='operations', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='total', ctx=Store())],
                            value=Constant(value=0.0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='operation', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='bom', ctx=Load()),
                                attr='operation_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='operation', ctx=Load()),
                                            attr='_skip_operation_line',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='product', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='operation_cycle', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Name(id='qty', ctx=Load()),
                                                op=Div(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='operation', ctx=Load()),
                                                        attr='workcenter_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='capacity',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='rounding_method',
                                                value=Constant(value='UP', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='duration_expected', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Name(id='operation_cycle', ctx=Load()),
                                                op=Mult(),
                                                right=Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='time_cycle',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            op=Add(),
                                            right=Attribute(
                                                value=Attribute(
                                                    value=Name(id='operation', ctx=Load()),
                                                    attr='workcenter_id',
                                                    ctx=Load(),
                                                ),
                                                attr='time_stop',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='operation', ctx=Load()),
                                                attr='workcenter_id',
                                                ctx=Load(),
                                            ),
                                            attr='time_start',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='total', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Name(id='duration_expected', ctx=Load()),
                                            op=Div(),
                                            right=Constant(value=60.0, kind=None),
                                        ),
                                        op=Mult(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='operation', ctx=Load()),
                                                attr='workcenter_id',
                                                ctx=Load(),
                                            ),
                                            attr='costs_hour',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='operations', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='level', kind=None),
                                                    Constant(value='operation', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='duration_expected', kind=None),
                                                    Constant(value='total', kind=None),
                                                ],
                                                values=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='level', ctx=Load()),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                    Name(id='operation', ctx=Load()),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Attribute(
                                                                value=Name(id='operation', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Constant(value=' - ', kind=None),
                                                        ),
                                                        op=Add(),
                                                        right=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='operation', ctx=Load()),
                                                                attr='workcenter_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Name(id='duration_expected', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='company',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='currency_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='round',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='total', ctx=Load())],
                                                        keywords=[],
                                                    ),
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
                        Return(
                            value=Name(id='operations', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_price',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom', annotation=None, type_comment=None),
                            arg(arg='factor', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='price', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='bom', ctx=Load()),
                                attr='operation_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='operation_cycle', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[Name(id='factor', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='rounding_method',
                                                value=Constant(value='UP', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='operations', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_operation_line',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='product', ctx=Load()),
                                            Name(id='bom', ctx=Load()),
                                            Name(id='operation_cycle', ctx=Load()),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='price', ctx=Store()),
                                    op=Add(),
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Subscript(
                                                    value=Name(id='op', ctx=Load()),
                                                    slice=Constant(value='total', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='op', ctx=Store()),
                                                        iter=Name(id='operations', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='bom', ctx=Load()),
                                attr='bom_line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='_skip_bom_line',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='product', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='child_bom_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='qty', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='_compute_quantity',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        BinOp(
                                                            left=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_qty',
                                                                ctx=Load(),
                                                            ),
                                                            op=Mult(),
                                                            right=Name(id='factor', ctx=Load()),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='child_bom_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_uom_id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Div(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='child_bom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_qty',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='sub_price', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_price',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='child_bom_id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='qty', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='byproduct_cost_share', ctx=Store())],
                                            value=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='child_bom_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='byproduct_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='cost_share', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='byproduct_cost_share', ctx=Load()),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='sub_price', ctx=Store()),
                                                    op=Mult(),
                                                    value=Call(
                                                        func=Name(id='float_round', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value=1, kind=None),
                                                                op=Sub(),
                                                                right=BinOp(
                                                                    left=Name(id='byproduct_cost_share', ctx=Load()),
                                                                    op=Div(),
                                                                    right=Constant(value=100, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_rounding',
                                                                value=Constant(value=0.0001, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        AugAssign(
                                            target=Name(id='price', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='sub_price', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='prod_qty', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_qty',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Name(id='factor', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='company', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='bom', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='not_rounded_price', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='_compute_price',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='force_comany',
                                                                        value=Attribute(
                                                                            value=Name(id='company', ctx=Load()),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='standard_price',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_uom_id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Mult(),
                                                right=Name(id='prod_qty', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='price', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='company', ctx=Load()),
                                                        attr='currency_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='round',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='not_rounded_price', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='price', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_sub_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='line_qty', annotation=None, type_comment=None),
                            arg(arg='line_id', annotation=None, type_comment=None),
                            arg(arg='level', annotation=None, type_comment=None),
                            arg(arg='child_bom_ids', annotation=None, type_comment=None),
                            arg(arg='unfolded', annotation=None, type_comment=None),
                        ],
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
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_bom',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Attribute(
                                            value=Name(id='bom', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='product_id',
                                        value=Name(id='product_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='line_qty',
                                        value=Name(id='line_qty', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='line_id',
                                        value=Name(id='line_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='level',
                                        value=Name(id='level', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bom_lines', ctx=Store())],
                            value=Subscript(
                                value=Name(id='data', ctx=Load()),
                                slice=Constant(value='components', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='bom_line', ctx=Store()),
                            iter=Name(id='bom_lines', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='uom', kind=None),
                                                    Constant(value='prod_cost', kind=None),
                                                    Constant(value='bom_cost', kind=None),
                                                    Constant(value='level', kind=None),
                                                    Constant(value='code', kind=None),
                                                    Constant(value='child_bom', kind=None),
                                                    Constant(value='prod_id', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='bom_line', ctx=Load()),
                                                        slice=Constant(value='prod_name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='bom', kind=None),
                                                    Subscript(
                                                        value=Name(id='bom_line', ctx=Load()),
                                                        slice=Constant(value='prod_qty', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='bom_line', ctx=Load()),
                                                        slice=Constant(value='prod_uom', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='bom_line', ctx=Load()),
                                                        slice=Constant(value='prod_cost', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='bom_line', ctx=Load()),
                                                        slice=Constant(value='total', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='bom_line', ctx=Load()),
                                                        slice=Constant(value='level', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='bom_line', ctx=Load()),
                                                        slice=Constant(value='code', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='bom_line', ctx=Load()),
                                                        slice=Constant(value='child_bom', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='bom_line', ctx=Load()),
                                                        slice=Constant(value='prod_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Subscript(
                                                value=Name(id='bom_line', ctx=Load()),
                                                slice=Constant(value='child_bom', kind=None),
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='unfolded', ctx=Load()),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='bom_line', ctx=Load()),
                                                            slice=Constant(value='child_bom', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='child_bom_ids', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='line', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='mrp.bom.line', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='bom_line', ctx=Load()),
                                                        slice=Constant(value='line_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Name(id='lines', ctx=Store()),
                                            op=Add(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_sub_lines',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='child_bom_id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='bom_line', ctx=Load()),
                                                        slice=Constant(value='prod_qty', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='line', ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='level', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    Name(id='child_bom_ids', ctx=Load()),
                                                    Name(id='unfolded', ctx=Load()),
                                                ],
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
                        If(
                            test=Subscript(
                                value=Name(id='data', ctx=Load()),
                                slice=Constant(value='operations', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='uom', kind=None),
                                                    Constant(value='bom_cost', kind=None),
                                                    Constant(value='level', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Operations', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='operation', kind=None),
                                                    Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='operations_time', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='minutes', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='operations_cost', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='level', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='operation', ctx=Store()),
                                    iter=Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='operations', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='unfolded', ctx=Load()),
                                                    Compare(
                                                        left=BinOp(
                                                            left=Constant(value='operation-', kind=None),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='bom', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='child_bom_ids', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='lines', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='uom', kind=None),
                                                                    Constant(value='bom_cost', kind=None),
                                                                    Constant(value='level', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Name(id='operation', ctx=Load()),
                                                                        slice=Constant(value='name', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='operation', kind=None),
                                                                    Subscript(
                                                                        value=Name(id='operation', ctx=Load()),
                                                                        slice=Constant(value='duration_expected', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='minutes', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    Subscript(
                                                                        value=Name(id='operation', ctx=Load()),
                                                                        slice=Constant(value='total', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    BinOp(
                                                                        left=Name(id='level', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
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
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Subscript(
                                value=Name(id='data', ctx=Load()),
                                slice=Constant(value='byproducts', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='uom', kind=None),
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='bom_cost', kind=None),
                                                    Constant(value='level', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Byproducts', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='byproduct', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='byproducts_total', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='data', ctx=Load()),
                                                        slice=Constant(value='byproducts_cost', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='level', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='byproduct', ctx=Store()),
                                    iter=Subscript(
                                        value=Name(id='data', ctx=Load()),
                                        slice=Constant(value='byproducts', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='unfolded', ctx=Load()),
                                                    Compare(
                                                        left=BinOp(
                                                            left=Constant(value='byproduct-', kind=None),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='bom', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[Name(id='child_bom_ids', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='lines', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='quantity', kind=None),
                                                                    Constant(value='uom', kind=None),
                                                                    Constant(value='prod_cost', kind=None),
                                                                    Constant(value='bom_cost', kind=None),
                                                                    Constant(value='level', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Name(id='byproduct', ctx=Load()),
                                                                        slice=Constant(value='product_name', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='byproduct', kind=None),
                                                                    Subscript(
                                                                        value=Name(id='byproduct', ctx=Load()),
                                                                        slice=Constant(value='product_qty', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Name(id='byproduct', ctx=Load()),
                                                                        slice=Constant(value='product_uom', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Name(id='byproduct', ctx=Load()),
                                                                        slice=Constant(value='product_cost', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Subscript(
                                                                        value=Name(id='byproduct', ctx=Load()),
                                                                        slice=Constant(value='bom_cost', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    BinOp(
                                                                        left=Name(id='level', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='lines', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_pdf_line',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='bom_id', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='qty', annotation=None, type_comment=None),
                            arg(arg='child_bom_ids', annotation=None, type_comment=None),
                            arg(arg='unfolded', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=1, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='child_bom_ids', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='child_bom_ids', ctx=Store())],
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='bom', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.bom', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='bom_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='product_id', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='product_id', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='bom', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='bom', ctx=Load()),
                                                attr='product_tmpl_id',
                                                ctx=Load(),
                                            ),
                                            attr='product_variant_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_bom',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='bom_id',
                                        value=Name(id='bom_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='product_id',
                                        value=Name(id='product_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='line_qty',
                                        value=Name(id='qty', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pdf_lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_sub_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='bom', ctx=Load()),
                                    Name(id='product_id', ctx=Load()),
                                    Name(id='qty', ctx=Load()),
                                    Constant(value=False, kind=None),
                                    Constant(value=1, kind=None),
                                    Name(id='child_bom_ids', ctx=Load()),
                                    Name(id='unfolded', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='components', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='lines', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='pdf_lines', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='data', ctx=Load()),
                                    slice=Constant(value='extra_column_count', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_extra_column_count',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_extra_column_count',
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
                        Return(
                            value=Constant(value=0, kind=None),
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
