Module(
    body=[
        Import(
            names=[alias(name='random', asname=None)],
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
            module='odoo.tools',
            names=[alias(name='pycompat', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='Random',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='seed', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a random number generator object with the given seed. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='r', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='random', ctx=Load()),
                            attr='Random',
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
                            value=Name(id='r', ctx=Load()),
                            attr='seed',
                            ctx=Load(),
                        ),
                        args=[Name(id='seed', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='version',
                                value=Constant(value=2, kind=None),
                            ),
                        ],
                    ),
                ),
                Return(
                    value=Name(id='r', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='format_str',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='val', annotation=None, type_comment=None),
                    arg(arg='counter', annotation=None, type_comment=None),
                    arg(arg='values', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Format the given value (with method ``format``) when it is a string. ', kind=None),
                ),
                If(
                    test=Call(
                        func=Name(id='isinstance', ctx=Load()),
                        args=[
                            Name(id='val', ctx=Load()),
                            Name(id='str', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='val', ctx=Load()),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='counter',
                                        value=Name(id='counter', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='values',
                                        value=Name(id='values', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='val', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='chain_factories',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='field_factories', annotation=None, type_comment=None),
                    arg(arg='model_name', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Instantiate a generator by calling all the field factories. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='generator', ctx=Store())],
                    value=Call(
                        func=Name(id='root_factory', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Tuple(
                        elts=[
                            Name(id='fname', ctx=Store()),
                            Name(id='field_factory', ctx=Store()),
                        ],
                        ctx=Store(),
                    ),
                    iter=Name(id='field_factories', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='generator', ctx=Store())],
                            value=Call(
                                func=Name(id='field_factory', ctx=Load()),
                                args=[
                                    Name(id='generator', ctx=Load()),
                                    Name(id='fname', ctx=Load()),
                                    Name(id='model_name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=Name(id='generator', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='root_factory',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value=' Return a generator with empty values dictionaries (except for the flag ``__complete``). ', kind=None),
                ),
                Expr(
                    value=Yield(
                        value=Dict(
                            keys=[Constant(value='__complete', kind=None)],
                            values=[Constant(value=False, kind=None)],
                        ),
                    ),
                ),
                While(
                    test=Constant(value=True, kind=None),
                    body=[
                        Expr(
                            value=Yield(
                                value=Dict(
                                    keys=[Constant(value='__complete', kind=None)],
                                    values=[Constant(value=True, kind=None)],
                                ),
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
            name='randomize',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='vals', annotation=None, type_comment=None),
                    arg(arg='weights', annotation=None, type_comment=None),
                    arg(arg='seed', annotation=None, type_comment=None),
                    arg(arg='formatter', annotation=None, type_comment=None),
                    arg(arg='counter_offset', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=False, kind=None),
                    Name(id='format_str', ctx=Load()),
                    Constant(value=0, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a factory for an iterator of values dicts with pseudo-randomly\n    chosen values (among ``vals``) for a field.\n\n    :param list vals: list in which a value will be chosen, depending on `weights`\n    :param list weights: list of probabilistic weights\n    :param seed: optional initialization of the random number generator\n    :param function formatter: (val, counter, values) --> formatted_value\n    :param int counter_offset:\n    :returns: function of the form (iterator, field_name, model_name) -> values\n    :rtype: function (iterator, str, str) -> dict\n    ', kind=None),
                ),
                FunctionDef(
                    name='generate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='iterator', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='model_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Name(id='Random', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s+field+%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='model_name', ctx=Load()),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='seed', ctx=Load()),
                                                        Name(id='field_name', ctx=Load()),
                                                    ],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='counter', ctx=Store()),
                                    Name(id='values', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='iterator', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='val', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='r', ctx=Load()),
                                                attr='choices',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='vals', ctx=Load()),
                                                Name(id='weights', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Name(id='field_name', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='formatter', ctx=Load()),
                                        args=[
                                            Name(id='val', ctx=Load()),
                                            BinOp(
                                                left=Name(id='counter', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='counter_offset', ctx=Load()),
                                            ),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Yield(
                                        value=Name(id='values', ctx=Load()),
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
                Return(
                    value=Name(id='generate', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='cartesian',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='vals', annotation=None, type_comment=None),
                    arg(arg='weights', annotation=None, type_comment=None),
                    arg(arg='seed', annotation=None, type_comment=None),
                    arg(arg='formatter', annotation=None, type_comment=None),
                    arg(arg='then', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=False, kind=None),
                    Name(id='format_str', ctx=Load()),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a factory for an iterator of values dicts that combines all ``vals`` for\n    the field with the other field values in input.\n\n    :param list vals: list in which a value will be chosen, depending on `weights`\n    :param list weights: list of probabilistic weights\n    :param seed: optional initialization of the random number generator\n    :param function formatter: (val, counter, values) --> formatted_value\n    :param function then: if defined, factory used when vals has been consumed.\n    :returns: function of the form (iterator, field_name, model_name) -> values\n    :rtype: function (iterator, str, str) -> dict\n    ', kind=None),
                ),
                FunctionDef(
                    name='generate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='iterator', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='model_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='counter', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='values', ctx=Store()),
                            iter=Name(id='iterator', ctx=Load()),
                            body=[
                                If(
                                    test=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='__complete', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='val', ctx=Store()),
                                    iter=Name(id='vals', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Yield(
                                                value=Dict(
                                                    keys=[
                                                        None,
                                                        Name(id='field_name', ctx=Load()),
                                                    ],
                                                    values=[
                                                        Name(id='values', ctx=Load()),
                                                        Call(
                                                            func=Name(id='formatter', ctx=Load()),
                                                            args=[
                                                                Name(id='val', ctx=Load()),
                                                                Name(id='counter', ctx=Load()),
                                                                Name(id='values', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='counter', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='factory', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='then', ctx=Load()),
                                    Call(
                                        func=Name(id='randomize', ctx=Load()),
                                        args=[
                                            Name(id='vals', ctx=Load()),
                                            Name(id='weights', ctx=Load()),
                                            Name(id='seed', ctx=Load()),
                                            Name(id='formatter', ctx=Load()),
                                            Name(id='counter', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=YieldFrom(
                                value=Call(
                                    func=Name(id='factory', ctx=Load()),
                                    args=[
                                        Name(id='iterator', ctx=Load()),
                                        Name(id='field_name', ctx=Load()),
                                        Name(id='model_name', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Name(id='generate', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='iterate',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='vals', annotation=None, type_comment=None),
                    arg(arg='weights', annotation=None, type_comment=None),
                    arg(arg='seed', annotation=None, type_comment=None),
                    arg(arg='formatter', annotation=None, type_comment=None),
                    arg(arg='then', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=False, kind=None),
                    Name(id='format_str', ctx=Load()),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a factory for an iterator of values dicts that picks a value among ``vals``\n    for each input.  Once all ``vals`` have been used once, resume as ``then`` or as a\n    ``randomize`` generator.\n\n    :param list vals: list in which a value will be chosen, depending on `weights`\n    :param list weights: list of probabilistic weights\n    :param seed: optional initialization of the random number generator\n    :param function formatter: (val, counter, values) --> formatted_value\n    :param function then: if defined, factory used when vals has been consumed.\n    :returns: function of the form (iterator, field_name, model_name) -> values\n    :rtype: function (iterator, str, str) -> dict\n    ', kind=None),
                ),
                FunctionDef(
                    name='generate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='iterator', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='model_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='counter', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='val', ctx=Store()),
                            iter=Name(id='vals', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='iterator', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Name(id='field_name', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='formatter', ctx=Load()),
                                        args=[
                                            Name(id='val', ctx=Load()),
                                            Name(id='counter', ctx=Load()),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='__complete', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Yield(
                                        value=Name(id='values', ctx=Load()),
                                    ),
                                ),
                                AugAssign(
                                    target=Name(id='counter', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='factory', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='then', ctx=Load()),
                                    Call(
                                        func=Name(id='randomize', ctx=Load()),
                                        args=[
                                            Name(id='vals', ctx=Load()),
                                            Name(id='weights', ctx=Load()),
                                            Name(id='seed', ctx=Load()),
                                            Name(id='formatter', ctx=Load()),
                                            Name(id='counter', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=YieldFrom(
                                value=Call(
                                    func=Name(id='factory', ctx=Load()),
                                    args=[
                                        Name(id='iterator', ctx=Load()),
                                        Name(id='field_name', ctx=Load()),
                                        Name(id='model_name', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Name(id='generate', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='constant',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='val', annotation=None, type_comment=None),
                    arg(arg='formatter', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Name(id='format_str', ctx=Load())],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a factory for an iterator of values dicts that sets the field\n    to the given value in each input dict.\n\n    :returns: function of the form (iterator, field_name, model_name) -> values\n    :rtype: function (iterator, str, str) -> dict\n    ', kind=None),
                ),
                FunctionDef(
                    name='generate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='iterator', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='_', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='counter', ctx=Store()),
                                    Name(id='values', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='iterator', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Name(id='field_name', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='formatter', ctx=Load()),
                                        args=[
                                            Name(id='val', ctx=Load()),
                                            Name(id='counter', ctx=Load()),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Yield(
                                        value=Name(id='values', ctx=Load()),
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
                Return(
                    value=Name(id='generate', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='compute',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='function', annotation=None, type_comment=None),
                    arg(arg='seed', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a factory for an iterator of values dicts that computes the field value\n    as ``function(values, counter, random)``, where ``values`` is the other field values,\n    ``counter`` is an integer, and ``random`` is a pseudo-random number generator.\n\n    :param function function: (values, counter, random) --> field_values\n    :param seed: optional initialization of the random number generator\n    :returns: function of the form (iterator, field_name, model_name) -> values\n    :rtype: function (iterator, str, str) -> dict\n    ', kind=None),
                ),
                FunctionDef(
                    name='generate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='iterator', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='model_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Name(id='Random', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Constant(value='%s+field+%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='model_name', ctx=Load()),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='seed', ctx=Load()),
                                                        Name(id='field_name', ctx=Load()),
                                                    ],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='counter', ctx=Store()),
                                    Name(id='values', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='iterator', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='val', ctx=Store())],
                                    value=Call(
                                        func=Name(id='function', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='values',
                                                value=Name(id='values', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='counter',
                                                value=Name(id='counter', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='random',
                                                value=Name(id='r', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Name(id='field_name', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='val', ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Yield(
                                        value=Name(id='values', ctx=Load()),
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
                Return(
                    value=Name(id='generate', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='randint',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='a', annotation=None, type_comment=None),
                    arg(arg='b', annotation=None, type_comment=None),
                    arg(arg='seed', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a factory for an iterator of values dicts that sets the field\n    to a random integer between a and b included in each input dict.\n\n    :param int a: minimal random value\n    :param int b: maximal random value\n    :returns: function of the form (iterator, field_name, model_name) -> values\n    :rtype: function (iterator, str, str) -> dict\n    ', kind=None),
                ),
                FunctionDef(
                    name='get_rand_int',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='random', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='random', ctx=Load()),
                                    attr='randint',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='a', ctx=Load()),
                                    Name(id='b', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='compute', ctx=Load()),
                        args=[Name(id='get_rand_int', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='seed',
                                value=Name(id='seed', ctx=Load()),
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
            name='randfloat',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='a', annotation=None, type_comment=None),
                    arg(arg='b', annotation=None, type_comment=None),
                    arg(arg='seed', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a factory for an iterator of values dicts that sets the field\n    to a random float between a and b included in each input dict.\n    ', kind=None),
                ),
                FunctionDef(
                    name='get_rand_float',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='random', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='random', ctx=Load()),
                                    attr='uniform',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='a', ctx=Load()),
                                    Name(id='b', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='compute', ctx=Load()),
                        args=[Name(id='get_rand_float', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='seed',
                                value=Name(id='seed', ctx=Load()),
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
            name='randdatetime',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=None,
                kwonlyargs=[
                    arg(arg='base_date', annotation=None, type_comment=None),
                    arg(arg='relative_before', annotation=None, type_comment=None),
                    arg(arg='relative_after', annotation=None, type_comment=None),
                    arg(arg='seed', annotation=None, type_comment=None),
                ],
                kw_defaults=[
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a factory for an iterator of values dicts that sets the field\n    to a random datetime between relative_before and relative_after, relatively to\n    base_date\n\n    :param base_date (datetime): override the default base date if needed.\n    :param relative_after (relativedelta, timedelta): range up which we can go after the\n         base date. If not set, defaults to 0, i.e. only in the past of reference.\n    :param relative_before (relativedelta, timedelta): range up which we can go before the\n         base date. If not set, defaults to 0, i.e. only in the future of reference.\n    :return (generator): iterator for random dates inside the defined range\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='base_date', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            Name(id='base_date', ctx=Load()),
                            Call(
                                func=Name(id='datetime', ctx=Load()),
                                args=[
                                    Constant(value=2020, kind=None),
                                    Constant(value=1, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                keywords=[],
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='seconds_before', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            BoolOp(
                                op=And(),
                                values=[
                                    Name(id='relative_before', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Name(id='base_date', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='relative_before', ctx=Load()),
                                                ),
                                                op=Sub(),
                                                right=Name(id='base_date', ctx=Load()),
                                            ),
                                            attr='total_seconds',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            Constant(value=0, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='seconds_after', ctx=Store())],
                    value=BoolOp(
                        op=Or(),
                        values=[
                            BoolOp(
                                op=And(),
                                values=[
                                    Name(id='relative_after', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Name(id='base_date', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='relative_after', ctx=Load()),
                                                ),
                                                op=Sub(),
                                                right=Name(id='base_date', ctx=Load()),
                                            ),
                                            attr='total_seconds',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            Constant(value=0, kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_rand_datetime',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='random', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=Name(id='base_date', ctx=Load()),
                                op=Add(),
                                right=Call(
                                    func=Name(id='relativedelta', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='seconds',
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='random', ctx=Load()),
                                                    attr='randint',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='seconds_before', ctx=Load()),
                                                    Name(id='seconds_after', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Name(id='compute', ctx=Load()),
                        args=[Name(id='get_rand_datetime', ctx=Load())],
                        keywords=[
                            keyword(
                                arg='seed',
                                value=Name(id='seed', ctx=Load()),
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
    type_ignores=[],
)
