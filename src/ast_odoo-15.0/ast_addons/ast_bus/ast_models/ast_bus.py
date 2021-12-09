Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='select', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        Import(
            names=[alias(name='odoo.service.server', asname='servermod')],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='DEFAULT_SERVER_DATETIME_FORMAT', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='date_utils', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TIMEOUT', ctx=Store())],
            value=Constant(value=50, kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='json_dump',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='v', annotation=None, type_comment=None)],
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
                            value=Name(id='json', ctx=Load()),
                            attr='dumps',
                            ctx=Load(),
                        ),
                        args=[Name(id='v', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='separators',
                                value=Tuple(
                                    elts=[
                                        Constant(value=',', kind=None),
                                        Constant(value=':', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='default',
                                value=Attribute(
                                    value=Name(id='date_utils', ctx=Load()),
                                    attr='json_default',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='hashable',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='key', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='key', ctx=Load()),
                            Name(id='list', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='key', ctx=Store())],
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[Name(id='key', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='key', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='channel_with_db',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='dbname', annotation=None, type_comment=None),
                    arg(arg='channel', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='channel', ctx=Load()),
                            Attribute(
                                value=Name(id='models', ctx=Load()),
                                attr='Model',
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='dbname', ctx=Load()),
                                    Attribute(
                                        value=Name(id='channel', ctx=Load()),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='channel', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='channel', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='dbname', ctx=Load()),
                                    Name(id='channel', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='channel', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='ImBus',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='bus.bus', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Communication Bus', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='channel', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Channel', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='message', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Message', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_gc_messages',
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
                            targets=[Name(id='timeout_ago', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        attr='utcnow',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
                                        attr='timedelta',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='seconds',
                                            value=BinOp(
                                                left=Name(id='TIMEOUT', ctx=Load()),
                                                op=Mult(),
                                                right=Constant(value=2, kind=None),
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='create_date', kind=None),
                                            Constant(value='<', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='timeout_ago', ctx=Load()),
                                                    attr='strftime',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                keywords=[],
                                            ),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='autovacuum',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_sendmany',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='notifications', annotation=None, type_comment=None),
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
                                func=Name(id='set', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='target', ctx=Store()),
                                    Name(id='notification_type', ctx=Store()),
                                    Name(id='message', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='notifications', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='channel', ctx=Store())],
                                    value=Call(
                                        func=Name(id='channel_with_db', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='dbname',
                                                ctx=Load(),
                                            ),
                                            Name(id='target', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='channels', ctx=Load()),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='channel', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='channel', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Name(id='json_dump', ctx=Load()),
                                                        args=[Name(id='channel', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Name(id='json_dump', ctx=Load()),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='type', kind=None),
                                                                    Constant(value='payload', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='notification_type', ctx=Load()),
                                                                    Name(id='message', ctx=Load()),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='channels', ctx=Load()),
                            body=[
                                FunctionDef(
                                    name='notify',
                                    args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='odoo', ctx=Load()),
                                                                        attr='sql_db',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='db_connect',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='postgres', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='cursor',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='cr', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='cr', ctx=Load()),
                                                            attr='execute',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='notify imbus, %s', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Call(
                                                                        func=Name(id='json_dump', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='list', ctx=Load()),
                                                                                args=[Name(id='channels', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    decorator_list=[
                                        Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='postcommit',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                    ],
                                    returns=None,
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_sendone',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='channel', annotation=None, type_comment=None),
                            arg(arg='notification_type', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_sendmany',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Name(id='channel', ctx=Load()),
                                                    Name(id='notification_type', ctx=Load()),
                                                    Name(id='message', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_poll',
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
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                        ],
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
                            test=Compare(
                                left=Name(id='last', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='timeout_ago', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='datetime',
                                                    ctx=Load(),
                                                ),
                                                attr='utcnow',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='datetime', ctx=Load()),
                                                attr='timedelta',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='seconds',
                                                    value=Name(id='TIMEOUT', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='create_date', kind=None),
                                                    Constant(value='>', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='timeout_ago', ctx=Load()),
                                                            attr='strftime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='DEFAULT_SERVER_DATETIME_FORMAT', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='>', kind=None),
                                                    Name(id='last', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='channels', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='json_dump', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Name(id='channel_with_db', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='dbname',
                                                    ctx=Load(),
                                                ),
                                                Name(id='c', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='c', ctx=Store()),
                                        iter=Name(id='channels', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='domain', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value='channel', kind=None),
                                            Constant(value='in', kind=None),
                                            Name(id='channels', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='notifications', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='notif', ctx=Store()),
                            iter=Name(id='notifications', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='notif', ctx=Load()),
                                                        slice=Constant(value='id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='json', ctx=Load()),
                                                            attr='loads',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='notif', ctx=Load()),
                                                                slice=Constant(value='message', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
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
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ImDispatch',
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
                                    attr='channels',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='started',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
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
                            arg(arg='dbname', annotation=None, type_comment=None),
                            arg(arg='channels', annotation=None, type_comment=None),
                            arg(arg='last', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='channels', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='channel_with_db', ctx=Load()),
                                    args=[
                                        Name(id='dbname', ctx=Load()),
                                        Name(id='channel', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='channel', ctx=Store()),
                                        iter=Name(id='channels', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='timeout', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='timeout', ctx=Store())],
                                    value=Name(id='TIMEOUT', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
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
                                operand=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='evented',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='current', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='current_thread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='current', ctx=Load()),
                                            attr='_daemonic',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='current', ctx=Load()),
                                            attr='setName',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='openerp.longpolling.request.%s', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Name(id='current', ctx=Load()),
                                                    attr='ident',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='registry', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='odoo', ctx=Load()),
                                    attr='registry',
                                    ctx=Load(),
                                ),
                                args=[Name(id='dbname', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='registry', ctx=Load()),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='cr', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='api', ctx=Load()),
                                            attr='Environment',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='cr', ctx=Load()),
                                            Name(id='SUPERUSER_ID', ctx=Load()),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='notifications', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='bus.bus', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_poll',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='channels', ctx=Load()),
                                            Name(id='last', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='peek', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='notifications',
                                                value=Name(id='notifications', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='channels',
                                                value=Name(id='channels', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='notifications', ctx=Load()),
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='started',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='start',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='event', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='Event',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='channel', ctx=Store()),
                                    iter=Name(id='channels', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='channels',
                                                                ctx=Load(),
                                                            ),
                                                            attr='setdefault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='hashable', ctx=Load()),
                                                                args=[Name(id='channel', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Name(id='set', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='add',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='event', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='wait',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='timeout',
                                                        value=Name(id='timeout', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Name(id='registry', ctx=Load()),
                                                            attr='cursor',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='cr', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                Assign(
                                                    targets=[Name(id='env', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='api', ctx=Load()),
                                                            attr='Environment',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='cr', ctx=Load()),
                                                            Name(id='SUPERUSER_ID', ctx=Load()),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='notifications', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Constant(value='bus.bus', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_poll',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='channels', ctx=Load()),
                                                            Name(id='last', ctx=Load()),
                                                            Name(id='options', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[
                                        For(
                                            target=Name(id='channel', ctx=Store()),
                                            iter=Name(id='channels', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='channel_events', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='channels',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='hashable', ctx=Load()),
                                                                args=[Name(id='channel', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='channel_events', ctx=Load()),
                                                            Compare(
                                                                left=Name(id='event', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[Name(id='channel_events', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='channel_events', ctx=Load()),
                                                                    attr='remove',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='event', ctx=Load())],
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
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='notifications', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='loop',
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
                        Expr(
                            value=Constant(value=' Dispatch postgres notifications to the relevant polling threads/greenlets ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='info',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Bus.loop listen imbus on db postgres', kind=None)],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='odoo', ctx=Load()),
                                                        attr='sql_db',
                                                        ctx=Load(),
                                                    ),
                                                    attr='db_connect',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='postgres', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='cr', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='conn', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='_cnx',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='listen imbus', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='commit',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                While(
                                    test=Constant(value=True, kind=None),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='select', ctx=Load()),
                                                        attr='select',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[Name(id='conn', ctx=Load())],
                                                            ctx=Load(),
                                                        ),
                                                        List(elts=[], ctx=Load()),
                                                        List(elts=[], ctx=Load()),
                                                        Name(id='TIMEOUT', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            List(elts=[], ctx=Load()),
                                                            List(elts=[], ctx=Load()),
                                                            List(elts=[], ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[Pass()],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='conn', ctx=Load()),
                                                            attr='poll',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='channels', ctx=Store())],
                                                    value=List(elts=[], ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                While(
                                                    test=Attribute(
                                                        value=Name(id='conn', ctx=Load()),
                                                        attr='notifies',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='channels', ctx=Load()),
                                                                    attr='extend',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='json', ctx=Load()),
                                                                            attr='loads',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='conn', ctx=Load()),
                                                                                            attr='notifies',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='pop',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[],
                                                                                    keywords=[],
                                                                                ),
                                                                                attr='payload',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='events', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='set', ctx=Load()),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='channel', ctx=Store()),
                                                    iter=Name(id='channels', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='events', ctx=Load()),
                                                                    attr='update',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='channels',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='pop',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='hashable', ctx=Load()),
                                                                                args=[Name(id='channel', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            Call(
                                                                                func=Name(id='set', ctx=Load()),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='event', ctx=Store()),
                                                    iter=Name(id='events', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='event', ctx=Load()),
                                                                    attr='set',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='wakeup_workers',
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
                        Expr(
                            value=Constant(value="\n        Wake up all http workers that are waiting for an event, useful\n        on server shutdown when they can't reveive anymore messages.\n        ", kind=None),
                        ),
                        For(
                            target=Name(id='events', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='channels',
                                        ctx=Load(),
                                    ),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='event', ctx=Store()),
                                    iter=Name(id='events', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='set',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
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
                    name='run',
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
                        While(
                            test=Constant(value=True, kind=None),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='loop',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name='e',
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='exception',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='Bus.loop error, sleep and retry', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='sleep',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='TIMEOUT', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='start',
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
                        If(
                            test=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='evented',
                                ctx=Load(),
                            ),
                            body=[
                                Import(
                                    names=[alias(name='gevent', asname=None)],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='Event',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='gevent', ctx=Load()),
                                            attr='event',
                                            ctx=Load(),
                                        ),
                                        attr='Event',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='gevent', ctx=Load()),
                                            attr='spawn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='run',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='Event',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='threading', ctx=Load()),
                                        attr='Event',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='t', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='Thread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='name',
                                                value=BinOp(
                                                    left=Constant(value='%s.Bus', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='__name__', ctx=Load()),
                                                ),
                                            ),
                                            keyword(
                                                arg='target',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='run',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='t', ctx=Load()),
                                            attr='daemon',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='t', ctx=Load()),
                                            attr='start',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='started',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='self', ctx=Load()),
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
            targets=[Name(id='dispatch', ctx=Store())],
            value=Constant(value=None, kind=None),
            type_comment=None,
        ),
        If(
            test=BoolOp(
                op=Or(),
                values=[
                    UnaryOp(
                        op=Not(),
                        operand=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='multi_process',
                            ctx=Load(),
                        ),
                    ),
                    Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='evented',
                        ctx=Load(),
                    ),
                ],
            ),
            body=[
                Assign(
                    targets=[Name(id='dispatch', ctx=Store())],
                    value=Call(
                        func=Name(id='ImDispatch', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Attribute(
                        value=Name(id='servermod', ctx=Load()),
                        attr='server',
                        ctx=Load(),
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='servermod', ctx=Load()),
                                        attr='server',
                                        ctx=Load(),
                                    ),
                                    attr='on_stop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='dispatch', ctx=Load()),
                                        attr='wakeup_workers',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
            ],
            orelse=[],
        ),
    ],
    type_ignores=[],
)
