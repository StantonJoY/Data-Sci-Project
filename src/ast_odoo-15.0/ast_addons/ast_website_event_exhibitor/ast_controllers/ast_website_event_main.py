Module(
    body=[
        ImportFrom(
            module='babel.dates',
            names=[alias(name='format_datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website_event.controllers',
            names=[alias(name='main', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteEventController',
            bases=[
                Attribute(
                    value=Name(id='main', ctx=Load()),
                    attr='WebsiteEventController',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='_prepare_event_register_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='WebsiteEventController', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_prepare_event_register_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='event', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='from_sponsor_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='post', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='is_ongoing',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sponsor', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='event.sponsor', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='post', ctx=Load()),
                                                                slice=Constant(value='from_sponsor_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='sponsor', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='date_begin', ctx=Store())],
                                            value=Call(
                                                func=Name(id='format_datetime', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='event', ctx=Load()),
                                                                attr='with_context',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='tz',
                                                                    value=Attribute(
                                                                        value=Name(id='event', ctx=Load()),
                                                                        attr='date_tz',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        attr='date_begin',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='format',
                                                        value=Constant(value='medium', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='toast_message', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='The event %s starts on %s (%s). \nJoin us there to meet %s !', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='date_begin', ctx=Load()),
                                                        Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='date_tz',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='sponsor', ctx=Load()),
                                                            attr='partner_name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
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
