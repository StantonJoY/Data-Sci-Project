Module(
    body=[
        Import(
            names=[alias(name='ast', asname=None)],
        ),
        Import(
            names=[alias(name='itertools', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='date', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[
                alias(name='relativedelta', asname=None),
                alias(name='MO', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='_', asname=None),
                alias(name='exceptions', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='ustr', asname=None)],
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
            targets=[Name(id='MAX_VISIBILITY_RANKING', ctx=Store())],
            value=Constant(value=3, kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='start_end_date_for_period',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='period', annotation=None, type_comment=None),
                    arg(arg='default_start_date', annotation=None, type_comment=None),
                    arg(arg='default_end_date', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value=False, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='Return the start and end date for a goal period based on today\n\n    :param str default_start_date: string date in DEFAULT_SERVER_DATE_FORMAT format\n    :param str default_end_date: string date in DEFAULT_SERVER_DATE_FORMAT format\n\n    :return: (start_date, end_date), dates in string format, False if the period is\n    not defined or unknown', kind=None),
                ),
                Assign(
                    targets=[Name(id='today', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='date', ctx=Load()),
                            attr='today',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='period', ctx=Load()),
                        ops=[Eq()],
                        comparators=[Constant(value='daily', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='start_date', ctx=Store())],
                            value=Name(id='today', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end_date', ctx=Store())],
                            value=Name(id='start_date', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        If(
                            test=Compare(
                                left=Name(id='period', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='weekly', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='start_date', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='today', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='relativedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='weekday',
                                                    value=Call(
                                                        func=Name(id='MO', ctx=Load()),
                                                        args=[
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='end_date', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='start_date', ctx=Load()),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Constant(value=7, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='period', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='monthly', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='start_date', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='today', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='day',
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='end_date', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='today', ctx=Load()),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='months',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                        keyword(
                                                            arg='day',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                        keyword(
                                                            arg='days',
                                                            value=UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=1, kind=None),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='period', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='yearly', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='start_date', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='today', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='month',
                                                                value=Constant(value=1, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='day',
                                                                value=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='end_date', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='today', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='month',
                                                                value=Constant(value=12, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='day',
                                                                value=Constant(value=31, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='start_date', ctx=Store())],
                                                    value=Name(id='default_start_date', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='end_date', ctx=Store())],
                                                    value=Name(id='default_end_date', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Return(
                                                    value=Tuple(
                                                        elts=[
                                                            Name(id='start_date', ctx=Load()),
                                                            Name(id='end_date', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                Return(
                    value=Tuple(
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
                                args=[Name(id='start_date', ctx=Load())],
                                keywords=[],
                            ),
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
                                args=[Name(id='end_date', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                        ctx=Load(),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='Challenge',
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
                    value=Constant(value="Gamification challenge\n\n    Set of predifined objectives assigned to people with rules for recurrence and\n    rewards\n\n    If 'user_ids' is defined and 'period' is different than 'one', the set will\n    be assigned to the users for each period (eg: every 1st of each month if\n    'monthly' is selected)\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='gamification.challenge', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Gamification Challenge', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='mail.thread', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='end_date, start_date, name, id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Challenge Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='description', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Description', kind=None)],
                        keywords=[
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state', ctx=Store())],
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
                                            Constant(value='draft', kind=None),
                                            Constant(value='Draft', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='inprogress', kind=None),
                                            Constant(value='In Progress', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='done', kind=None),
                                            Constant(value='Done', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='draft', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='State', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='tracking',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='manager_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
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
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Responsible', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The user responsible for the challenge.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.users', kind=None),
                            Constant(value='gamification_challenge_users_rel', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Users', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='List of users participating to the challenge', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_domain', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='User domain', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Alternative to a list of users', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='period', ctx=Store())],
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
                                            Constant(value='once', kind=None),
                                            Constant(value='Non recurring', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='daily', kind=None),
                                            Constant(value='Daily', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='weekly', kind=None),
                                            Constant(value='Weekly', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='monthly', kind=None),
                                            Constant(value='Monthly', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='yearly', kind=None),
                                            Constant(value='Yearly', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='once', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Periodicity', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Period of automatic goal assigment. If none is selected, should be launched manually.', kind=None),
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
                    targets=[Name(id='start_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Start Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='The day a new challenge will be automatically started. If no periodicity is set, will use this date as the goal start date.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='end_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(value='End Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='The day a new challenge will be automatically closed. If no periodicity is set, will use this date as the goal end date.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='invited_user_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.users', kind=None),
                            Constant(value='gamification_invited_user_ids_rel', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Suggest to users', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='line_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='gamification.challenge.line', kind=None),
                            Constant(value='challenge_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Lines', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='List of goals that will be set', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reward_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='gamification.badge', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='For Every Succeeding User', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reward_first_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='gamification.badge', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='For 1st user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reward_second_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='gamification.badge', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='For 2nd user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reward_third_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='gamification.badge', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='For 3rd user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reward_failure', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Reward Bests if not Succeeded?', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reward_realtime', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Reward as soon as every goal is reached', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='With this option enabled, a user can receive a badge only once. The top 3 badges are still rewarded only at the end of the challenge.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='visibility_mode', ctx=Store())],
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
                                            Constant(value='personal', kind=None),
                                            Constant(value='Individual Goals', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='ranking', kind=None),
                                            Constant(value='Leader Board (Group Ranking)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='personal', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Display Mode', kind=None),
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
                    targets=[Name(id='report_message_frequency', ctx=Store())],
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
                                            Constant(value='never', kind=None),
                                            Constant(value='Never', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='onchange', kind=None),
                                            Constant(value='On change', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='daily', kind=None),
                                            Constant(value='Daily', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='weekly', kind=None),
                                            Constant(value='Weekly', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='monthly', kind=None),
                                            Constant(value='Monthly', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='yearly', kind=None),
                                            Constant(value='Yearly', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='never', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Report Frequency', kind=None),
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
                    targets=[Name(id='report_message_group_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='mail.channel', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Send a copy to', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Group that will receive a copy of the report in addition to the user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='report_template_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='mail.template', kind=None)],
                        keywords=[
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
                                    body=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_report_template',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Report Template', kind=None),
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
                    targets=[Name(id='remind_update_delay', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Non-updated manual goals will be reminded after', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Never reminded if no value or zero is specified.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='last_report_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Last Report Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='today',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='next_report_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Next Report Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_get_next_report_date', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='challenge_category', ctx=Store())],
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
                                            Constant(value='hr', kind=None),
                                            Constant(value='Human Resources / Engagement', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='other', kind=None),
                                            Constant(value='Settings / Gamification Tools', kind=None),
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
                                value=Constant(value='Appears in', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='hr', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Define the visibility of the challenge through menus', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='REPORT_OFFSETS', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='daily', kind=None),
                            Constant(value='weekly', kind=None),
                            Constant(value='monthly', kind=None),
                            Constant(value='yearly', kind=None),
                        ],
                        values=[
                            Call(
                                func=Name(id='timedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='days',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            Call(
                                func=Name(id='timedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='days',
                                        value=Constant(value=7, kind=None),
                                    ),
                                ],
                            ),
                            Call(
                                func=Name(id='relativedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='months',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            Call(
                                func=Name(id='relativedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='years',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_next_report_date',
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
                            value=Constant(value=' Return the next report date based on the last report date and\n        report period.\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='challenge', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='last', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='challenge', ctx=Load()),
                                        attr='last_report_date',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='offset', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='REPORT_OFFSETS',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='report_message_frequency',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='offset', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='challenge', ctx=Load()),
                                                    attr='next_report_date',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Name(id='last', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='offset', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='challenge', ctx=Load()),
                                                    attr='next_report_date',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='last_report_date', kind=None),
                                Constant(value='report_message_frequency', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_report_template',
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
                            targets=[Name(id='template', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='ref',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='gamification.simple_report_template', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=IfExp(
                                test=Name(id='template', ctx=Load()),
                                body=Attribute(
                                    value=Name(id='template', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                orelse=Constant(value=False, kind=None),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Overwrite the create method to add the user of groups', kind=None),
                        ),
                        For(
                            target=Name(id='vals', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='user_domain', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='users', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_challenger_users',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='ustr', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='vals', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='user_domain', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='vals', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='user_ids', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='vals', ctx=Load()),
                                                            slice=Constant(value='user_ids', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=List(elts=[], ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Constant(value='user_ids', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='extend',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Tuple(
                                                            elts=[
                                                                Constant(value=4, kind=None),
                                                                Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='user', ctx=Store()),
                                                                iter=Name(id='users', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
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
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='user_domain', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='users', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_challenger_users',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='ustr', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='vals', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='user_domain', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='vals', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='user_ids', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='user_ids', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='user_ids', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='extend',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Tuple(
                                                    elts=[
                                                        Constant(value=4, kind=None),
                                                        Attribute(
                                                            value=Name(id='user', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='user', ctx=Store()),
                                                        iter=Name(id='users', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='write_res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Challenge', ctx=Load()),
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
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='vals', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='report_message_frequency', kind=None),
                                        Constant(value='never', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='never', kind=None)],
                            ),
                            body=[
                                For(
                                    target=Name(id='challenge', ctx=Store()),
                                    iter=Name(id='self', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='challenge', ctx=Load()),
                                                    attr='message_subscribe',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    ListComp(
                                                        elt=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='partner_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='user', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='challenge', ctx=Load()),
                                                                    attr='user_ids',
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
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
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='vals', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='state', kind=None)],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='inprogress', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_recompute_challenge_users',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_generate_goals_from_challenge',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='vals', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='state', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='done', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_check_challenge_reward',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='force',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='vals', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='state', kind=None)],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='draft', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='gamification.goal', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='challenge_id', kind=None),
                                                                            Constant(value='in', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='ids',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='state', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Constant(value='inprogress', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='limit',
                                                                value=Constant(value=1, kind=None),
                                                            ),
                                                        ],
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
                                                                        args=[Constant(value='You can not reset a challenge with unfinished goals.', kind=None)],
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
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='write_res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_cron_update',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='ids', annotation=None, type_comment=None),
                            arg(arg='commit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Daily cron check.\n\n        - Start planned challenges (in draft and with start_date = today)\n        - Create the missing goals (eg: modified the challenge to add lines)\n        - Update every running challenge\n        ', kind=None),
                        ),
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
                                        arg='commit_gamification',
                                        value=Name(id='commit', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='planned_challenges', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='draft', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='start_date', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='today',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
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
                        If(
                            test=Name(id='planned_challenges', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='planned_challenges', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='state', kind=None)],
                                                values=[Constant(value='inprogress', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='scheduled_challenges', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='inprogress', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='end_date', kind=None),
                                                    Constant(value='<', kind=None),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='today',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
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
                        If(
                            test=Name(id='scheduled_challenges', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='scheduled_challenges', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='state', kind=None)],
                                                values=[Constant(value='done', kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=IfExp(
                                test=Name(id='ids', ctx=Load()),
                                body=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='browse',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='ids', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='search',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='state', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Constant(value='inprogress', kind=None),
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
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='records', ctx=Load()),
                                    attr='_update_all',
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
                    name='_update_all',
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
                            value=Constant(value='Update the challenges and related goals\n\n        :param list(int) ids: the ids of the challenges to update, if False will\n        update only challenges in progress.', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='self', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='Goals', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='gamification.goal', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='yesterday', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='to_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='date', ctx=Load()),
                                                attr='today',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="SELECT gg.id\n                        FROM gamification_goal as gg\n                        JOIN res_users_log as log ON gg.user_id = log.create_uid\n                       WHERE gg.write_date < log.create_date\n                         AND gg.closed IS NOT TRUE\n                         AND gg.challenge_id IN %s\n                         AND (gg.state = 'inprogress'\n                              OR (gg.state = 'reached' AND gg.end_date >= %s))\n                      GROUP BY gg.id\n        ", kind=None),
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
                                            Name(id='yesterday', ctx=Load()),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Goals', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Name(id='goal_id', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=List(
                                                            elts=[Name(id='goal_id', ctx=Store())],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='fetchall',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='update_goal',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_recompute_challenge_users',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_generate_goals_from_challenge',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='challenge', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='challenge', ctx=Load()),
                                            attr='last_report_date',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='today',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='challenge', ctx=Load()),
                                                        attr='next_report_date',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='fields', ctx=Load()),
                                                                    attr='Date',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='today',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ops=[GtE()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='challenge', ctx=Load()),
                                                                attr='next_report_date',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='challenge', ctx=Load()),
                                                            attr='report_progress',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='closed_goals_to_report', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Goals', ctx=Load()),
                                                            attr='search',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='challenge_id', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='challenge', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='start_date', kind=None),
                                                                            Constant(value='>=', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='challenge', ctx=Load()),
                                                                                attr='last_report_date',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='end_date', kind=None),
                                                                            Constant(value='<=', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='challenge', ctx=Load()),
                                                                                attr='last_report_date',
                                                                                ctx=Load(),
                                                                            ),
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
                                                If(
                                                    test=Name(id='closed_goals_to_report', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='challenge', ctx=Load()),
                                                                    attr='report_progress',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='subset_goals',
                                                                        value=Name(id='closed_goals_to_report', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_check_challenge_reward',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
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
                    name='_get_challenger_users',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
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
                            targets=[Name(id='user_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ast', ctx=Load()),
                                    attr='literal_eval',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='user_domain', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_recompute_challenge_users',
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
                            value=Constant(value='Recompute the domain to add new users and remove the one no longer matching the domain', kind=None),
                        ),
                        For(
                            target=Name(id='challenge', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='c', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='c', ctx=Load()),
                                            attr='user_domain',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='current_users', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='challenge', ctx=Load()),
                                        attr='user_ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_users', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_challenger_users',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='user_domain',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='current_users', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Name(id='new_users', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='challenge', ctx=Load()),
                                                    attr='user_ids',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='new_users', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
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
                    name='action_start',
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
                            value=Constant(value='Start a challenge', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='inprogress', kind=None)],
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
                FunctionDef(
                    name='action_check',
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
                            value=Constant(value="Check a challenge\n\n        Create goals that haven't been created yet (eg: if added users)\n        Recompute the current value for each goal related", kind=None),
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
                                                slice=Constant(value='gamification.goal', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='challenge_id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='state', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='inprogress', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_update_all',
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
                    name='action_report_progress',
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
                            value=Constant(value='Manual report of a goal, does not influence automatic report frequency', kind=None),
                        ),
                        For(
                            target=Name(id='challenge', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='challenge', ctx=Load()),
                                            attr='report_progress',
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
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_generate_goals_from_challenge',
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
                            value=Constant(value='Generate the goals for each line and user.\n\n        If goals already exist for this line and user, the line is skipped. This\n        can be called after each change in the list of users or lines.\n        :param list(int) ids: the list of challenge concerned', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='Goals', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='gamification.goal', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='challenge', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='start_date', ctx=Store()),
                                                Name(id='end_date', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='start_end_date_for_period', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='period',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='start_date',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='end_date',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='to_update', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Goals', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Tuple(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='line', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='challenge', ctx=Load()),
                                        attr='line_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='date_clause', ctx=Store())],
                                            value=Constant(value='', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='query_params', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='start_date', ctx=Load()),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='date_clause', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=' AND g.start_date = %s', kind=None),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='query_params', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='start_date', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Name(id='end_date', ctx=Load()),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='date_clause', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=' AND g.end_date = %s', kind=None),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='query_params', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='end_date', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='query', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Constant(value='SELECT u.id AS user_id\n                             FROM res_users u\n                        LEFT JOIN gamification_goal g\n                               ON (u.id = g.user_id)\n                            WHERE line_id = %s\n                              {date_clause}\n                        ', kind=None),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='date_clause',
                                                        value=Name(id='date_clause', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='query', ctx=Load()),
                                                    Name(id='query_params', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='user_with_goal_ids', ctx=Store())],
                                            value=SetComp(
                                                elt=Name(id='it', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=List(
                                                            elts=[Name(id='it', ctx=Store())],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='cr',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_obj',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='participant_user_ids', ctx=Store())],
                                            value=Call(
                                                func=Name(id='set', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='challenge', ctx=Load()),
                                                            attr='user_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='user_squating_challenge_ids', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='user_with_goal_ids', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='participant_user_ids', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='user_squating_challenge_ids', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='Goals', ctx=Load()),
                                                                    attr='search',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='challenge_id', kind=None),
                                                                                    Constant(value='=', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='challenge', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='user_id', kind=None),
                                                                                    Constant(value='in', kind=None),
                                                                                    Call(
                                                                                        func=Name(id='list', ctx=Load()),
                                                                                        args=[Name(id='user_squating_challenge_ids', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
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
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='definition_id', kind=None),
                                                    Constant(value='line_id', kind=None),
                                                    Constant(value='target_goal', kind=None),
                                                    Constant(value='state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='line', ctx=Load()),
                                                            attr='definition_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='target_goal',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='inprogress', kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='start_date', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='start_date', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='start_date', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Name(id='end_date', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='end_date', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='end_date', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='condition',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='higher', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='current', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='min', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='target_goal',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Sub(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='current', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='max', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='target_goal',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Add(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='remind_update_delay',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='remind_update_delay', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='challenge', ctx=Load()),
                                                        attr='remind_update_delay',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        For(
                                            target=Name(id='user_id', ctx=Store()),
                                            iter=BinOp(
                                                left=Name(id='participant_user_ids', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='user_with_goal_ids', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='user_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='user_id', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='to_update', ctx=Store()),
                                                    op=BitOr(),
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Goals', ctx=Load()),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='values', ctx=Load())],
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='to_update', ctx=Load()),
                                            attr='update_goal',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='commit_gamification', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='commit',
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
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_serialized_challenge_lines',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                            arg(arg='restrict_goals', annotation=None, type_comment=None),
                            arg(arg='restrict_top', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Tuple(elts=[], ctx=Load()),
                            Tuple(elts=[], ctx=Load()),
                            Constant(value=0, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Return a serialised version of the goals information if the user has not completed every goal\n\n        :param user: user retrieving progress (False if no distinction,\n                     only for ranking challenges)\n        :param restrict_goals: compute only the results for this subset of\n                               gamification.goal ids, if False retrieve every\n                               goal of current running challenge\n        :param int restrict_top: for challenge lines where visibility_mode is\n                                 ``ranking``, retrieve only the best\n                                 ``restrict_top`` results and itself, if 0\n                                 retrieve all restrict_goal_ids has priority\n                                 over restrict_top\n\n        format list\n        # if visibility_mode == 'ranking'\n        {\n            'name': <gamification.goal.description name>,\n            'description': <gamification.goal.description description>,\n            'condition': <reach condition {lower,higher}>,\n            'computation_mode': <target computation {manually,count,sum,python}>,\n            'monetary': <{True,False}>,\n            'suffix': <value suffix>,\n            'action': <{True,False}>,\n            'display_mode': <{progress,boolean}>,\n            'target': <challenge line target>,\n            'own_goal_id': <gamification.goal id where user_id == uid>,\n            'goals': [\n                {\n                    'id': <gamification.goal id>,\n                    'rank': <user ranking>,\n                    'user_id': <res.users id>,\n                    'name': <res.users name>,\n                    'state': <gamification.goal state {draft,inprogress,reached,failed,canceled}>,\n                    'completeness': <percentage>,\n                    'current': <current value>,\n                }\n            ]\n        },\n        # if visibility_mode == 'personal'\n        {\n            'id': <gamification.goal id>,\n            'name': <gamification.goal.description name>,\n            'description': <gamification.goal.description description>,\n            'condition': <reach condition {lower,higher}>,\n            'computation_mode': <target computation {manually,count,sum,python}>,\n            'monetary': <{True,False}>,\n            'suffix': <value suffix>,\n            'action': <{True,False}>,\n            'display_mode': <{progress,boolean}>,\n            'target': <challenge line target>,\n            'state': <gamification.goal state {draft,inprogress,reached,failed,canceled}>,\n            'completeness': <percentage>,\n            'current': <current value>,\n        }\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='Goals', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='gamification.goal', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='start_date', ctx=Store()),
                                        Name(id='end_date', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='start_end_date_for_period', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='period',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res_lines', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='line_data', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='description', kind=None),
                                            Constant(value='condition', kind=None),
                                            Constant(value='computation_mode', kind=None),
                                            Constant(value='monetary', kind=None),
                                            Constant(value='suffix', kind=None),
                                            Constant(value='action', kind=None),
                                            Constant(value='display_mode', kind=None),
                                            Constant(value='target', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='definition_id',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='definition_id',
                                                    ctx=Load(),
                                                ),
                                                attr='description',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='definition_id',
                                                    ctx=Load(),
                                                ),
                                                attr='condition',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='definition_id',
                                                    ctx=Load(),
                                                ),
                                                attr='computation_mode',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='definition_id',
                                                    ctx=Load(),
                                                ),
                                                attr='monetary',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='definition_id',
                                                    ctx=Load(),
                                                ),
                                                attr='suffix',
                                                ctx=Load(),
                                            ),
                                            IfExp(
                                                test=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='definition_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='action_id',
                                                    ctx=Load(),
                                                ),
                                                body=Constant(value=True, kind=None),
                                                orelse=Constant(value=False, kind=None),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='definition_id',
                                                    ctx=Load(),
                                                ),
                                                attr='display_mode',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='target_goal',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='line_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='!=', kind=None),
                                                    Constant(value='draft', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='restrict_goals', ctx=Load()),
                                    body=[
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
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Attribute(
                                                                value=Name(id='restrict_goals', ctx=Load()),
                                                                attr='ids',
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
                                    orelse=[
                                        If(
                                            test=Name(id='start_date', ctx=Load()),
                                            body=[
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
                                                                    Constant(value='start_date', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Name(id='start_date', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Name(id='end_date', ctx=Load()),
                                            body=[
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
                                                                    Constant(value='end_date', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Name(id='end_date', ctx=Load()),
                                                                ],
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
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='visibility_mode',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='personal', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='user', ctx=Load()),
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
                                                                args=[Constant(value='Retrieving progress for personal challenge without user information', kind=None)],
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
                                                            Constant(value='user_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='goal', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Goals', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='domain', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='limit',
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='goal', ctx=Load()),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='goal', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='reached', kind=None)],
                                            ),
                                            body=[
                                                Return(
                                                    value=List(elts=[], ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='line_data', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='goal', ctx=Load()),
                                                                attr='read',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[
                                                                        Constant(value='id', kind=None),
                                                                        Constant(value='current', kind=None),
                                                                        Constant(value='completeness', kind=None),
                                                                        Constant(value='state', kind=None),
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='res_lines', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='line_data', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='line_data', ctx=Load()),
                                            slice=Constant(value='own_goal_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[Constant(value=False, kind=None)],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='line_data', ctx=Load()),
                                            slice=Constant(value='goals', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='condition',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='higher', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='goals', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Goals', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='domain', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='order',
                                                        value=Constant(value='completeness desc, current desc', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='goals', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Goals', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='domain', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='order',
                                                        value=Constant(value='completeness desc, current asc', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='goals', ctx=Load()),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='ranking', ctx=Store()),
                                            Name(id='goal', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='enumerate', ctx=Load()),
                                        args=[Name(id='goals', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='user', ctx=Load()),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='goal', ctx=Load()),
                                                            attr='user_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='user', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='line_data', ctx=Load()),
                                                            slice=Constant(value='own_goal_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Name(id='goal', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='restrict_top', ctx=Load()),
                                                            Compare(
                                                                left=Name(id='ranking', ctx=Load()),
                                                                ops=[Gt()],
                                                                comparators=[Name(id='restrict_top', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='line_data', ctx=Load()),
                                                        slice=Constant(value='goals', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='user_id', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='rank', kind=None),
                                                            Constant(value='current', kind=None),
                                                            Constant(value='completeness', kind=None),
                                                            Constant(value='state', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='goal', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='goal', ctx=Load()),
                                                                    attr='user_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='goal', ctx=Load()),
                                                                    attr='user_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='ranking', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='goal', ctx=Load()),
                                                                attr='current',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='goal', ctx=Load()),
                                                                attr='completeness',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='goal', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
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
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='goals', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=3, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='missing', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value=3, kind=None),
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='goals', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='ranking', ctx=Store()),
                                                    Name(id='mock_goal', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Name(id='enumerate', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=List(
                                                            elts=[
                                                                Dict(
                                                                    keys=[
                                                                        Constant(value='id', kind=None),
                                                                        Constant(value='user_id', kind=None),
                                                                        Constant(value='name', kind=None),
                                                                        Constant(value='current', kind=None),
                                                                        Constant(value='completeness', kind=None),
                                                                        Constant(value='state', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Constant(value=False, kind=None),
                                                                        Constant(value=False, kind=None),
                                                                        Constant(value='', kind=None),
                                                                        Constant(value=0, kind=None),
                                                                        Constant(value=0, kind=None),
                                                                        Constant(value=False, kind=None),
                                                                    ],
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        op=Mult(),
                                                        right=Name(id='missing', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='start',
                                                        value=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='goals', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='mock_goal', ctx=Load()),
                                                            slice=Constant(value='rank', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='ranking', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='line_data', ctx=Load()),
                                                                slice=Constant(value='goals', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='mock_goal', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res_lines', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='line_data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res_lines', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='report_progress',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='users', annotation=None, type_comment=None),
                            arg(arg='subset_goals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Tuple(elts=[], ctx=Load()),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Post report about the progress of the goals\n\n        :param users: users that are concerned by the report. If False, will\n                      send the report to every user concerned (goal users and\n                      group that receive a copy). Only used for challenge with\n                      a visibility mode set to 'personal'.\n        :param subset_goals: goals to restrict the report\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='challenge', ctx=Store())],
                            value=Name(id='self', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='challenge', ctx=Load()),
                                    attr='visibility_mode',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='ranking', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='lines_boards', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='challenge', ctx=Load()),
                                            attr='_get_serialized_challenge_lines',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='restrict_goals',
                                                value=Name(id='subset_goals', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='body_html', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='challenge', ctx=Load()),
                                                            attr='report_template_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='with_context',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='challenge_lines',
                                                            value=Name(id='lines_boards', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                                attr='_render_field',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='body_html', kind=None),
                                                Attribute(
                                                    value=Name(id='challenge', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Attribute(
                                            value=Name(id='challenge', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='challenge', ctx=Load()),
                                            attr='message_post',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='body',
                                                value=Name(id='body_html', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='partner_ids',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='challenge', ctx=Load()),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='user_ids.partner_id.id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            keyword(
                                                arg='subtype_xmlid',
                                                value=Constant(value='mail.mt_comment', kind=None),
                                            ),
                                            keyword(
                                                arg='email_layout_xmlid',
                                                value=Constant(value='mail.mail_notification_light', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='challenge', ctx=Load()),
                                        attr='report_message_group_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='challenge', ctx=Load()),
                                                        attr='report_message_group_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=Name(id='body_html', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='subtype_xmlid',
                                                        value=Constant(value='mail.mt_comment', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                For(
                                    target=Name(id='user', ctx=Store()),
                                    iter=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='users', ctx=Load()),
                                            Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='user_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='lines', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='challenge', ctx=Load()),
                                                    attr='_get_serialized_challenge_lines',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='user', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='restrict_goals',
                                                        value=Name(id='subset_goals', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='lines', ctx=Load()),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='body_html', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='challenge', ctx=Load()),
                                                                            attr='report_template_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='with_user',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='user', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                attr='with_context',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='challenge_lines',
                                                                    value=Name(id='lines', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                        attr='_render_field',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='body_html', kind=None),
                                                        Attribute(
                                                            value=Name(id='challenge', ctx=Load()),
                                                            attr='ids',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='challenge', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='challenge', ctx=Load()),
                                                    attr='message_notify',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='body',
                                                        value=Name(id='body_html', ctx=Load()),
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
                                                    keyword(
                                                        arg='subtype_xmlid',
                                                        value=Constant(value='mail.mt_comment', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='email_layout_xmlid',
                                                        value=Constant(value='mail.mail_notification_light', kind=None),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='report_message_group_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='challenge', ctx=Load()),
                                                                attr='report_message_group_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='message_post',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='body',
                                                                value=Name(id='body_html', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='subtype_xmlid',
                                                                value=Constant(value='mail.mt_comment', kind=None),
                                                            ),
                                                            keyword(
                                                                arg='email_layout_xmlid',
                                                                value=Constant(value='mail.mail_notification_light', kind=None),
                                                            ),
                                                        ],
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='challenge', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='last_report_date', kind=None)],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Date',
                                                        ctx=Load(),
                                                    ),
                                                    attr='today',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
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
                FunctionDef(
                    name='accept_challenge',
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
                            targets=[Name(id='sudoed', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sudo',
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
                                    value=Name(id='sudoed', ctx=Load()),
                                    attr='message_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='body',
                                        value=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[
                                                Constant(value='%s has joined the challenge', kind=None),
                                                Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sudoed', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='invited_user_ids', kind=None),
                                            Constant(value='user_ids', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=3, kind=None),
                                                            Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=4, kind=None),
                                                            Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sudoed', ctx=Load()),
                                    attr='_generate_goals_from_challenge',
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
                    name='discard_challenge',
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
                            value=Constant(value='The user discard the suggested challenge', kind=None),
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
                            targets=[Name(id='sudoed', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sudo',
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
                                    value=Name(id='sudoed', ctx=Load()),
                                    attr='message_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='body',
                                        value=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[
                                                Constant(value='%s has refused the challenge', kind=None),
                                                Attribute(
                                                    value=Name(id='user', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sudoed', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='invited_user_ids', kind=None)],
                                        values=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=3, kind=None),
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='_check_challenge_reward',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='force', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Actions for the end of a challenge\n\n        If a reward was selected, grant it to the correct users.\n        Rewards granted at:\n            - the end date for a challenge with no periodicity\n            - the end of a period for challenge with periodicity\n            - when a challenge is manually closed\n        (if no end date, a running challenge is never rewarded)\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='commit', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='commit_gamification', kind=None)],
                                        keywords=[],
                                    ),
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
                                        attr='commit',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='challenge', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='start_date', ctx=Store()),
                                                Name(id='end_date', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='start_end_date_for_period', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='period',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='start_date',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='end_date',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='yesterday', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='date', ctx=Load()),
                                                attr='today',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='timedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='rewarded_users', ctx=Store())],
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
                                    targets=[Name(id='challenge_ended', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='force', ctx=Load()),
                                            Compare(
                                                left=Name(id='end_date', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='to_string',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='yesterday', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='reward_id',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='challenge_ended', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='challenge', ctx=Load()),
                                                        attr='reward_realtime',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='reached_goals', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='gamification.goal', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='read_group',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='challenge_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='challenge', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='end_date', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Name(id='end_date', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='state', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='reached', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='fields',
                                                        value=List(
                                                            elts=[Constant(value='user_id', kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='groupby',
                                                        value=List(
                                                            elts=[Constant(value='user_id', kind=None)],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='reach_goals_user', ctx=Store()),
                                            iter=Name(id='reached_goals', ctx=Load()),
                                            body=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='reach_goals_user', ctx=Load()),
                                                            slice=Constant(value='user_id_count', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Call(
                                                                func=Name(id='len', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='challenge', ctx=Load()),
                                                                        attr='line_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='user', ctx=Store())],
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
                                                                    attr='browse',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Subscript(
                                                                            value=Name(id='reach_goals_user', ctx=Load()),
                                                                            slice=Constant(value='user_id', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Attribute(
                                                                value=Name(id='challenge', ctx=Load()),
                                                                attr='reward_realtime',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='badges', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Subscript(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                slice=Constant(value='gamification.badge.user', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='search_count',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            List(
                                                                                elts=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value='challenge_id', kind=None),
                                                                                            Constant(value='=', kind=None),
                                                                                            Attribute(
                                                                                                value=Name(id='challenge', ctx=Load()),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value='badge_id', kind=None),
                                                                                            Constant(value='=', kind=None),
                                                                                            Attribute(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='challenge', ctx=Load()),
                                                                                                    attr='reward_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Constant(value='user_id', kind=None),
                                                                                            Constant(value='=', kind=None),
                                                                                            Attribute(
                                                                                                value=Name(id='user', ctx=Load()),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
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
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='badges', ctx=Load()),
                                                                        ops=[Gt()],
                                                                        comparators=[Constant(value=0, kind=None)],
                                                                    ),
                                                                    body=[Continue()],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='challenge', ctx=Load()),
                                                                    attr='_reward_user',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='user', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='challenge', ctx=Load()),
                                                                        attr='reward_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='rewarded_users', ctx=Store()),
                                                            op=BitOr(),
                                                            value=Name(id='user', ctx=Load()),
                                                        ),
                                                        If(
                                                            test=Name(id='commit', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Name(id='commit', ctx=Load()),
                                                                        args=[],
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
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='challenge_ended', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message_body', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='The challenge %s is finished.', kind=None),
                                                    Attribute(
                                                        value=Name(id='challenge', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='rewarded_users', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='user_names', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='rewarded_users', ctx=Load()),
                                                            attr='name_get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='message_body', ctx=Store()),
                                                    op=Add(),
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='<br/>Reward (badge %(badge_name)s) for every succeeding user was sent to %(users)s.', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='badge_name',
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='challenge', ctx=Load()),
                                                                        attr='reward_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='users',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Constant(value=', ', kind=None),
                                                                        attr='join',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        GeneratorExp(
                                                                            elt=Name(id='name', ctx=Load()),
                                                                            generators=[
                                                                                comprehension(
                                                                                    target=Tuple(
                                                                                        elts=[
                                                                                            Name(id='user_id', ctx=Store()),
                                                                                            Name(id='name', ctx=Store()),
                                                                                        ],
                                                                                        ctx=Store(),
                                                                                    ),
                                                                                    iter=Name(id='user_names', ctx=Load()),
                                                                                    ifs=[],
                                                                                    is_async=0,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                AugAssign(
                                                    target=Name(id='message_body', ctx=Store()),
                                                    op=Add(),
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='<br/>Nobody has succeeded to reach every goal, no badge is rewarded for this challenge.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='reward_message', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='<br/> %(rank)d. %(user_name)s - %(reward_name)s', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='challenge', ctx=Load()),
                                                attr='reward_first_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='first_user', ctx=Store()),
                                                                Name(id='second_user', ctx=Store()),
                                                                Name(id='third_user', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='challenge', ctx=Load()),
                                                            attr='_get_topN_users',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='MAX_VISIBILITY_RANKING', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='first_user', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='challenge', ctx=Load()),
                                                                    attr='_reward_user',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='first_user', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='challenge', ctx=Load()),
                                                                        attr='reward_first_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='message_body', ctx=Store()),
                                                            op=Add(),
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='<br/>Special rewards were sent to the top competing users. The ranking for this challenge is :', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='message_body', ctx=Store()),
                                                            op=Add(),
                                                            value=BinOp(
                                                                left=Name(id='reward_message', ctx=Load()),
                                                                op=Mod(),
                                                                right=Dict(
                                                                    keys=[
                                                                        Constant(value='rank', kind=None),
                                                                        Constant(value='user_name', kind=None),
                                                                        Constant(value='reward_name', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Constant(value=1, kind=None),
                                                                        Attribute(
                                                                            value=Name(id='first_user', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='challenge', ctx=Load()),
                                                                                attr='reward_first_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        AugAssign(
                                                            target=Name(id='message_body', ctx=Store()),
                                                            op=Add(),
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Nobody reached the required conditions to receive special badges.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='second_user', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='challenge', ctx=Load()),
                                                                attr='reward_second_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='challenge', ctx=Load()),
                                                                    attr='_reward_user',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='second_user', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='challenge', ctx=Load()),
                                                                        attr='reward_second_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='message_body', ctx=Store()),
                                                            op=Add(),
                                                            value=BinOp(
                                                                left=Name(id='reward_message', ctx=Load()),
                                                                op=Mod(),
                                                                right=Dict(
                                                                    keys=[
                                                                        Constant(value='rank', kind=None),
                                                                        Constant(value='user_name', kind=None),
                                                                        Constant(value='reward_name', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Constant(value=2, kind=None),
                                                                        Attribute(
                                                                            value=Name(id='second_user', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='challenge', ctx=Load()),
                                                                                attr='reward_second_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='third_user', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='challenge', ctx=Load()),
                                                                attr='reward_third_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='challenge', ctx=Load()),
                                                                    attr='_reward_user',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='third_user', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='challenge', ctx=Load()),
                                                                        attr='reward_third_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='message_body', ctx=Store()),
                                                            op=Add(),
                                                            value=BinOp(
                                                                left=Name(id='reward_message', ctx=Load()),
                                                                op=Mod(),
                                                                right=Dict(
                                                                    keys=[
                                                                        Constant(value='rank', kind=None),
                                                                        Constant(value='user_name', kind=None),
                                                                        Constant(value='reward_name', kind=None),
                                                                    ],
                                                                    values=[
                                                                        Constant(value=3, kind=None),
                                                                        Attribute(
                                                                            value=Name(id='third_user', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='challenge', ctx=Load()),
                                                                                attr='reward_third_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='challenge', ctx=Load()),
                                                    attr='message_post',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='partner_ids',
                                                        value=ListComp(
                                                            elt=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='user', ctx=Load()),
                                                                    attr='partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='user', ctx=Store()),
                                                                    iter=Attribute(
                                                                        value=Name(id='challenge', ctx=Load()),
                                                                        attr='user_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ifs=[],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='body',
                                                        value=Name(id='message_body', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        If(
                                            test=Name(id='commit', ctx=Load()),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='commit', ctx=Load()),
                                                        args=[],
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
                    name='_get_topN_users',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='n', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Get the top N users for a defined challenge\n\n        Ranking criterias:\n            1. succeed every goal of the challenge\n            2. total completeness of each goal (can be over 100)\n\n        Only users having reached every goal of the challenge will be returned\n        unless the challenge ``reward_failure`` is set, in which case any user\n        may be considered.\n\n        :returns: an iterable of exactly N records, either User objects or\n                  False if there was no user for the rank. There can be no\n                  False between two users (if users[k] = False then\n                  users[k+1] = False\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='Goals', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='gamification.goal', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='start_date', ctx=Store()),
                                        Name(id='end_date', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='start_end_date_for_period', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='period',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='start_date',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='end_date',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='challengers', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='user', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='user_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='all_reached', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='total_completeness', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='goal_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Goals', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='challenge_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='user_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='user', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='start_date', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='start_date', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='end_date', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='end_date', ctx=Load()),
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
                                For(
                                    target=Name(id='goal', ctx=Store()),
                                    iter=Name(id='goal_ids', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='goal', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='reached', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='all_reached', ctx=Store())],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='goal', ctx=Load()),
                                                    attr='definition_condition',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='higher', kind=None)],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Name(id='total_completeness', ctx=Store()),
                                                    op=Add(),
                                                    value=IfExp(
                                                        test=Attribute(
                                                            value=Name(id='goal', ctx=Load()),
                                                            attr='target_goal',
                                                            ctx=Load(),
                                                        ),
                                                        body=BinOp(
                                                            left=BinOp(
                                                                left=Constant(value=100.0, kind=None),
                                                                op=Mult(),
                                                                right=Attribute(
                                                                    value=Name(id='goal', ctx=Load()),
                                                                    attr='current',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            op=Div(),
                                                            right=Attribute(
                                                                value=Name(id='goal', ctx=Load()),
                                                                attr='target_goal',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        orelse=Constant(value=0, kind=None),
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='goal', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='reached', kind=None)],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='total_completeness', ctx=Store()),
                                                            op=Add(),
                                                            value=Constant(value=100, kind=None),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='challengers', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='user', kind=None),
                                                    Constant(value='all_reached', kind=None),
                                                    Constant(value='total_completeness', kind=None),
                                                ],
                                                values=[
                                                    Name(id='user', ctx=Load()),
                                                    Name(id='all_reached', ctx=Load()),
                                                    Name(id='total_completeness', ctx=Load()),
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
                                    value=Name(id='challengers', ctx=Load()),
                                    attr='sort',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='k', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Tuple(
                                                elts=[
                                                    Subscript(
                                                        value=Name(id='k', ctx=Load()),
                                                        slice=Constant(value='all_reached', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='k', ctx=Load()),
                                                        slice=Constant(value='total_completeness', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    keyword(
                                        arg='reverse',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='reward_failure',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='challengers', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='itertools', ctx=Load()),
                                            attr='takewhile',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='c', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Subscript(
                                                    value=Name(id='c', ctx=Load()),
                                                    slice=Constant(value='all_reached', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Name(id='challengers', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='challengers', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='itertools', ctx=Load()),
                                    attr='islice',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='itertools', ctx=Load()),
                                            attr='chain',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            GeneratorExp(
                                                elt=Subscript(
                                                    value=Name(id='c', ctx=Load()),
                                                    slice=Constant(value='user', kind=None),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='c', ctx=Store()),
                                                        iter=Name(id='challengers', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='itertools', ctx=Load()),
                                                    attr='repeat',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=False, kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                    Name(id='n', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[Name(id='challengers', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_reward_user',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='user', annotation=None, type_comment=None),
                            arg(arg='badge', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Create a badge user and send the badge to him\n\n        :param user: the user to reward\n        :param badge: the concerned badge\n        ', kind=None),
                        ),
                        Return(
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
                                                slice=Constant(value='gamification.badge.user', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='user_id', kind=None),
                                                    Constant(value='badge_id', kind=None),
                                                    Constant(value='challenge_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='user', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='badge', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_send_badge',
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ChallengeLine',
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
                    value=Constant(value="Gamification challenge line\n\n    Predefined goal for 'gamification_challenge'\n    These are generic list of goals with only the target goal defined\n    Should only be created for the gamification.challenge object\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='gamification.challenge.line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Gamification generic goal for challenge', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence, id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='challenge_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='gamification.challenge', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Challenge', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='definition_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='gamification.goal.definition', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Goal Definition', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Sequence', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Sequence number for ordering', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='target_goal', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Target Value to Reach', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
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
                                value=Constant(value='definition_id.name', kind=None),
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
                    targets=[Name(id='condition', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Condition', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='definition_id.condition', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='definition_suffix', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Unit', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='definition_id.suffix', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='definition_monetary', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Monetary', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='definition_id.monetary', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='definition_full_suffix', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Suffix', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='definition_id.full_suffix', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
