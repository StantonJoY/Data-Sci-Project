Module(
    body=[
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='Controller', asname=None),
                alias(name='request', asname=None),
                alias(name='route', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='TestBusController',
            bases=[Name(id='Controller', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value="\n    This controller is only useful for test purpose. Bus is unavailable in test mode, but there is no way to know,\n    at client side, if we are running in test mode or not. This route can be called while running tours to mock\n    some behaviour in function of the test mode status (activated or not).\n\n    E.g. : To test the livechat and to check there is no duplicates in message displayed in the chatter,\n    in test mode, we need to mock a 'message added' notification that is normally triggered by the bus.\n    In Normal mode, the bus triggers itself the notification.\n    ", kind=None),
                ),
                FunctionDef(
                    name='is_test_mode_activated',
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
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='in_test_mode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[Constant(value='/bus/test_mode_activated', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                            ],
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
