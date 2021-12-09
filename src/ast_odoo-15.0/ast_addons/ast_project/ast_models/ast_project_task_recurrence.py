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
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='calendar',
            names=[alias(name='monthrange', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.rrule',
            names=[
                alias(name='rrule', asname=None),
                alias(name='rruleset', asname=None),
                alias(name='DAILY', asname=None),
                alias(name='WEEKLY', asname=None),
                alias(name='MONTHLY', asname=None),
                alias(name='YEARLY', asname=None),
                alias(name='MO', asname=None),
                alias(name='TU', asname=None),
                alias(name='WE', asname=None),
                alias(name='TH', asname=None),
                alias(name='FR', asname=None),
                alias(name='SA', asname=None),
                alias(name='SU', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='MONTHS', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='january', kind=None),
                    Constant(value='february', kind=None),
                    Constant(value='march', kind=None),
                    Constant(value='april', kind=None),
                    Constant(value='may', kind=None),
                    Constant(value='june', kind=None),
                    Constant(value='july', kind=None),
                    Constant(value='august', kind=None),
                    Constant(value='september', kind=None),
                    Constant(value='october', kind=None),
                    Constant(value='november', kind=None),
                    Constant(value='december', kind=None),
                ],
                values=[
                    Constant(value=31, kind=None),
                    Constant(value=28, kind=None),
                    Constant(value=31, kind=None),
                    Constant(value=30, kind=None),
                    Constant(value=31, kind=None),
                    Constant(value=30, kind=None),
                    Constant(value=31, kind=None),
                    Constant(value=31, kind=None),
                    Constant(value=30, kind=None),
                    Constant(value=31, kind=None),
                    Constant(value=30, kind=None),
                    Constant(value=31, kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DAYS', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='mon', kind=None),
                    Constant(value='tue', kind=None),
                    Constant(value='wed', kind=None),
                    Constant(value='thu', kind=None),
                    Constant(value='fri', kind=None),
                    Constant(value='sat', kind=None),
                    Constant(value='sun', kind=None),
                ],
                values=[
                    Name(id='MO', ctx=Load()),
                    Name(id='TU', ctx=Load()),
                    Name(id='WE', ctx=Load()),
                    Name(id='TH', ctx=Load()),
                    Name(id='FR', ctx=Load()),
                    Name(id='SA', ctx=Load()),
                    Name(id='SU', ctx=Load()),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='WEEKS', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='first', kind=None),
                    Constant(value='second', kind=None),
                    Constant(value='third', kind=None),
                    Constant(value='last', kind=None),
                ],
                values=[
                    Constant(value=1, kind=None),
                    Constant(value=2, kind=None),
                    Constant(value=3, kind=None),
                    Constant(value=4, kind=None),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='ProjectTaskRecurrence',
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
                    value=Constant(value='project.task.recurrence', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Task Recurrence', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='task_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='project.task', kind=None),
                            Constant(value='recurrence_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='next_recurrence_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='recurrence_left', ctx=Store())],
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
                                value=Constant(value='Number of Tasks Left to Create', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='repeat_interval', ctx=Store())],
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
                                value=Constant(value='Repeat Every', kind=None),
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
                    targets=[Name(id='repeat_unit', ctx=Store())],
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
                                            Constant(value='day', kind=None),
                                            Constant(value='Days', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='week', kind=None),
                                            Constant(value='Weeks', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='month', kind=None),
                                            Constant(value='Months', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='year', kind=None),
                                            Constant(value='Years', kind=None),
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
                                value=Constant(value='week', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='repeat_type', ctx=Store())],
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
                                            Constant(value='forever', kind=None),
                                            Constant(value='Forever', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='until', kind=None),
                                            Constant(value='End Date', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='after', kind=None),
                                            Constant(value='Number of Repetitions', kind=None),
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
                                value=Constant(value='forever', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Until', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='repeat_until', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='End Date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='repeat_number', ctx=Store())],
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
                                value=Constant(value='Repetitions', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='repeat_on_month', ctx=Store())],
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
                                            Constant(value='date', kind=None),
                                            Constant(value='Date of the Month', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='day', kind=None),
                                            Constant(value='Day of the Month', kind=None),
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
                    targets=[Name(id='repeat_on_year', ctx=Store())],
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
                                            Constant(value='date', kind=None),
                                            Constant(value='Date of the Year', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='day', kind=None),
                                            Constant(value='Day of the Year', kind=None),
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
                    targets=[Name(id='mon', ctx=Store())],
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
                                value=Constant(value='Mon', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tue', ctx=Store())],
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
                                value=Constant(value='Tue', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='wed', ctx=Store())],
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
                                value=Constant(value='Wed', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='thu', ctx=Store())],
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
                                value=Constant(value='Thu', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='fri', ctx=Store())],
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
                                value=Constant(value='Fri', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sat', ctx=Store())],
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
                                value=Constant(value='Sat', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sun', ctx=Store())],
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
                                value=Constant(value='Sun', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='repeat_day', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            ListComp(
                                elt=Tuple(
                                    elts=[
                                        Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='i', ctx=Load())],
                                            keywords=[],
                                        ),
                                        Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[Name(id='i', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='i', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[
                                                Constant(value=1, kind=None),
                                                Constant(value=32, kind=None),
                                            ],
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
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='repeat_week', ctx=Store())],
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
                                            Constant(value='first', kind=None),
                                            Constant(value='First', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='second', kind=None),
                                            Constant(value='Second', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='third', kind=None),
                                            Constant(value='Third', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='last', kind=None),
                                            Constant(value='Last', kind=None),
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
                    targets=[Name(id='repeat_weekday', ctx=Store())],
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
                                            Constant(value='mon', kind=None),
                                            Constant(value='Monday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='tue', kind=None),
                                            Constant(value='Tuesday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='wed', kind=None),
                                            Constant(value='Wednesday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='thu', kind=None),
                                            Constant(value='Thursday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='fri', kind=None),
                                            Constant(value='Friday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sat', kind=None),
                                            Constant(value='Saturday', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sun', kind=None),
                                            Constant(value='Sunday', kind=None),
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
                                value=Constant(value='Day Of The Week', kind=None),
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
                    targets=[Name(id='repeat_month', ctx=Store())],
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
                                            Constant(value='january', kind=None),
                                            Constant(value='January', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='february', kind=None),
                                            Constant(value='February', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='march', kind=None),
                                            Constant(value='March', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='april', kind=None),
                                            Constant(value='April', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='may', kind=None),
                                            Constant(value='May', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='june', kind=None),
                                            Constant(value='June', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='july', kind=None),
                                            Constant(value='July', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='august', kind=None),
                                            Constant(value='August', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='september', kind=None),
                                            Constant(value='September', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='october', kind=None),
                                            Constant(value='October', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='november', kind=None),
                                            Constant(value='November', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='december', kind=None),
                                            Constant(value='December', kind=None),
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
                FunctionDef(
                    name='_check_recurrence_days',
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
                            target=Name(id='project', ctx=Store()),
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
                                            args=[arg(arg='p', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='p', ctx=Load()),
                                                attr='repeat_unit',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='week', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='any', ctx=Load()),
                                            args=[
                                                List(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='project', ctx=Load()),
                                                            attr='mon',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='project', ctx=Load()),
                                                            attr='tue',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='project', ctx=Load()),
                                                            attr='wed',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='project', ctx=Load()),
                                                            attr='thu',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='project', ctx=Load()),
                                                            attr='fri',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='project', ctx=Load()),
                                                            attr='sat',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='project', ctx=Load()),
                                                            attr='sun',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[Constant(value='You should select a least one day', kind=None)],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
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
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='repeat_unit', kind=None),
                                Constant(value='mon', kind=None),
                                Constant(value='tue', kind=None),
                                Constant(value='wed', kind=None),
                                Constant(value='thu', kind=None),
                                Constant(value='fri', kind=None),
                                Constant(value='sat', kind=None),
                                Constant(value='sun', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_repeat_interval',
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
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='t', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='t', ctx=Load()),
                                                attr='repeat_interval',
                                                ctx=Load(),
                                            ),
                                            ops=[LtE()],
                                            comparators=[Constant(value=0, kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[Constant(value='The interval should be greater than 0', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='repeat_interval', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_repeat_number',
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
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='t', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='t', ctx=Load()),
                                                        attr='repeat_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='after', kind=None)],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='t', ctx=Load()),
                                                        attr='repeat_number',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[LtE()],
                                                    comparators=[Constant(value=0, kind=None)],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[Constant(value='Should repeat at least once', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='repeat_number', kind=None),
                                Constant(value='repeat_type', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_repeat_until_date',
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
                            targets=[Name(id='today', ctx=Store())],
                            value=Call(
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
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='t', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='t', ctx=Load()),
                                                        attr='repeat_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='until', kind=None)],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='t', ctx=Load()),
                                                        attr='repeat_until',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Lt()],
                                                    comparators=[Name(id='today', ctx=Load())],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[Constant(value='The end date should be in the future', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='repeat_type', kind=None),
                                Constant(value='repeat_until', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_repeat_until_month',
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
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='r', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='repeat_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='until', kind=None)],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='repeat_unit',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='month', kind=None)],
                                                ),
                                                Attribute(
                                                    value=Name(id='r', ctx=Load()),
                                                    attr='repeat_until',
                                                    ctx=Load(),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='repeat_on_month',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='date', kind=None)],
                                                ),
                                                Compare(
                                                    left=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='r', ctx=Load()),
                                                                attr='repeat_day',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    ops=[Gt()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='r', ctx=Load()),
                                                                attr='repeat_until',
                                                                ctx=Load(),
                                                            ),
                                                            attr='day',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[Constant(value='The end date should be after the day of the month', kind=None)],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='repeat_unit', kind=None),
                                Constant(value='repeat_on_month', kind=None),
                                Constant(value='repeat_day', kind=None),
                                Constant(value='repeat_type', kind=None),
                                Constant(value='repeat_until', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_recurring_fields',
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
                                    Constant(value='message_partner_ids', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='description', kind=None),
                                    Constant(value='displayed_image_id', kind=None),
                                    Constant(value='email_cc', kind=None),
                                    Constant(value='parent_id', kind=None),
                                    Constant(value='partner_email', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='partner_phone', kind=None),
                                    Constant(value='planned_hours', kind=None),
                                    Constant(value='project_id', kind=None),
                                    Constant(value='display_project_id', kind=None),
                                    Constant(value='project_privacy_visibility', kind=None),
                                    Constant(value='sequence', kind=None),
                                    Constant(value='tag_ids', kind=None),
                                    Constant(value='recurrence_id', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='recurring_task', kind=None),
                                    Constant(value='analytic_account_id', kind=None),
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
                FunctionDef(
                    name='_get_weekdays',
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
                        defaults=[Constant(value=1, kind=None)],
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='repeat_unit',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='week', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=ListComp(
                                        elt=Call(
                                            func=Name(id='fn', ctx=Load()),
                                            args=[Name(id='n', ctx=Load())],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='day', ctx=Store()),
                                                        Name(id='fn', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='DAYS', ctx=Load()),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[
                                                    Subscript(
                                                        value=Name(id='self', ctx=Load()),
                                                        slice=Name(id='day', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Call(
                                        func=Call(
                                            func=Attribute(
                                                value=Name(id='DAYS', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='repeat_weekday',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        args=[Name(id='n', ctx=Load())],
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
                FunctionDef(
                    name='_get_next_recurring_dates',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='date_start', annotation=None, type_comment=None),
                            arg(arg='repeat_interval', annotation=None, type_comment=None),
                            arg(arg='repeat_unit', annotation=None, type_comment=None),
                            arg(arg='repeat_type', annotation=None, type_comment=None),
                            arg(arg='repeat_until', annotation=None, type_comment=None),
                            arg(arg='repeat_on_month', annotation=None, type_comment=None),
                            arg(arg='repeat_on_year', annotation=None, type_comment=None),
                            arg(arg='weekdays', annotation=None, type_comment=None),
                            arg(arg='repeat_day', annotation=None, type_comment=None),
                            arg(arg='repeat_week', annotation=None, type_comment=None),
                            arg(arg='repeat_month', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='count', kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rrule_kwargs', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='interval', kind=None),
                                    Constant(value='dtstart', kind=None),
                                ],
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='repeat_interval', ctx=Load()),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Name(id='date_start', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='repeat_day', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[Name(id='repeat_day', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dates', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='repeat_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='until', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='rrule_kwargs', ctx=Load()),
                                            slice=Constant(value='until', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Name(id='repeat_until', ctx=Load()),
                                        body=Name(id='repeat_until', ctx=Load()),
                                        orelse=Call(
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
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='rrule_kwargs', ctx=Load()),
                                            slice=Constant(value='count', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='count', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='repeat_unit', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='week', kind=None)],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='repeat_unit', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='month', kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='repeat_on_month', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='day', kind=None)],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='repeat_unit', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='year', kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='repeat_on_year', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='day', kind=None)],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='rrule_kwargs', ctx=Load()),
                                            slice=Constant(value='byweekday', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='weekdays', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='repeat_unit', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='day', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='rrule_kwargs', ctx=Load()),
                                            slice=Constant(value='freq', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='DAILY', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='repeat_unit', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='month', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='rrule_kwargs', ctx=Load()),
                                                    slice=Constant(value='freq', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='MONTHLY', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='repeat_on_month', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='date', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='start', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='date_start', ctx=Load()),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='relativedelta', ctx=Load()),
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
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='repeat_type', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='until', kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Name(id='repeat_until', ctx=Load()),
                                                                ops=[Gt()],
                                                                comparators=[Name(id='date_start', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='delta', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='relativedelta', ctx=Load()),
                                                                args=[
                                                                    Name(id='repeat_until', ctx=Load()),
                                                                    Name(id='date_start', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='count', ctx=Store())],
                                                            value=BinOp(
                                                                left=BinOp(
                                                                    left=Attribute(
                                                                        value=Name(id='delta', ctx=Load()),
                                                                        attr='years',
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=Mult(),
                                                                    right=Constant(value=12, kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Attribute(
                                                                    value=Name(id='delta', ctx=Load()),
                                                                    attr='months',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                For(
                                                    target=Name(id='i', ctx=Store()),
                                                    iter=Call(
                                                        func=Name(id='range', ctx=Load()),
                                                        args=[Name(id='count', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='start', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='start', ctx=Load()),
                                                                    attr='replace',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='day',
                                                                        value=Call(
                                                                            func=Name(id='min', ctx=Load()),
                                                                            args=[
                                                                                Name(id='repeat_day', ctx=Load()),
                                                                                Subscript(
                                                                                    value=Call(
                                                                                        func=Name(id='monthrange', ctx=Load()),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='start', ctx=Load()),
                                                                                                attr='year',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Attribute(
                                                                                                value=Name(id='start', ctx=Load()),
                                                                                                attr='month',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    slice=Constant(value=1, kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
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
                                                                        left=Name(id='i', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value=0, kind=None)],
                                                                    ),
                                                                    Compare(
                                                                        left=Name(id='start', ctx=Load()),
                                                                        ops=[Lt()],
                                                                        comparators=[Name(id='date_start', ctx=Load())],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                AugAssign(
                                                                    target=Name(id='start', ctx=Store()),
                                                                    op=Add(),
                                                                    value=Call(
                                                                        func=Name(id='relativedelta', ctx=Load()),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='months',
                                                                                value=Name(id='repeat_interval', ctx=Load()),
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
                                                                    value=Name(id='dates', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='start', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='start', ctx=Store()),
                                                            op=Add(),
                                                            value=Call(
                                                                func=Name(id='relativedelta', ctx=Load()),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='months',
                                                                        value=Name(id='repeat_interval', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                Return(
                                                    value=Name(id='dates', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='repeat_unit', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='year', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='rrule_kwargs', ctx=Load()),
                                                            slice=Constant(value='freq', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='YEARLY', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='month', ctx=Store())],
                                                    value=BinOp(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Name(id='list', ctx=Load()),
                                                                    args=[
                                                                        Call(
                                                                            func=Attribute(
                                                                                value=Name(id='MONTHS', ctx=Load()),
                                                                                attr='keys',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='index',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='repeat_month', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='rrule_kwargs', ctx=Load()),
                                                            slice=Constant(value='bymonth', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='month', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='repeat_on_year', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='date', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='rrule_kwargs', ctx=Load()),
                                                                    slice=Constant(value='bymonthday', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Name(id='min', ctx=Load()),
                                                                args=[
                                                                    Name(id='repeat_day', ctx=Load()),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='MONTHS', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='repeat_month', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='rrule_kwargs', ctx=Load()),
                                                                    slice=Constant(value='bymonth', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='month', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='rrule_kwargs', ctx=Load()),
                                                            slice=Constant(value='freq', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='WEEKLY', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='rules', ctx=Store())],
                            value=Call(
                                func=Name(id='rrule', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='rrule_kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=IfExp(
                                test=Name(id='rules', ctx=Load()),
                                body=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[Name(id='rules', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=List(elts=[], ctx=Load()),
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
                    name='_new_task_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='task', annotation=None, type_comment=None),
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='fields_to_copy', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_recurring_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='task_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='task', ctx=Load()),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='fields_to_copy', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='create_values', ctx=Store())],
                            value=DictComp(
                                key=Name(id='field', ctx=Load()),
                                value=IfExp(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='value', ctx=Load()),
                                            Name(id='tuple', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=Subscript(
                                        value=Name(id='value', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    orelse=Name(id='value', ctx=Load()),
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='field', ctx=Store()),
                                                Name(id='value', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='task_values', ctx=Load()),
                                                attr='items',
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='create_values', ctx=Load()),
                                    slice=Constant(value='stage_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=IfExp(
                                test=Attribute(
                                    value=Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='project_id',
                                        ctx=Load(),
                                    ),
                                    attr='type_ids',
                                    ctx=Load(),
                                ),
                                body=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='task', ctx=Load()),
                                                attr='project_id',
                                                ctx=Load(),
                                            ),
                                            attr='type_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                orelse=Attribute(
                                    value=Attribute(
                                        value=Name(id='task', ctx=Load()),
                                        attr='stage_id',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='create_values', ctx=Load()),
                                    slice=Constant(value='user_ids', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='create_values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_subtasks',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='task', annotation=None, type_comment=None),
                            arg(arg='new_task', annotation=None, type_comment=None),
                            arg(arg='depth', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=3, kind=None)],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='depth', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='task', ctx=Load()),
                                            attr='child_ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='children', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='child_recurrence', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='child', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='task', ctx=Load()),
                                attr='child_ids',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='child', ctx=Load()),
                                                attr='recurrence_id',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='child', ctx=Load()),
                                                        attr='recurrence_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[Name(id='child_recurrence', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='child_values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_new_task_values',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='child', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='child_values', ctx=Load()),
                                            slice=Constant(value='parent_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='new_task', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='child', ctx=Load()),
                                        attr='recurrence_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='child_recurrence', ctx=Store()),
                                            op=Add(),
                                            value=List(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='child', ctx=Load()),
                                                            attr='recurrence_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='child_values', ctx=Load()),
                                                    slice=Constant(value='recurrence_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='child', ctx=Load()),
                                                            attr='recurrence_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='copy',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='child', ctx=Load()),
                                                attr='child_ids',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Name(id='depth', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='new_child', ctx=Store())],
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
                                                                slice=Constant(value='project.task', kind=None),
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
                                                args=[Name(id='child_values', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_create_subtasks',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='child', ctx=Load()),
                                                    Name(id='new_child', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='depth',
                                                        value=BinOp(
                                                            left=Name(id='depth', ctx=Load()),
                                                            op=Sub(),
                                                            right=Constant(value=1, kind=None),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='children', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='child_values', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='children_tasks', ctx=Store())],
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
                                                slice=Constant(value='project.task', kind=None),
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
                                args=[Name(id='children', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_next_task',
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
                            target=Name(id='recurrence', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='task', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='recurrence', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='task_ids',
                                            ctx=Load(),
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='create_values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='recurrence', ctx=Load()),
                                            attr='_new_task_values',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='task', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_task', ctx=Store())],
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
                                                        slice=Constant(value='project.task', kind=None),
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
                                        args=[Name(id='create_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='recurrence', ctx=Load()),
                                            attr='_create_subtasks',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='task', ctx=Load()),
                                            Name(id='new_task', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='depth',
                                                value=Constant(value=3, kind=None),
                                            ),
                                        ],
                                    ),
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
                    name='_set_next_recurrence_date',
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
                            targets=[Name(id='today', ctx=Store())],
                            value=Call(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tomorrow', ctx=Store())],
                            value=BinOp(
                                left=Name(id='today', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='relativedelta', ctx=Load()),
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
                        For(
                            target=Name(id='recurrence', ctx=Store()),
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
                                            args=[arg(arg='r', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=Or(),
                                            values=[
                                                BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='r', ctx=Load()),
                                                                attr='repeat_type',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='after', kind=None)],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='r', ctx=Load()),
                                                                attr='recurrence_left',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[GtE()],
                                                            comparators=[Constant(value=0, kind=None)],
                                                        ),
                                                    ],
                                                ),
                                                BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='r', ctx=Load()),
                                                                attr='repeat_type',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='until', kind=None)],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='r', ctx=Load()),
                                                                attr='repeat_until',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[GtE()],
                                                            comparators=[Name(id='today', ctx=Load())],
                                                        ),
                                                    ],
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='r', ctx=Load()),
                                                        attr='repeat_type',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='forever', kind=None)],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='recurrence', ctx=Load()),
                                                    attr='repeat_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='after', kind=None)],
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='recurrence', ctx=Load()),
                                                    attr='recurrence_left',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='recurrence', ctx=Load()),
                                                    attr='next_recurrence_date',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='next_date', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_next_recurring_dates',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='tomorrow', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
                                                        attr='repeat_interval',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
                                                        attr='repeat_unit',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
                                                        attr='repeat_type',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
                                                        attr='repeat_until',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
                                                        attr='repeat_on_month',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
                                                        attr='repeat_on_year',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='recurrence', ctx=Load()),
                                                            attr='_get_weekdays',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
                                                        attr='repeat_day',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
                                                        attr='repeat_week',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='recurrence', ctx=Load()),
                                                        attr='repeat_month',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='count',
                                                        value=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='recurrence', ctx=Load()),
                                                    attr='next_recurrence_date',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=IfExp(
                                                test=Name(id='next_date', ctx=Load()),
                                                body=Subscript(
                                                    value=Name(id='next_date', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                orelse=Constant(value=False, kind=None),
                                            ),
                                            type_comment=None,
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
                    name='_cron_create_recurring_tasks',
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='has_group',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='project.group_project_recurring_tasks', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='today', ctx=Store())],
                            value=Call(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recurring_today', ctx=Store())],
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
                                                    Constant(value='next_recurrence_date', kind=None),
                                                    Constant(value='<=', kind=None),
                                                    Name(id='today', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='recurring_today', ctx=Load()),
                                    attr='_create_next_task',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='recurrence', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='recurring_today', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='r', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='r', ctx=Load()),
                                                attr='repeat_type',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='after', kind=None)],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='recurrence', ctx=Load()),
                                        attr='recurrence_left',
                                        ctx=Store(),
                                    ),
                                    op=Sub(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='recurring_today', ctx=Load()),
                                    attr='_set_next_recurrence_date',
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
                    name='create',
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
                                args=[Constant(value='repeat_number', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='recurrence_left', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='repeat_number', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProjectTaskRecurrence', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='res', ctx=Load()),
                                    attr='_set_next_recurrence_date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
                                args=[Constant(value='repeat_number', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='recurrence_left', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='repeat_number', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ProjectTaskRecurrence', ctx=Load()),
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
                                left=Constant(value='next_recurrence_date', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='vals', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_set_next_recurrence_date',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
