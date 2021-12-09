Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='pytz',
            names=[alias(name='utc', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        FunctionDef(
            name='timezone_datetime',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='time', annotation=None, type_comment=None)],
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
                        operand=Attribute(
                            value=Name(id='time', ctx=Load()),
                            attr='tzinfo',
                            ctx=Load(),
                        ),
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Name(id='utc', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='time', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='ResourceMixin',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='resource.mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Resource Mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='resource_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='resource.resource', kind=None),
                            Constant(value='Resource', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='auto_join',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
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
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.company', kind=None),
                            Constant(value='Company', kind=None),
                        ],
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
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='resource_id.company_id', kind=None),
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
                    targets=[Name(id='resource_calendar_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='resource.calendar', kind=None),
                            Constant(value='Working Hours', kind=None),
                        ],
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
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
                                        attr='resource_calendar_id',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='resource_id.calendar_id', kind=None),
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
                    targets=[Name(id='tz', ctx=Store())],
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
                                value=Constant(value='Timezone', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='resource_id.tz', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This field is used in order to define in which timezone the resources will work.', kind=None),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='values', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='resource_id', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='resource_vals', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_rec_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tz', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='tz', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='resource.calendar', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='values', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='resource_calendar_id', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='tz',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='tz', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='resource_vals', ctx=Load()),
                                                    slice=Constant(value='tz', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='tz', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='resource', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='resource.resource', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='resource_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='resource_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='resource', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
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
                                            Name(id='ResourceMixin', ctx=Load()),
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
                    name='copy_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='default', annotation=None, type_comment=None),
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
                                left=Name(id='default', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='default', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='resource', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='resource_id',
                                        ctx=Load(),
                                    ),
                                    attr='copy',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='default', ctx=Load()),
                                    slice=Constant(value='resource_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='resource', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='default', ctx=Load()),
                                    slice=Constant(value='company_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='company_id',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='default', ctx=Load()),
                                    slice=Constant(value='resource_calendar_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='calendar_id',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='ResourceMixin', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='copy_data',
                                    ctx=Load(),
                                ),
                                args=[Name(id='default', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_work_days_data_batch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='from_datetime', annotation=None, type_comment=None),
                            arg(arg='to_datetime', annotation=None, type_comment=None),
                            arg(arg='compute_leaves', annotation=None, type_comment=None),
                            arg(arg='calendar', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n            By default the resource calendar is used, but it can be\n            changed using the `calendar` argument.\n\n            `domain` is used in order to recognise the leaves to take,\n            None means default value ('time_type', '=', 'leave')\n\n            Returns a dict {'days': n, 'hours': h} containing the\n            quantity of working time expressed as days and as hours.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='resources', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='resource_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapped_employees', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Attribute(
                                        value=Name(id='e', ctx=Load()),
                                        attr='resource_id',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Attribute(
                                    value=Name(id='e', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='e', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='from_datetime', ctx=Store())],
                            value=Call(
                                func=Name(id='timezone_datetime', ctx=Load()),
                                args=[Name(id='from_datetime', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='to_datetime', ctx=Store())],
                            value=Call(
                                func=Name(id='timezone_datetime', ctx=Load()),
                                args=[Name(id='to_datetime', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapped_resources', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='resource.resource', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='mapped_resources', ctx=Load()),
                                        slice=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='calendar', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=BitOr(),
                                    value=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='resource_id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='calendar', ctx=Store()),
                                    Name(id='calendar_resources', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='mapped_resources', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='calendar', ctx=Load()),
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='calendar_resource', ctx=Store()),
                                            iter=Name(id='calendar_resources', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='result', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='calendar_resource', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='days', kind=None),
                                                            Constant(value='hours', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='day_total', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='calendar', ctx=Load()),
                                            attr='_get_resources_day_total',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='from_datetime', ctx=Load()),
                                            Name(id='to_datetime', ctx=Load()),
                                            Name(id='calendar_resources', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='compute_leaves', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='intervals', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='calendar', ctx=Load()),
                                                    attr='_work_intervals_batch',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='from_datetime', ctx=Load()),
                                                    Name(id='to_datetime', ctx=Load()),
                                                    Name(id='calendar_resources', ctx=Load()),
                                                    Name(id='domain', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='intervals', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='calendar', ctx=Load()),
                                                    attr='_attendance_intervals_batch',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='from_datetime', ctx=Load()),
                                                    Name(id='to_datetime', ctx=Load()),
                                                    Name(id='calendar_resources', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                For(
                                    target=Name(id='calendar_resource', ctx=Store()),
                                    iter=Name(id='calendar_resources', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='calendar_resource', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='calendar', ctx=Load()),
                                                    attr='_get_days_data',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='intervals', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='calendar_resource', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='day_total', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='calendar_resource', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=DictComp(
                                key=Subscript(
                                    value=Name(id='mapped_employees', ctx=Load()),
                                    slice=Attribute(
                                        value=Name(id='r', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Attribute(
                                        value=Name(id='r', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Name(id='resources', ctx=Load()),
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
                FunctionDef(
                    name='_get_leave_days_data_batch',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='from_datetime', annotation=None, type_comment=None),
                            arg(arg='to_datetime', annotation=None, type_comment=None),
                            arg(arg='calendar', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
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
                        Expr(
                            value=Constant(value="\n            By default the resource calendar is used, but it can be\n            changed using the `calendar` argument.\n\n            `domain` is used in order to recognise the leaves to take,\n            None means default value ('time_type', '=', 'leave')\n\n            Returns a dict {'days': n, 'hours': h} containing the number of leaves\n            expressed as days and as hours.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='resources', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='resource_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapped_employees', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Attribute(
                                        value=Name(id='e', ctx=Load()),
                                        attr='resource_id',
                                        ctx=Load(),
                                    ),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                value=Attribute(
                                    value=Name(id='e', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='e', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='from_datetime', ctx=Store())],
                            value=Call(
                                func=Name(id='timezone_datetime', ctx=Load()),
                                args=[Name(id='from_datetime', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='to_datetime', ctx=Store())],
                            value=Call(
                                func=Name(id='timezone_datetime', ctx=Load()),
                                args=[Name(id='to_datetime', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapped_resources', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='resource.resource', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='mapped_resources', ctx=Load()),
                                        slice=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='calendar', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='resource_calendar_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=BitOr(),
                                    value=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='resource_id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='calendar', ctx=Store()),
                                    Name(id='calendar_resources', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='mapped_resources', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='day_total', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='calendar', ctx=Load()),
                                            attr='_get_resources_day_total',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='from_datetime', ctx=Load()),
                                            Name(id='to_datetime', ctx=Load()),
                                            Name(id='calendar_resources', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='attendances', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='calendar', ctx=Load()),
                                            attr='_attendance_intervals_batch',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='from_datetime', ctx=Load()),
                                            Name(id='to_datetime', ctx=Load()),
                                            Name(id='calendar_resources', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='leaves', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='calendar', ctx=Load()),
                                            attr='_leave_intervals_batch',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='from_datetime', ctx=Load()),
                                            Name(id='to_datetime', ctx=Load()),
                                            Name(id='calendar_resources', ctx=Load()),
                                            Name(id='domain', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='calendar_resource', ctx=Store()),
                                    iter=Name(id='calendar_resources', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='calendar_resource', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='calendar', ctx=Load()),
                                                    attr='_get_days_data',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Subscript(
                                                            value=Name(id='attendances', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='calendar_resource', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        op=BitAnd(),
                                                        right=Subscript(
                                                            value=Name(id='leaves', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='calendar_resource', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='day_total', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='calendar_resource', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=DictComp(
                                key=Subscript(
                                    value=Name(id='mapped_employees', ctx=Load()),
                                    slice=Attribute(
                                        value=Name(id='r', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    ctx=Load(),
                                ),
                                value=Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Attribute(
                                        value=Name(id='r', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Name(id='resources', ctx=Load()),
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
                FunctionDef(
                    name='_adjust_to_calendar',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='start', annotation=None, type_comment=None),
                            arg(arg='end', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='resource_results', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='resource_id',
                                        ctx=Load(),
                                    ),
                                    attr='_adjust_to_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='start', ctx=Load()),
                                    Name(id='end', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=DictComp(
                                key=Name(id='record', ctx=Load()),
                                value=Subscript(
                                    value=Name(id='resource_results', ctx=Load()),
                                    slice=Attribute(
                                        value=Name(id='record', ctx=Load()),
                                        attr='resource_id',
                                        ctx=Load(),
                                    ),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='record', ctx=Store()),
                                        iter=Name(id='self', ctx=Load()),
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
                FunctionDef(
                    name='list_work_time_per_day',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='from_datetime', annotation=None, type_comment=None),
                            arg(arg='to_datetime', annotation=None, type_comment=None),
                            arg(arg='calendar', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
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
                        Expr(
                            value=Constant(value="\n            By default the resource calendar is used, but it can be\n            changed using the `calendar` argument.\n\n            `domain` is used in order to recognise the leaves to take,\n            None means default value ('time_type', '=', 'leave')\n\n            Returns a list of tuples (day, hours) for each day\n            containing at least an attendance.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='resource', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='resource_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='calendar', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='resource_calendar_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='from_datetime', ctx=Load()),
                                    attr='tzinfo',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='from_datetime', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='from_datetime', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Name(id='utc', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='to_datetime', ctx=Load()),
                                    attr='tzinfo',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='to_datetime', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='to_datetime', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Name(id='utc', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='intervals', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='calendar', ctx=Load()),
                                        attr='_work_intervals_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='from_datetime', ctx=Load()),
                                        Name(id='to_datetime', ctx=Load()),
                                        Name(id='resource', ctx=Load()),
                                        Name(id='domain', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='float', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='start', ctx=Store()),
                                    Name(id='stop', ctx=Store()),
                                    Name(id='meta', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='intervals', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Call(
                                            func=Attribute(
                                                value=Name(id='start', ctx=Load()),
                                                attr='date',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=BinOp(
                                                    left=Name(id='stop', ctx=Load()),
                                                    op=Sub(),
                                                    right=Name(id='start', ctx=Load()),
                                                ),
                                                attr='total_seconds',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Div(),
                                        right=Constant(value=3600, kind=None),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
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
                    name='list_leaves',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='from_datetime', annotation=None, type_comment=None),
                            arg(arg='to_datetime', annotation=None, type_comment=None),
                            arg(arg='calendar', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
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
                        Expr(
                            value=Constant(value="\n            By default the resource calendar is used, but it can be\n            changed using the `calendar` argument.\n\n            `domain` is used in order to recognise the leaves to take,\n            None means default value ('time_type', '=', 'leave')\n\n            Returns a list of tuples (day, hours, resource.calendar.leaves)\n            for each leave in the calendar.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='resource', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='resource_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='calendar', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='calendar', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='resource_calendar_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='from_datetime', ctx=Load()),
                                    attr='tzinfo',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='from_datetime', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='from_datetime', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Name(id='utc', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='to_datetime', ctx=Load()),
                                    attr='tzinfo',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='to_datetime', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='to_datetime', ctx=Load()),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tzinfo',
                                                value=Name(id='utc', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='attendances', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='calendar', ctx=Load()),
                                        attr='_attendance_intervals_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='from_datetime', ctx=Load()),
                                        Name(id='to_datetime', ctx=Load()),
                                        Name(id='resource', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='leaves', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='calendar', ctx=Load()),
                                        attr='_leave_intervals_batch',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='from_datetime', ctx=Load()),
                                        Name(id='to_datetime', ctx=Load()),
                                        Name(id='resource', ctx=Load()),
                                        Name(id='domain', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='resource', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='start', ctx=Store()),
                                    Name(id='stop', ctx=Store()),
                                    Name(id='leave', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=BinOp(
                                left=Name(id='leaves', ctx=Load()),
                                op=BitAnd(),
                                right=Name(id='attendances', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='hours', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=BinOp(
                                                    left=Name(id='stop', ctx=Load()),
                                                    op=Sub(),
                                                    right=Name(id='start', ctx=Load()),
                                                ),
                                                attr='total_seconds',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Div(),
                                        right=Constant(value=3600, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='start', ctx=Load()),
                                                            attr='date',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Name(id='hours', ctx=Load()),
                                                    Name(id='leave', ctx=Load()),
                                                ],
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
                        Return(
                            value=Name(id='result', ctx=Load()),
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
