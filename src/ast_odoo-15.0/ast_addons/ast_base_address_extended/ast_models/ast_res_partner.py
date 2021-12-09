Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ClassDef(
            name='Partner',
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
                    value=List(
                        elts=[Constant(value='res.partner', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='street_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Street Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_street_data', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_inverse_street_data', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='street_number', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='House', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_street_data', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_inverse_street_data', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='street_number2', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Door', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_street_data', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_inverse_street_data', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_inverse_street_data',
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
                            value=Constant(value='Updates the street field.\n        Writes the `street` field on the partners when one of the sub-fields in STREET_FIELDS\n        has been touched', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='street_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_street_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='street_format', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='street_format',
                                                ctx=Load(),
                                            ),
                                            Constant(value='%(street_number)s/%(street_number2)s %(street_name)s', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='previous_field', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='previous_pos', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='street_value', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='separator', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='re_match', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='finditer',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='%\\(\\w+\\)s', kind=None),
                                            Name(id='street_format', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='field_name', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='re_match', ctx=Load()),
                                                        attr='group',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                slice=Slice(
                                                    lower=Constant(value=2, kind=None),
                                                    upper=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2, kind=None),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='field_pos', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re_match', ctx=Load()),
                                                    attr='start',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='field_name', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='street_fields', ctx=Load())],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='Unrecognized field %s in street format.', kind=None),
                                                                    Name(id='field_name', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='previous_field', ctx=Load()),
                                            ),
                                            body=[
                                                If(
                                                    test=Subscript(
                                                        value=Name(id='partner', ctx=Load()),
                                                        slice=Name(id='field_name', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='street_value', ctx=Store()),
                                                            op=Add(),
                                                            value=BinOp(
                                                                left=Subscript(
                                                                    value=Name(id='street_format', ctx=Load()),
                                                                    slice=Slice(
                                                                        lower=Constant(value=0, kind=None),
                                                                        upper=Name(id='field_pos', ctx=Load()),
                                                                        step=None,
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                op=Add(),
                                                                right=Subscript(
                                                                    value=Name(id='partner', ctx=Load()),
                                                                    slice=Name(id='field_name', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='separator', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='street_format', ctx=Load()),
                                                        slice=Slice(
                                                            lower=Name(id='previous_pos', ctx=Load()),
                                                            upper=Name(id='field_pos', ctx=Load()),
                                                            step=None,
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='street_value', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='partner', ctx=Load()),
                                                                slice=Name(id='field_name', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='street_value', ctx=Store()),
                                                            op=Add(),
                                                            value=Name(id='separator', ctx=Load()),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                If(
                                                    test=Subscript(
                                                        value=Name(id='partner', ctx=Load()),
                                                        slice=Name(id='field_name', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='street_value', ctx=Store()),
                                                            op=Add(),
                                                            value=Subscript(
                                                                value=Name(id='partner', ctx=Load()),
                                                                slice=Name(id='field_name', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                        Assign(
                                            targets=[Name(id='previous_field', ctx=Store())],
                                            value=Name(id='field_name', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='previous_pos', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re_match', ctx=Load()),
                                                    attr='end',
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
                                AugAssign(
                                    target=Name(id='street_value', ctx=Store()),
                                    op=Add(),
                                    value=Subscript(
                                        value=Name(id='street_format', ctx=Load()),
                                        slice=Slice(
                                            lower=Name(id='previous_pos', ctx=Load()),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='street',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='street_value', ctx=Load()),
                                    type_comment=None,
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
                    name='_compute_street_data',
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
                            value=Constant(value='Splits street value into sub-fields.\n        Recomputes the fields of STREET_FIELDS when `street` of a partner is updated', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='street_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_street_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='partner', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='street',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='field', ctx=Store()),
                                            iter=Name(id='street_fields', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='partner', ctx=Load()),
                                                            slice=Name(id='field', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=None, kind=None),
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
                                    targets=[Name(id='street_format', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='street_format',
                                                ctx=Load(),
                                            ),
                                            Constant(value='%(street_number)s/%(street_number2)s %(street_name)s', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='street_raw', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='street',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='vals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_split_street_with_params',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='street_raw', ctx=Load()),
                                            Name(id='street_format', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='k', ctx=Store()),
                                            Name(id='v', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='partner', ctx=Load()),
                                                    slice=Name(id='k', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='v', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='k', ctx=Store()),
                                    iter=BinOp(
                                        left=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[Name(id='street_fields', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[Name(id='vals', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='partner', ctx=Load()),
                                                    slice=Name(id='k', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=None, kind=None),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='street', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_split_street_with_params',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='street_raw', annotation=None, type_comment=None),
                            arg(arg='street_format', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='street_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_street_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vals', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='previous_pos', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='field_name', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='re_match', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='finditer',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='%\\(\\w+\\)s', kind=None),
                                    Name(id='street_format', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='field_pos', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re_match', ctx=Load()),
                                            attr='start',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='field_name', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='street_raw', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='street_raw', ctx=Load()),
                                                slice=Slice(
                                                    lower=Name(id='field_pos', ctx=Load()),
                                                    upper=None,
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='separator', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='street_format', ctx=Load()),
                                        slice=Slice(
                                            lower=Name(id='previous_pos', ctx=Load()),
                                            upper=Name(id='field_pos', ctx=Load()),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='field_value', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='separator', ctx=Load()),
                                            Name(id='field_name', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='tmp', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='street_raw', ctx=Load()),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='separator', ctx=Load()),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='previous_greedy', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='append_previous', ctx=Store()),
                                                                Name(id='sep', ctx=Store()),
                                                                Subscript(
                                                                    value=Name(id='tmp', ctx=Load()),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='tmp', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='rpartition',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=' ', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='street_raw', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='separator', ctx=Load()),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='tmp', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Name(id='previous_greedy', ctx=Load()),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=BinOp(
                                                        left=Name(id='sep', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='append_previous', ctx=Load()),
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='tmp', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=2, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='field_value', ctx=Store()),
                                                                Name(id='street_raw', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='tmp', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='vals', ctx=Load()),
                                                            slice=Name(id='field_name', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='field_value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='field_value', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='field_name', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='previous_greedy', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='field_name', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='street_name', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='separator', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=' ', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='previous_greedy', ctx=Store())],
                                                    value=Name(id='field_name', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='field_name', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='re_match', ctx=Load()),
                                                        attr='group',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                slice=Slice(
                                                    lower=Constant(value=2, kind=None),
                                                    upper=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=2, kind=None),
                                                    ),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[Pass()],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='field_name', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='street_fields', ctx=Load())],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='Unrecognized field %s in street format.', kind=None),
                                                            Name(id='field_name', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='previous_pos', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re_match', ctx=Load()),
                                            attr='end',
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
                        Assign(
                            targets=[Name(id='trailing_chars', ctx=Store())],
                            value=Subscript(
                                value=Name(id='street_format', ctx=Load()),
                                slice=Slice(
                                    lower=Name(id='previous_pos', ctx=Load()),
                                    upper=None,
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='trailing_chars', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='street_raw', ctx=Load()),
                                            attr='endswith',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='trailing_chars', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Name(id='field_name', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='street_raw', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='trailing_chars', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Name(id='field_name', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='street_raw', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Name(id='vals', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
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
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Partner', ctx=Load()),
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='country_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='street', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_inverse_street_data',
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
                FunctionDef(
                    name='_formatting_address_fields',
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
                            value=Constant(value='Returns the list of address fields usable to format addresses.', kind=None),
                        ),
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[
                                                Name(id='Partner', ctx=Load()),
                                                Name(id='self', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='_formatting_address_fields',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_street_fields',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_street_fields',
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
                            value=Constant(value='Returns the fields that can be used in a street format.\n        Overwrite this function if you want to add your own fields.', kind=None),
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='street_name', kind=None),
                                    Constant(value='street_number', kind=None),
                                    Constant(value='street_number2', kind=None),
                                ],
                                ctx=Load(),
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
