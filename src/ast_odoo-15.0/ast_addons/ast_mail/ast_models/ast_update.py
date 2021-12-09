Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.urls', asname=None)],
        ),
        ImportFrom(
            module='ast',
            names=[alias(name='literal_eval', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='release', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.models',
            names=[alias(name='AbstractModel', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='config', asname=None),
                alias(name='misc', asname=None),
                alias(name='ustr', asname=None),
            ],
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
        ClassDef(
            name='PublisherWarrantyContract',
            bases=[Name(id='AbstractModel', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='publisher_warranty.contract', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Publisher Warranty Contract', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_message',
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
                            targets=[Name(id='Users', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.users', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='IrParamSudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dbuuid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrParamSudo', ctx=Load()),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='database.uuid', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='db_create_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrParamSudo', ctx=Load()),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='database.create_date', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='limit_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
                                        attr='datetime',
                                        ctx=Load(),
                                    ),
                                    attr='now',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='limit_date', ctx=Store())],
                            value=BinOp(
                                left=Name(id='limit_date', ctx=Load()),
                                op=Sub(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='datetime', ctx=Load()),
                                        attr='timedelta',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value=15, kind=None)],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='limit_date_str', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='limit_date', ctx=Load()),
                                    attr='strftime',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='misc', ctx=Load()),
                                        attr='DEFAULT_SERVER_DATETIME_FORMAT',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='nbr_users', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Users', ctx=Load()),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='nbr_active_users', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Users', ctx=Load()),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='login_date', kind=None),
                                                    Constant(value='>=', kind=None),
                                                    Name(id='limit_date_str', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=True, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='nbr_share_users', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='nbr_active_share_users', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='share', kind=None),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='Users', ctx=Load()),
                                        attr='_fields',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='nbr_share_users', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Users', ctx=Load()),
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='share', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='active', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='nbr_active_share_users', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Users', ctx=Load()),
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='share', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='login_date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Name(id='limit_date_str', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='active', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='user', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='user',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='application', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='in', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='installed', kind=None),
                                                    Constant(value='to upgrade', kind=None),
                                                    Constant(value='to remove', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='apps', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.module.module', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    List(
                                        elts=[Constant(value='name', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='enterprise_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrParamSudo', ctx=Load()),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='database.enterprise_code', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='web_base_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrParamSudo', ctx=Load()),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='web.base.url', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='dbuuid', kind=None),
                                    Constant(value='nbr_users', kind=None),
                                    Constant(value='nbr_active_users', kind=None),
                                    Constant(value='nbr_share_users', kind=None),
                                    Constant(value='nbr_active_share_users', kind=None),
                                    Constant(value='dbname', kind=None),
                                    Constant(value='db_create_date', kind=None),
                                    Constant(value='version', kind=None),
                                    Constant(value='language', kind=None),
                                    Constant(value='web_base_url', kind=None),
                                    Constant(value='apps', kind=None),
                                    Constant(value='enterprise_code', kind=None),
                                ],
                                values=[
                                    Name(id='dbuuid', ctx=Load()),
                                    Name(id='nbr_users', ctx=Load()),
                                    Name(id='nbr_active_users', ctx=Load()),
                                    Name(id='nbr_share_users', ctx=Load()),
                                    Name(id='nbr_active_share_users', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_cr',
                                            ctx=Load(),
                                        ),
                                        attr='dbname',
                                        ctx=Load(),
                                    ),
                                    Name(id='db_create_date', ctx=Load()),
                                    Attribute(
                                        value=Name(id='release', ctx=Load()),
                                        attr='version',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='user', ctx=Load()),
                                        attr='lang',
                                        ctx=Load(),
                                    ),
                                    Name(id='web_base_url', ctx=Load()),
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='app', ctx=Load()),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='app', ctx=Store()),
                                                iter=Name(id='apps', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Name(id='enterprise_code', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='user', ctx=Load()),
                                    attr='partner_id',
                                    ctx=Load(),
                                ),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='company_id', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='user', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='msg', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='company_id', ctx=Load()),
                                                        attr='read',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='email', kind=None),
                                                                Constant(value='phone', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='msg', ctx=Load()),
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
                    name='_get_sys_logs',
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
                            value=Constant(value='\n        Utility method to send a publisher warranty get logs messages.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_message',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='arguments', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='arg0', kind=None),
                                    Constant(value='action', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='ustr', ctx=Load()),
                                        args=[Name(id='msg', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value='update', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='config', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='publisher_warranty_url', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='requests', ctx=Load()),
                                    attr='post',
                                    ctx=Load(),
                                ),
                                args=[Name(id='url', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='data',
                                        value=Name(id='arguments', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Constant(value=30, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='r', ctx=Load()),
                                    attr='raise_for_status',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='literal_eval', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='r', ctx=Load()),
                                        attr='text',
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
                    name='update_notification',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cron_mode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Send a message to Odoo's publisher warranty server to check the\n        validity of the contracts, get notifications, etc...\n\n        @param cron_mode: If true, catch all exceptions (appropriate for usage in a cron).\n        @type cron_mode: boolean\n        ", kind=None),
                        ),
                        Try(
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='result', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_sys_logs',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[
                                                If(
                                                    test=Name(id='cron_mode', ctx=Load()),
                                                    body=[
                                                        Return(
                                                            value=Constant(value=False, kind=None),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='debug',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='Exception while sending a get logs messages', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='exc_info',
                                                                value=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Error during communication with the publisher warranty server.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Assign(
                                    targets=[Name(id='user', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.users', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='SUPERUSER_ID', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='poster', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='sudo',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mail.channel_all_employees', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=BoolOp(
                                            op=And(),
                                            values=[
                                                Name(id='poster', ctx=Load()),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='poster', ctx=Load()),
                                                        attr='exists',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='exists',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='poster', ctx=Store())],
                                            value=Name(id='user', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='message', ctx=Store()),
                                    iter=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='messages', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='poster', ctx=Load()),
                                                            attr='message_post',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='body',
                                                                value=Name(id='message', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='subtype_xmlid',
                                                                value=Constant(value='mail.mt_comment', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='partner_ids',
                                                                value=List(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='user', ctx=Load()),
                                                                                attr='partner_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
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
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='enterprise_info', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='set_param', ctx=Store())],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='ir.config_parameter', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='sudo',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='set_param',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='set_param', ctx=Load()),
                                                args=[
                                                    Constant(value='database.expiration_date', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='result', ctx=Load()),
                                                                slice=Constant(value='enterprise_info', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='expiration_date', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='set_param', ctx=Load()),
                                                args=[
                                                    Constant(value='database.expiration_reason', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='result', ctx=Load()),
                                                                slice=Constant(value='enterprise_info', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='expiration_reason', kind=None),
                                                            Constant(value='trial', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='set_param', ctx=Load()),
                                                args=[
                                                    Constant(value='database.enterprise_code', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='result', ctx=Load()),
                                                                slice=Constant(value='enterprise_info', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='enterprise_code', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='set_param', ctx=Load()),
                                                args=[
                                                    Constant(value='database.already_linked_subscription_url', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='result', ctx=Load()),
                                                                slice=Constant(value='enterprise_info', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='database_already_linked_subscription_url', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='set_param', ctx=Load()),
                                                args=[
                                                    Constant(value='database.already_linked_email', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='result', ctx=Load()),
                                                                slice=Constant(value='enterprise_info', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='database_already_linked_email', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='set_param', ctx=Load()),
                                                args=[
                                                    Constant(value='database.already_linked_send_mail_url', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='result', ctx=Load()),
                                                                slice=Constant(value='enterprise_info', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='database_already_linked_send_mail_url', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        If(
                                            test=Name(id='cron_mode', ctx=Load()),
                                            body=[
                                                Return(
                                                    value=Constant(value=False, kind=None),
                                                ),
                                            ],
                                            orelse=[Raise(exc=None, cause=None)],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
