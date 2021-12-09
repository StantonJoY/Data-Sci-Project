Module(
    body=[
        ImportFrom(
            module='odoo.api',
            names=[alias(name='model', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='typing',
            names=[
                alias(name='Iterator', asname=None),
                alias(name='Mapping', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='abc', asname=None)],
            level=0,
        ),
        ClassDef(
            name='MicrosoftEvent',
            bases=[
                Attribute(
                    value=Name(id='abc', ctx=Load()),
                    attr='Set',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='This helper class holds the values of a Microsoft event.\n    Inspired by Odoo recordset, one instance can be a single Microsoft event or a\n    (immutable) set of Microsoft events.\n    All usual set operations are supported (union, intersection, etc).\n\n    :param iterable: iterable of MicrosoftCalendar instances or iterable of dictionnaries\n\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='iterable', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Tuple(elts=[], ctx=Load())],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_events',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='item', ctx=Store()),
                            iter=Name(id='iterable', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='item', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='__class__',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_events',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Attribute(
                                                        value=Name(id='item', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='item', ctx=Load()),
                                                    attr='_events',
                                                    ctx=Load(),
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='item', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
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
                                                    Name(id='item', ctx=Load()),
                                                    Name(id='Mapping', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_events',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Call(
                                                                func=Attribute(
                                                                    value=Name(id='item', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='id', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='item', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValueError', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Only %s or iterable of dict are supported', kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='__class__',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='__name__',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__iter__',
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
                            value=Call(
                                func=Name(id='iter', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='MicrosoftEvent', ctx=Load()),
                                            args=[
                                                List(
                                                    elts=[Name(id='vals', ctx=Load())],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='vals', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_events',
                                                            ctx=Load(),
                                                        ),
                                                        attr='values',
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
                        ),
                    ],
                    decorator_list=[],
                    returns=Subscript(
                        value=Name(id='Iterator', ctx=Load()),
                        slice=Constant(value='MicrosoftEvent', kind=None),
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__contains__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='microsoft_event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='microsoft_event', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_events',
                                        ctx=Load(),
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
                    name='__len__',
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
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_events',
                                        ctx=Load(),
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
                    name='__bool__',
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
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_events',
                                        ctx=Load(),
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
                    name='__getattr__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
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
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[Name(id='event', ctx=Store())],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_events',
                                                ctx=Load(),
                                            ),
                                            attr='keys',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValueError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='Expected singleton: %s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='self', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='event_id', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Name(id='list', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_events',
                                                    ctx=Load(),
                                                ),
                                                attr='keys',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_events',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='event_id', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='name', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__repr__',
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
                            value=BinOp(
                                left=Constant(value='%s%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='__class__',
                                                ctx=Load(),
                                            ),
                                            attr='__name__',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='ids',
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
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Attribute(
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
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='microsoft_ids',
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
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Attribute(
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
                    name='odoo_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
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
                                    attr='odoo_ids',
                                    ctx=Load(),
                                ),
                                args=[Name(id='env', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_odoo_id',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_meta_odoo_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='microsoft_guid', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Returns the Odoo id stored in the Microsoft Event metadata.\n        This id might not actually exists in the database.\n        ', kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='singleValueExtendedProperties',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='o_id', ctx=Store())],
                                    value=Subscript(
                                        value=ListComp(
                                            elt=Subscript(
                                                value=Name(id='prop', ctx=Load()),
                                                slice=Constant(value='value', kind=None),
                                                ctx=Load(),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='prop', ctx=Store()),
                                                    iter=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='singleValueExtendedProperties',
                                                        ctx=Load(),
                                                    ),
                                                    ifs=[
                                                        Compare(
                                                            left=Subscript(
                                                                value=Name(id='prop', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                BinOp(
                                                                    left=Constant(value='String {%s} Name odoo_id', kind=None),
                                                                    op=Mod(),
                                                                    right=Name(id='microsoft_guid', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='o_id', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='odoo_ids',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='ids', ctx=Store())],
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Attribute(
                                            value=Name(id='e', ctx=Load()),
                                            attr='_odoo_id',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='e', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='_odoo_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='ids', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='self', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='ids', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='found', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_load_odoo_ids_from_db',
                                    ctx=Load(),
                                ),
                                args=[Name(id='env', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='unsure', ctx=Store())],
                            value=BinOp(
                                left=Name(id='self', ctx=Load()),
                                op=Sub(),
                                right=Name(id='found', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='unsure', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='unsure', ctx=Load()),
                                            attr='_load_odoo_ids_from_metadata',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='env', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Attribute(
                                            value=Name(id='e', ctx=Load()),
                                            attr='_odoo_id',
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
                    name='_load_odoo_ids_from_metadata',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='model_env', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_model',
                                    ctx=Load(),
                                ),
                                args=[Name(id='env', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='microsoft_guid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='microsoft_calendar.microsoft_guid', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='unsure_odoo_ids', ctx=Store())],
                            value=Call(
                                func=Name(id='tuple', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='e', ctx=Load()),
                                                attr='_meta_odoo_id',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='microsoft_guid', ctx=Load())],
                                            keywords=[],
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='odoo_events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_env', ctx=Load()),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='_id', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='_id', ctx=Store()),
                                                iter=Name(id='unsure_odoo_ids', ctx=Load()),
                                                ifs=[Name(id='_id', ctx=Load())],
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
                            targets=[Name(id='o_ids', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='odoo_events', ctx=Load()),
                                                attr='exists',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='filtered',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='e', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='microsoft_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='e', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='odoo_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='e', ctx=Load()),
                                            attr='_meta_odoo_id',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='microsoft_guid', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='odoo_id', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='o_ids', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='_events',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='_odoo_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='odoo_id', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
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
                    name='_load_odoo_ids_from_db',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='model_env', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_model',
                                    ctx=Load(),
                                ),
                                args=[Name(id='env', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='odoo_events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='model_env', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='active_test',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='_from_microsoft_ids',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='with_env',
                                    ctx=Load(),
                                ),
                                args=[Name(id='env', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mapping', ctx=Store())],
                            value=DictComp(
                                key=Attribute(
                                    value=Name(id='e', ctx=Load()),
                                    attr='microsoft_id',
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
                                        iter=Name(id='odoo_events', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='existing_microsoft_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='odoo_events', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='microsoft_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='e', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='odoo_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mapping', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='e', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='odoo_id', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='_events',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='_odoo_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='odoo_id', ctx=Load()),
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filter',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='e', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Compare(
                                            left=Attribute(
                                                value=Name(id='e', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[Name(id='existing_microsoft_ids', ctx=Load())],
                                        ),
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
                    name='owner',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='singleValueExtendedProperties',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='microsoft_guid', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Constant(value='ir.config_parameter', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='microsoft_calendar.microsoft_guid', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='real_owner_id', ctx=Store())],
                                    value=Subscript(
                                        value=ListComp(
                                            elt=Subscript(
                                                value=Name(id='prop', ctx=Load()),
                                                slice=Constant(value='value', kind=None),
                                                ctx=Load(),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='prop', ctx=Store()),
                                                    iter=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='singleValueExtendedProperties',
                                                        ctx=Load(),
                                                    ),
                                                    ifs=[
                                                        Compare(
                                                            left=Subscript(
                                                                value=Name(id='prop', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                BinOp(
                                                                    left=Constant(value='String {%s} Name owner_odoo_id', kind=None),
                                                                    op=Mod(),
                                                                    right=Name(id='microsoft_guid', ctx=Load()),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='real_owner', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='real_owner_id', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Constant(value='res.users', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[Name(id='real_owner_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='real_owner_id', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='real_owner_id', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='real_owner', ctx=Load()),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='real_owner', ctx=Load()),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='isOrganizer',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Return(
                                            value=Attribute(
                                                value=Name(id='env', ctx=Load()),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='organizer',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='organizer',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='emailAddress', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='organizer',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='emailAddress', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='address', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Constant(value='res.users', kind=None),
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
                                                                            Constant(value='email', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='organizer',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='get',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='emailAddress', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    attr='get',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='address', kind=None)],
                                                                                keywords=[],
                                                                            ),
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
                                                ),
                                            ],
                                            orelse=[
                                                Return(
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Constant(value='res.users', kind=None),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='filter',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='func', annotation=None, type_comment=None),
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
                                func=Name(id='MicrosoftEvent', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='e', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='e', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[
                                                    Call(
                                                        func=Name(id='func', ctx=Load()),
                                                        args=[Name(id='e', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=Constant(value='MicrosoftEvent', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_recurrence',
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
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='seriesMaster', kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_recurrent',
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
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='seriesMasterId',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='is_recurrence',
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
                    name='is_recurrent_not_master',
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
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='seriesMasterId',
                                        ctx=Load(),
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
                    name='get_recurrence',
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
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='recurrence',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='pattern', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='recurrence',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='pattern', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='range', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='recurrence',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='range', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end_type_dict', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='endDate', kind=None),
                                    Constant(value='noEnd', kind=None),
                                    Constant(value='numbered', kind=None),
                                ],
                                values=[
                                    Constant(value='end_date', kind=None),
                                    Constant(value='forever', kind=None),
                                    Constant(value='count', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='type_dict', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='absoluteMonthly', kind=None),
                                    Constant(value='relativeMonthly', kind=None),
                                    Constant(value='absoluteYearly', kind=None),
                                    Constant(value='relativeYearly', kind=None),
                                ],
                                values=[
                                    Constant(value='monthly', kind=None),
                                    Constant(value='monthly', kind=None),
                                    Constant(value='yearly', kind=None),
                                    Constant(value='yearly', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='index_dict', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='first', kind=None),
                                    Constant(value='second', kind=None),
                                    Constant(value='third', kind=None),
                                    Constant(value='fourth', kind=None),
                                    Constant(value='last', kind=None),
                                ],
                                values=[
                                    Constant(value='1', kind=None),
                                    Constant(value='2', kind=None),
                                    Constant(value='3', kind=None),
                                    Constant(value='4', kind=None),
                                    Constant(value='-1', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rrule_type', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='type_dict', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='pattern', ctx=Load()),
                                        slice=Constant(value='type', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='pattern', ctx=Load()),
                                        slice=Constant(value='type', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='interval', ctx=Store())],
                            value=Subscript(
                                value=Name(id='pattern', ctx=Load()),
                                slice=Constant(value='interval', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='rrule_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='yearly', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='interval', ctx=Store()),
                                    op=Mult(),
                                    value=Constant(value=12, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='rrule_type', kind=None),
                                    Constant(value='end_type', kind=None),
                                    Constant(value='interval', kind=None),
                                    Constant(value='count', kind=None),
                                    Constant(value='day', kind=None),
                                    Constant(value='byday', kind=None),
                                    Constant(value='until', kind=None),
                                ],
                                values=[
                                    Name(id='rrule_type', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='end_type_dict', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='range', ctx=Load()),
                                                slice=Constant(value='type', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='interval', ctx=Load()),
                                    Subscript(
                                        value=Name(id='range', ctx=Load()),
                                        slice=Constant(value='numberOfOccurrences', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='pattern', ctx=Load()),
                                        slice=Constant(value='dayOfMonth', kind=None),
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='index_dict', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='pattern', ctx=Load()),
                                                slice=Constant(value='index', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='range', ctx=Load()),
                                                    slice=Constant(value='type', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='endDate', kind=None)],
                                            ),
                                            Subscript(
                                                value=Name(id='range', ctx=Load()),
                                                slice=Constant(value='endDate', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='month_by_dict', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='absoluteMonthly', kind=None),
                                    Constant(value='relativeMonthly', kind=None),
                                    Constant(value='absoluteYearly', kind=None),
                                    Constant(value='relativeYearly', kind=None),
                                ],
                                values=[
                                    Constant(value='date', kind=None),
                                    Constant(value='day', kind=None),
                                    Constant(value='date', kind=None),
                                    Constant(value='day', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='month_by', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='month_by_dict', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='pattern', ctx=Load()),
                                        slice=Constant(value='type', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='month_by', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='month_by', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='month_by', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='week_days', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='x', ctx=Load()),
                                    slice=Slice(
                                        lower=None,
                                        upper=Constant(value=3, kind=None),
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='x', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='pattern', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='daysOfWeek', kind=None),
                                                List(elts=[], ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='week_day', ctx=Store()),
                            iter=List(
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
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Name(id='week_day', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Compare(
                                        left=Name(id='week_day', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='week_days', ctx=Load())],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='week_days', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='weekday', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='week_days', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='upper',
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
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='is_cancelled',
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
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='isCancelled',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='__getattr__',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='@removed', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='__getattr__',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value='@removed', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='reason', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='deleted', kind=None)],
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
                    name='is_recurrence_outlier',
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
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='originalStartTime',
                                        ctx=Load(),
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
                    name='cancelled',
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filter',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='e', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Call(
                                            func=Attribute(
                                                value=Name(id='e', ctx=Load()),
                                                attr='is_cancelled',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
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
                    name='exists',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='recurrences', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filter',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='MicrosoftEvent', ctx=Load()),
                                        attr='is_recurrence',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=BinOp(
                                left=Name(id='self', ctx=Load()),
                                op=Sub(),
                                right=Name(id='recurrences', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='recurrences', ctx=Load()),
                                    attr='odoo_ids',
                                    ctx=Load(),
                                ),
                                args=[Name(id='env', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='events', ctx=Load()),
                                    attr='odoo_ids',
                                    ctx=Load(),
                                ),
                                args=[Name(id='env', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filter',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='e', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='e', ctx=Load()),
                                            attr='_odoo_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=Constant(value='MicrosoftEvent', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_model',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
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
                                func=Name(id='all', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Attribute(
                                                value=Name(id='e', ctx=Load()),
                                                attr='is_recurrence',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
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
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='calendar.recurrence', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='all', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=UnaryOp(
                                            op=Not(),
                                            operand=Call(
                                                func=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='is_recurrence',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
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
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='calendar.event', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='TypeError', ctx=Load()),
                                args=[Constant(value='Mixing Microsoft events and Microsoft recurrences', kind=None)],
                                keywords=[],
                            ),
                            cause=None,
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
