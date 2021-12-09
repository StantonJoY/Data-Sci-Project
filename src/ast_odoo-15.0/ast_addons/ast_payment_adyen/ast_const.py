Module(
    body=[
        Assign(
            targets=[Name(id='API_ENDPOINT_VERSIONS', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='/disable', kind=None),
                    Constant(value='/payments', kind=None),
                    Constant(value='/payments/details', kind=None),
                    Constant(value='/payments/{}/refunds', kind=None),
                    Constant(value='/paymentMethods', kind=None),
                ],
                values=[
                    Constant(value=49, kind=None),
                    Constant(value=67, kind=None),
                    Constant(value=67, kind=None),
                    Constant(value=67, kind=None),
                    Constant(value=67, kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='CURRENCY_DECIMALS', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='CLP', kind=None),
                    Constant(value='CVE', kind=None),
                    Constant(value='IDR', kind=None),
                    Constant(value='ISK', kind=None),
                ],
                values=[
                    Constant(value=2, kind=None),
                    Constant(value=0, kind=None),
                    Constant(value=0, kind=None),
                    Constant(value=2, kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='RESULT_CODES_MAPPING', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='pending', kind=None),
                    Constant(value='done', kind=None),
                    Constant(value='cancel', kind=None),
                    Constant(value='error', kind=None),
                    Constant(value='refused', kind=None),
                ],
                values=[
                    Tuple(
                        elts=[
                            Constant(value='ChallengeShopper', kind=None),
                            Constant(value='IdentifyShopper', kind=None),
                            Constant(value='Pending', kind=None),
                            Constant(value='PresentToShopper', kind=None),
                            Constant(value='Received', kind=None),
                            Constant(value='RedirectShopper', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[Constant(value='Authorised', kind=None)],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[Constant(value='Cancelled', kind=None)],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[Constant(value='Error', kind=None)],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[Constant(value='Refused', kind=None)],
                        ctx=Load(),
                    ),
                ],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
