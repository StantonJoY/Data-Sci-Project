Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='namedtuple', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='PMT', ctx=Store())],
            value=Call(
                func=Name(id='namedtuple', ctx=Load()),
                args=[
                    Constant(value='PaymentMethodType', kind=None),
                    List(
                        elts=[
                            Constant(value='name', kind=None),
                            Constant(value='countries', kind=None),
                            Constant(value='currencies', kind=None),
                            Constant(value='recurrence', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='PAYMENT_METHOD_TYPES', ctx=Store())],
            value=List(
                elts=[
                    Call(
                        func=Name(id='PMT', ctx=Load()),
                        args=[
                            Constant(value='card', kind=None),
                            List(elts=[], ctx=Load()),
                            List(elts=[], ctx=Load()),
                            Constant(value='recurring', kind=None),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='PMT', ctx=Load()),
                        args=[
                            Constant(value='ideal', kind=None),
                            List(
                                elts=[Constant(value='nl', kind=None)],
                                ctx=Load(),
                            ),
                            List(
                                elts=[Constant(value='eur', kind=None)],
                                ctx=Load(),
                            ),
                            Constant(value='punctual', kind=None),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='PMT', ctx=Load()),
                        args=[
                            Constant(value='bancontact', kind=None),
                            List(
                                elts=[Constant(value='be', kind=None)],
                                ctx=Load(),
                            ),
                            List(
                                elts=[Constant(value='eur', kind=None)],
                                ctx=Load(),
                            ),
                            Constant(value='punctual', kind=None),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='PMT', ctx=Load()),
                        args=[
                            Constant(value='eps', kind=None),
                            List(
                                elts=[Constant(value='at', kind=None)],
                                ctx=Load(),
                            ),
                            List(
                                elts=[Constant(value='eur', kind=None)],
                                ctx=Load(),
                            ),
                            Constant(value='punctual', kind=None),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='PMT', ctx=Load()),
                        args=[
                            Constant(value='giropay', kind=None),
                            List(
                                elts=[Constant(value='de', kind=None)],
                                ctx=Load(),
                            ),
                            List(
                                elts=[Constant(value='eur', kind=None)],
                                ctx=Load(),
                            ),
                            Constant(value='punctual', kind=None),
                        ],
                        keywords=[],
                    ),
                    Call(
                        func=Name(id='PMT', ctx=Load()),
                        args=[
                            Constant(value='p24', kind=None),
                            List(
                                elts=[Constant(value='pl', kind=None)],
                                ctx=Load(),
                            ),
                            List(
                                elts=[
                                    Constant(value='eur', kind=None),
                                    Constant(value='pln', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Constant(value='punctual', kind=None),
                        ],
                        keywords=[],
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='INTENT_STATUS_MAPPING', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='draft', kind=None),
                    Constant(value='pending', kind=None),
                    Constant(value='done', kind=None),
                    Constant(value='cancel', kind=None),
                ],
                values=[
                    Tuple(
                        elts=[
                            Constant(value='requires_payment_method', kind=None),
                            Constant(value='requires_confirmation', kind=None),
                            Constant(value='requires_action', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[Constant(value='processing', kind=None)],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[Constant(value='succeeded', kind=None)],
                        ctx=Load(),
                    ),
                    Tuple(
                        elts=[Constant(value='canceled', kind=None)],
                        ctx=Load(),
                    ),
                ],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
