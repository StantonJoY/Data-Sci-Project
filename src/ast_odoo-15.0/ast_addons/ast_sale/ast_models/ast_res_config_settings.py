Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='ResConfigSettings',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.config.settings', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_auto_done_setting', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Lock Confirmed Sales', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='sale.group_auto_done_setting', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_sale_margin', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Margins', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='quotation_validity_days', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.quotation_validity_days', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Default Quotation Validity (Days)', kind=None),
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
                    targets=[Name(id='use_quotation_validity_days', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Default Quotation Validity', kind=None)],
                        keywords=[
                            keyword(
                                arg='config_parameter',
                                value=Constant(value='sale.use_quotation_validity_days', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_warning_sale', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Sale Order Warnings', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='sale.group_warning_sale', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='portal_confirmation_sign', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.portal_confirmation_sign', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Online Signature', kind=None),
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
                    targets=[Name(id='portal_confirmation_pay', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='company_id.portal_confirmation_pay', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Online Payment', kind=None),
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
                    targets=[Name(id='group_sale_delivery_address', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Customer Addresses', kind=None)],
                        keywords=[
                            keyword(
                                arg='implied_group',
                                value=Constant(value='sale.group_delivery_invoice_address', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_proforma_sales', ctx=Store())],
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
                                value=Constant(value='Pro-Forma Invoice', kind=None),
                            ),
                            keyword(
                                arg='implied_group',
                                value=Constant(value='sale.group_proforma_sales', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Allows you to send pro-forma invoice.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='default_invoice_policy', ctx=Store())],
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
                                            Constant(value='order', kind=None),
                                            Constant(value='Invoice what is ordered', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='delivery', kind=None),
                                            Constant(value='Invoice what is delivered', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            Constant(value='Invoicing Policy', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='order', kind=None),
                            ),
                            keyword(
                                arg='default_model',
                                value=Constant(value='product.template', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='deposit_default_product_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='product.product', kind=None),
                            Constant(value='Deposit Product', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=Constant(value="[('type', '=', 'service')]", kind=None),
                            ),
                            keyword(
                                arg='config_parameter',
                                value=Constant(value='sale.default_deposit_product_id', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Default product used for payment advances', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='auth_signup_uninvited', ctx=Store())],
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
                                            Constant(value='b2b', kind=None),
                                            Constant(value='On invitation', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='b2c', kind=None),
                                            Constant(value='Free sign up', kind=None),
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
                                value=Constant(value='Customer Account', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='b2b', kind=None),
                            ),
                            keyword(
                                arg='config_parameter',
                                value=Constant(value='auth_signup.invitation_scope', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Delivery Methods', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery_dhl', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='DHL USA Connector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery_fedex', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='FedEx Connector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery_ups', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='UPS Connector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery_usps', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='USPS Connector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery_bpost', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='bpost Connector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_delivery_easypost', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Easypost Connector', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_product_email_template', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Specific Email', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_sale_coupon', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Coupons & Promotions', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='module_sale_amazon', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Amazon Sync', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='automatic_invoice', ctx=Store())],
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
                                value=Constant(value='Automatic Invoice', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The invoice is generated automatically and available in the customer portal when the transaction is confirmed by the payment acquirer.\nThe invoice is marked as paid and the payment is registered in the payment journal defined in the configuration of the payment acquirer.\nThis mode is advised if you issue the final invoice at the order and not after the delivery.', kind=None),
                            ),
                            keyword(
                                arg='config_parameter',
                                value=Constant(value='sale.automatic_invoice', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='invoice_mail_template_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='mail.template', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Invoice Email Template', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('model', '=', 'account.move')]", kind=None),
                            ),
                            keyword(
                                arg='config_parameter',
                                value=Constant(value='sale.default_invoice_email_template', kind=None),
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
                                    body=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='account.email_template_edi_invoice', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='confirmation_mail_template_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='mail.template', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Confirmation Email Template', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('model', '=', 'sale.order')]", kind=None),
                            ),
                            keyword(
                                arg='config_parameter',
                                value=Constant(value='sale.default_confirmation_template', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Email sent to the customer once the order is paid.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='set_values',
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
                                            Name(id='ResConfigSettings', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='set_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='default_invoice_policy',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='order', kind=None)],
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
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='set_param',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='sale.automatic_invoice', kind=None),
                                            Constant(value=False, kind=None),
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
                    name='_onchange_use_quotation_validity_days',
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
                                    attr='quotation_validity_days',
                                    ctx=Load(),
                                ),
                                ops=[LtE()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='quotation_validity_days',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='res.company', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='default_get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[Constant(value='quotation_validity_days', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='quotation_validity_days', kind=None),
                                        ctx=Load(),
                                    ),
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
                            args=[Constant(value='use_quotation_validity_days', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_quotation_validity_days',
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
                                    attr='quotation_validity_days',
                                    ctx=Load(),
                                ),
                                ops=[LtE()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='quotation_validity_days',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='res.company', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='default_get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[Constant(value='quotation_validity_days', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='quotation_validity_days', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='warning', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='title', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Warning', kind=None),
                                                    Constant(value='Quotation Validity is required and must be greater than 0.', kind=None),
                                                ],
                                            ),
                                        ],
                                    ),
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
                            args=[Constant(value='quotation_validity_days', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
