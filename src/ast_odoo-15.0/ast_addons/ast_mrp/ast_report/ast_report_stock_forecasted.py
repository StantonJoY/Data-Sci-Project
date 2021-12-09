Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ReplenishmentReport',
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='report.stock.report_product_product_replenishment', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_move_draft_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_template_ids', annotation=None, type_comment=None),
                            arg(arg='product_variant_ids', annotation=None, type_comment=None),
                            arg(arg='wh_location_ids', annotation=None, type_comment=None),
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
                                Tuple(
                                    elts=[
                                        Name(id='in_domain', ctx=Store()),
                                        Name(id='out_domain', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_move_draft_domain',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product_template_ids', ctx=Load()),
                                    Name(id='product_variant_ids', ctx=Load()),
                                    Name(id='wh_location_ids', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='in_domain', ctx=Store()),
                            op=Add(),
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='production_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                        AugAssign(
                            target=Name(id='out_domain', ctx=Store()),
                            op=Add(),
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='raw_material_production_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='in_domain', ctx=Load()),
                                    Name(id='out_domain', ctx=Load()),
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
                    name='_compute_draft_quantity_count',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_template_ids', annotation=None, type_comment=None),
                            arg(arg='product_variant_ids', annotation=None, type_comment=None),
                            arg(arg='wh_location_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_compute_draft_quantity_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product_template_ids', ctx=Load()),
                                    Name(id='product_variant_ids', ctx=Load()),
                                    Name(id='wh_location_ids', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='draft_production_qty', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_product_domain',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product_template_ids', ctx=Load()),
                                    Name(id='product_variant_ids', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='domain', ctx=Store()),
                            op=Add(),
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='draft', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mo_domain', ctx=Store())],
                            value=BinOp(
                                left=Name(id='domain', ctx=Load()),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='location_dest_id', kind=None),
                                                Constant(value='in', kind=None),
                                                Name(id='wh_location_ids', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='grouped_mo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mrp.production', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='mo_domain', ctx=Load()),
                                    List(
                                        elts=[Constant(value='product_qty:sum', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Constant(value='product_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='draft_production_qty', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='in', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='mo', ctx=Load()),
                                            slice=Constant(value='product_qty', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='mo', ctx=Store()),
                                                iter=Name(id='grouped_mo', ctx=Load()),
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
                            targets=[Name(id='move_domain', ctx=Store())],
                            value=BinOp(
                                left=Name(id='domain', ctx=Load()),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='raw_material_production_id', kind=None),
                                                Constant(value='!=', kind=None),
                                                Constant(value=False, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='location_id', kind=None),
                                                Constant(value='in', kind=None),
                                                Name(id='wh_location_ids', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='grouped_moves', ctx=Store())],
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
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='move_domain', ctx=Load()),
                                    List(
                                        elts=[Constant(value='product_qty:sum', kind=None)],
                                        ctx=Load(),
                                    ),
                                    Constant(value='product_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='draft_production_qty', kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='out', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Subscript(
                                            value=Name(id='move', ctx=Load()),
                                            slice=Constant(value='product_qty', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='move', ctx=Store()),
                                                iter=Name(id='grouped_moves', ctx=Load()),
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
                        AugAssign(
                            target=Subscript(
                                value=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='draft_production_qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='in', kind=None),
                                ctx=Load(),
                            ),
                        ),
                        AugAssign(
                            target=Subscript(
                                value=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='out', kind=None),
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='draft_production_qty', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='out', kind=None),
                                ctx=Load(),
                            ),
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
