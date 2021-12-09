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
        Assign(
            targets=[Name(id='_TYPE_EC', ctx=Store())],
            value=List(
                elts=[
                    Tuple(
                        elts=[
                            Constant(value='vat12', kind=None),
                            Constant(value='VAT 12%', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='vat14', kind=None),
                            Constant(value='VAT 14%', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='zero_vat', kind=None),
                            Constant(value='VAT 0%', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='not_charged_vat', kind=None),
                            Constant(value='VAT Not Charged', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='exempt_vat', kind=None),
                            Constant(value='VAT Exempt', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='withhold_vat', kind=None),
                            Constant(value='VAT Withhold', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='withhold_income_tax', kind=None),
                            Constant(value='Profit Withhold', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='ice', kind=None),
                            Constant(value='Special Consumptions Tax (ICE)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='irbpnr', kind=None),
                            Constant(value='Plastic Bottles (IRBPNR)', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='outflows_tax', kind=None),
                            Constant(value='Exchange Outflows', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='other', kind=None),
                            Constant(value='Others', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='AccountTaxGroup',
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
                    value=Constant(value='account.tax.group', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l10n_ec_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[Name(id='_TYPE_EC', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Type Ecuadorian Tax', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Ecuadorian taxes subtype', kind=None),
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
