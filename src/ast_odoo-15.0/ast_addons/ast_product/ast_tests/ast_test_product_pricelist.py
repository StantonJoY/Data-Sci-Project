Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_compare', asname=None),
                alias(name='test_reports', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestProductPricelist',
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
                                            Name(id='TestProductPricelist', ctx=Load()),
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
                                    attr='ProductPricelist',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.pricelist', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='res_partner_4',
                                    ctx=Store(),
                                ),
                            ],
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
                                        values=[Constant(value='Ready Mat', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='res_partner_1',
                                    ctx=Store(),
                                ),
                            ],
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
                                        values=[Constant(value='Wood Corner', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='category_5_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='product.category', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='create',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Dict(
                                            keys=[
                                                Constant(value='name', kind=None),
                                                Constant(value='parent_id', kind=None),
                                            ],
                                            values=[
                                                Constant(value='Office Furniture', kind=None),
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
                                                        args=[Constant(value='product.product_category_1', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='computer_SC234',
                                    ctx=Store(),
                                ),
                            ],
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
                                            Constant(value='categ_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Desk Combination', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category_5_id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ipad_retina_display',
                                    ctx=Store(),
                                ),
                            ],
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
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Customizable Desk', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='custom_computer_kit',
                                    ctx=Store(),
                                ),
                            ],
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
                                            Constant(value='categ_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Corner Desk Right Sit', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category_5_id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ipad_mini',
                                    ctx=Store(),
                                ),
                            ],
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
                                            Constant(value='categ_id', kind=None),
                                            Constant(value='standard_price', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Large Cabinet', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category_5_id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=800.0, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='monitor',
                                    ctx=Store(),
                                ),
                            ],
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
                                            Constant(value='categ_id', kind=None),
                                            Constant(value='list_price', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Super nice monitor', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category_5_id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1000.0, kind=None),
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
                                        slice=Constant(value='product.supplierinfo', kind=None),
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
                                                    Constant(value='name', kind=None),
                                                    Constant(value='product_tmpl_id', kind=None),
                                                    Constant(value='delay', kind=None),
                                                    Constant(value='min_qty', kind=None),
                                                    Constant(value='price', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='res_partner_1',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='ipad_mini',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_tmpl_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=750, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='product_tmpl_id', kind=None),
                                                    Constant(value='delay', kind=None),
                                                    Constant(value='min_qty', kind=None),
                                                    Constant(value='price', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='res_partner_4',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='ipad_mini',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_tmpl_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=790, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='product_tmpl_id', kind=None),
                                                    Constant(value='delay', kind=None),
                                                    Constant(value='min_qty', kind=None),
                                                    Constant(value='price', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='res_partner_4',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='ipad_mini',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_tmpl_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=785, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='product_tmpl_id', kind=None),
                                                    Constant(value='delay', kind=None),
                                                    Constant(value='min_qty', kind=None),
                                                    Constant(value='price', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='res_partner_4',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='monitor',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_tmpl_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value=100, kind=None),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='apple_in_ear_headphones',
                                    ctx=Store(),
                                ),
                            ],
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
                                            Constant(value='categ_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Storage Box', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category_5_id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='laptop_E5023',
                                    ctx=Store(),
                                ),
                            ],
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
                                            Constant(value='categ_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Office Chair', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category_5_id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='laptop_S3450',
                                    ctx=Store(),
                                ),
                            ],
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
                                            Constant(value='categ_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Acoustic Bloc Screens', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category_5_id',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='uom_unit_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='uom.product_uom_unit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='list0',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product.list0', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ipad_retina_display',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='uom_id', kind=None),
                                            Constant(value='categ_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='uom_unit_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='category_5_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='customer_pricelist',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ProductPricelist',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='item_ids', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Customer Pricelist', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='compute_price', kind=None),
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value='base_pricelist_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Default pricelist', kind=None),
                                                                    Constant(value='formula', kind=None),
                                                                    Constant(value='pricelist', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='list0',
                                                                        ctx=Load(),
                                                                    ),
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
                                                                    Constant(value='applied_on', kind=None),
                                                                    Constant(value='product_tmpl_id', kind=None),
                                                                    Constant(value='compute_price', kind=None),
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value='price_discount', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='10% Discount on Assemble Computer', kind=None),
                                                                    Constant(value='1_product', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='ipad_retina_display',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='product_tmpl_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='formula', kind=None),
                                                                    Constant(value='list_price', kind=None),
                                                                    Constant(value=10, kind=None),
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
                                                                    Constant(value='applied_on', kind=None),
                                                                    Constant(value='product_tmpl_id', kind=None),
                                                                    Constant(value='compute_price', kind=None),
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value='price_surcharge', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='1 surchange on Laptop', kind=None),
                                                                    Constant(value='1_product', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='laptop_E5023',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='product_tmpl_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='formula', kind=None),
                                                                    Constant(value='list_price', kind=None),
                                                                    Constant(value=1, kind=None),
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
                                                                    Constant(value='applied_on', kind=None),
                                                                    Constant(value='min_quantity', kind=None),
                                                                    Constant(value='compute_price', kind=None),
                                                                    Constant(value='base', kind=None),
                                                                    Constant(value='categ_id', kind=None),
                                                                    Constant(value='price_discount', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='5% Discount on all Computer related products', kind=None),
                                                                    Constant(value='2_product_category', kind=None),
                                                                    Constant(value=2, kind=None),
                                                                    Constant(value='formula', kind=None),
                                                                    Constant(value='list_price', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='category_5_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=5, kind=None),
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
                                                                    Constant(value='applied_on', kind=None),
                                                                    Constant(value='date_start', kind=None),
                                                                    Constant(value='date_end', kind=None),
                                                                    Constant(value='compute_price', kind=None),
                                                                    Constant(value='price_discount', kind=None),
                                                                    Constant(value='base', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='30% Discount on all products', kind=None),
                                                                    Constant(value='3_global', kind=None),
                                                                    Constant(value='2011-12-27', kind=None),
                                                                    Constant(value='2011-12-31', kind=None),
                                                                    Constant(value='formula', kind=None),
                                                                    Constant(value=30, kind=None),
                                                                    Constant(value='list_price', kind=None),
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
                                                                    Constant(value='applied_on', kind=None),
                                                                    Constant(value='product_tmpl_id', kind=None),
                                                                    Constant(value='date_start', kind=None),
                                                                    Constant(value='date_end', kind=None),
                                                                    Constant(value='compute_price', kind=None),
                                                                    Constant(value='price_discount', kind=None),
                                                                    Constant(value='base', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Fixed on all products', kind=None),
                                                                    Constant(value='1_product', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='monitor',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='product_tmpl_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='2020-04-06 09:00:00', kind=None),
                                                                    Constant(value='2020-04-09 12:00:00', kind=None),
                                                                    Constant(value='formula', kind=None),
                                                                    Constant(value=50, kind=None),
                                                                    Constant(value='list_price', kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_10_calculation_price_of_products_pricelist',
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
                            value=Constant(value='Test calculation of product price based on pricelist', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='pricelist', kind=None),
                                            Constant(value='quantity', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='customer_pricelist',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ipad_retina_display', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ipad_retina_display',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='Wrong sale price: Customizable Desk. should be %s instead of %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='ipad_retina_display', ctx=Load()),
                                            attr='price',
                                            ctx=Load(),
                                        ),
                                        BinOp(
                                            left=Attribute(
                                                value=Name(id='ipad_retina_display', ctx=Load()),
                                                attr='lst_price',
                                                ctx=Load(),
                                            ),
                                            op=Sub(),
                                            right=BinOp(
                                                left=Attribute(
                                                    value=Name(id='ipad_retina_display', ctx=Load()),
                                                    attr='lst_price',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Constant(value=0.1, kind=None),
                                            ),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='ipad_retina_display', ctx=Load()),
                                                attr='price',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='ipad_retina_display', ctx=Load()),
                                                    attr='lst_price',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='ipad_retina_display', ctx=Load()),
                                                        attr='lst_price',
                                                        ctx=Load(),
                                                    ),
                                                    op=Mult(),
                                                    right=Constant(value=0.1, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Name(id='msg', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='laptop_E5023', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='laptop_E5023',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='Wrong sale price: Laptop. should be %s instead of %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='laptop_E5023', ctx=Load()),
                                            attr='price',
                                            ctx=Load(),
                                        ),
                                        BinOp(
                                            left=Attribute(
                                                value=Name(id='laptop_E5023', ctx=Load()),
                                                attr='lst_price',
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='laptop_E5023', ctx=Load()),
                                                attr='price',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='laptop_E5023', ctx=Load()),
                                                    attr='lst_price',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Name(id='msg', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='apple_headphones', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='apple_in_ear_headphones',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='Wrong sale price: IT component. should be %s instead of %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='apple_headphones', ctx=Load()),
                                            attr='price',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='apple_headphones', ctx=Load()),
                                            attr='lst_price',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='apple_headphones', ctx=Load()),
                                                attr='price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='apple_headphones', ctx=Load()),
                                                attr='lst_price',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Name(id='msg', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='quantity', kind=None)],
                                        values=[Constant(value=5, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='laptop_S3450', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='laptop_S3450',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='Wrong sale price: IT component if more than 3 Unit. should be %s instead of %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='laptop_S3450', ctx=Load()),
                                            attr='price',
                                            ctx=Load(),
                                        ),
                                        BinOp(
                                            left=Attribute(
                                                value=Name(id='laptop_S3450', ctx=Load()),
                                                attr='lst_price',
                                                ctx=Load(),
                                            ),
                                            op=Sub(),
                                            right=BinOp(
                                                left=Attribute(
                                                    value=Name(id='laptop_S3450', ctx=Load()),
                                                    attr='lst_price',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Constant(value=0.05, kind=None),
                                            ),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='laptop_S3450', ctx=Load()),
                                                attr='price',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='laptop_S3450', ctx=Load()),
                                                    attr='lst_price',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='laptop_S3450', ctx=Load()),
                                                        attr='lst_price',
                                                        ctx=Load(),
                                                    ),
                                                    op=Mult(),
                                                    right=Constant(value=0.05, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Name(id='msg', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='quantity', kind=None)],
                                        values=[Constant(value=1, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ipad_mini', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ipad_mini',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='Wrong sale price: LCD Monitor. should be %s instead of %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='ipad_mini', ctx=Load()),
                                            attr='price',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='ipad_mini', ctx=Load()),
                                            attr='lst_price',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='ipad_mini', ctx=Load()),
                                                attr='price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='ipad_mini', ctx=Load()),
                                                attr='lst_price',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Name(id='msg', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quantity', kind=None),
                                            Constant(value='date', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Constant(value='2011-12-31', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ipad_mini', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ipad_mini',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='Wrong sale price: LCD Monitor on end of year. should be %s instead of %s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='ipad_mini', ctx=Load()),
                                            attr='price',
                                            ctx=Load(),
                                        ),
                                        BinOp(
                                            left=Attribute(
                                                value=Name(id='ipad_mini', ctx=Load()),
                                                attr='lst_price',
                                                ctx=Load(),
                                            ),
                                            op=Sub(),
                                            right=BinOp(
                                                left=Attribute(
                                                    value=Name(id='ipad_mini', ctx=Load()),
                                                    attr='lst_price',
                                                    ctx=Load(),
                                                ),
                                                op=Mult(),
                                                right=Constant(value=0.3, kind=None),
                                            ),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
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
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='ipad_mini', ctx=Load()),
                                                attr='price',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='ipad_mini', ctx=Load()),
                                                    attr='lst_price',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=BinOp(
                                                    left=Attribute(
                                                        value=Name(id='ipad_mini', ctx=Load()),
                                                        attr='lst_price',
                                                        ctx=Load(),
                                                    ),
                                                    op=Mult(),
                                                    right=Constant(value=0.3, kind=None),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Name(id='msg', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quantity', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='partner_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='res_partner_4',
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
                        Assign(
                            targets=[Name(id='ipad_mini', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ipad_mini',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='res_partner_4',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='Wrong cost price: LCD Monitor. should be 790 instead of %s', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ipad_mini', ctx=Load()),
                                            attr='_select_seller',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Name(id='partner', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='quantity',
                                                value=Constant(value=1.0, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='price',
                                    ctx=Load(),
                                ),
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
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='ipad_mini', ctx=Load()),
                                                        attr='_select_seller',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='partner_id',
                                                            value=Name(id='partner', ctx=Load()),
                                                        ),
                                                        keyword(
                                                            arg='quantity',
                                                            value=Constant(value=1.0, kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='price',
                                                ctx=Load(),
                                            ),
                                            Constant(value=790, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Name(id='msg', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='quantity', kind=None)],
                                        values=[Constant(value=3, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ipad_mini', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ipad_mini',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='res_partner_4',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='Wrong cost price: LCD Monitor if more than 3 Unit.should be 785 instead of %s', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ipad_mini', ctx=Load()),
                                            attr='_select_seller',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Name(id='partner', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='quantity',
                                                value=Constant(value=3.0, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='price',
                                    ctx=Load(),
                                ),
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
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='ipad_mini', ctx=Load()),
                                                        attr='_select_seller',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='partner_id',
                                                            value=Name(id='partner', ctx=Load()),
                                                        ),
                                                        keyword(
                                                            arg='quantity',
                                                            value=Constant(value=3.0, kind=None),
                                                        ),
                                                    ],
                                                ),
                                                attr='price',
                                                ctx=Load(),
                                            ),
                                            Constant(value=785, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Name(id='msg', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quantity', kind=None),
                                            Constant(value='date', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2020-04-05 08:00:00', kind=None),
                                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='monitor', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='monitor',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='res_partner_4',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='Wrong cost price: LCD Monitor. should be 1000 instead of %s', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='monitor', ctx=Load()),
                                            attr='_select_seller',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Name(id='partner', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='quantity',
                                                value=Constant(value=1.0, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='price',
                                    ctx=Load(),
                                ),
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
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='monitor', ctx=Load()),
                                                attr='price',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='monitor', ctx=Load()),
                                                attr='lst_price',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
                                    Name(id='msg', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='context', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='quantity', kind=None),
                                            Constant(value='date', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='strptime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='2020-04-06 10:00:00', kind=None),
                                                    Constant(value='%Y-%m-%d %H:%M:%S', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='monitor', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='monitor',
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[Name(id='context', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='Wrong cost price: LCD Monitor. should be 500 instead of %s', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='monitor', ctx=Load()),
                                            attr='_select_seller',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='partner_id',
                                                value=Name(id='partner', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='quantity',
                                                value=Constant(value=1.0, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='price',
                                    ctx=Load(),
                                ),
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
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='monitor', ctx=Load()),
                                                attr='price',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='monitor', ctx=Load()),
                                                    attr='lst_price',
                                                    ctx=Load(),
                                                ),
                                                op=Div(),
                                                right=Constant(value=2, kind=None),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Constant(value=2, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value=0, kind=None),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
