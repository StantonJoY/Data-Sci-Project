Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='psycopg2', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
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
            targets=[Name(id='BASE_VERSION', ctx=Store())],
            value=Subscript(
                value=Call(
                    func=Attribute(
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='modules',
                            ctx=Load(),
                        ),
                        attr='load_information_from_description_file',
                        ctx=Load(),
                    ),
                    args=[Constant(value='base', kind=None)],
                    keywords=[],
                ),
                slice=Constant(value='version', kind=None),
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='MAX_FAIL_TIME', ctx=Store())],
            value=Call(
                func=Name(id='timedelta', ctx=Load()),
                args=[],
                keywords=[
                    keyword(
                        arg='hours',
                        value=Constant(value=5, kind=None),
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='BadVersion',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        ClassDef(
            name='BadModuleState',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='_intervalTypes', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='days', kind=None),
                    Constant(value='hours', kind=None),
                    Constant(value='weeks', kind=None),
                    Constant(value='months', kind=None),
                    Constant(value='minutes', kind=None),
                ],
                values=[
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='interval', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Call(
                            func=Name(id='relativedelta', ctx=Load()),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='days',
                                    value=Name(id='interval', ctx=Load()),
                                ),
                            ],
                        ),
                    ),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='interval', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Call(
                            func=Name(id='relativedelta', ctx=Load()),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='hours',
                                    value=Name(id='interval', ctx=Load()),
                                ),
                            ],
                        ),
                    ),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='interval', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Call(
                            func=Name(id='relativedelta', ctx=Load()),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='days',
                                    value=BinOp(
                                        left=Constant(value=7, kind=None),
                                        op=Mult(),
                                        right=Name(id='interval', ctx=Load()),
                                    ),
                                ),
                            ],
                        ),
                    ),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='interval', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Call(
                            func=Name(id='relativedelta', ctx=Load()),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='months',
                                    value=Name(id='interval', ctx=Load()),
                                ),
                            ],
                        ),
                    ),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='interval', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Call(
                            func=Name(id='relativedelta', ctx=Load()),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='minutes',
                                    value=Name(id='interval', ctx=Load()),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='ir_cron',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Model describing cron jobs (also called actions or tasks).\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.cron', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='cron_name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Scheduled Actions', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ir_actions_server_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.actions.server', kind=None),
                            Constant(value='Server action', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='delegate',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cron_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='ir_actions_server_id.name', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Scheduler User', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='interval_number', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Repeat every x.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='interval_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='minutes', kind=None),
                                            Constant(value='Minutes', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='hours', kind=None),
                                            Constant(value='Hours', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='days', kind=None),
                                            Constant(value='Days', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='weeks', kind=None),
                                            Constant(value='Weeks', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='months', kind=None),
                                            Constant(value='Months', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Interval Unit', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='months', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='numbercall', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Number of Calls', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='How many times the method is called,\na negative number indicates no limit.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='doall', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Repeat Missed', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Specify if missed occurrences should be executed when the server restarts.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='nextcall', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Next Execution Date', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='now',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Next planned execution date for this job.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lastcall', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Last Execution Date', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Previous time the cron ran successfully, provided to the job through the context on the `lastcall` key', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='priority', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=5, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The priority of the job, as an integer: 0 means higher priority, 10 means lower priority.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
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
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='usage', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='ir_cron', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='os', ctx=Load()),
                                    attr='getenv',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='ODOO_NOTIFY_CRON_CHANGES', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_cr',
                                                    ctx=Load(),
                                                ),
                                                attr='postcommit',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_notifydb',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ir_cron', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
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
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_context',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='default_state', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='self', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='default_state',
                                                value=Constant(value='code', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ir_cron', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields_list', ctx=Load())],
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
                    name='method_direct_trigger',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_access_rights',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='write', kind=None)],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='cron', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='cron', ctx=Load()),
                                                                attr='with_user',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='cron', ctx=Load()),
                                                                    attr='user_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='lastcall',
                                                            value=Attribute(
                                                                value=Name(id='cron', ctx=Load()),
                                                                attr='lastcall',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                attr='ir_actions_server_id',
                                                ctx=Load(),
                                            ),
                                            attr='run',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='cron', ctx=Load()),
                                            attr='lastcall',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_process_jobs',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='db_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Execute every job ready to be run on this database. ', kind=None),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='db', ctx=Store())],
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
                                        args=[Name(id='db_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='threading', ctx=Load()),
                                                    attr='current_thread',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='dbname',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='db_name', ctx=Load()),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='db', ctx=Load()),
                                                    attr='cursor',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='cron_cr', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='_check_version',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='cron_cr', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='jobs', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='_get_all_ready_jobs',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='cron_cr', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='jobs', ctx=Load()),
                                            ),
                                            body=[Return(value=None)],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='_check_modules_state',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cron_cr', ctx=Load()),
                                                    Name(id='jobs', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='job_ids', ctx=Store())],
                                            value=Call(
                                                func=Name(id='tuple', ctx=Load()),
                                                args=[
                                                    ListComp(
                                                        elt=Subscript(
                                                            value=Name(id='job', ctx=Load()),
                                                            slice=Constant(value='id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='job', ctx=Store()),
                                                                iter=Name(id='jobs', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        While(
                                            test=Constant(value=True, kind=None),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='job', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='cls', ctx=Load()),
                                                            attr='_acquire_one_job',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='cron_cr', ctx=Load()),
                                                            Name(id='job_ids', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='job', ctx=Load()),
                                                    ),
                                                    body=[Break()],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='debug',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='job %s acquired', kind=None),
                                                            Subscript(
                                                                value=Name(id='job', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='registry', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='odoo', ctx=Load()),
                                                            attr='registry',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='db_name', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='registry', ctx=Load()),
                                                                slice=Attribute(
                                                                    value=Name(id='cls', ctx=Load()),
                                                                    attr='_name',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_process_job',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='db', ctx=Load()),
                                                            Name(id='cron_cr', ctx=Load()),
                                                            Name(id='job', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='debug',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='job %s updated and released', kind=None),
                                                            Subscript(
                                                                value=Name(id='job', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
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
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='BadVersion', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Skipping database %s as its base version is not %s.', kind=None),
                                                    Name(id='db_name', ctx=Load()),
                                                    Name(id='BASE_VERSION', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='BadModuleState', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Skipping database %s because of modules to install/upgrade/remove.', kind=None),
                                                    Name(id='db_name', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='psycopg2', ctx=Load()),
                                        attr='ProgrammingError',
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='pgcode',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='42P01', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Tried to poll an undefined table on database %s.', kind=None),
                                                            Name(id='db_name', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[Raise(exc=None, cause=None)],
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='Exception', ctx=Load()),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='Exception in cron:', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='exc_info',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[
                                If(
                                    test=Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='threading', ctx=Load()),
                                                    attr='current_thread',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='dbname', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Delete(
                                            targets=[
                                                Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='threading', ctx=Load()),
                                                            attr='current_thread',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='dbname',
                                                    ctx=Del(),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_version',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='cron_cr', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Ensure the code version matches the database version ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cron_cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="\n            SELECT latest_version\n            FROM ir_module_module\n             WHERE name='base'\n        ", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[Name(id='version', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cron_cr', ctx=Load()),
                                    attr='fetchone',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='version', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='BadModuleState', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='version', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Name(id='BASE_VERSION', ctx=Load())],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='BadVersion', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_modules_state',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                            arg(arg='jobs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Ensure no module is installing or upgrading ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\n            SELECT COUNT(*)\n            FROM ir_module_module\n            WHERE state LIKE %s\n        ', kind=None),
                                    List(
                                        elts=[Constant(value='to %', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[Name(id='changes', ctx=Store())],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='fetchone',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='changes', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='jobs', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='BadModuleState', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='oldest', ctx=Store())],
                            value=Call(
                                func=Name(id='min', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='fields', ctx=Load()),
                                                    attr='Datetime',
                                                    ctx=Load(),
                                                ),
                                                attr='from_string',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Name(id='job', ctx=Load()),
                                                    slice=Constant(value='nextcall', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='job', ctx=Store()),
                                                iter=Name(id='jobs', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=BinOp(
                                    left=Call(
                                        func=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='now',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    op=Sub(),
                                    right=Name(id='oldest', ctx=Load()),
                                ),
                                ops=[Lt()],
                                comparators=[Name(id='MAX_FAIL_TIME', ctx=Load())],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='BadModuleState', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='odoo', ctx=Load()),
                                        attr='modules',
                                        ctx=Load(),
                                    ),
                                    attr='reset_modules_state',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='cr', ctx=Load()),
                                        attr='dbname',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_all_ready_jobs',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return a list of all jobs that are ready to be executed ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value="\n            SELECT *\n            FROM ir_cron\n            WHERE active = true\n              AND numbercall != 0\n              AND (nextcall <= (now() at time zone 'UTC')\n                OR id in (\n                    SELECT cron_id\n                    FROM ir_cron_trigger\n                    WHERE call_at <= (now() at time zone 'UTC')\n                )\n              )\n            ORDER BY priority\n        ", kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='dictfetchall',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_acquire_one_job',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                            arg(arg='job_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Acquire one job for update from the job_ids tuple. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="\n            SELECT *\n            FROM ir_cron\n            WHERE active = true\n              AND numbercall != 0\n              AND (nextcall <= (now() at time zone 'UTC')\n                OR EXISTS (\n                    SELECT cron_id\n                    FROM ir_cron_trigger\n                    WHERE call_at <= (now() at time zone 'UTC')\n                      AND cron_id = ir_cron.id\n                )\n              )\n              AND id in %s\n            ORDER BY priority\n            LIMIT 1 FOR NO KEY UPDATE SKIP LOCKED\n        ", kind=None),
                                    List(
                                        elts=[Name(id='job_ids', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='dictfetchone',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_process_job',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='db', annotation=None, type_comment=None),
                            arg(arg='cron_cr', annotation=None, type_comment=None),
                            arg(arg='job', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Execute a cron job and re-schedule a call for later. ', kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='pool',
                                                ctx=Load(),
                                            ),
                                            attr='cursor',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='job_cr', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='lastcall', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='to_datetime',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='job', ctx=Load()),
                                                slice=Constant(value='lastcall', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='interval', ctx=Store())],
                                    value=Call(
                                        func=Subscript(
                                            value=Name(id='_intervalTypes', ctx=Load()),
                                            slice=Subscript(
                                                value=Name(id='job', ctx=Load()),
                                                slice=Constant(value='interval_type', kind=None),
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='job', ctx=Load()),
                                                slice=Constant(value='interval_number', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='api', ctx=Load()),
                                            attr='Environment',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='job_cr', ctx=Load()),
                                            Subscript(
                                                value=Name(id='job', ctx=Load()),
                                                slice=Constant(value='user_id', kind=None),
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='lastcall', kind=None)],
                                                values=[Name(id='lastcall', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ir_cron', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='now', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='context_timestamp',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ir_cron', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='datetime', ctx=Load()),
                                                    attr='utcnow',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='past_nextcall', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='context_timestamp',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ir_cron', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_datetime',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='job', ctx=Load()),
                                                        slice=Constant(value='nextcall', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='missed_call', ctx=Store())],
                                    value=Name(id='past_nextcall', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='missed_call_count', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                While(
                                    test=Compare(
                                        left=Name(id='missed_call', ctx=Load()),
                                        ops=[LtE()],
                                        comparators=[Name(id='now', ctx=Load())],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='missed_call', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='interval', ctx=Load()),
                                        ),
                                        AugAssign(
                                            target=Name(id='missed_call_count', ctx=Store()),
                                            op=Add(),
                                            value=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='future_nextcall', ctx=Store())],
                                    value=Name(id='missed_call', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='effective_call_count', ctx=Store())],
                                    value=IfExp(
                                        test=UnaryOp(
                                            op=Not(),
                                            operand=Name(id='missed_call_count', ctx=Load()),
                                        ),
                                        body=Constant(value=1, kind=None),
                                        orelse=IfExp(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Subscript(
                                                    value=Name(id='job', ctx=Load()),
                                                    slice=Constant(value='doall', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=Constant(value=1, kind=None),
                                            orelse=IfExp(
                                                test=Compare(
                                                    left=Subscript(
                                                        value=Name(id='job', ctx=Load()),
                                                        slice=Constant(value='numbercall', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[
                                                        UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
                                                    ],
                                                ),
                                                body=Name(id='missed_call_count', ctx=Load()),
                                                orelse=Call(
                                                    func=Name(id='min', ctx=Load()),
                                                    args=[
                                                        Name(id='missed_call_count', ctx=Load()),
                                                        Subscript(
                                                            value=Name(id='job', ctx=Load()),
                                                            slice=Constant(value='numbercall', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='call_count_left', ctx=Store())],
                                    value=Call(
                                        func=Name(id='max', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Subscript(
                                                    value=Name(id='job', ctx=Load()),
                                                    slice=Constant(value='numbercall', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Name(id='effective_call_count', ctx=Load()),
                                            ),
                                            UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='call', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[Name(id='effective_call_count', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ir_cron', ctx=Load()),
                                                    attr='_callback',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='job', ctx=Load()),
                                                        slice=Constant(value='cron_name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='job', ctx=Load()),
                                                        slice=Constant(value='ir_actions_server_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='job', ctx=Load()),
                                                        slice=Constant(value='id', kind=None),
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
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cron_cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='\n            UPDATE ir_cron\n            SET nextcall=%s,\n                numbercall=%s,\n                lastcall=%s,\n                active=%s\n            WHERE id=%s\n        ', kind=None),
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_string',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='future_nextcall', ctx=Load()),
                                                            attr='astimezone',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='pytz', ctx=Load()),
                                                                attr='UTC',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='call_count_left', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='to_string',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='now', ctx=Load()),
                                                            attr='astimezone',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='pytz', ctx=Load()),
                                                                attr='UTC',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='job', ctx=Load()),
                                                        slice=Constant(value='active', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='bool', ctx=Load()),
                                                        args=[Name(id='call_count_left', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Subscript(
                                                value=Name(id='job', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cron_cr', ctx=Load()),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="\n            DELETE FROM ir_cron_trigger\n            WHERE cron_id = %s\n              AND call_at < (now() at time zone 'UTC')\n        ", kind=None),
                                    List(
                                        elts=[
                                            Subscript(
                                                value=Name(id='job', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cron_cr', ctx=Load()),
                                    attr='commit',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_callback',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cron_name', annotation=None, type_comment=None),
                            arg(arg='server_action_id', annotation=None, type_comment=None),
                            arg(arg='job_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Run the method associated to a given job. It takes care of logging\n        and exception handling. Note that the user running the server action\n        is the user calling this method. ', kind=None),
                        ),
                        Try(
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='pool',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='pool',
                                                        ctx=Load(),
                                                    ),
                                                    attr='check_signaling',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='reset',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='self', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_name',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='log_depth', ctx=Store())],
                                    value=IfExp(
                                        test=Call(
                                            func=Attribute(
                                                value=Name(id='_logger', ctx=Load()),
                                                attr='isEnabledFor',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='logging', ctx=Load()),
                                                    attr='DEBUG',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        body=Constant(value=None, kind=None),
                                        orelse=Constant(value=1, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='netsvc',
                                                ctx=Load(),
                                            ),
                                            attr='log',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='_logger', ctx=Load()),
                                            Attribute(
                                                value=Name(id='logging', ctx=Load()),
                                                attr='DEBUG',
                                                ctx=Load(),
                                            ),
                                            Constant(value='cron.object.execute', kind=None),
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_cr',
                                                            ctx=Load(),
                                                        ),
                                                        attr='dbname',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_uid',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='*', kind=None),
                                                    Name(id='cron_name', ctx=Load()),
                                                    Name(id='server_action_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='depth',
                                                value=Name(id='log_depth', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='start_time', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Starting job `%s`.', kind=None),
                                            Name(id='cron_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='isEnabledFor',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='logging', ctx=Load()),
                                                attr='DEBUG',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='start_time', ctx=Store())],
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
                                    ],
                                    orelse=[],
                                ),
                                Expr(
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
                                                        slice=Constant(value='ir.actions.server', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='server_action_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='run',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='Job `%s` done.', kind=None),
                                            Name(id='cron_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='start_time', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='isEnabledFor',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='logging', ctx=Load()),
                                                        attr='DEBUG',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='end_time', ctx=Store())],
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='%.3fs (cron %s, server action %d with uid %d)', kind=None),
                                                    BinOp(
                                                        left=Name(id='end_time', ctx=Load()),
                                                        op=Sub(),
                                                        right=Name(id='start_time', ctx=Load()),
                                                    ),
                                                    Name(id='cron_name', ctx=Load()),
                                                    Name(id='server_action_id', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uid',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='pool',
                                                ctx=Load(),
                                            ),
                                            attr='signal_changes',
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
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='pool',
                                                        ctx=Load(),
                                                    ),
                                                    attr='reset_changes',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='exception',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Call from cron %s for server action #%s failed in Job #%s', kind=None),
                                                    Name(id='cron_name', ctx=Load()),
                                                    Name(id='server_action_id', ctx=Load()),
                                                    Name(id='job_id', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_handle_callback_exception',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cron_name', ctx=Load()),
                                                    Name(id='server_action_id', ctx=Load()),
                                                    Name(id='job_id', ctx=Load()),
                                                    Name(id='e', ctx=Load()),
                                                ],
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
                    name='_handle_callback_exception',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cron_name', annotation=None, type_comment=None),
                            arg(arg='server_action_id', annotation=None, type_comment=None),
                            arg(arg='job_id', annotation=None, type_comment=None),
                            arg(arg='job_exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Method called when an exception is raised by a job.\n\n        Simply logs the exception and rollback the transaction. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_cr',
                                        ctx=Load(),
                                    ),
                                    attr='rollback',
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
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_try_lock',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='lockfk', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Try to grab a dummy exclusive write-lock to the rows with the given ids,\n           to make sure a following write() or unlink() will not block due\n           to a process currently executing those cron tasks.\n\n           :param lockfk: acquire a strong row lock which conflicts with\n                          the lock aquired by foreign keys when they\n                          reference this row.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='row_level_lock', ctx=Store())],
                            value=IfExp(
                                test=Name(id='lockfk', ctx=Load()),
                                body=Constant(value='UPDATE', kind=None),
                                orelse=Constant(value='NO KEY UPDATE', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value='\n                SELECT id\n                FROM "', kind=None),
                                                    FormattedValue(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_table',
                                                            ctx=Load(),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='"\n                WHERE id IN %s\n                FOR ', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='row_level_lock', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=' NOWAIT\n            ', kind=None),
                                                ],
                                            ),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='tuple', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='log_exceptions',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='psycopg2', ctx=Load()),
                                        attr='OperationalError',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='rollback',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Record cannot be modified right now: This cron task is currently being executed and may not be modified Please try again in a few minutes', kind=None)],
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
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
                                    attr='_try_lock',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Constant(value='nextcall', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='active', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='getenv',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='ODOO_NOTIFY_CRON_CHANGES', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_cr',
                                                    ctx=Load(),
                                                ),
                                                attr='postcommit',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_notifydb',
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
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ir_cron', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_try_lock',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='lockfk',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ir_cron', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='try_write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='savepoint',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    JoinedStr(
                                                        values=[
                                                            Constant(value='\n                    SELECT id\n                    FROM "', kind=None),
                                                            FormattedValue(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_table',
                                                                    ctx=Load(),
                                                                ),
                                                                conversion=-1,
                                                                format_spec=None,
                                                            ),
                                                            Constant(value='"\n                    WHERE id IN %s\n                    FOR NO KEY UPDATE NOWAIT\n                ', kind=None),
                                                        ],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Name(id='tuple', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='log_exceptions',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='psycopg2', ctx=Load()),
                                        attr='OperationalError',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='ir_cron', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            finalbody=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='toggle',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='active', ctx=Store())],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='model', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='try_write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='active', kind=None)],
                                        values=[Name(id='active', ctx=Load())],
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
                    name='_trigger',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='at', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Schedule a cron job to be executed soon independently of its\n        ``nextcall`` field value.\n\n        By default the cron is scheduled to be executed in the next batch but\n        the optional `at` argument may be given to delay the execution later\n        with a precision down to 1 minute.\n\n        The method may be called with a datetime or an iterable of datetime.\n        The actual implementation is in :meth:`~._trigger_list`, which is the\n        recommended method for overrides.\n\n        :param Optional[Union[datetime.datetime, list[datetime.datetime]]] at:\n            When to execute the cron, at one or several moments in time instead\n            of as soon as possible.\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='at', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='at_list', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='at', ctx=Load()),
                                            Name(id='datetime', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='at_list', ctx=Store())],
                                            value=List(
                                                elts=[Name(id='at', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='at_list', ctx=Store())],
                                            value=Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[Name(id='at', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assert(
                                            test=Call(
                                                func=Name(id='all', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Call(
                                                            func=Name(id='isinstance', ctx=Load()),
                                                            args=[
                                                                Name(id='at', ctx=Load()),
                                                                Name(id='datetime', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='at', ctx=Store()),
                                                                iter=Name(id='at_list', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            msg=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_trigger_list',
                                    ctx=Load(),
                                ),
                                args=[Name(id='at_list', ctx=Load())],
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
                    name='_trigger_list',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='at_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Implementation of :meth:`~._trigger`.\n\n        :param list[datetime.datetime] at_list:\n            Execute the cron later, at precise moments in time.\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='at_list', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='now', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
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
                        Expr(
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
                                                slice=Constant(value='ir.cron.trigger', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='cron_id', kind=None),
                                                Constant(value='call_at', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Name(id='at', ctx=Load()),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='at', ctx=Store()),
                                                iter=Name(id='at_list', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='isEnabledFor',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='logging', ctx=Load()),
                                        attr='DEBUG',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ats', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value=', ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='map', ctx=Load()),
                                                args=[
                                                    Name(id='str', ctx=Load()),
                                                    Name(id='at_list', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='debug',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="will execute '%s' at %s", kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='sudo',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Name(id='ats', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Name(id='min', ctx=Load()),
                                            args=[Name(id='at_list', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[LtE()],
                                        comparators=[Name(id='now', ctx=Load())],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='os', ctx=Load()),
                                            attr='getenv',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='ODOO_NOTIFY_CRON_CHANGES', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_cr',
                                                    ctx=Load(),
                                                ),
                                                attr='postcommit',
                                                ctx=Load(),
                                            ),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_notifydb',
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
                    name='_notifydb',
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
                            value=Constant(value=' Wake up the cron workers\n        The ODOO_NOTIFY_CRON_CHANGES environment variable allows to force the notifydb on both\n        ir_cron modification and on trigger creation (regardless of call_at)\n        ', kind=None),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='NOTIFY cron_trigger, %s', kind=None),
                                            List(
                                                elts=[
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='cron workers notified', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ir_cron_trigger',
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
                    value=Constant(value='ir.cron.trigger', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Triggered actions', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='cron_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.cron', kind=None)],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='call_at', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
