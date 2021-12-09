Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='modules', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Users',
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
                    value=Constant(value='res.users', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[Constant(value='res.users', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='systray_get_activities',
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
                            value=Constant(value=' Update the systray icon of res.partner activities to use the\n        contact application one instead of base icon. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='activities', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Users', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='systray_get_activities',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='activity', ctx=Store()),
                            iter=Name(id='activities', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='activity', ctx=Load()),
                                            slice=Constant(value='model', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='res.partner', kind=None)],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='activity', ctx=Load()),
                                            slice=Constant(value='icon', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='modules', ctx=Load()),
                                                attr='module',
                                                ctx=Load(),
                                            ),
                                            attr='get_module_icon',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='contacts', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='activities', ctx=Load()),
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
    ],
    type_ignores=[],
)
