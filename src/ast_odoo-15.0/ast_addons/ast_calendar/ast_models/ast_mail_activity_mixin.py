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
            name='MailActivityMixin',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='mail.activity.mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='activity_calendar_event_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='calendar.event', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Next Activity Calendar Event', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_activity_calendar_event_id', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_activity_calendar_event_id',
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
                            value=Constant(value='This computes the calendar event of the next activity.\n        It evaluates to false if there is no such event.', kind=None),
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='activity_calendar_event_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='activity_ids',
                                                ctx=Load(),
                                            ),
                                            slice=Slice(
                                                lower=None,
                                                upper=Constant(value=1, kind=None),
                                                step=None,
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='calendar_event_id',
                                        ctx=Load(),
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
                            args=[Constant(value='activity_ids.calendar_event_id', kind=None)],
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
