Module(
    body=[
        Assign(
            targets=[Name(id='SUPPORTED_CURRENCIES', ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value='AUD', kind=None),
                    Constant(value='BRL', kind=None),
                    Constant(value='CAD', kind=None),
                    Constant(value='CNY', kind=None),
                    Constant(value='CZK', kind=None),
                    Constant(value='DKK', kind=None),
                    Constant(value='EUR', kind=None),
                    Constant(value='HKD', kind=None),
                    Constant(value='HUF', kind=None),
                    Constant(value='ILS', kind=None),
                    Constant(value='JPY', kind=None),
                    Constant(value='MYR', kind=None),
                    Constant(value='MXN', kind=None),
                    Constant(value='TWD', kind=None),
                    Constant(value='NZD', kind=None),
                    Constant(value='NOK', kind=None),
                    Constant(value='PHP', kind=None),
                    Constant(value='PLN', kind=None),
                    Constant(value='GBP', kind=None),
                    Constant(value='RUB', kind=None),
                    Constant(value='SGD', kind=None),
                    Constant(value='SEK', kind=None),
                    Constant(value='CHF', kind=None),
                    Constant(value='THB', kind=None),
                    Constant(value='USD', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='PAYMENT_STATUS_MAPPING', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='pending', kind=None),
                    Constant(value='done', kind=None),
                    Constant(value='cancel', kind=None),
                ],
                values=[
                    Tuple(
                        elts=[Constant(value='Pending', kind=None)],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='Processed', kind=None),
                            Constant(value='Completed', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[
                            Constant(value='Voided', kind=None),
                            Constant(value='Expired', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
