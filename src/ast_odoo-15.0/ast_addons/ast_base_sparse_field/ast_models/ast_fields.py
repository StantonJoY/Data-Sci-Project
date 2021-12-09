Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='fields', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='monkey_patch',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='cls', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Return a method decorator to monkey-patch the given class. ', kind=None),
                ),
                FunctionDef(
                    name='decorate',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='func', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Attribute(
                                value=Name(id='func', ctx=Load()),
                                attr='__name__',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='func', ctx=Load()),
                                    attr='super',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='cls', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Name(id='setattr', ctx=Load()),
                                args=[
                                    Name(id='cls', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Name(id='func', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='func', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Name(id='decorate', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        AugAssign(
            target=Attribute(
                value=Attribute(
                    value=Name(id='fields', ctx=Load()),
                    attr='Field',
                    ctx=Load(),
                ),
                attr='__doc__',
                ctx=Store(),
            ),
            op=Add(),
            value=Constant(value='\n\n        .. _field-sparse:\n\n        .. rubric:: Sparse fields\n\n        Sparse fields have a very small probability of being not null. Therefore\n        many such fields can be serialized compactly into a common location, the\n        latter being a so-called "serialized" field.\n\n        :param sparse: the name of the field where the value of this field must\n            be stored.\n', kind=None),
        ),
        Assign(
            targets=[
                Attribute(
                    value=Attribute(
                        value=Name(id='fields', ctx=Load()),
                        attr='Field',
                        ctx=Load(),
                    ),
                    attr='sparse',
                    ctx=Store(),
                ),
            ],
            value=Constant(value=None, kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='_get_attrs',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='model_class', annotation=None, type_comment=None),
                    arg(arg='name', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='attrs', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='_get_attrs', ctx=Load()),
                            attr='super',
                            ctx=Load(),
                        ),
                        args=[
                            Name(id='self', ctx=Load()),
                            Name(id='model_class', ctx=Load()),
                            Name(id='name', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Call(
                        func=Attribute(
                            value=Name(id='attrs', ctx=Load()),
                            attr='get',
                            ctx=Load(),
                        ),
                        args=[Constant(value='sparse', kind=None)],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='attrs', ctx=Load()),
                                    slice=Constant(value='store', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='attrs', ctx=Load()),
                                    slice=Constant(value='copy', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attrs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='copy', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='attrs', ctx=Load()),
                                    slice=Constant(value='compute', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_compute_sparse',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='attrs', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='readonly', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='attrs', ctx=Load()),
                                            slice=Constant(value='inverse', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_inverse_sparse',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='attrs', ctx=Load()),
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='monkey_patch', ctx=Load()),
                    args=[
                        Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Field',
                            ctx=Load(),
                        ),
                    ],
                    keywords=[],
                ),
            ],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_compute_sparse',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='records', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                For(
                    target=Name(id='record', ctx=Store()),
                    iter=Name(id='records', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Subscript(
                                value=Name(id='record', ctx=Load()),
                                slice=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sparse',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='record', ctx=Load()),
                                    slice=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
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
                If(
                    test=Attribute(
                        value=Name(id='self', ctx=Load()),
                        attr='relational',
                        ctx=Load(),
                    ),
                    body=[
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='records', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='record', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='exists',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='monkey_patch', ctx=Load()),
                    args=[
                        Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Field',
                            ctx=Load(),
                        ),
                    ],
                    keywords=[],
                ),
            ],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_inverse_sparse',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='self', annotation=None, type_comment=None),
                    arg(arg='records', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                For(
                    target=Name(id='record', ctx=Store()),
                    iter=Name(id='records', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Subscript(
                                value=Name(id='record', ctx=Load()),
                                slice=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='sparse',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='convert_to_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='record', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Name(id='record', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='use_name_get',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='value', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='value', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='value', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='record', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='sparse',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='values', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='record', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='sparse',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='values', ctx=Load()),
                                            type_comment=None,
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
            ],
            decorator_list=[
                Call(
                    func=Name(id='monkey_patch', ctx=Load()),
                    args=[
                        Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Field',
                            ctx=Load(),
                        ),
                    ],
                    keywords=[],
                ),
            ],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='Serialized',
            bases=[
                Attribute(
                    value=Name(id='fields', ctx=Load()),
                    attr='Field',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Serialized fields provide the storage for sparse fields. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='type', ctx=Store())],
                    value=Constant(value='serialized', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='column_type', ctx=Store())],
                    value=Tuple(
                        elts=[
                            Constant(value='text', kind=None),
                            Constant(value='text', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='prefetch', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='convert_to_column',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='validate', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='convert_to_cache',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='value', ctx=Load()),
                                    Name(id='record', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='validate',
                                        value=Name(id='validate', ctx=Load()),
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
                    name='convert_to_cache',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='validate', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Return(
                            value=IfExp(
                                test=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='value', ctx=Load()),
                                        Name(id='dict', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Name(id='json', ctx=Load()),
                                        attr='dumps',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='value', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=BoolOp(
                                    op=Or(),
                                    values=[
                                        Name(id='value', ctx=Load()),
                                        Constant(value=None, kind=None),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='convert_to_record',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
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
                                    value=Name(id='json', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='value', ctx=Load()),
                                            Constant(value='{}', kind=None),
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
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='fields', ctx=Load()),
                    attr='Serialized',
                    ctx=Store(),
                ),
            ],
            value=Name(id='Serialized', ctx=Load()),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
