Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='HrEmployee',
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
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='hr.employee', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Employee', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='generate_work_entries',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='date_start', annotation=None, type_comment=None),
                            arg(arg='date_stop', annotation=None, type_comment=None),
                            arg(arg='force', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='date_start', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='to_date',
                                    ctx=Load(),
                                ),
                                args=[Name(id='date_start', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_stop', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='to_date',
                                    ctx=Load(),
                                ),
                                args=[Name(id='date_stop', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='current_contracts', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_contracts',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='date_start', ctx=Load()),
                                            Name(id='date_stop', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='states',
                                                value=List(
                                                    elts=[
                                                        Constant(value='open', kind=None),
                                                        Constant(value='close', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='current_contracts', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_all_contracts',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='date_start', ctx=Load()),
                                            Name(id='date_stop', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='states',
                                                value=List(
                                                    elts=[
                                                        Constant(value='open', kind=None),
                                                        Constant(value='close', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='current_contracts', ctx=Load()),
                                            attr='_generate_work_entries',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='date_start', ctx=Load()),
                                            Name(id='date_stop', ctx=Load()),
                                            Name(id='force', ctx=Load()),
                                        ],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
