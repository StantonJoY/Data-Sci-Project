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
            name='Followers',
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
                    value=List(
                        elts=[Constant(value='mail.followers', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_recipient_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='message_type', annotation=None, type_comment=None),
                            arg(arg='subtype_id', annotation=None, type_comment=None),
                            arg(arg='pids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='message_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='sms', kind=None)],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='pids', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='sms_pids', ctx=Store())],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='records', ctx=Load()),
                                                        attr='_sms_get_default_partners',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='sms_pids', ctx=Store())],
                                            value=Name(id='pids', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='Followers', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_get_recipient_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='records', ctx=Load()),
                                            Name(id='message_type', ctx=Load()),
                                            Name(id='subtype_id', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='pids',
                                                value=Name(id='pids', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_res', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='pid', ctx=Store()),
                                            Name(id='active', ctx=Store()),
                                            Name(id='pshare', ctx=Store()),
                                            Name(id='notif', ctx=Store()),
                                            Name(id='groups', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Name(id='res', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='pid', ctx=Load()),
                                                    Compare(
                                                        left=Name(id='pid', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='sms_pids', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='notif', ctx=Store())],
                                                    value=Constant(value='sms', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='new_res', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='pid', ctx=Load()),
                                                            Name(id='active', ctx=Load()),
                                                            Name(id='pshare', ctx=Load()),
                                                            Name(id='notif', ctx=Load()),
                                                            Name(id='groups', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='new_res', ctx=Load()),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='Followers', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_get_recipient_data',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='records', ctx=Load()),
                                            Name(id='message_type', ctx=Load()),
                                            Name(id='subtype_id', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='pids',
                                                value=Name(id='pids', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
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
