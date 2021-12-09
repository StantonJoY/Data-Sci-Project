Module(
    body=[
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ProductTemplate',
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
                    value=Constant(value='product.template', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_template_matrix',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='company_id', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='company_id', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
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
                            targets=[Name(id='currency_id', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='currency_id', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='display_extra', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='display_extra_price', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attribute_lines', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='valid_product_template_attribute_line_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Attrib', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.template.attribute.value', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='first_line_attributes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Subscript(
                                            value=Name(id='attribute_lines', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='product_template_value_ids',
                                        ctx=Load(),
                                    ),
                                    attr='_only_active',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attribute_ids_by_line', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='product_template_value_ids',
                                                ctx=Load(),
                                            ),
                                            attr='_only_active',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='ids',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='line', ctx=Store()),
                                        iter=Name(id='attribute_lines', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='header', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Dict(
                                            keys=[Constant(value='name', kind=None)],
                                            values=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='display_name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=ListComp(
                                    elt=Call(
                                        func=Attribute(
                                            value=Name(id='attr', ctx=Load()),
                                            attr='_grid_header_cell',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='fro_currency',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='to_currency',
                                                value=Name(id='currency_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='company',
                                                value=Name(id='company_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='display_extra',
                                                value=Name(id='display_extra', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id='attr', ctx=Store()),
                                            iter=Name(id='first_line_attributes', ctx=Load()),
                                            ifs=[],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=List(
                                elts=[List(elts=[], ctx=Load())],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='pool', ctx=Store()),
                            iter=Name(id='attribute_ids_by_line', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=ListComp(
                                        elt=BinOp(
                                            left=Name(id='x', ctx=Load()),
                                            op=Add(),
                                            right=List(
                                                elts=[Name(id='y', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='y', ctx=Store()),
                                                iter=Name(id='pool', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Name(id='result', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='args', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Call(
                                            func=Name(id='iter', ctx=Load()),
                                            args=[Name(id='result', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Mult(),
                                right=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='first_line_attributes', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rows', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='itertools', ctx=Load()),
                                    attr='zip_longest',
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='matrix', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Name(id='rows', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='row_attributes', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Attrib', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Name(id='row', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Slice(
                                                    lower=Constant(value=1, kind=None),
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
                                    targets=[Name(id='row_header_cell', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='row_attributes', ctx=Load()),
                                            attr='_grid_header_cell',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='fro_currency',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='currency_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='to_currency',
                                                value=Name(id='currency_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='company',
                                                value=Name(id='company_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='display_extra',
                                                value=Name(id='display_extra', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=List(
                                        elts=[Name(id='row_header_cell', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='cell', ctx=Store()),
                                    iter=Name(id='row', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='combination', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Attrib', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='cell', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='is_possible_combination', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_is_combination_possible',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='combination', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cell', ctx=Load()),
                                                    attr='sort',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='ptav_ids', kind=None),
                                                            Constant(value='qty', kind=None),
                                                            Constant(value='is_possible_combination', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='cell', ctx=Load()),
                                                            Constant(value=0, kind=None),
                                                            Name(id='is_possible_combination', ctx=Load()),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='matrix', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='result', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='header', kind=None),
                                    Constant(value='matrix', kind=None),
                                ],
                                values=[
                                    Name(id='header', ctx=Load()),
                                    Name(id='matrix', ctx=Load()),
                                ],
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
            name='ProductTemplateAttributeValue',
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
                    value=Constant(value='product.template.attribute.value', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_grid_header_cell',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fro_currency', annotation=None, type_comment=None),
                            arg(arg='to_currency', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                            arg(arg='display_extra', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Generate a header matrix cell for 1 or multiple attributes.\n\n        :param res.currency fro_currency:\n        :param res.currency to_currency:\n        :param res.company company:\n        :param bool display_extra: whether extra prices should be displayed in the cell\n            True by default, used to avoid showing extra prices on purchases.\n        :returns: cell with name (and price if any price_extra is defined on self)\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='header_cell', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='name', kind=None)],
                                values=[
                                    IfExp(
                                        test=Name(id='self', ctx=Load()),
                                        body=Call(
                                            func=Attribute(
                                                value=Constant(value=' • ', kind=None),
                                                attr='join',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                ListComp(
                                                    elt=Attribute(
                                                        value=Name(id='attr', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='attr', ctx=Store()),
                                                            iter=Name(id='self', ctx=Load()),
                                                            ifs=[],
                                                            is_async=0,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=' ', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='extra_price', ctx=Store())],
                            value=IfExp(
                                test=Name(id='display_extra', ctx=Load()),
                                body=Call(
                                    func=Name(id='sum', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='mapped',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='price_extra', kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                orelse=Constant(value=0, kind=None),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='extra_price', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='header_cell', ctx=Load()),
                                            slice=Constant(value='currency_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='to_currency', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='header_cell', ctx=Load()),
                                            slice=Constant(value='price', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fro_currency', ctx=Load()),
                                            attr='_convert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='extra_price', ctx=Load()),
                                            Name(id='to_currency', ctx=Load()),
                                            Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='today',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='header_cell', ctx=Load()),
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
