Module(
    body=[
        ImportFrom(
            module='odoo.addons.account.tests.common',
            names=[alias(name='AccountTestInvoicingCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestProductMargin',
            bases=[Name(id='AccountTestInvoicingCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_product_margin',
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
                            value=Constant(value=' In order to test the product_margin module ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='supplier', ctx=Store())],
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
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Supplier', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='customer', ctx=Store())],
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
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Customer', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ipad', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='standard_price', kind=None),
                                            Constant(value='list_price', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Ipad', kind=None),
                                            Constant(value=500.0, kind=None),
                                            Constant(value=750.0, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoices', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='account.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='invoice_line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='in_invoice', kind=None),
                                                    Attribute(
                                                        value=Name(id='supplier', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                            Constant(value='price_unit', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='ipad', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=10.0, kind=None),
                                                                            Constant(value=300.0, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='invoice_line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='in_invoice', kind=None),
                                                    Attribute(
                                                        value=Name(id='supplier', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                            Constant(value='price_unit', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='ipad', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=4.0, kind=None),
                                                                            Constant(value=450.0, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='invoice_line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='out_invoice', kind=None),
                                                    Attribute(
                                                        value=Name(id='customer', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                            Constant(value='price_unit', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='ipad', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=20.0, kind=None),
                                                                            Constant(value=750.0, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='move_type', kind=None),
                                                    Constant(value='partner_id', kind=None),
                                                    Constant(value='invoice_line_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='out_invoice', kind=None),
                                                    Attribute(
                                                        value=Name(id='customer', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=0, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='product_id', kind=None),
                                                                            Constant(value='quantity', kind=None),
                                                                            Constant(value='price_unit', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='ipad', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=10.0, kind=None),
                                                                            Constant(value=550.0, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='invoices', ctx=Load()),
                                    attr='invoice_date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Subscript(
                                    value=Name(id='invoices', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                attr='date',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='invoices', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ipad', ctx=Load()),
                                    attr='_compute_product_margin_fields_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sale_turnover', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value=20.0, kind=None),
                                    op=Mult(),
                                    right=Constant(value=750.0, kind=None),
                                ),
                                op=Add(),
                                right=BinOp(
                                    left=Constant(value=10.0, kind=None),
                                    op=Mult(),
                                    right=Constant(value=550.0, kind=None),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sale_expected', ctx=Store())],
                            value=BinOp(
                                left=Constant(value=750.0, kind=None),
                                op=Mult(),
                                right=Constant(value=30.0, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='purchase_total_cost', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value=10.0, kind=None),
                                    op=Mult(),
                                    right=Constant(value=300.0, kind=None),
                                ),
                                op=Add(),
                                right=BinOp(
                                    left=Constant(value=4.0, kind=None),
                                    op=Mult(),
                                    right=Constant(value=450.0, kind=None),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='purchase_normal_cost', ctx=Store())],
                            value=BinOp(
                                left=Constant(value=14.0, kind=None),
                                op=Mult(),
                                right=Constant(value=500.0, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='total_margin', ctx=Store())],
                            value=BinOp(
                                left=Name(id='sale_turnover', ctx=Load()),
                                op=Sub(),
                                right=Name(id='purchase_total_cost', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected_margin', ctx=Store())],
                            value=BinOp(
                                left=Name(id='sale_expected', ctx=Load()),
                                op=Sub(),
                                right=Name(id='purchase_normal_cost', ctx=Load()),
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
                                            value=Name(id='result', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='ipad', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='total_margin', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='total_margin', ctx=Load()),
                                    Constant(value='Wrong Total Margin.', kind=None),
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
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='ipad', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='expected_margin', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='expected_margin', ctx=Load()),
                                    Constant(value='Wrong Expected Margin.', kind=None),
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
