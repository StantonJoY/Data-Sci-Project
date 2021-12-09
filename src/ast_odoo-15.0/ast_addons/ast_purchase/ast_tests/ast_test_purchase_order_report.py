Module(
    body=[
        ImportFrom(
            module='odoo.addons.account.tests.common',
            names=[alias(name='AccountTestInvoicingCommon', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='Form', asname=None),
                alias(name='tagged', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestPurchaseOrderReport',
            bases=[Name(id='AccountTestInvoicingCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_00_purchase_order_report',
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
                            targets=[Name(id='uom_dozen', ctx=Store())],
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
                                args=[Constant(value='uom.product_uom_dozen', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='po', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='purchase.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner_id', kind=None),
                                            Constant(value='currency_id', kind=None),
                                            Constant(value='order_line', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='partner_a',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='currency_data',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='currency', kind=None),
                                                    ctx=Load(),
                                                ),
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
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                    Constant(value='product_uom', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='date_planned', kind=None),
                                                                    Constant(value='taxes_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_a',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_a',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=1.0, kind=None),
                                                                    Attribute(
                                                                        value=Name(id='uom_dozen', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=100.0, kind=None),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='datetime', ctx=Load()),
                                                                            attr='today',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='product_id', kind=None),
                                                                    Constant(value='product_qty', kind=None),
                                                                    Constant(value='product_uom', kind=None),
                                                                    Constant(value='price_unit', kind=None),
                                                                    Constant(value='date_planned', kind=None),
                                                                    Constant(value='taxes_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_b',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='product_b',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=1.0, kind=None),
                                                                    Attribute(
                                                                        value=Name(id='uom_dozen', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=200.0, kind=None),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='datetime', ctx=Load()),
                                                                            attr='today',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    Constant(value=False, kind=None),
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
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='po', ctx=Load()),
                                    attr='button_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='f', ctx=Store())],
                            value=Call(
                                func=Name(id='Form', ctx=Load()),
                                args=[
                                    Call(
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
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='default_move_type',
                                                value=Constant(value='in_invoice', kind=None),
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
                                Attribute(
                                    value=Name(id='f', ctx=Load()),
                                    attr='invoice_date',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='f', ctx=Load()),
                                attr='date',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='f', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='po', ctx=Load()),
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='f', ctx=Load()),
                                    attr='purchase_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='po', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='invoice', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='f', ctx=Load()),
                                    attr='save',
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
                                    value=Name(id='invoice', ctx=Load()),
                                    attr='action_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='po', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res_product1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='purchase.report', kind=None),
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
                                                    Constant(value='order_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='po', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_a',
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
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='company', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='res_product1', ctx=Load()),
                                        attr='qty_ordered',
                                        ctx=Load(),
                                    ),
                                    Constant(value=12.0, kind=None),
                                    Constant(value='UoM conversion is not working', kind=None),
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
                                        value=Name(id='res_product1', ctx=Load()),
                                        attr='price_total',
                                        ctx=Load(),
                                    ),
                                    Constant(value=50.0, kind=None),
                                    Constant(value='Currency conversion is not working', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res_product2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='purchase.report', kind=None),
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
                                                    Constant(value='order_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='po', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_b',
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
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='company_data',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='company', kind=None),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='res_product2', ctx=Load()),
                                        attr='qty_ordered',
                                        ctx=Load(),
                                    ),
                                    Constant(value=1.0, kind=None),
                                    Constant(value='No conversion needed since product_b is already a dozen', kind=None),
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
                                        value=Name(id='res_product2', ctx=Load()),
                                        attr='price_total',
                                        ctx=Load(),
                                    ),
                                    Constant(value=100.0, kind=None),
                                    Constant(value='Currency conversion is not working', kind=None),
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
