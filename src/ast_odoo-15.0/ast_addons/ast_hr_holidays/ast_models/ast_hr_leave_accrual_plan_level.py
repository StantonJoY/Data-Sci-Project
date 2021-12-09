Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='calendar', asname=None)],
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='num2words',
            names=[alias(name='num2words', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.date_utils',
            names=[alias(name='get_timedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='get_lang', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='DAYS', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='sun', kind=None),
                    Constant(value='mon', kind=None),
                    Constant(value='tue', kind=None),
                    Constant(value='wed', kind=None),
                    Constant(value='thu', kind=None),
                    Constant(value='fri', kind=None),
                    Constant(value='sat', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='MONTHS', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='jan', kind=None),
                    Constant(value='feb', kind=None),
                    Constant(value='mar', kind=None),
                    Constant(value='apr', kind=None),
                    Constant(value='may', kind=None),
                    Constant(value='jun', kind=None),
                    Constant(value='jul', kind=None),
                    Constant(value='aug', kind=None),
                    Constant(value='sep', kind=None),
                    Constant(value='oct', kind=None),
                    Constant(value='nov', kind=None),
                    Constant(value='dec', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DAY_SELECT_VALUES', ctx=Store())],
            value=BinOp(
                left=ListComp(
                    elt=Call(
                        func=Name(id='str', ctx=Load()),
                        args=[Name(id='i', ctx=Load())],
                        keywords=[],
                    ),
                    generators=[
                        comprehension(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=1, kind=None),
                                    Constant(value=29, kind=None),
                                ],
                                keywords=[],
                            ),
                            ifs=[],
                            is_async=0,
                        ),
                    ],
                ),
                op=Add(),
                right=List(
                    elts=[Constant(value='last', kind=None)],
                    ctx=Load(),
                ),
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_get_selection_days',
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
                    targets=[Name(id='lang', ctx=Store())],
                    value=Attribute(
                        value=Call(
                            func=Name(id='get_lang', ctx=Load()),
                            args=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                        attr='code',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Return(
                    value=ListComp(
                        elt=Tuple(
                            elts=[
                                Subscript(
                                    value=Name(id='DAY_SELECT_VALUES', ctx=Load()),
                                    slice=BinOp(
                                        left=Name(id='i', ctx=Load()),
                                        op=Sub(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                    ctx=Load(),
                                ),
                                IfExp(
                                    test=Compare(
                                        left=Name(id='i', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Constant(value=29, kind=None)],
                                    ),
                                    body=Call(
                                        func=Name(id='num2words', ctx=Load()),
                                        args=[Name(id='i', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Name(id='lang', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='to',
                                                value=Constant(value='ordinal_num', kind=None),
                                            ),
                                        ],
                                    ),
                                    orelse=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='last day', kind=None)],
                                        keywords=[],
                                    ),
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
                                        Constant(value=30, kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='AccrualPlanLevel',
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
                    value=Constant(value='hr.leave.accrual.level', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Accrual Plan Level', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence asc', kind=None),
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
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='sequence', kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_sequence', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Sequence is generated automatically by start time delta.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='level', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_level', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Level computed through the sequence.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='accrual_plan_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='hr.leave.accrual.plan', kind=None),
                            Constant(value='Accrual Plan', kind=None),
                        ],
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
                    targets=[Name(id='start_count', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Start after', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='The accrual starts after a defined period from the employee start date. This field defines the number of days, months or years after which accrual is used.', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='1', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='start_type', ctx=Store())],
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
                                            Constant(value='day(s)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='month', kind=None),
                                            Constant(value='month(s)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='year', kind=None),
                                            Constant(value='year(s)', kind=None),
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
                                value=Constant(value='day', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value=' ', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This field defines the unit of time after which the accrual starts.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_based_on_worked_time', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Based on worked time', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Only accrue for the time worked by the employee. This is the time when the employee did not take time off.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='added_value', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Rate', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The number of hours/days that will be incremented in the specified Time Off Type for every period', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='added_value_type', ctx=Store())],
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
                                            Constant(value='days', kind=None),
                                            Constant(value='Days', kind=None),
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
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='days', kind=None),
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
                    targets=[Name(id='frequency', ctx=Store())],
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
                                            Constant(value='bimonthly', kind=None),
                                            Constant(value='Twice a month', kind=None),
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
                                            Constant(value='biyearly', kind=None),
                                            Constant(value='Twice a year', kind=None),
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
                                value=Constant(value='daily', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Frequency', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='week_day', ctx=Store())],
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
                                arg='default',
                                value=Constant(value='mon', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Allocation on', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='first_day', ctx=Store())],
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
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='first_day_display', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[Name(id='_get_selection_days', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_days_display', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_inverse_first_day_display', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='second_day', ctx=Store())],
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
                                value=Constant(value=15, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='second_day_display', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[Name(id='_get_selection_days', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_days_display', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_inverse_second_day_display', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='first_month_day', ctx=Store())],
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
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='first_month_day_display', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[Name(id='_get_selection_days', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_days_display', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_inverse_first_month_day_display', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='first_month', ctx=Store())],
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
                                            Constant(value='jan', kind=None),
                                            Constant(value='January', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='feb', kind=None),
                                            Constant(value='February', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='mar', kind=None),
                                            Constant(value='March', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='apr', kind=None),
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
                                            Constant(value='jun', kind=None),
                                            Constant(value='June', kind=None),
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
                                value=Constant(value='jan', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='second_month_day', ctx=Store())],
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
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='second_month_day_display', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[Name(id='_get_selection_days', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_days_display', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_inverse_second_month_day_display', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='second_month', ctx=Store())],
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
                                            Constant(value='jul', kind=None),
                                            Constant(value='July', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='aug', kind=None),
                                            Constant(value='August', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sep', kind=None),
                                            Constant(value='September', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='oct', kind=None),
                                            Constant(value='October', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='nov', kind=None),
                                            Constant(value='November', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='dec', kind=None),
                                            Constant(value='December', kind=None),
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
                                value=Constant(value='jul', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='yearly_month', ctx=Store())],
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
                                            Constant(value='jan', kind=None),
                                            Constant(value='January', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='feb', kind=None),
                                            Constant(value='February', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='mar', kind=None),
                                            Constant(value='March', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='apr', kind=None),
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
                                            Constant(value='jun', kind=None),
                                            Constant(value='June', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='jul', kind=None),
                                            Constant(value='July', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='aug', kind=None),
                                            Constant(value='August', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sep', kind=None),
                                            Constant(value='September', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='oct', kind=None),
                                            Constant(value='October', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='nov', kind=None),
                                            Constant(value='November', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='dec', kind=None),
                                            Constant(value='December', kind=None),
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
                                value=Constant(value='jan', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='yearly_day', ctx=Store())],
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
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='yearly_day_display', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[Name(id='_get_selection_days', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_days_display', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_inverse_yearly_day_display', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='maximum_leave', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Limit to', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=100, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Choose a cap for this accrual. 0 means no cap.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='parent_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='hr.leave.accrual.level', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Previous Level', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If this field is empty, this level is the first one.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='action_with_unused_accruals', ctx=Store())],
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
                                            Constant(value='postponed', kind=None),
                                            Constant(value='Transferred to the next year', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lost', kind=None),
                                            Constant(value='Lost', kind=None),
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
                                value=Constant(value='At the end of the calendar year, unused accruals will be', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='postponed', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value='True', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='check_dates', kind=None),
                                    Constant(value="CHECK( (frequency = 'daily') or(week_day IS NOT NULL AND frequency = 'weekly') or (first_day > 0 AND second_day > first_day AND first_day <= 31 AND second_day <= 31 AND frequency = 'bimonthly') or (first_day > 0 AND first_day <= 31 AND frequency = 'monthly')or (first_month_day > 0 AND first_month_day <= 31 AND second_month_day > 0 AND second_month_day <= 31 AND frequency = 'biyearly') or (yearly_day > 0 AND yearly_day <= 31 AND frequency = 'yearly'))", kind=None),
                                    Constant(value="The dates you've set up aren't correct. Please check them.", kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    Constant(value='start_count_check', kind=None),
                                    Constant(value='CHECK( start_count >= 0 )', kind=None),
                                    Constant(value='You can not start an accrual in the past.', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            Tuple(
                                elts=[
                                    Constant(value='added_value_greater_than_zero', kind=None),
                                    Constant(value='CHECK(added_value > 0)', kind=None),
                                    Constant(value='You must give a rate greater than 0 in accrual plan levels.', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_sequence',
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
                            targets=[Name(id='start_type_multipliers', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='day', kind=None),
                                    Constant(value='month', kind=None),
                                    Constant(value='year', kind=None),
                                ],
                                values=[
                                    Constant(value=1, kind=None),
                                    Constant(value=30, kind=None),
                                    Constant(value=365, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='sequence',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='start_count',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Subscript(
                                            value=Name(id='start_type_multipliers', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='level', ctx=Load()),
                                                attr='start_type',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
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
                                Constant(value='start_count', kind=None),
                                Constant(value='start_type', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_level',
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
                            targets=[Name(id='mapped_level_ids', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='plan', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='accrual_plan_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='mapped_level_ids', ctx=Load()),
                                            slice=Name(id='plan', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=ListComp(
                                        elt=Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='level', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='plan', ctx=Load()),
                                                            attr='level_ids',
                                                            ctx=Load(),
                                                        ),
                                                        attr='sorted',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='sequence', kind=None)],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='level', ctx=Load()),
                                        attr='accrual_plan_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='level', ctx=Load()),
                                                    attr='level',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='mapped_level_ids', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='level', ctx=Load()),
                                                                attr='accrual_plan_id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        attr='index',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='level', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='level', ctx=Load()),
                                                    attr='level',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=1, kind=None),
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
                                Constant(value='sequence', kind=None),
                                Constant(value='accrual_plan_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_days_display',
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
                            targets=[Name(id='days_select', ctx=Store())],
                            value=Call(
                                func=Name(id='_get_selection_days', ctx=Load()),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='first_day_display',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='days_select', ctx=Load()),
                                            slice=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='level', ctx=Load()),
                                                            attr='first_day',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    Constant(value=28, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='second_day_display',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='days_select', ctx=Load()),
                                            slice=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='level', ctx=Load()),
                                                            attr='second_day',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    Constant(value=28, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='first_month_day_display',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='days_select', ctx=Load()),
                                            slice=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='level', ctx=Load()),
                                                            attr='first_month_day',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    Constant(value=28, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='second_month_day_display',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='days_select', ctx=Load()),
                                            slice=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='level', ctx=Load()),
                                                            attr='second_month_day',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    Constant(value=28, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='yearly_day_display',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='days_select', ctx=Load()),
                                            slice=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='level', ctx=Load()),
                                                            attr='yearly_day',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                    Constant(value=28, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
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
                            args=[
                                Constant(value='first_day', kind=None),
                                Constant(value='second_day', kind=None),
                                Constant(value='first_month_day', kind=None),
                                Constant(value='second_month_day', kind=None),
                                Constant(value='yearly_day', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_inverse_first_day_display',
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
                            target=Name(id='level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='first_day_display',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='last', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='level', ctx=Load()),
                                                    attr='first_day',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=31, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='level', ctx=Load()),
                                                    attr='first_day',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='DAY_SELECT_VALUES', ctx=Load()),
                                                        attr='index',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='level', ctx=Load()),
                                                            attr='first_day_display',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
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
                    name='_inverse_second_day_display',
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
                            target=Name(id='level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='second_day_display',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='last', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='level', ctx=Load()),
                                                    attr='second_day',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=31, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='level', ctx=Load()),
                                                    attr='second_day',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='DAY_SELECT_VALUES', ctx=Load()),
                                                        attr='index',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='level', ctx=Load()),
                                                            attr='second_day_display',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
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
                    name='_inverse_first_month_day_display',
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
                            target=Name(id='level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='first_month_day_display',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='last', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='level', ctx=Load()),
                                                    attr='first_month_day',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=31, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='level', ctx=Load()),
                                                    attr='first_month_day',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='DAY_SELECT_VALUES', ctx=Load()),
                                                        attr='index',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='level', ctx=Load()),
                                                            attr='first_month_day_display',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
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
                    name='_inverse_second_month_day_display',
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
                            target=Name(id='level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='second_month_day_display',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='last', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='level', ctx=Load()),
                                                    attr='second_month_day',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=31, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='level', ctx=Load()),
                                                    attr='second_month_day',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='DAY_SELECT_VALUES', ctx=Load()),
                                                        attr='index',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='level', ctx=Load()),
                                                            attr='second_month_day_display',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
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
                    name='_inverse_yearly_day_display',
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
                            target=Name(id='level', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='level', ctx=Load()),
                                            attr='yearly_day_display',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='last', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='level', ctx=Load()),
                                                    attr='yearly_day',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=31, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='level', ctx=Load()),
                                                    attr='yearly_day',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='DAY_SELECT_VALUES', ctx=Load()),
                                                        attr='index',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='level', ctx=Load()),
                                                            attr='yearly_day_display',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
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
                    name='_get_next_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='last_call', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Returns the next date with the given last call\n        ', kind=None),
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='frequency',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='daily', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=BinOp(
                                        left=Name(id='last_call', ctx=Load()),
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
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='frequency',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='weekly', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='daynames', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Constant(value='mon', kind=None),
                                                    Constant(value='tue', kind=None),
                                                    Constant(value='wed', kind=None),
                                                    Constant(value='thu', kind=None),
                                                    Constant(value='fri', kind=None),
                                                    Constant(value='sat', kind=None),
                                                    Constant(value='sun', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='weekday', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='daynames', ctx=Load()),
                                                    attr='index',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='week_day',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=BinOp(
                                                left=Name(id='last_call', ctx=Load()),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                        keyword(
                                                            arg='weekday',
                                                            value=Name(id='weekday', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='frequency',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='bimonthly', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='first_date', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='last_call', ctx=Load()),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='relativedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='day',
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='first_day',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='second_date', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='last_call', ctx=Load()),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='relativedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='day',
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='second_day',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='last_call', ctx=Load()),
                                                        ops=[Lt()],
                                                        comparators=[Name(id='first_date', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Name(id='first_date', ctx=Load()),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='last_call', ctx=Load()),
                                                                ops=[Lt()],
                                                                comparators=[Name(id='second_date', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Return(
                                                                    value=Name(id='second_date', ctx=Load()),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Return(
                                                                    value=BinOp(
                                                                        left=Name(id='last_call', ctx=Load()),
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
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='first_day',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='frequency',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='monthly', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='date', ctx=Store())],
                                                            value=BinOp(
                                                                left=Name(id='last_call', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='first_day',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='last_call', ctx=Load()),
                                                                ops=[Lt()],
                                                                comparators=[Name(id='date', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Return(
                                                                    value=Name(id='date', ctx=Load()),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Return(
                                                                    value=BinOp(
                                                                        left=Name(id='last_call', ctx=Load()),
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
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='first_day',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='frequency',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='biyearly', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='first_month', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='MONTHS', ctx=Load()),
                                                                                attr='index',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='first_month',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='second_month', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='MONTHS', ctx=Load()),
                                                                                attr='index',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='second_month',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='first_date', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Name(id='last_call', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='relativedelta', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='month',
                                                                                    value=Name(id='first_month', ctx=Load()),
                                                                                ),
                                                                                keyword(
                                                                                    arg='day',
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='first_month_day',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='second_date', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Name(id='last_call', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='relativedelta', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='month',
                                                                                    value=Name(id='second_month', ctx=Load()),
                                                                                ),
                                                                                keyword(
                                                                                    arg='day',
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='second_month_day',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='last_call', ctx=Load()),
                                                                        ops=[Lt()],
                                                                        comparators=[Name(id='first_date', ctx=Load())],
                                                                    ),
                                                                    body=[
                                                                        Return(
                                                                            value=Name(id='first_date', ctx=Load()),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Name(id='last_call', ctx=Load()),
                                                                                ops=[Lt()],
                                                                                comparators=[Name(id='second_date', ctx=Load())],
                                                                            ),
                                                                            body=[
                                                                                Return(
                                                                                    value=Name(id='second_date', ctx=Load()),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Return(
                                                                                    value=BinOp(
                                                                                        left=Name(id='last_call', ctx=Load()),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Name(id='relativedelta', ctx=Load()),
                                                                                            args=[],
                                                                                            keywords=[
                                                                                                keyword(
                                                                                                    arg='years',
                                                                                                    value=Constant(value=1, kind=None),
                                                                                                ),
                                                                                                keyword(
                                                                                                    arg='month',
                                                                                                    value=Name(id='first_month', ctx=Load()),
                                                                                                ),
                                                                                                keyword(
                                                                                                    arg='day',
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='first_month_day',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='frequency',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='yearly', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='month', ctx=Store())],
                                                                            value=BinOp(
                                                                                left=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='MONTHS', ctx=Load()),
                                                                                        attr='index',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='yearly_month',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=1, kind=None),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='date', ctx=Store())],
                                                                            value=BinOp(
                                                                                left=Name(id='last_call', ctx=Load()),
                                                                                op=Add(),
                                                                                right=Call(
                                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                                    args=[],
                                                                                    keywords=[
                                                                                        keyword(
                                                                                            arg='month',
                                                                                            value=Name(id='month', ctx=Load()),
                                                                                        ),
                                                                                        keyword(
                                                                                            arg='day',
                                                                                            value=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='yearly_day',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        If(
                                                                            test=Compare(
                                                                                left=Name(id='last_call', ctx=Load()),
                                                                                ops=[Lt()],
                                                                                comparators=[Name(id='date', ctx=Load())],
                                                                            ),
                                                                            body=[
                                                                                Return(
                                                                                    value=Name(id='date', ctx=Load()),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Return(
                                                                                    value=BinOp(
                                                                                        left=Name(id='last_call', ctx=Load()),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Name(id='relativedelta', ctx=Load()),
                                                                                            args=[],
                                                                                            keywords=[
                                                                                                keyword(
                                                                                                    arg='years',
                                                                                                    value=Constant(value=1, kind=None),
                                                                                                ),
                                                                                                keyword(
                                                                                                    arg='month',
                                                                                                    value=Name(id='month', ctx=Load()),
                                                                                                ),
                                                                                                keyword(
                                                                                                    arg='day',
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='yearly_day',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Return(
                                                                            value=Constant(value=False, kind=None),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_previous_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='last_call', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Returns the date a potential previous call would have been at\n        For example if you have a monthly level giving 16/02 would return 01/02\n        Contrary to `_get_next_date` this function will return the 01/02 if that date is given\n        ', kind=None),
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='frequency',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='daily', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Name(id='last_call', ctx=Load()),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='frequency',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='weekly', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='daynames', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Constant(value='mon', kind=None),
                                                    Constant(value='tue', kind=None),
                                                    Constant(value='wed', kind=None),
                                                    Constant(value='thu', kind=None),
                                                    Constant(value='fri', kind=None),
                                                    Constant(value='sat', kind=None),
                                                    Constant(value='sun', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='weekday', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='daynames', ctx=Load()),
                                                    attr='index',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='week_day',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=BinOp(
                                                left=Name(id='last_call', ctx=Load()),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=6, kind=None),
                                                            ),
                                                        ),
                                                        keyword(
                                                            arg='weekday',
                                                            value=Name(id='weekday', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='frequency',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='bimonthly', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='second_date', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='last_call', ctx=Load()),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='relativedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='day',
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='second_day',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='first_date', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='last_call', ctx=Load()),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Name(id='relativedelta', ctx=Load()),
                                                            args=[],
                                                            keywords=[
                                                                keyword(
                                                                    arg='day',
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='first_day',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='last_call', ctx=Load()),
                                                        ops=[GtE()],
                                                        comparators=[Name(id='second_date', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Name(id='second_date', ctx=Load()),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='last_call', ctx=Load()),
                                                                ops=[GtE()],
                                                                comparators=[Name(id='first_date', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Return(
                                                                    value=Name(id='first_date', ctx=Load()),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Return(
                                                                    value=BinOp(
                                                                        left=Name(id='last_call', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='relativedelta', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='months',
                                                                                    value=UnaryOp(
                                                                                        op=USub(),
                                                                                        operand=Constant(value=1, kind=None),
                                                                                    ),
                                                                                ),
                                                                                keyword(
                                                                                    arg='day',
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='second_day',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='frequency',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='monthly', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='date', ctx=Store())],
                                                            value=BinOp(
                                                                left=Name(id='last_call', ctx=Load()),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='day',
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='first_day',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='last_call', ctx=Load()),
                                                                ops=[GtE()],
                                                                comparators=[Name(id='date', ctx=Load())],
                                                            ),
                                                            body=[
                                                                Return(
                                                                    value=Name(id='date', ctx=Load()),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Return(
                                                                    value=BinOp(
                                                                        left=Name(id='last_call', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='relativedelta', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='months',
                                                                                    value=UnaryOp(
                                                                                        op=USub(),
                                                                                        operand=Constant(value=1, kind=None),
                                                                                    ),
                                                                                ),
                                                                                keyword(
                                                                                    arg='day',
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='first_day',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='frequency',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='biyearly', kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='first_month', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='MONTHS', ctx=Load()),
                                                                                attr='index',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='first_month',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='second_month', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='MONTHS', ctx=Load()),
                                                                                attr='index',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='second_month',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Add(),
                                                                        right=Constant(value=1, kind=None),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='first_date', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Name(id='last_call', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='relativedelta', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='month',
                                                                                    value=Name(id='first_month', ctx=Load()),
                                                                                ),
                                                                                keyword(
                                                                                    arg='day',
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='first_month_day',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='second_date', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Name(id='last_call', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='relativedelta', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='month',
                                                                                    value=Name(id='second_month', ctx=Load()),
                                                                                ),
                                                                                keyword(
                                                                                    arg='day',
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='second_month_day',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Name(id='last_call', ctx=Load()),
                                                                        ops=[GtE()],
                                                                        comparators=[Name(id='second_date', ctx=Load())],
                                                                    ),
                                                                    body=[
                                                                        Return(
                                                                            value=Name(id='second_date', ctx=Load()),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Name(id='last_call', ctx=Load()),
                                                                                ops=[GtE()],
                                                                                comparators=[Name(id='first_date', ctx=Load())],
                                                                            ),
                                                                            body=[
                                                                                Return(
                                                                                    value=Name(id='first_date', ctx=Load()),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Return(
                                                                                    value=BinOp(
                                                                                        left=Name(id='last_call', ctx=Load()),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Name(id='relativedelta', ctx=Load()),
                                                                                            args=[],
                                                                                            keywords=[
                                                                                                keyword(
                                                                                                    arg='years',
                                                                                                    value=UnaryOp(
                                                                                                        op=USub(),
                                                                                                        operand=Constant(value=1, kind=None),
                                                                                                    ),
                                                                                                ),
                                                                                                keyword(
                                                                                                    arg='month',
                                                                                                    value=Name(id='second_month', ctx=Load()),
                                                                                                ),
                                                                                                keyword(
                                                                                                    arg='day',
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='second_month_day',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='frequency',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='yearly', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='month', ctx=Store())],
                                                                            value=BinOp(
                                                                                left=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='MONTHS', ctx=Load()),
                                                                                        attr='index',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='yearly_month',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Add(),
                                                                                right=Constant(value=1, kind=None),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='year_date', ctx=Store())],
                                                                            value=BinOp(
                                                                                left=Name(id='last_call', ctx=Load()),
                                                                                op=Add(),
                                                                                right=Call(
                                                                                    func=Name(id='relativedelta', ctx=Load()),
                                                                                    args=[],
                                                                                    keywords=[
                                                                                        keyword(
                                                                                            arg='month',
                                                                                            value=Name(id='month', ctx=Load()),
                                                                                        ),
                                                                                        keyword(
                                                                                            arg='day',
                                                                                            value=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='yearly_day',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        If(
                                                                            test=Compare(
                                                                                left=Name(id='last_call', ctx=Load()),
                                                                                ops=[GtE()],
                                                                                comparators=[Name(id='year_date', ctx=Load())],
                                                                            ),
                                                                            body=[
                                                                                Return(
                                                                                    value=Name(id='year_date', ctx=Load()),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Return(
                                                                                    value=BinOp(
                                                                                        left=Name(id='last_call', ctx=Load()),
                                                                                        op=Add(),
                                                                                        right=Call(
                                                                                            func=Name(id='relativedelta', ctx=Load()),
                                                                                            args=[],
                                                                                            keywords=[
                                                                                                keyword(
                                                                                                    arg='years',
                                                                                                    value=UnaryOp(
                                                                                                        op=USub(),
                                                                                                        operand=Constant(value=1, kind=None),
                                                                                                    ),
                                                                                                ),
                                                                                                keyword(
                                                                                                    arg='month',
                                                                                                    value=Name(id='month', ctx=Load()),
                                                                                                ),
                                                                                                keyword(
                                                                                                    arg='day',
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='yearly_day',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        Return(
                                                                            value=Constant(value=False, kind=None),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
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
