Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='api', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.float_utils',
            names=[alias(name='float_compare', asname=None)],
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
            name='BarcodeRule',
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
                    value=Constant(value='barcode.rule', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection_add',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='credit', kind=None),
                                                Constant(value='Credit Card', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Dict(
                                    keys=[Constant(value='credit', kind=None)],
                                    values=[Constant(value='set default', kind=None)],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='PosMercuryConfiguration',
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
                    value=Constant(value='pos_mercury.configuration', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Point of Sale Vantiv Configuration', kind=None),
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
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Name of this Vantiv configuration', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='merchant_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Merchant ID', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='ID of the merchant to authenticate him on the payment provider server', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='merchant_pwd', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Merchant Password', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Password of the merchant to authenticate him on the payment provider server', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='PoSPayment',
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
                    value=Constant(value='pos.payment', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mercury_card_number', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Card Number', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The last 4 numbers of the card used to pay', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mercury_prefixed_card_number', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Card Number Prefix', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_prefixed_card_number', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The card number used for the payment.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mercury_card_brand', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Card Brand', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The brand of the payment card (e.g. Visa, AMEX, ...)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mercury_card_owner_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Card Owner Name', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The name of the card owner', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mercury_ref_no', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Vantiv reference number', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Payment reference number from Vantiv Pay', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mercury_record_no', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Vantiv record number', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Payment record number from Vantiv Pay', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mercury_invoice_no', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Vantiv invoice number', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Invoice number from Vantiv Pay', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_prefixed_card_number',
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
                                If(
                                    test=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='mercury_card_number',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='mercury_prefixed_card_number',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value='********', kind=None),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='mercury_card_number',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='mercury_prefixed_card_number',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='', kind=None),
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='PoSPaymentMethod',
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
                    value=Constant(value='pos.payment.method', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pos_mercury_config_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='pos_mercury.configuration', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Vantiv Credentials', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The configuration of Vantiv used for this journal', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_payment_terminal_selection',
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
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[
                                                Name(id='PoSPaymentMethod', ctx=Load()),
                                                Name(id='self', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='_get_payment_terminal_selection',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='mercury', kind=None),
                                                Constant(value='Vantiv', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
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
                    name='_onchange_use_payment_terminal',
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
                                            Name(id='PoSPaymentMethod', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_onchange_use_payment_terminal',
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
                                    attr='use_payment_terminal',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='mercury', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='pos_mercury_config_id',
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
                            args=[Constant(value='use_payment_terminal', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='PosOrder',
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
                    value=Constant(value='pos.order', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_payment_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                            arg(arg='ui_paymentline', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PosOrder', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_payment_fields',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='order', ctx=Load()),
                                    Name(id='ui_paymentline', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='fields', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='mercury_card_number', kind=None),
                                            Constant(value='mercury_card_brand', kind=None),
                                            Constant(value='mercury_card_owner_name', kind=None),
                                            Constant(value='mercury_ref_no', kind=None),
                                            Constant(value='mercury_record_no', kind=None),
                                            Constant(value='mercury_invoice_no', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='ui_paymentline', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mercury_card_number', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='ui_paymentline', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mercury_card_brand', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='ui_paymentline', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mercury_card_owner_name', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='ui_paymentline', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mercury_ref_no', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='ui_paymentline', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mercury_record_no', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='ui_paymentline', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='mercury_invoice_no', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='fields', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
