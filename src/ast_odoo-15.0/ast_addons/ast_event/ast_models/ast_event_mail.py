Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='exception_to_unicode', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
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
            targets=[Name(id='_INTERVALS', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='hours', kind=None),
                    Constant(value='days', kind=None),
                    Constant(value='weeks', kind=None),
                    Constant(value='months', kind=None),
                    Constant(value='now', kind=None),
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
                                    arg='hours',
                                    value=Constant(value=0, kind=None),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='EventTypeMail',
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
                    value=Constant(value=' Template of event.mail to attach to event.type. Those will be copied\n    upon all events created in that type to ease event creation. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='event.type.mail', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Mail Scheduling on Event Category', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_selection_template_model',
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
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='mail.template', kind=None),
                                            Constant(value='Mail', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
                Assign(
                    targets=[Name(id='event_type_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='event.type', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Event Type', kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
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
                    targets=[Name(id='notification_type', ctx=Store())],
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
                                            Constant(value='mail', kind=None),
                                            Constant(value='Mail', kind=None),
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
                                value=Constant(value='Send', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='mail', kind=None),
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
                    targets=[Name(id='interval_nbr', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Interval', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='interval_unit', ctx=Store())],
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
                                            Constant(value='now', kind=None),
                                            Constant(value='Immediately', kind=None),
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
                                value=Constant(value='Unit', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='hours', kind=None),
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
                                            Constant(value='after_sub', kind=None),
                                            Constant(value='After each registration', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='before_event', kind=None),
                                            Constant(value='Before the event', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='after_event', kind=None),
                                            Constant(value='After the event', kind=None),
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
                                value=Constant(value='Trigger', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='before_event', kind=None),
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
                    targets=[Name(id='template_model_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.model', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Template Model', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_template_model_id', kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='template_ref', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Reference',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Template', kind=None),
                            ),
                            keyword(
                                arg='selection',
                                value=Constant(value='_selection_template_model', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_template_model_id',
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
                            targets=[Name(id='mail_model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='mail.template', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='mail', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='mail', ctx=Load()),
                                            attr='template_model_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Compare(
                                            left=Attribute(
                                                value=Name(id='mail', ctx=Load()),
                                                attr='notification_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='mail', kind=None)],
                                        ),
                                        body=Name(id='mail_model', ctx=Load()),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
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
                            args=[Constant(value='notification_type', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_event_mail_values',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='notification_type', kind=None),
                                    Constant(value='interval_nbr', kind=None),
                                    Constant(value='interval_unit', kind=None),
                                    Constant(value='interval_type', kind=None),
                                    Constant(value='template_ref', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='notification_type',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='interval_nbr',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='interval_unit',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='interval_type',
                                        ctx=Load(),
                                    ),
                                    BinOp(
                                        left=Constant(value='%s,%i', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='template_ref',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='template_ref',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='EventMailScheduler',
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
                    value=Constant(value=' Event automated mailing. This model replaces all existing fields and\n    configuration allowing to send emails on events since Odoo 9. A cron exists\n    that periodically checks for mailing to run. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='event.mail', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='event_id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Event Automated Mailing', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_selection_template_model',
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
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='mail.template', kind=None),
                                            Constant(value='Mail', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
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
                Assign(
                    targets=[Name(id='event_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='event.event', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Event', kind=None),
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
                        args=[Constant(value='Display order', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='notification_type', ctx=Store())],
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
                                            Constant(value='mail', kind=None),
                                            Constant(value='Mail', kind=None),
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
                                value=Constant(value='Send', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='mail', kind=None),
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
                    targets=[Name(id='interval_nbr', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Interval', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='interval_unit', ctx=Store())],
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
                                            Constant(value='now', kind=None),
                                            Constant(value='Immediately', kind=None),
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
                                value=Constant(value='Unit', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='hours', kind=None),
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
                                            Constant(value='after_sub', kind=None),
                                            Constant(value='After each registration', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='before_event', kind=None),
                                            Constant(value='Before the event', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='after_event', kind=None),
                                            Constant(value='After the event', kind=None),
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
                                value=Constant(value='Trigger ', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='before_event', kind=None),
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
                    targets=[Name(id='scheduled_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Schedule Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_scheduled_date', kind=None),
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
                    targets=[Name(id='mail_registration_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='event.mail.registration', kind=None),
                            Constant(value='scheduler_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Communication related to event registrations', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mail_done', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Sent', kind=None)],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
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
                    targets=[Name(id='mail_state', ctx=Store())],
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
                                            Constant(value='running', kind=None),
                                            Constant(value='Running', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='scheduled', kind=None),
                                            Constant(value='Scheduled', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sent', kind=None),
                                            Constant(value='Sent', kind=None),
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
                                value=Constant(value='Global communication Status', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_mail_state', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mail_count_done', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='# Sent', kind=None)],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
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
                    targets=[Name(id='template_model_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.model', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Template Model', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_template_model_id', kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='template_ref', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Reference',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Template', kind=None),
                            ),
                            keyword(
                                arg='selection',
                                value=Constant(value='_selection_template_model', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_template_model_id',
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
                            targets=[Name(id='mail_model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='mail.template', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='mail', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='mail', ctx=Load()),
                                            attr='template_model_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Compare(
                                            left=Attribute(
                                                value=Name(id='mail', ctx=Load()),
                                                attr='notification_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='mail', kind=None)],
                                        ),
                                        body=Name(id='mail_model', ctx=Load()),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
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
                            args=[Constant(value='notification_type', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_scheduled_date',
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
                        For(
                            target=Name(id='scheduler', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='scheduler', ctx=Load()),
                                            attr='interval_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='after_sub', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='date', ctx=Store()),
                                                        Name(id='sign', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='scheduler', ctx=Load()),
                                                            attr='event_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='create_date',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='scheduler', ctx=Load()),
                                                    attr='interval_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='before_event', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='date', ctx=Store()),
                                                                Name(id='sign', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='scheduler', ctx=Load()),
                                                                    attr='event_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='date_begin',
                                                                ctx=Load(),
                                                            ),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=1, kind=None),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='date', ctx=Store()),
                                                                Name(id='sign', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='scheduler', ctx=Load()),
                                                                    attr='event_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='date_end',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=1, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='scheduler', ctx=Load()),
                                            attr='scheduled_date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Name(id='date', ctx=Load()),
                                        body=BinOp(
                                            left=Name(id='date', ctx=Load()),
                                            op=Add(),
                                            right=Call(
                                                func=Subscript(
                                                    value=Name(id='_INTERVALS', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='scheduler', ctx=Load()),
                                                        attr='interval_unit',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='sign', ctx=Load()),
                                                        op=Mult(),
                                                        right=Attribute(
                                                            value=Name(id='scheduler', ctx=Load()),
                                                            attr='interval_nbr',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
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
                                Constant(value='event_id.date_begin', kind=None),
                                Constant(value='event_id.date_end', kind=None),
                                Constant(value='interval_type', kind=None),
                                Constant(value='interval_unit', kind=None),
                                Constant(value='interval_nbr', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_mail_state',
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
                        For(
                            target=Name(id='scheduler', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='scheduler', ctx=Load()),
                                            attr='interval_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='after_sub', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='scheduler', ctx=Load()),
                                                    attr='mail_state',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='running', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='scheduler', ctx=Load()),
                                                attr='mail_done',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='scheduler', ctx=Load()),
                                                            attr='mail_state',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value='sent', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Attribute(
                                                        value=Name(id='scheduler', ctx=Load()),
                                                        attr='scheduled_date',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='scheduler', ctx=Load()),
                                                                    attr='mail_state',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='scheduled', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='scheduler', ctx=Load()),
                                                                    attr='mail_state',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value='running', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
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
                                Constant(value='interval_type', kind=None),
                                Constant(value='scheduled_date', kind=None),
                                Constant(value='mail_done', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='execute',
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
                        For(
                            target=Name(id='scheduler', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
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
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='scheduler', ctx=Load()),
                                            attr='interval_type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='after_sub', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='new_registrations', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='scheduler', ctx=Load()),
                                                                attr='event_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='registration_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='filtered_domain',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='state', kind=None),
                                                                        Constant(value='not in', kind=None),
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value='cancel', kind=None),
                                                                                Constant(value='draft', kind=None),
                                                                            ],
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
                                                op=Sub(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='scheduler', ctx=Load()),
                                                        attr='mail_registration_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='registration_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='scheduler', ctx=Load()),
                                                    attr='_create_missing_mail_registrations',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='new_registrations', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='scheduler', ctx=Load()),
                                                        attr='mail_registration_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='total_sent', ctx=Store())],
                                            value=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='scheduler', ctx=Load()),
                                                                attr='mail_registration_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='reg', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Attribute(
                                                                    value=Name(id='reg', ctx=Load()),
                                                                    attr='mail_sent',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
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
                                                    value=Name(id='scheduler', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='mail_done', kind=None),
                                                            Constant(value='mail_count_done', kind=None),
                                                        ],
                                                        values=[
                                                            Compare(
                                                                left=Name(id='total_sent', ctx=Load()),
                                                                ops=[GtE()],
                                                                comparators=[
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='scheduler', ctx=Load()),
                                                                                attr='event_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='seats_reserved',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='scheduler', ctx=Load()),
                                                                                attr='event_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='seats_used',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            Name(id='total_sent', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='scheduler', ctx=Load()),
                                                        attr='mail_done',
                                                        ctx=Load(),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='scheduler', ctx=Load()),
                                                            attr='notification_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[Constant(value='mail', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='scheduler', ctx=Load()),
                                                    attr='template_ref',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='scheduler', ctx=Load()),
                                                            attr='scheduled_date',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[LtE()],
                                                        comparators=[Name(id='now', ctx=Load())],
                                                    ),
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='scheduler', ctx=Load()),
                                                                    attr='interval_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[Constant(value='before_event', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='scheduler', ctx=Load()),
                                                                        attr='event_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='date_end',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Name(id='now', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='scheduler', ctx=Load()),
                                                                attr='event_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='mail_attendees',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='scheduler', ctx=Load()),
                                                                    attr='template_ref',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='scheduler', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='mail_done', kind=None),
                                                                    Constant(value='mail_count_done', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value=True, kind=None),
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='scheduler', ctx=Load()),
                                                                                attr='event_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='seats_reserved',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='scheduler', ctx=Load()),
                                                                                attr='event_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='seats_used',
                                                                            ctx=Load(),
                                                                        ),
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
                    name='_create_missing_mail_registrations',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='registrations', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='new', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='scheduler', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='new', ctx=Store()),
                                    op=Add(),
                                    value=ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='registration_id', kind=None),
                                                Constant(value='scheduler_id', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='registration', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='scheduler', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='registration', ctx=Store()),
                                                iter=Name(id='registrations', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='new', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='event.mail.registration', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='new', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='event.mail.registration', kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_warn_template_error',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='scheduler', annotation=None, type_comment=None),
                            arg(arg='exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='random', ctx=Load()),
                                                attr='random',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=0.1666, kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='scheduler', ctx=Load()),
                                            attr='interval_unit',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='now', kind=None),
                                                    Constant(value='hours', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ex_s', ctx=Store())],
                                    value=Call(
                                        func=Name(id='exception_to_unicode', ctx=Load()),
                                        args=[Name(id='exception', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='event', ctx=Store()),
                                                        Name(id='template', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='scheduler', ctx=Load()),
                                                        attr='event_id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='scheduler', ctx=Load()),
                                                        attr='template_ref',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='emails', ctx=Store())],
                                            value=Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='set', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='event', ctx=Load()),
                                                                            attr='organizer_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='email',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='event', ctx=Load()),
                                                                            attr='user_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='email',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='template', ctx=Load()),
                                                                            attr='write_uid',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='email',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
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
                                            targets=[Name(id='subject', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='WARNING: Event Scheduler Error for event: %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='body', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Event Scheduler for:\n  - Event: %(event_name)s (%(event_id)s)\n  - Scheduled: %(date)s\n  - Template: %(template_name)s (%(template_id)s)\n\nFailed with error:\n  - %(error)s\n\nYou receive this email because you are:\n  - the organizer of the event,\n  - or the responsible of the event,\n  - or the last writer of the template.\n', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='event_name',
                                                        value=Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='event_id',
                                                        value=Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='date',
                                                        value=Attribute(
                                                            value=Name(id='scheduler', ctx=Load()),
                                                            attr='scheduled_date',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='template_name',
                                                        value=Attribute(
                                                            value=Name(id='template', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='template_id',
                                                        value=Attribute(
                                                            value=Name(id='template', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='error',
                                                        value=Name(id='ex_s', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='email', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.mail_server', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='build_email',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='email_from',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='user',
                                                                ctx=Load(),
                                                            ),
                                                            attr='email',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='email_to',
                                                        value=Name(id='emails', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='subject',
                                                        value=Name(id='subject', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='body',
                                                        value=Name(id='body', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.mail_server', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='send_email',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='email', ctx=Load())],
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
                                                            attr='error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='Exception while sending traceback by email: %s.\n Original Traceback:\n%s', kind=None),
                                                            Name(id='e', ctx=Load()),
                                                            Name(id='exception', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Pass(),
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
                    name='run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='autocommit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Backward compatible method, notably if crons are not updated when\n        migrating for some reason. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='schedule_communications',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='autocommit',
                                        value=Name(id='autocommit', ctx=Load()),
                                    ),
                                ],
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
                    name='schedule_communications',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='autocommit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='schedulers', ctx=Store())],
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
                                                    Constant(value='mail_done', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='scheduled_date', kind=None),
                                                    Constant(value='<=', kind=None),
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
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='scheduler', ctx=Store()),
                            iter=Name(id='schedulers', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='scheduler', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='execute',
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
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='invalidate_cache',
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
                                                            attr='_warn_template_error',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='scheduler', ctx=Load()),
                                                            Name(id='e', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='autocommit', ctx=Load()),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Name(id='getattr', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Attribute(
                                                                        value=Name(id='threading', ctx=Load()),
                                                                        attr='currentThread',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                Constant(value='testing', kind=None),
                                                                Constant(value=False, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
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
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
            name='EventMailRegistration',
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
                    value=Constant(value='event.mail.registration', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Registration Mail Scheduler', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='scheduler_id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='scheduled_date DESC', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='scheduler_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='event.mail', kind=None),
                            Constant(value='Mail Scheduler', kind=None),
                        ],
                        keywords=[
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
                    targets=[Name(id='registration_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='event.registration', kind=None),
                            Constant(value='Attendee', kind=None),
                        ],
                        keywords=[
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
                    targets=[Name(id='scheduled_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Scheduled Time', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_scheduled_date', kind=None),
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
                    targets=[Name(id='mail_sent', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Mail Sent', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='execute',
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
                        Assign(
                            targets=[Name(id='todo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='reg_mail', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='reg_mail', ctx=Load()),
                                                        attr='mail_sent',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='reg_mail', ctx=Load()),
                                                            attr='registration_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        List(
                                                            elts=[
                                                                Constant(value='open', kind=None),
                                                                Constant(value='done', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='reg_mail', ctx=Load()),
                                                            attr='scheduled_date',
                                                            ctx=Load(),
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='reg_mail', ctx=Load()),
                                                                attr='scheduled_date',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[LtE()],
                                                            comparators=[Name(id='now', ctx=Load())],
                                                        ),
                                                    ],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='reg_mail', ctx=Load()),
                                                            attr='scheduler_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='notification_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='mail', kind=None)],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='reg_mail', ctx=Store()),
                            iter=Name(id='todo', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='organizer', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='reg_mail', ctx=Load()),
                                                attr='scheduler_id',
                                                ctx=Load(),
                                            ),
                                            attr='event_id',
                                            ctx=Load(),
                                        ),
                                        attr='organizer_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='company', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='author', ctx=Store())],
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
                                        args=[Constant(value='base.user_root', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='organizer', ctx=Load()),
                                        attr='email',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='author', ctx=Store())],
                                            value=Name(id='organizer', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='company', ctx=Load()),
                                                attr='email',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='author', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='company', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='email',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='author', ctx=Store())],
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
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='email_values', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='email_from', kind=None),
                                            Constant(value='author_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='author', ctx=Load()),
                                                attr='email_formatted',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='author', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
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
                                                    value=Name(id='reg_mail', ctx=Load()),
                                                    attr='scheduler_id',
                                                    ctx=Load(),
                                                ),
                                                attr='template_ref',
                                                ctx=Load(),
                                            ),
                                            attr='send_mail',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='reg_mail', ctx=Load()),
                                                    attr='registration_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='email_values',
                                                value=Name(id='email_values', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='todo', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='mail_sent', kind=None)],
                                        values=[Constant(value=True, kind=None)],
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
                    name='_compute_scheduled_date',
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
                        For(
                            target=Name(id='mail', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='mail', ctx=Load()),
                                        attr='registration_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='date_open', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='registration_id',
                                                    ctx=Load(),
                                                ),
                                                attr='date_open',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='date_open_datetime', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='date_open', ctx=Load()),
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
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='scheduled_date',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Name(id='date_open_datetime', ctx=Load()),
                                                op=Add(),
                                                right=Call(
                                                    func=Subscript(
                                                        value=Name(id='_INTERVALS', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='scheduler_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='interval_unit',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='mail', ctx=Load()),
                                                                attr='scheduler_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='interval_nbr',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='mail', ctx=Load()),
                                                    attr='scheduled_date',
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
                                Constant(value='registration_id', kind=None),
                                Constant(value='scheduler_id.interval_unit', kind=None),
                                Constant(value='scheduler_id.interval_type', kind=None),
                            ],
                            keywords=[],
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
