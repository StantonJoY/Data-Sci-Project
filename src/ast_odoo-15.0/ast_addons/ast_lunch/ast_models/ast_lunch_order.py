Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='ValidationError', asname=None),
                alias(name='UserError', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='LunchOrder',
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
                    value=Constant(value='lunch.order', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Lunch Order', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='id desc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_display_name', ctx=Store())],
                    value=Constant(value='product_id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.name', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Product Name', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='topping_ids_1', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='lunch.topping', kind=None),
                            Constant(value='lunch_order_topping', kind=None),
                            Constant(value='order_id', kind=None),
                            Constant(value='topping_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Extras 1', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='topping_category', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value=1, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='topping_ids_2', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='lunch.topping', kind=None),
                            Constant(value='lunch_order_topping', kind=None),
                            Constant(value='order_id', kind=None),
                            Constant(value='topping_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Extras 2', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='topping_category', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value=2, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='topping_ids_3', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='lunch.topping', kind=None),
                            Constant(value='lunch_order_topping', kind=None),
                            Constant(value='order_id', kind=None),
                            Constant(value='topping_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Extras 3', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='topping_category', kind=None),
                                                Constant(value='=', kind=None),
                                                Constant(value=3, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='lunch.product', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Product', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='category_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Product Category', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.category_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Order Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='new', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            keyword(
                                arg='default',
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='context_today',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='supplier_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Vendor', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.supplier_id', kind=None),
                            ),
                            keyword(
                                arg='store',
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
                Assign(
                    targets=[Name(id='user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.users', kind=None),
                            Constant(value='User', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='states',
                                value=Dict(
                                    keys=[Constant(value='new', kind=None)],
                                    values=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='readonly', kind=None),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lunch_location_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='lunch.location', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='last_lunch_location_id',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='note', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Notes', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='price', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Total Price', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_total_price', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Active', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
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
                                            Constant(value='new', kind=None),
                                            Constant(value='To Order', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='ordered', kind=None),
                                            Constant(value='Ordered', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='confirmed', kind=None),
                                            Constant(value='Received', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='cancelled', kind=None),
                                            Constant(value='Cancelled', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Constant(value='Status', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='new', kind=None),
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
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='currency_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.currency_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='quantity', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Quantity', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='display_toppings', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Extras', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_display_toppings', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_description', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Description', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.description', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='topping_label_1', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.supplier_id.topping_label_1', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='topping_label_2', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.supplier_id.topping_label_2', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='topping_label_3', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.supplier_id.topping_label_3', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='topping_quantity_1', ctx=Store())],
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
                                value=Constant(value='product_id.supplier_id.topping_quantity_1', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='topping_quantity_2', ctx=Store())],
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
                                value=Constant(value='product_id.supplier_id.topping_quantity_2', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='topping_quantity_3', ctx=Store())],
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
                                value=Constant(value='product_id.supplier_id.topping_quantity_3', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='image_1920', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_images', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='image_128', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_images', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='available_toppings_1', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Are extras available for this product', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_available_toppings', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='available_toppings_2', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Are extras available for this product', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_available_toppings', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='available_toppings_3', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Are extras available for this product', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_available_toppings', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='display_reorder_button', ctx=Store())],
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
                                value=Constant(value='_compute_display_reorder_button', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_product_images',
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
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='image_1920',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='image_1920',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='category_id',
                                                    ctx=Load(),
                                                ),
                                                attr='image_1920',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='image_128',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='image_128',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='category_id',
                                                    ctx=Load(),
                                                ),
                                                attr='image_128',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
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
                            args=[Constant(value='product_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_available_toppings',
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
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='available_toppings_1',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='lunch.topping', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search_count',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='supplier_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='order', ctx=Load()),
                                                                            attr='supplier_id',
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
                                                                    Constant(value='topping_category', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=1, kind=None),
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
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='available_toppings_2',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='lunch.topping', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search_count',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='supplier_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='order', ctx=Load()),
                                                                            attr='supplier_id',
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
                                                                    Constant(value='topping_category', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=2, kind=None),
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
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='available_toppings_3',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='order', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='lunch.topping', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search_count',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='supplier_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='order', ctx=Load()),
                                                                            attr='supplier_id',
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
                                                                    Constant(value='topping_category', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=3, kind=None),
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
                                        keywords=[],
                                    ),
                                    type_comment=None,
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
                            args=[Constant(value='category_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_display_reorder_button',
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
                            targets=[Name(id='show_button', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='show_reorder_button', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='display_reorder_button',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='show_button', ctx=Load()),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='order', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='confirmed', kind=None)],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
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
                                attr='depends_context',
                                ctx=Load(),
                            ),
                            args=[Constant(value='show_reorder_button', kind=None)],
                            keywords=[],
                        ),
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='state', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='init',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Constant(value='CREATE INDEX IF NOT EXISTS lunch_order_user_product_date ON %s (user_id, product_id, date)', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_table',
                                            ctx=Load(),
                                        ),
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
                    name='_extract_toppings',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n            If called in api.multi then it will pop topping_ids_1,2,3 from values\n        ', kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='topping_1', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Constant(value='topping_ids_1', kind=None),
                                            ops=[In()],
                                            comparators=[Name(id='values', ctx=Load())],
                                        ),
                                        body=Subscript(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='values', ctx=Load()),
                                                        attr='pop',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='topping_ids_1', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        orelse=Attribute(
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='self', ctx=Load()),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=Constant(value=1, kind=None),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                attr='topping_ids_1',
                                                ctx=Load(),
                                            ),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='topping_2', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Constant(value='topping_ids_2', kind=None),
                                            ops=[In()],
                                            comparators=[Name(id='values', ctx=Load())],
                                        ),
                                        body=Subscript(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='values', ctx=Load()),
                                                        attr='pop',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='topping_ids_2', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        orelse=Attribute(
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='self', ctx=Load()),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=Constant(value=1, kind=None),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                attr='topping_ids_2',
                                                ctx=Load(),
                                            ),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='topping_3', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Constant(value='topping_ids_3', kind=None),
                                            ops=[In()],
                                            comparators=[Name(id='values', ctx=Load())],
                                        ),
                                        body=Subscript(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='values', ctx=Load()),
                                                        attr='pop',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='topping_ids_3', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        orelse=Attribute(
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Name(id='self', ctx=Load()),
                                                    slice=Slice(
                                                        lower=None,
                                                        upper=Constant(value=1, kind=None),
                                                        step=None,
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                attr='topping_ids_3',
                                                ctx=Load(),
                                            ),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='topping_1', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Constant(value='topping_ids_1', kind=None),
                                            ops=[In()],
                                            comparators=[Name(id='values', ctx=Load())],
                                        ),
                                        body=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='topping_ids_1', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        orelse=List(elts=[], ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='topping_2', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Constant(value='topping_ids_2', kind=None),
                                            ops=[In()],
                                            comparators=[Name(id='values', ctx=Load())],
                                        ),
                                        body=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='topping_ids_2', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        orelse=List(elts=[], ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='topping_3', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Constant(value='topping_ids_3', kind=None),
                                            ops=[In()],
                                            comparators=[Name(id='values', ctx=Load())],
                                        ),
                                        body=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='topping_ids_3', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        orelse=List(elts=[], ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='topping_1', ctx=Load()),
                                    op=Add(),
                                    right=Name(id='topping_2', ctx=Load()),
                                ),
                                op=Add(),
                                right=Name(id='topping_3', ctx=Load()),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_topping_quantity',
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
                            targets=[Name(id='errors', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='1_more', kind=None),
                                    Constant(value='1', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='You should order at least one %s', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='You have to order one and only one %s', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='index', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[
                                            Constant(value=1, kind=None),
                                            Constant(value=4, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='availability', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=BinOp(
                                                    left=Constant(value='available_toppings_%s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='index', ctx=Load()),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='quantity', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=BinOp(
                                                    left=Constant(value='topping_quantity_%s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='index', ctx=Load()),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='toppings', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='line', ctx=Load()),
                                                        slice=BinOp(
                                                            left=Constant(value='topping_ids_%s', kind=None),
                                                            op=Mod(),
                                                            right=Name(id='index', ctx=Load()),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='topping_category',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Name(id='index', ctx=Load())],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='label', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='line', ctx=Load()),
                                                slice=BinOp(
                                                    left=Constant(value='topping_label_%s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='index', ctx=Load()),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='availability', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='quantity', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='0_more', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='check', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='bool', ctx=Load()),
                                                        args=[
                                                            IfExp(
                                                                test=Compare(
                                                                    left=Name(id='quantity', ctx=Load()),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value='1', kind=None)],
                                                                ),
                                                                body=Compare(
                                                                    left=Call(
                                                                        func=Name(id='len', ctx=Load()),
                                                                        args=[Name(id='toppings', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value=1, kind=None)],
                                                                ),
                                                                orelse=Name(id='toppings', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='check', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='ValidationError', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Subscript(
                                                                            value=Name(id='errors', ctx=Load()),
                                                                            slice=Name(id='quantity', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Mod(),
                                                                        right=Name(id='label', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                    orelse=[],
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='topping_ids_1', kind=None),
                                Constant(value='topping_ids_2', kind=None),
                                Constant(value='topping_ids_3', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='lines', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_find_matching_lines',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            None,
                                            Constant(value='toppings', kind=None),
                                        ],
                                        values=[
                                            Name(id='values', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_extract_toppings',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='lines', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines', ctx=Load()),
                                            attr='update_quantity',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=1, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Return(
                                    value=Subscript(
                                        value=Name(id='lines', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=1, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
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
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='merge_needed', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Constant(value='note', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='topping_ids_1', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='topping_ids_2', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='topping_ids_3', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='merge_needed', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='lines_to_deactivate', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='lunch.order', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='toppings', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_extract_toppings',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='invalidate_cache',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='topping_ids_2', kind=None),
                                                            Constant(value='topping_ids_3', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='topping_ids_1', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Name(id='toppings', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='matching_lines', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_find_matching_lines',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='user_id', kind=None),
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='note', kind=None),
                                                            Constant(value='toppings', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='user_id', kind=None),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='line', ctx=Load()),
                                                                            attr='user_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='product_id', kind=None),
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
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='note', kind=None),
                                                                    BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='note',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Name(id='toppings', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='matching_lines', ctx=Load()),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='lines_to_deactivate', ctx=Store()),
                                                    op=BitOr(),
                                                    value=Name(id='line', ctx=Load()),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='matching_lines', ctx=Load()),
                                                            attr='update_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='line', ctx=Load()),
                                                                attr='quantity',
                                                                ctx=Load(),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='lines_to_deactivate', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='active', kind=None)],
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
                                                    Name(id='LunchOrder', ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='self', ctx=Load()),
                                                        op=Sub(),
                                                        right=Name(id='lines_to_deactivate', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_find_matching_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='user_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='user_id', kind=None),
                                                    Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='default_get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[Constant(value='user_id', kind=None)],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value='user_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date', kind=None),
                                            Constant(value='=', kind=None),
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
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='note', kind=None),
                                            Constant(value='=', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='note', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='toppings', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='toppings', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='line', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='topping_ids_1',
                                                            ctx=Load(),
                                                        ),
                                                        op=BitOr(),
                                                        right=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='topping_ids_2',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    op=BitOr(),
                                                    right=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='topping_ids_3',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Name(id='toppings', ctx=Load())],
                                        ),
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
                    name='_compute_total_price',
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
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='price',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='quantity',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=BinOp(
                                            left=Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='price',
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=BinOp(
                                                                left=BinOp(
                                                                    left=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='topping_ids_1',
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=BitOr(),
                                                                    right=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='topping_ids_2',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                op=BitOr(),
                                                                right=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='topping_ids_3',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='price', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
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
                                Constant(value='topping_ids_1', kind=None),
                                Constant(value='topping_ids_2', kind=None),
                                Constant(value='topping_ids_3', kind=None),
                                Constant(value='product_id', kind=None),
                                Constant(value='quantity', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_display_toppings',
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
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='toppings', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='topping_ids_1',
                                                ctx=Load(),
                                            ),
                                            op=BitOr(),
                                            right=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='topping_ids_2',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='topping_ids_3',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='display_toppings',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value=' + ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='toppings', ctx=Load()),
                                                    attr='mapped',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='name', kind=None)],
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='topping_ids_1', kind=None),
                                Constant(value='topping_ids_2', kind=None),
                                Constant(value='topping_ids_3', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='update_quantity',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='increment', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='line', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='state',
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[Constant(value='confirmed', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='quantity',
                                            ctx=Load(),
                                        ),
                                        ops=[LtE()],
                                        comparators=[
                                            UnaryOp(
                                                op=USub(),
                                                operand=Name(id='increment', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='active',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='quantity',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id='increment', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_wallet',
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
                    name='add_to_cart',
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
                            value=Constant(value='\n            This method currently does nothing, we currently need it in order to\n            be able to reuse this model in place of a wizard\n        ', kind=None),
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_wallet',
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
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='lunch.cashmove', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='get_wallet_balance',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='user_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Your wallet does not contain enough money to order that. To add some money to your wallet, please contact your lunch manager.', kind=None)],
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
                    name='action_order',
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='line', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=UnaryOp(
                                            op=Not(),
                                            operand=Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='active',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Product is no longer available.', kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='ordered', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='order', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='lunch_location_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='order', ctx=Load()),
                                            attr='user_id',
                                            ctx=Load(),
                                        ),
                                        attr='last_lunch_location_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_wallet',
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
                    name='action_reorder',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='supplier_id',
                                        ctx=Load(),
                                    ),
                                    attr='available_today',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The vendor related to this order is not available today.', kind=None)],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='date', kind=None),
                                            Constant(value='state', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='context_today',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='self', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value='ordered', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.act_window', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='lunch.lunch_order_action', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_confirm',
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='confirmed', kind=None)],
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
                    name='action_cancel',
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='cancelled', kind=None)],
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
                    name='action_reset',
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='ordered', kind=None)],
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
