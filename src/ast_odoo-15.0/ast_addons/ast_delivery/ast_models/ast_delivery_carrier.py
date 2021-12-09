Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='psycopg2', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='registry', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='DeliveryCarrier',
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
                    value=Constant(value='delivery.carrier', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Shipping Methods', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence, id', kind=None),
                    type_comment=None,
                ),
                Expr(
                    value=Constant(value=' A Shipping Provider\n\n    In order to add your own external provider, follow these steps:\n\n    1. Create your model MyProvider that _inherit \'delivery.carrier\'\n    2. Extend the selection of the field "delivery_type" with a pair\n       (\'<my_provider>\', \'My Provider\')\n    3. Add your methods:\n       <my_provider>_rate_shipment\n       <my_provider>_send_shipping\n       <my_provider>_get_tracking_link\n       <my_provider>_cancel_shipment\n       _<my_provider>_get_default_custom_package_code\n       (they are documented hereunder)\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Delivery Method', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='translate',
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
                        args=[],
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
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Determine the display order', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=10, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='delivery_type', ctx=Store())],
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
                                            Constant(value='fixed', kind=None),
                                            Constant(value='Fixed Price', kind=None),
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
                                value=Constant(value='Provider', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='fixed', kind=None),
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
                    targets=[Name(id='integration_level', ctx=Store())],
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
                                            Constant(value='rate', kind=None),
                                            Constant(value='Get Rate', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='rate_and_ship', kind=None),
                                            Constant(value='Get Rate and Create Shipment', kind=None),
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
                                value=Constant(value='Integration Level', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='rate_and_ship', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Action while validating Delivery Orders', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='prod_environment', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Environment', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Set to True if your credentials are certified for production.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='debug_logging', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Debug logging', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Log requests in order to ease debugging', kind=None),
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
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.company_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
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
                        args=[Constant(value='product.product', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Delivery Product', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='invoice_policy', ctx=Store())],
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
                                            Constant(value='estimated', kind=None),
                                            Constant(value='Estimated cost', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='real', kind=None),
                                            Constant(value='Real cost', kind=None),
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
                                value=Constant(value='Invoicing Policy', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='estimated', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Estimated Cost: the customer will be invoiced the estimated cost of the shipping.\nReal Cost: the customer will be invoiced the real cost of the shipping, the cost of the shipping will be updated on the SO after the delivery.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='country_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.country', kind=None),
                            Constant(value='delivery_carrier_country_rel', kind=None),
                            Constant(value='carrier_id', kind=None),
                            Constant(value='country_id', kind=None),
                            Constant(value='Countries', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.country.state', kind=None),
                            Constant(value='delivery_carrier_state_rel', kind=None),
                            Constant(value='carrier_id', kind=None),
                            Constant(value='state_id', kind=None),
                            Constant(value='States', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='zip_from', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Zip From', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='zip_to', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Zip To', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='margin', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='This percentage will be added to the shipping price.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='free_over', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Free if order amount is above', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='If the order total amount (shipping excluded) is above or equal to this value, the customer benefits from a free shipping', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Amount', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Amount of the order to benefit from a free shipping, expressed in the company currency', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='can_generate_return', ctx=Store())],
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
                                value=Constant(value='_compute_can_generate_return', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='return_label_on_delivery', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Generate Return Label', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The return label is automatically generated at the delivery.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='get_return_label_from_portal', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Return Label Accessible from Customer Portal', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The return label can be downloaded by the customer from the customer portal.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='margin_not_under_100_percent', kind=None),
                                    Constant(value='CHECK (margin >= -100)', kind=None),
                                    Constant(value='Margin cannot be lower than -100%', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_can_generate_return',
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
                            target=Name(id='carrier', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='carrier', ctx=Load()),
                                            attr='can_generate_return',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
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
                            args=[Constant(value='delivery_type', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='toggle_prod_environment',
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
                            target=Name(id='c', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='c', ctx=Load()),
                                            attr='prod_environment',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='c', ctx=Load()),
                                            attr='prod_environment',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
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
                    name='toggle_debug',
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
                            target=Name(id='c', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='c', ctx=Load()),
                                            attr='debug_logging',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='c', ctx=Load()),
                                            attr='debug_logging',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
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
                    name='install_more_provider',
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
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='help', kind=None),
                                ],
                                values=[
                                    Constant(value='New Providers', kind=None),
                                    Constant(value='kanban,form', kind=None),
                                    Constant(value='ir.module.module', kind=None),
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='=like', kind=None),
                                                    Constant(value='delivery_%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value='delivery_barcode', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='<p class="o_view_nocontent">\n                    Buy Odoo Enterprise now to get more providers.\n                </p>', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='available_carriers',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
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
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='c', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='c', ctx=Load()),
                                                attr='_match_address',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='partner', ctx=Load())],
                                            keywords=[],
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
                    name='_match_address',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner', annotation=None, type_comment=None),
                        ],
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='country_ids',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='country_id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='country_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='state_ids',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='state_id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='state_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='zip_from',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='zip',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value='', kind=None),
                                                    ],
                                                ),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='zip_from',
                                                        ctx=Load(),
                                                    ),
                                                    attr='upper',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='zip_to',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='zip',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value='', kind=None),
                                                    ],
                                                ),
                                                attr='upper',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='zip_to',
                                                        ctx=Load(),
                                                    ),
                                                    attr='upper',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
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
                    name='_onchange_integration_level',
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
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='integration_level',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='rate', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='invoice_policy',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='estimated', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='integration_level', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_can_generate_return',
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='can_generate_return',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='return_label_on_delivery',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='can_generate_return', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_return_label_on_delivery',
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='return_label_on_delivery',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_return_label_from_portal',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='return_label_on_delivery', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='onchange_states',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='country_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=6, kind=None),
                                            Constant(value=0, kind=None),
                                            BinOp(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='country_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='state_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='country_id.id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='state_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='onchange_countries',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='state_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value=6, kind=None),
                                            Constant(value=0, kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='state_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='filtered',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Lambda(
                                                            args=arguments(
                                                                posonlyargs=[],
                                                                args=[arg(arg='state', annotation=None, type_comment=None)],
                                                                vararg=None,
                                                                kwonlyargs=[],
                                                                kw_defaults=[],
                                                                kwarg=None,
                                                                defaults=[],
                                                            ),
                                                            body=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='state', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='country_ids',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='mapped',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='state_ids', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='country_ids', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='rate_shipment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Compute the price of the order shipment\n\n        :param order: record of sale.order\n        :return dict: {'success': boolean,\n                       'price': a float,\n                       'error_message': a string containing an error message,\n                       'warning_message': a string containing a warning message}\n                       # TODO maybe the currency code?\n        ", kind=None),
                        ),
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
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='%s_rate_shipment', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='delivery_type',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='self', ctx=Load()),
                                                BinOp(
                                                    left=Constant(value='%s_rate_shipment', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='delivery_type',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        args=[Name(id='order', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='price', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='float', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='price', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Mult(),
                                        right=BinOp(
                                            left=Constant(value=1.0, kind=None),
                                            op=Add(),
                                            right=BinOp(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='margin',
                                                    ctx=Load(),
                                                ),
                                                op=Div(),
                                                right=Constant(value=100.0, kind=None),
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='carrier_price', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='res', ctx=Load()),
                                        slice=Constant(value='price', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Subscript(
                                                value=Name(id='res', ctx=Load()),
                                                slice=Constant(value='success', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='free_over',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='order', ctx=Load()),
                                                        attr='_compute_amount_total_without_delivery',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[GtE()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='amount',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='warning_message', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='The shipping is free since the order amount exceeds %.2f.', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='amount',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='price', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=0.0, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='res', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='send_shipping',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pickings', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Send the package to the service provider\n\n        :param pickings: A recordset of pickings\n        :return list: A list of dictionaries (one per picking) containing of the form::\n                         { 'exact_price': price,\n                           'tracking_number': number }\n                           # TODO missing labels per package\n                           # TODO missing currency\n                           # TODO missing success, error, warnings\n        ", kind=None),
                        ),
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
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='%s_send_shipping', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='delivery_type',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='self', ctx=Load()),
                                                BinOp(
                                                    left=Constant(value='%s_send_shipping', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='delivery_type',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        args=[Name(id='pickings', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_return_label',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pickings', annotation=None, type_comment=None),
                            arg(arg='tracking_number', annotation=None, type_comment=None),
                            arg(arg='origin_date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
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
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='can_generate_return',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='self', ctx=Load()),
                                                BinOp(
                                                    left=Constant(value='%s_get_return_label', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='delivery_type',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        args=[
                                            Name(id='pickings', ctx=Load()),
                                            Name(id='tracking_number', ctx=Load()),
                                            Name(id='origin_date', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_return_label_prefix',
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
                            value=BinOp(
                                left=Constant(value='ReturnLabel-%s', kind=None),
                                op=Mod(),
                                right=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='delivery_type',
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_tracking_link',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='picking', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Ask the tracking link to the service provider\n\n        :param picking: record of stock.picking\n        :return str: an URL containing the tracking link or False\n        ', kind=None),
                        ),
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
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='%s_get_tracking_link', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='delivery_type',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='self', ctx=Load()),
                                                BinOp(
                                                    left=Constant(value='%s_get_tracking_link', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='delivery_type',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        args=[Name(id='picking', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='cancel_shipment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pickings', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Cancel a shipment\n\n        :param pickings: A recordset of pickings\n        ', kind=None),
                        ),
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
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='%s_cancel_shipment', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='delivery_type',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='self', ctx=Load()),
                                                BinOp(
                                                    left=Constant(value='%s_cancel_shipment', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='delivery_type',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        args=[Name(id='pickings', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='log_xml',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='xml_string', annotation=None, type_comment=None),
                            arg(arg='func', annotation=None, type_comment=None),
                        ],
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
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='debug_logging',
                                ctx=Load(),
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
                                Assign(
                                    targets=[Name(id='db_name', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_cr',
                                            ctx=Load(),
                                        ),
                                        attr='dbname',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='db_registry', ctx=Store())],
                                            value=Call(
                                                func=Name(id='registry', ctx=Load()),
                                                args=[Name(id='db_name', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Name(id='db_registry', ctx=Load()),
                                                            attr='cursor',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='cr', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                Assign(
                                                    targets=[Name(id='env', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='api', ctx=Load()),
                                                            attr='Environment',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='cr', ctx=Load()),
                                                            Name(id='SUPERUSER_ID', ctx=Load()),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='IrLogging', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Constant(value='ir.logging', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='IrLogging', ctx=Load()),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='dbname', kind=None),
                                                                    Constant(value='level', kind=None),
                                                                    Constant(value='message', kind=None),
                                                                    Constant(value='path', kind=None),
                                                                    Constant(value='func', kind=None),
                                                                    Constant(value='line', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='delivery.carrier', kind=None),
                                                                    Constant(value='server', kind=None),
                                                                    Name(id='db_name', ctx=Load()),
                                                                    Constant(value='DEBUG', kind=None),
                                                                    Name(id='xml_string', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='delivery_type',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='func', ctx=Load()),
                                                                    Constant(value=1, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='psycopg2', ctx=Load()),
                                                attr='Error',
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_default_custom_package_code',
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
                            value=Constant(value=' Some delivery carriers require a prefix to be sent in order to use custom\n        packages (ie not official ones). This optional method will return it as a string.\n        ', kind=None),
                        ),
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
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    BinOp(
                                        left=Constant(value='_%s_get_default_custom_package_code', kind=None),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='delivery_type',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='self', ctx=Load()),
                                                BinOp(
                                                    left=Constant(value='_%s_get_default_custom_package_code', kind=None),
                                                    op=Mod(),
                                                    right=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='delivery_type',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='fixed_price', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_fixed_price', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_product_fixed_price', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Fixed Price', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_fixed_price',
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
                            target=Name(id='carrier', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='carrier', ctx=Load()),
                                            attr='fixed_price',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='carrier', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='list_price',
                                        ctx=Load(),
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
                                Constant(value='product_id.list_price', kind=None),
                                Constant(value='product_id.product_tmpl_id.list_price', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_product_fixed_price',
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
                            target=Name(id='carrier', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='carrier', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='list_price',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='carrier', ctx=Load()),
                                        attr='fixed_price',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
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
                    name='fixed_rate_shipment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='carrier', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_match_address',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='order', ctx=Load()),
                                        attr='partner_shipping_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='carrier', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='success', kind=None),
                                            Constant(value='price', kind=None),
                                            Constant(value='error_message', kind=None),
                                            Constant(value='warning_message', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=0.0, kind=None),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Error: this delivery method is not available for this address.', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='price', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='fixed_price',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='order', ctx=Load()),
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='company', ctx=Load()),
                                        attr='currency_id',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='company', ctx=Load()),
                                            attr='currency_id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='price', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            attr='_convert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='price', ctx=Load()),
                                            Attribute(
                                                value=Name(id='order', ctx=Load()),
                                                attr='currency_id',
                                                ctx=Load(),
                                            ),
                                            Name(id='company', ctx=Load()),
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
                            value=Dict(
                                keys=[
                                    Constant(value='success', kind=None),
                                    Constant(value='price', kind=None),
                                    Constant(value='error_message', kind=None),
                                    Constant(value='warning_message', kind=None),
                                ],
                                values=[
                                    Constant(value=True, kind=None),
                                    Name(id='price', ctx=Load()),
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='fixed_send_shipping',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pickings', annotation=None, type_comment=None),
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
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='p', ctx=Store()),
                            iter=Name(id='pickings', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='res', ctx=Load()),
                                        op=Add(),
                                        right=List(
                                            elts=[
                                                Dict(
                                                    keys=[
                                                        Constant(value='exact_price', kind=None),
                                                        Constant(value='tracking_number', kind=None),
                                                    ],
                                                    values=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='p', ctx=Load()),
                                                                attr='carrier_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='fixed_price',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value=False, kind=None),
                                                    ],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='fixed_get_tracking_link',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='picking', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='fixed_cancel_shipment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pickings', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Raise(
                            exc=Call(
                                func=Name(id='NotImplementedError', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            cause=None,
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
