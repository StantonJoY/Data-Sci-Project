Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Company',
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
                    value=Constant(value='res.company', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='po_lead', ctx=Store())],
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
                                value=Constant(value='Purchase Lead Time', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Margin of error for vendor lead times. When the system generates Purchase Orders for procuring products, they will be scheduled that many days earlier to cope with unexpected vendor delays.', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=0.0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='po_lock', ctx=Store())],
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
                                            Constant(value='edit', kind=None),
                                            Constant(value='Allow to edit purchase orders', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lock', kind=None),
                                            Constant(value='Confirmed purchase orders are not editable', kind=None),
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
                                value=Constant(value='Purchase Order Modification', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='edit', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Purchase Order Modification used when you want to purchase order editable after confirm', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='po_double_validation', ctx=Store())],
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
                                            Constant(value='one_step', kind=None),
                                            Constant(value='Confirm purchase orders in one step', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='two_step', kind=None),
                                            Constant(value='Get 2 levels of approvals to confirm a purchase order', kind=None),
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
                                value=Constant(value='Levels of Approvals', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='one_step', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Provide a double validation mechanism for purchases', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='po_double_validation_amount', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Monetary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Double validation amount', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=5000, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Minimum amount for which a double validation is required', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
