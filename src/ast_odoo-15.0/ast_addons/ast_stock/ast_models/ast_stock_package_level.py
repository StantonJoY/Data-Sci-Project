Module(
    body=[
        ImportFrom(
            module='itertools',
            names=[alias(name='groupby', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='operator',
            names=[alias(name='itemgetter', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='StockPackageLevel',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='stock.package_level', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Stock Package Level', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_check_company_auto', ctx=Store())],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='package_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.quant.package', kind=None),
                            Constant(value='Package', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('location_id', 'child_of', parent.location_id), '|', ('company_id', '=', False), ('company_id', '=', company_id)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='picking_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.picking', kind=None),
                            Constant(value='Picking', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='move_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.move', kind=None),
                            Constant(value='package_level_id', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='move_line_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.move.line', kind=None),
                            Constant(value='package_level_id', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='location_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.location', kind=None),
                            Constant(value='From', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_location_id', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='location_dest_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.location', kind=None),
                            Constant(value='To', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('id', 'child_of', parent.location_dest_id), '|', ('company_id', '=', False), ('company_id', '=', company_id)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_done', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Done', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_is_done', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_is_done', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='draft', kind=None),
                                            Constant(value='Draft', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='confirmed', kind=None),
                                            Constant(value='Confirmed', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='assigned', kind=None),
                                            Constant(value='Reserved', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='new', kind=None),
                                            Constant(value='New', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='done', kind=None),
                                            Constant(value='Done', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='cancel', kind=None),
                                            Constant(value='Cancelled', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='State', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_state', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_fresh_package', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_fresh_pack', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='picking_type_code', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='picking_id.picking_type_code', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='show_lots_m2o', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_show_lot', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='show_lots_text', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_show_lot', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.company', kind=None),
                            Constant(value='Company', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_is_done',
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
                            target=Name(id='package_level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='package_level', ctx=Load()),
                                        attr='is_fresh_package',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='is_done',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='is_done',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='_check_move_lines_map_quant_package',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='package_level', ctx=Load()),
                                                        attr='package_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='move_line_ids', kind=None),
                                Constant(value='move_line_ids.qty_done', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_is_done',
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
                            target=Name(id='package_level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='package_level', ctx=Load()),
                                        attr='is_done',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='is_fresh_package',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='ml_update_dict', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='defaultdict', ctx=Load()),
                                                        args=[Name(id='float', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='quant', ctx=Store()),
                                                    iter=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='package_level', ctx=Load()),
                                                            attr='package_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='quant_ids',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='corresponding_ml', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='package_level', ctx=Load()),
                                                                        attr='move_line_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='filtered',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Lambda(
                                                                        args=arguments(
                                                                            posonlyargs=[],
                                                                            args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                                            vararg=None,
                                                                            kwonlyargs=[],
                                                                            kw_defaults=[],
                                                                            kwarg=None,
                                                                            defaults=[],
                                                                        ),
                                                                        body=BoolOp(
                                                                            op=And(),
                                                                            values=[
                                                                                Compare(
                                                                                    left=Attribute(
                                                                                        value=Name(id='ml', ctx=Load()),
                                                                                        attr='product_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[
                                                                                        Attribute(
                                                                                            value=Name(id='quant', ctx=Load()),
                                                                                            attr='product_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                                Compare(
                                                                                    left=Attribute(
                                                                                        value=Name(id='ml', ctx=Load()),
                                                                                        attr='lot_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[
                                                                                        Attribute(
                                                                                            value=Name(id='quant', ctx=Load()),
                                                                                            attr='lot_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='corresponding_ml', ctx=Load()),
                                                            body=[
                                                                AugAssign(
                                                                    target=Subscript(
                                                                        value=Name(id='ml_update_dict', ctx=Load()),
                                                                        slice=Subscript(
                                                                            value=Name(id='corresponding_ml', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ctx=Store(),
                                                                    ),
                                                                    op=Add(),
                                                                    value=Attribute(
                                                                        value=Name(id='quant', ctx=Load()),
                                                                        attr='quantity',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='corresponding_move', ctx=Store())],
                                                                    value=Subscript(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='package_level', ctx=Load()),
                                                                                    attr='move_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='filtered',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Lambda(
                                                                                    args=arguments(
                                                                                        posonlyargs=[],
                                                                                        args=[arg(arg='m', annotation=None, type_comment=None)],
                                                                                        vararg=None,
                                                                                        kwonlyargs=[],
                                                                                        kw_defaults=[],
                                                                                        kwarg=None,
                                                                                        defaults=[],
                                                                                    ),
                                                                                    body=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='m', ctx=Load()),
                                                                                            attr='product_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[
                                                                                            Attribute(
                                                                                                value=Name(id='quant', ctx=Load()),
                                                                                                attr='product_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        slice=Slice(
                                                                            lower=None,
                                                                            upper=Constant(value=1, kind=None),
                                                                            step=None,
                                                                        ),
                                                                        ctx=Load(),
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
                                                                                slice=Constant(value='stock.move.line', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='create',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='location_id', kind=None),
                                                                                    Constant(value='location_dest_id', kind=None),
                                                                                    Constant(value='picking_id', kind=None),
                                                                                    Constant(value='product_id', kind=None),
                                                                                    Constant(value='qty_done', kind=None),
                                                                                    Constant(value='product_uom_id', kind=None),
                                                                                    Constant(value='lot_id', kind=None),
                                                                                    Constant(value='package_id', kind=None),
                                                                                    Constant(value='result_package_id', kind=None),
                                                                                    Constant(value='package_level_id', kind=None),
                                                                                    Constant(value='move_id', kind=None),
                                                                                    Constant(value='owner_id', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='package_level', ctx=Load()),
                                                                                            attr='location_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='package_level', ctx=Load()),
                                                                                            attr='location_dest_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='package_level', ctx=Load()),
                                                                                            attr='picking_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='quant', ctx=Load()),
                                                                                            attr='product_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='quant', ctx=Load()),
                                                                                        attr='quantity',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='quant', ctx=Load()),
                                                                                                attr='product_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='uom_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='quant', ctx=Load()),
                                                                                            attr='lot_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='package_level', ctx=Load()),
                                                                                            attr='package_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='package_level', ctx=Load()),
                                                                                            attr='package_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='package_level', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='corresponding_move', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='quant', ctx=Load()),
                                                                                            attr='owner_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Tuple(
                                                        elts=[
                                                            Name(id='rec', ctx=Store()),
                                                            Name(id='quant', ctx=Store()),
                                                        ],
                                                        ctx=Store(),
                                                    ),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='ml_update_dict', ctx=Load()),
                                                            attr='items',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='rec', ctx=Load()),
                                                                    attr='qty_done',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='quant', ctx=Load()),
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
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='package_level', ctx=Load()),
                                                                attr='move_line_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value=0, kind=None)],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='unlink',
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
                                                            value=Attribute(
                                                                value=Name(id='package_level', ctx=Load()),
                                                                attr='move_line_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[NotEq()],
                                                                    comparators=[Constant(value=0, kind=None)],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='qty_done', kind=None)],
                                                        values=[Constant(value=0, kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
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
                    name='_compute_fresh_pack',
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
                            target=Name(id='package_level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='move_line_ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Call(
                                                func=Name(id='all', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='package_id',
                                                                    ctx=Load(),
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='package_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[
                                                                        Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='result_package_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='ml', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='package_level', ctx=Load()),
                                                                    attr='move_line_ids',
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
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='is_fresh_package',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='is_fresh_package',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='move_line_ids', kind=None),
                                Constant(value='move_line_ids.package_id', kind=None),
                                Constant(value='move_line_ids.result_package_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_state',
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
                            target=Name(id='package_level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='move_ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='move_line_ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='state',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='draft', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='package_level', ctx=Load()),
                                                            attr='move_line_ids',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='package_level', ctx=Load()),
                                                                attr='move_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Attribute(
                                                                        value=Name(id='m', ctx=Load()),
                                                                        attr='state',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[NotIn()],
                                                                    comparators=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value='done', kind=None),
                                                                                Constant(value='cancel', kind=None),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='package_level', ctx=Load()),
                                                            attr='state',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='confirmed', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='package_level', ctx=Load()),
                                                                attr='move_line_ids',
                                                                ctx=Load(),
                                                            ),
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='package_level', ctx=Load()),
                                                                            attr='move_line_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='filtered',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Lambda(
                                                                            args=arguments(
                                                                                posonlyargs=[],
                                                                                args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                                                vararg=None,
                                                                                kwonlyargs=[],
                                                                                kw_defaults=[],
                                                                                kwarg=None,
                                                                                defaults=[],
                                                                            ),
                                                                            body=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='state',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='done', kind=None)],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Attribute(
                                                                value=Name(id='package_level', ctx=Load()),
                                                                attr='is_fresh_package',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='package_level', ctx=Load()),
                                                                            attr='state',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='new', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='package_level', ctx=Load()),
                                                                            attr='_check_move_lines_map_quant_package',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='package_level', ctx=Load()),
                                                                                attr='package_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value='product_uom_qty', kind=None),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='package_level', ctx=Load()),
                                                                                    attr='state',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value='assigned', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='package_level', ctx=Load()),
                                                                                    attr='state',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value='confirmed', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='package_level', ctx=Load()),
                                                                        attr='move_line_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='filtered',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Lambda(
                                                                        args=arguments(
                                                                            posonlyargs=[],
                                                                            args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                                            vararg=None,
                                                                            kwonlyargs=[],
                                                                            kw_defaults=[],
                                                                            kwarg=None,
                                                                            defaults=[],
                                                                        ),
                                                                        body=Compare(
                                                                            left=Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
                                                                                attr='state',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ops=[Eq()],
                                                                            comparators=[Constant(value='done', kind=None)],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='package_level', ctx=Load()),
                                                                            attr='state',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='done', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='package_level', ctx=Load()),
                                                                                        attr='move_line_ids',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='filtered',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Lambda(
                                                                                        args=arguments(
                                                                                            posonlyargs=[],
                                                                                            args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                                                            vararg=None,
                                                                                            kwonlyargs=[],
                                                                                            kw_defaults=[],
                                                                                            kwarg=None,
                                                                                            defaults=[],
                                                                                        ),
                                                                                        body=Compare(
                                                                                            left=Attribute(
                                                                                                value=Name(id='ml', ctx=Load()),
                                                                                                attr='state',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            ops=[Eq()],
                                                                                            comparators=[Constant(value='cancel', kind=None)],
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='package_level', ctx=Load()),
                                                                                        attr='move_ids',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='filtered',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Lambda(
                                                                                        args=arguments(
                                                                                            posonlyargs=[],
                                                                                            args=[arg(arg='m', annotation=None, type_comment=None)],
                                                                                            vararg=None,
                                                                                            kwonlyargs=[],
                                                                                            kw_defaults=[],
                                                                                            kwarg=None,
                                                                                            defaults=[],
                                                                                        ),
                                                                                        body=Compare(
                                                                                            left=Attribute(
                                                                                                value=Name(id='m', ctx=Load()),
                                                                                                attr='state',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            ops=[Eq()],
                                                                                            comparators=[Constant(value='cancel', kind=None)],
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='package_level', ctx=Load()),
                                                                                    attr='state',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value='cancel', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='package_level', ctx=Load()),
                                                                                    attr='state',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Constant(value='draft', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='move_ids', kind=None),
                                Constant(value='move_ids.state', kind=None),
                                Constant(value='move_line_ids', kind=None),
                                Constant(value='move_line_ids.state', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_show_lot',
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
                            target=Name(id='package_level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='tracking',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value='none', kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='ml', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='package_level', ctx=Load()),
                                                            attr='move_line_ids',
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
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='package_level', ctx=Load()),
                                                                attr='picking_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='picking_type_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='use_existing_lots',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='package_level', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='done', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='package_level', ctx=Load()),
                                                            attr='show_lots_m2o',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='package_level', ctx=Load()),
                                                            attr='show_lots_text',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='picking_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='picking_type_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='use_create_lots',
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='package_level', ctx=Load()),
                                                                    attr='state',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value='done', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='package_level', ctx=Load()),
                                                                    attr='show_lots_m2o',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=False, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='package_level', ctx=Load()),
                                                                    attr='show_lots_text',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=True, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='package_level', ctx=Load()),
                                                                    attr='show_lots_m2o',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=False, kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='package_level', ctx=Load()),
                                                                    attr='show_lots_text',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=False, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='show_lots_m2o',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='show_lots_text',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
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
                    name='_generate_moves',
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
                            target=Name(id='package_level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='package_level', ctx=Load()),
                                        attr='package_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='quant', ctx=Store()),
                                            iter=Attribute(
                                                value=Attribute(
                                                    value=Name(id='package_level', ctx=Load()),
                                                    attr='package_id',
                                                    ctx=Load(),
                                                ),
                                                attr='quant_ids',
                                                ctx=Load(),
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
                                                                slice=Constant(value='stock.move', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='picking_id', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_uom_qty', kind=None),
                                                                    Constant(value='product_uom', kind=None),
                                                                    Constant(value='location_id', kind=None),
                                                                    Constant(value='location_dest_id', kind=None),
                                                                    Constant(value='package_level_id', kind=None),
                                                                    Constant(value='company_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='package_level', ctx=Load()),
                                                                            attr='picking_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='quant', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='display_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='quant', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='quant', ctx=Load()),
                                                                        attr='quantity',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='quant', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='uom_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='package_level', ctx=Load()),
                                                                            attr='location_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='package_level', ctx=Load()),
                                                                            attr='location_dest_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='package_level', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='package_level', ctx=Load()),
                                                                            attr='company_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
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
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockPackageLevel', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='location_dest_id', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='move_line_ids', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='location_dest_id', kind=None)],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Constant(value='location_dest_id', kind=None),
                                                        ctx=Load(),
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
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='move_ids', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='location_dest_id', kind=None)],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Constant(value='location_dest_id', kind=None),
                                                        ctx=Load(),
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
                        Return(
                            value=Name(id='result', ctx=Load()),
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
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockPackageLevel', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='location_dest_id', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='move_line_ids', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='location_dest_id', kind=None)],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Constant(value='location_dest_id', kind=None),
                                                        ctx=Load(),
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
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='move_ids', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='location_dest_id', kind=None)],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Constant(value='location_dest_id', kind=None),
                                                        ctx=Load(),
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
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
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
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='move_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='package_level_id', kind=None)],
                                        values=[Constant(value=False, kind=None)],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='move_line_ids', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='result_package_id', kind=None)],
                                        values=[Constant(value=False, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockPackageLevel', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_move_lines_map_quant_package',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='package', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='qty_done', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' should compare in good uom ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='all_in', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pack_move_lines', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='move_line_ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='keys', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='product_id', kind=None),
                                    Constant(value='lot_id', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='sorted_key',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='object', annotation=None, type_comment=None)],
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
                                            value=Name(id='object', ctx=Load()),
                                            attr='ensure_one',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=List(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='object', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='object', ctx=Load()),
                                                    attr='lot_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='grouped_quants', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='k', ctx=Store()),
                                    Name(id='g', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='groupby', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='package', ctx=Load()),
                                                attr='quant_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Name(id='sorted_key', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Call(
                                            func=Name(id='itemgetter', ctx=Load()),
                                            args=[
                                                Starred(
                                                    value=Name(id='keys', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='grouped_quants', ctx=Load()),
                                            slice=Name(id='k', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='stock.quant', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='concat',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Starred(
                                                                value=Call(
                                                                    func=Name(id='list', ctx=Load()),
                                                                    args=[Name(id='g', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='quantity', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='grouped_ops', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='k', ctx=Store()),
                                    Name(id='g', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='groupby', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[Name(id='pack_move_lines', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='key',
                                                value=Name(id='sorted_key', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Call(
                                            func=Name(id='itemgetter', ctx=Load()),
                                            args=[
                                                Starred(
                                                    value=Name(id='keys', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='grouped_ops', ctx=Load()),
                                            slice=Name(id='k', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='stock.move.line', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='concat',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Starred(
                                                                value=Call(
                                                                    func=Name(id='list', ctx=Load()),
                                                                    args=[Name(id='g', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='field', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='grouped_quants', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='key', ctx=Load()),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='grouped_ops', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='key', ctx=Load()),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value=0, kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='key', ctx=Store()),
                                                        iter=Name(id='grouped_quants', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Name(id='grouped_ops', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='key', ctx=Load()),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='grouped_quants', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Name(id='key', ctx=Load()),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[Constant(value=0, kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='key', ctx=Store()),
                                                        iter=Name(id='grouped_ops', ctx=Load()),
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
                            body=[
                                Assign(
                                    targets=[Name(id='all_in', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='all_in', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_location_id',
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
                            target=Name(id='pl', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='pl', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='new', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='pl', ctx=Load()),
                                                attr='is_fresh_package',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='pl', ctx=Load()),
                                                    attr='location_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='pl', ctx=Load()),
                                                attr='package_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='pl', ctx=Load()),
                                                            attr='location_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='pl', ctx=Load()),
                                                            attr='package_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='location_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='pl', ctx=Load()),
                                                                    attr='state',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='confirmed', kind=None)],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='pl', ctx=Load()),
                                                                attr='move_ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='pl', ctx=Load()),
                                                                    attr='location_id',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='pl', ctx=Load()),
                                                                        attr='move_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='location_id',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='pl', ctx=Load()),
                                                                            attr='state',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[In()],
                                                                        comparators=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='assigned', kind=None),
                                                                                    Constant(value='done', kind=None),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='pl', ctx=Load()),
                                                                        attr='move_line_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='pl', ctx=Load()),
                                                                            attr='location_id',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='pl', ctx=Load()),
                                                                                attr='move_line_ids',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='location_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='pl', ctx=Load()),
                                                                            attr='location_id',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='pl', ctx=Load()),
                                                                            attr='picking_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='location_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='package_id', kind=None),
                                Constant(value='state', kind=None),
                                Constant(value='is_fresh_package', kind=None),
                                Constant(value='move_ids', kind=None),
                                Constant(value='move_line_ids', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_show_package_details',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='view', ctx=Store())],
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
                                args=[Constant(value='stock.package_level_form_edit_view', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='views', kind=None),
                                    Constant(value='view_id', kind=None),
                                    Constant(value='target', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='flags', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Package Content', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='form', kind=None),
                                    Constant(value='stock.package_level', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='view', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='view', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='new', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[Constant(value='mode', kind=None)],
                                        values=[Constant(value='readonly', kind=None)],
                                    ),
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
    ],
    type_ignores=[],
)
