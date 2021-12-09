Module(
    body=[
        ImportFrom(
            module='datetime',
            names=[alias(name='datetime', asname=None)],
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
        ClassDef(
            name='MailTracking',
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
                    value=Constant(value='mail.tracking.value', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Mail Tracking Value', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='field', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='tracking_sequence asc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='field', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.model.fields', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='field_desc', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Field Description', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='field_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Field Type', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='field_groups', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_field_groups', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='old_value_integer', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Old Value Integer', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='old_value_float', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Old Value Float', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='old_value_monetary', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Old Value Monetary', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='old_value_char', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Old Value Char', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='old_value_text', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Old Value Text', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='old_value_datetime', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Old Value DateTime', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='new_value_integer', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='New Value Integer', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='new_value_float', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='New Value Float', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='new_value_monetary', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='New Value Monetary', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='new_value_char', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='New Value Char', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='new_value_text', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='New Value Text', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='new_value_datetime', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='New Value Datetime', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='currency_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.currency', kind=None),
                            Constant(value='Currency', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='set null', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Used to display the currency when tracking monetary values', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='mail_message_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='mail.message', kind=None),
                            Constant(value='Message ID', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tracking_sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Tracking field sequence', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=1, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=100, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_field_groups',
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
                            target=Name(id='tracking', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Attribute(
                                                value=Name(id='tracking', ctx=Load()),
                                                attr='mail_message_id',
                                                ctx=Load(),
                                            ),
                                            attr='model',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='field', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='tracking', ctx=Load()),
                                                    attr='field',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='tracking', ctx=Load()),
                                            attr='field_groups',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=IfExp(
                                        test=Name(id='field', ctx=Load()),
                                        body=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='groups',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value='base.group_system', kind=None),
                                    ),
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
                    name='create_tracking_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='initial_value', annotation=None, type_comment=None),
                            arg(arg='new_value', annotation=None, type_comment=None),
                            arg(arg='col_name', annotation=None, type_comment=None),
                            arg(arg='col_info', annotation=None, type_comment=None),
                            arg(arg='tracking_sequence', annotation=None, type_comment=None),
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
                            targets=[Name(id='tracked', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='field', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='model_name', ctx=Load()),
                                    Name(id='col_name', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='field', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='field', kind=None),
                                    Constant(value='field_desc', kind=None),
                                    Constant(value='field_type', kind=None),
                                    Constant(value='tracking_sequence', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='col_info', ctx=Load()),
                                        slice=Constant(value='string', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='col_info', ctx=Load()),
                                        slice=Constant(value='type', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='tracking_sequence', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='col_info', ctx=Load()),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='integer', kind=None),
                                            Constant(value='float', kind=None),
                                            Constant(value='char', kind=None),
                                            Constant(value='text', kind=None),
                                            Constant(value='datetime', kind=None),
                                            Constant(value='monetary', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    BinOp(
                                                        left=Constant(value='old_value_%s', kind=None),
                                                        op=Mod(),
                                                        right=Subscript(
                                                            value=Name(id='col_info', ctx=Load()),
                                                            slice=Constant(value='type', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='new_value_%s', kind=None),
                                                        op=Mod(),
                                                        right=Subscript(
                                                            value=Name(id='col_info', ctx=Load()),
                                                            slice=Constant(value='type', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                values=[
                                                    Name(id='initial_value', ctx=Load()),
                                                    Name(id='new_value', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='col_info', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='date', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='old_value_datetime', kind=None),
                                                            Constant(value='new_value_datetime', kind=None),
                                                        ],
                                                        values=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='initial_value', ctx=Load()),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='fields', ctx=Load()),
                                                                                        attr='Datetime',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='to_string',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='datetime', ctx=Load()),
                                                                                            attr='combine',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Call(
                                                                                                func=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='fields', ctx=Load()),
                                                                                                        attr='Date',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='from_string',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Name(id='initial_value', ctx=Load())],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            Call(
                                                                                                func=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='datetime', ctx=Load()),
                                                                                                        attr='min',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='time',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='new_value', ctx=Load()),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='fields', ctx=Load()),
                                                                                        attr='Datetime',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='to_string',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='datetime', ctx=Load()),
                                                                                            attr='combine',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Call(
                                                                                                func=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='fields', ctx=Load()),
                                                                                                        attr='Date',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='from_string',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Name(id='new_value', ctx=Load())],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            Call(
                                                                                                func=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='datetime', ctx=Load()),
                                                                                                        attr='min',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='time',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='col_info', ctx=Load()),
                                                    slice=Constant(value='type', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='boolean', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='update',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='old_value_integer', kind=None),
                                                                    Constant(value='new_value_integer', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='initial_value', ctx=Load()),
                                                                    Name(id='new_value', ctx=Load()),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='col_info', ctx=Load()),
                                                            slice=Constant(value='type', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='selection', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    attr='update',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='old_value_char', kind=None),
                                                                            Constant(value='new_value_char', kind=None),
                                                                        ],
                                                                        values=[
                                                                            BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Name(id='initial_value', ctx=Load()),
                                                                                            Subscript(
                                                                                                value=Call(
                                                                                                    func=Name(id='dict', ctx=Load()),
                                                                                                    args=[
                                                                                                        Subscript(
                                                                                                            value=Name(id='col_info', ctx=Load()),
                                                                                                            slice=Constant(value='selection', kind=None),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                                slice=Name(id='initial_value', ctx=Load()),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    Constant(value='', kind=None),
                                                                                ],
                                                                            ),
                                                                            BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Name(id='new_value', ctx=Load()),
                                                                                            Subscript(
                                                                                                value=Call(
                                                                                                    func=Name(id='dict', ctx=Load()),
                                                                                                    args=[
                                                                                                        Subscript(
                                                                                                            value=Name(id='col_info', ctx=Load()),
                                                                                                            slice=Constant(value='selection', kind=None),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                                slice=Name(id='new_value', ctx=Load()),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    Constant(value='', kind=None),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Subscript(
                                                                    value=Name(id='col_info', ctx=Load()),
                                                                    slice=Constant(value='type', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='many2one', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            attr='update',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Dict(
                                                                                keys=[
                                                                                    Constant(value='old_value_integer', kind=None),
                                                                                    Constant(value='new_value_integer', kind=None),
                                                                                    Constant(value='old_value_char', kind=None),
                                                                                    Constant(value='new_value_char', kind=None),
                                                                                ],
                                                                                values=[
                                                                                    BoolOp(
                                                                                        op=Or(),
                                                                                        values=[
                                                                                            BoolOp(
                                                                                                op=And(),
                                                                                                values=[
                                                                                                    Name(id='initial_value', ctx=Load()),
                                                                                                    Attribute(
                                                                                                        value=Name(id='initial_value', ctx=Load()),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            Constant(value=0, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    BoolOp(
                                                                                        op=Or(),
                                                                                        values=[
                                                                                            BoolOp(
                                                                                                op=And(),
                                                                                                values=[
                                                                                                    Name(id='new_value', ctx=Load()),
                                                                                                    Attribute(
                                                                                                        value=Name(id='new_value', ctx=Load()),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            Constant(value=0, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    BoolOp(
                                                                                        op=Or(),
                                                                                        values=[
                                                                                            BoolOp(
                                                                                                op=And(),
                                                                                                values=[
                                                                                                    Name(id='initial_value', ctx=Load()),
                                                                                                    Subscript(
                                                                                                        value=Subscript(
                                                                                                            value=Call(
                                                                                                                func=Attribute(
                                                                                                                    value=Call(
                                                                                                                        func=Attribute(
                                                                                                                            value=Name(id='initial_value', ctx=Load()),
                                                                                                                            attr='sudo',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        args=[],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                    attr='name_get',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                args=[],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                            slice=Constant(value=0, kind=None),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Constant(value=1, kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            Constant(value='', kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    BoolOp(
                                                                                        op=Or(),
                                                                                        values=[
                                                                                            BoolOp(
                                                                                                op=And(),
                                                                                                values=[
                                                                                                    Name(id='new_value', ctx=Load()),
                                                                                                    Subscript(
                                                                                                        value=Subscript(
                                                                                                            value=Call(
                                                                                                                func=Attribute(
                                                                                                                    value=Call(
                                                                                                                        func=Attribute(
                                                                                                                            value=Name(id='new_value', ctx=Load()),
                                                                                                                            attr='sudo',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        args=[],
                                                                                                                        keywords=[],
                                                                                                                    ),
                                                                                                                    attr='name_get',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                args=[],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                            slice=Constant(value=0, kind=None),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Constant(value=1, kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            Constant(value='', kind=None),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='tracked', ctx=Store())],
                                                                    value=Constant(value=False, kind=None),
                                                                    type_comment=None,
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
                        If(
                            test=Name(id='tracked', ctx=Load()),
                            body=[
                                Return(
                                    value=Name(id='values', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(keys=[], values=[]),
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
                    name='get_display_value',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='type', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assert(
                            test=Compare(
                                left=Name(id='type', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='new', kind=None),
                                            Constant(value='old', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='field_type',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='integer', kind=None),
                                                    Constant(value='float', kind=None),
                                                    Constant(value='char', kind=None),
                                                    Constant(value='text', kind=None),
                                                    Constant(value='monetary', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='getattr', ctx=Load()),
                                                        args=[
                                                            Name(id='record', ctx=Load()),
                                                            BinOp(
                                                                left=Constant(value='%s_value_%s', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='type', ctx=Load()),
                                                                        Attribute(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            attr='field_type',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='field_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='datetime', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Subscript(
                                                        value=Name(id='record', ctx=Load()),
                                                        slice=BinOp(
                                                            left=Constant(value='%s_value_datetime', kind=None),
                                                            op=Mod(),
                                                            right=Name(id='type', ctx=Load()),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='new_datetime', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='getattr', ctx=Load()),
                                                                args=[
                                                                    Name(id='record', ctx=Load()),
                                                                    BinOp(
                                                                        left=Constant(value='%s_value_datetime', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='type', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[],
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
                                                                    BinOp(
                                                                        left=Constant(value='%sZ', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='new_datetime', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='result', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        slice=BinOp(
                                                                            left=Constant(value='%s_value_datetime', kind=None),
                                                                            op=Mod(),
                                                                            right=Name(id='type', ctx=Load()),
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='field_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='date', kind=None)],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Subscript(
                                                                value=Name(id='record', ctx=Load()),
                                                                slice=BinOp(
                                                                    left=Constant(value='%s_value_datetime', kind=None),
                                                                    op=Mod(),
                                                                    right=Name(id='type', ctx=Load()),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='new_date', ctx=Store())],
                                                                    value=Subscript(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        slice=BinOp(
                                                                            left=Constant(value='%s_value_datetime', kind=None),
                                                                            op=Mod(),
                                                                            right=Name(id='type', ctx=Load()),
                                                                        ),
                                                                        ctx=Load(),
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
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='fields', ctx=Load()),
                                                                                        attr='Date',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='to_string',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='new_date', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='result', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='record', ctx=Load()),
                                                                                slice=BinOp(
                                                                                    left=Constant(value='%s_value_datetime', kind=None),
                                                                                    op=Mod(),
                                                                                    right=Name(id='type', ctx=Load()),
                                                                                ),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='record', ctx=Load()),
                                                                    attr='field_type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='boolean', kind=None)],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='result', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Name(id='bool', ctx=Load()),
                                                                                args=[
                                                                                    Subscript(
                                                                                        value=Name(id='record', ctx=Load()),
                                                                                        slice=BinOp(
                                                                                            left=Constant(value='%s_value_integer', kind=None),
                                                                                            op=Mod(),
                                                                                            right=Name(id='type', ctx=Load()),
                                                                                        ),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='result', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Subscript(
                                                                                value=Name(id='record', ctx=Load()),
                                                                                slice=BinOp(
                                                                                    left=Constant(value='%s_value_char', kind=None),
                                                                                    op=Mod(),
                                                                                    right=Name(id='type', ctx=Load()),
                                                                                ),
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
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
                FunctionDef(
                    name='get_old_display_value',
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
                                    attr='get_display_value',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='old', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_new_display_value',
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
                                    attr='get_display_value',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='new', kind=None)],
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
