Module(
    body=[
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestResourceCommon',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_define_calendar',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='attendances', annotation=None, type_comment=None),
                            arg(arg='tz', annotation=None, type_comment=None),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='tz', kind=None),
                                            Constant(value='attendance_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='name', ctx=Load()),
                                            Name(id='tz', ctx=Load()),
                                            ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='hour_from', kind=None),
                                                                Constant(value='hour_to', kind=None),
                                                                Constant(value='dayofweek', kind=None),
                                                            ],
                                                            values=[
                                                                BinOp(
                                                                    left=Constant(value='%s_%d', kind=None),
                                                                    op=Mod(),
                                                                    right=Tuple(
                                                                        elts=[
                                                                            Name(id='name', ctx=Load()),
                                                                            Name(id='index', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='att', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='att', ctx=Load()),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Name(id='att', ctx=Load()),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='index', ctx=Store()),
                                                                Name(id='att', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Name(id='enumerate', ctx=Load()),
                                                            args=[Name(id='attendances', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
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
                    name='_define_calendar_2_weeks',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='attendances', annotation=None, type_comment=None),
                            arg(arg='tz', annotation=None, type_comment=None),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.calendar', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='tz', kind=None),
                                            Constant(value='two_weeks_calendar', kind=None),
                                            Constant(value='attendance_ids', kind=None),
                                        ],
                                        values=[
                                            Name(id='name', ctx=Load()),
                                            Name(id='tz', ctx=Load()),
                                            Constant(value=True, kind=None),
                                            ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value=0, kind=None),
                                                        Dict(
                                                            keys=[
                                                                Constant(value='name', kind=None),
                                                                Constant(value='hour_from', kind=None),
                                                                Constant(value='hour_to', kind=None),
                                                                Constant(value='dayofweek', kind=None),
                                                                Constant(value='week_type', kind=None),
                                                                Constant(value='display_type', kind=None),
                                                                Constant(value='sequence', kind=None),
                                                            ],
                                                            values=[
                                                                BinOp(
                                                                    left=Constant(value='%s_%d', kind=None),
                                                                    op=Mod(),
                                                                    right=Tuple(
                                                                        elts=[
                                                                            Name(id='name', ctx=Load()),
                                                                            Name(id='index', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='att', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='att', ctx=Load()),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Call(
                                                                    func=Name(id='str', ctx=Load()),
                                                                    args=[
                                                                        Subscript(
                                                                            value=Name(id='att', ctx=Load()),
                                                                            slice=Constant(value=2, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='att', ctx=Load()),
                                                                    slice=Constant(value=3, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='att', ctx=Load()),
                                                                    slice=Constant(value=4, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                Subscript(
                                                                    value=Name(id='att', ctx=Load()),
                                                                    slice=Constant(value=5, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Tuple(
                                                            elts=[
                                                                Name(id='index', ctx=Store()),
                                                                Name(id='att', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                        iter=Call(
                                                            func=Name(id='enumerate', ctx=Load()),
                                                            args=[Name(id='attendances', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
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
                    name='setUp',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestResourceCommon', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='calendar_jean',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_define_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='40 Hours', kind=None),
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Constant(value=8, kind=None),
                                                Constant(value=16, kind=None),
                                                Name(id='i', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='i', ctx=Store()),
                                                iter=Call(
                                                    func=Name(id='range', ctx=Load()),
                                                    args=[Constant(value=5, kind=None)],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    Constant(value='Europe/Brussels', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='calendar_patel',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_define_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='38 Hours', kind=None),
                                    Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=9, kind=None),
                                                                Constant(value=12, kind=None),
                                                                Name(id='i', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=13, kind=None),
                                                                Constant(value=17, kind=None),
                                                                Name(id='i', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='i', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='range', ctx=Load()),
                                                            args=[Constant(value=5, kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            Tuple(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='Etc/GMT-6', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='calendar_john',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_define_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='8+12 Hours', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=8, kind=None),
                                                    Constant(value=16, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=8, kind=None),
                                                    Constant(value=13, kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=16, kind=None),
                                                    Constant(value=23, kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='America/Los_Angeles', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='calendar_jules',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_define_calendar_2_weeks',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Week 1: 30 Hours - Week 2: 16 Hours', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value='0', kind=None),
                                                    Constant(value='line_section', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=8, kind=None),
                                                    Constant(value=16, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value='0', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=9, kind=None),
                                                    Constant(value=17, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='0', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value='1', kind=None),
                                                    Constant(value='line_section', kind=None),
                                                    Constant(value=10, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=8, kind=None),
                                                    Constant(value=16, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value='1', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=11, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=7, kind=None),
                                                    Constant(value=15, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value='1', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=12, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=8, kind=None),
                                                    Constant(value=16, kind=None),
                                                    Constant(value=3, kind=None),
                                                    Constant(value='1', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=13, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=10, kind=None),
                                                    Constant(value=16, kind=None),
                                                    Constant(value=4, kind=None),
                                                    Constant(value='1', kind=None),
                                                    Constant(value=False, kind=None),
                                                    Constant(value=14, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='Europe/Brussels', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='calendar_paul',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_define_calendar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='Morning and evening shifts', kind=None),
                                    Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            ListComp(
                                                elt=Tuple(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=2, kind=None),
                                                                Constant(value=7, kind=None),
                                                                Name(id='i', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value=10, kind=None),
                                                                Constant(value=16, kind=None),
                                                                Name(id='i', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='i', ctx=Store()),
                                                        iter=Call(
                                                            func=Name(id='range', ctx=Load()),
                                                            args=[Constant(value=5, kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            Tuple(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='Brazil/DeNoronha', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='jean',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.test', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='resource_calendar_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Jean', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jean',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='patel',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.test', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='resource_calendar_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Patel', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_patel',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='john',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.test', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='resource_calendar_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='John', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_john',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='jules',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.test', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='resource_calendar_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Jules', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_jules',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='paul',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='resource.test', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='resource_calendar_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Paul', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='calendar_paul',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
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
