Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='exceptions', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='Controller', asname=None),
                alias(name='request', asname=None),
                alias(name='route', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.bus.models.bus',
            names=[alias(name='dispatch', asname=None)],
            level=0,
        ),
        ClassDef(
            name='BusController',
            bases=[Name(id='Controller', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_poll',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='dbname', annotation=None, type_comment=None),
                            arg(arg='channels', annotation=None, type_comment=None),
                            arg(arg='last', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='channels', ctx=Store())],
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[Name(id='channels', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='channels', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='broadcast', kind=None)],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Constant(value='bus_inactivity', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='options', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='bus.presence', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='inactivity_period',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='options', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='bus_inactivity', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='identity_field',
                                                value=Constant(value='user_id', kind=None),
                                            ),
                                            keyword(
                                                arg='identity_value',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='session',
                                                        ctx=Load(),
                                                    ),
                                                    attr='uid',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='_cr',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dispatch', ctx=Load()),
                                    attr='poll',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='dbname', ctx=Load()),
                                    Name(id='channels', ctx=Load()),
                                    Name(id='last', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='poll',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='channels', annotation=None, type_comment=None),
                            arg(arg='last', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
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
                                left=Name(id='options', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='options', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='dispatch', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[Constant(value='bus.Bus unavailable', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=ListComp(
                                elt=Name(id='c', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='c', ctx=Store()),
                                        iter=Name(id='channels', ctx=Load()),
                                        ifs=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='isinstance', ctx=Load()),
                                                    args=[
                                                        Name(id='c', ctx=Load()),
                                                        Name(id='str', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[Constant(value='bus.Bus only string channels are allowed.', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
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
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Name(id='exceptions', ctx=Load()),
                                            attr='UserError',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='bus.Bus not available in test mode', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_poll',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                    Name(id='channels', ctx=Load()),
                                    Name(id='last', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[Constant(value='/longpolling/poll', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='cors',
                                    value=Constant(value='*', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='im_status',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='partner_ids', annotation=None, type_comment=None),
                        ],
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
                                                        slice=Constant(value='res.partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_test',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='partner_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='im_status', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[Constant(value='/longpolling/im_status', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='health',
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
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='dumps',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='status', kind=None)],
                                        values=[Constant(value='pass', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='Content-Type', kind=None),
                                            Constant(value='application/json', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='Cache-Control', kind=None),
                                            Constant(value='no-store', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data', ctx=Load()),
                                    Name(id='headers', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[Constant(value='/longpolling/health', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                                keyword(
                                    arg='save_session',
                                    value=Constant(value=False, kind=None),
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
