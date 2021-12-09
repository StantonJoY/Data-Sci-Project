Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='threading',
            names=[alias(name='Event', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ClassDef(
            name='EventManager',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='events',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sessions',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_delete_expired_sessions',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='max_time', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=70, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Clears sessions that are no longer called.\n\n        :param max_time: time a session can stay unused before being deleted\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='now', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='time',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expired_sessions', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='session', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='session', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sessions',
                                            ctx=Load(),
                                        ),
                                        ifs=[
                                            Compare(
                                                left=BinOp(
                                                    left=Name(id='now', ctx=Load()),
                                                    op=Sub(),
                                                    right=Subscript(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='sessions',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='session', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='time_request', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                ops=[Gt()],
                                                comparators=[Name(id='max_time', ctx=Load())],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='session', ctx=Store()),
                            iter=Name(id='expired_sessions', ctx=Load()),
                            body=[
                                Delete(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sessions',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='session', ctx=Load()),
                                            ctx=Del(),
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
                FunctionDef(
                    name='add_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='listener', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='session',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='session_id', kind=None),
                                    Constant(value='devices', kind=None),
                                    Constant(value='event', kind=None),
                                    Constant(value='result', kind=None),
                                    Constant(value='time_request', kind=None),
                                ],
                                values=[
                                    Subscript(
                                        value=Name(id='listener', ctx=Load()),
                                        slice=Constant(value='session_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='listener', ctx=Load()),
                                        slice=Constant(value='devices', kind=None),
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='Event', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Dict(keys=[], values=[]),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='time',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_delete_expired_sessions',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sessions',
                                        ctx=Load(),
                                    ),
                                    slice=Subscript(
                                        value=Name(id='listener', ctx=Load()),
                                        slice=Constant(value='session_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='session',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sessions',
                                    ctx=Load(),
                                ),
                                slice=Subscript(
                                    value=Name(id='listener', ctx=Load()),
                                    slice=Constant(value='session_id', kind=None),
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='device_changed',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='device', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
                            value=Dict(
                                keys=[
                                    None,
                                    Constant(value='device_identifier', kind=None),
                                    Constant(value='time', kind=None),
                                    Constant(value='request_data', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='device', ctx=Load()),
                                        attr='data',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='device', ctx=Load()),
                                        attr='device_identifier',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='time',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    IfExp(
                                        test=BoolOp(
                                            op=And(),
                                            values=[
                                                Name(id='request', ctx=Load()),
                                                Compare(
                                                    left=Constant(value='data', kind=None),
                                                    ops=[In()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='params',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='loads',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='params',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='data', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        orelse=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='events',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Name(id='event', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='session', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='sessions',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='device', ctx=Load()),
                                                    attr='device_identifier',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Subscript(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='sessions',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='session', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='devices', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='sessions',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Name(id='session', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='event', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='isSet',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='sessions',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='session', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='result', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='event', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='sessions',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='session', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='event', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
        Assign(
            targets=[Name(id='event_manager', ctx=Store())],
            value=Call(
                func=Name(id='EventManager', ctx=Load()),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
