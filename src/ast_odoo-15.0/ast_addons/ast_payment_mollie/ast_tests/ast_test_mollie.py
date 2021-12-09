Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='common',
            names=[alias(name='MollieCommon', asname=None)],
            level=1,
        ),
        ClassDef(
            name='MollieTest',
            bases=[Name(id='MollieCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_payment_request_payload_values',
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
                            targets=[Name(id='tx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='create_transaction',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='flow',
                                        value=Constant(value='redirect', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='payload', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='tx', ctx=Load()),
                                    attr='_mollie_prepare_payment_request_payload',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertDictEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='payload', ctx=Load()),
                                        slice=Constant(value='amount', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='currency', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='EUR', kind=None),
                                            Constant(value='1111.11', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='payload', ctx=Load()),
                                        slice=Constant(value='description', kind=None),
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='tx', ctx=Load()),
                                        attr='reference',
                                        ctx=Load(),
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
