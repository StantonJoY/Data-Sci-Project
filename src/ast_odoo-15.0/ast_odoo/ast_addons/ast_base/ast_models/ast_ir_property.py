Module(
    body=[
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
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='ormcache', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='TYPE2FIELD', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='char', kind=None),
                    Constant(value='float', kind=None),
                    Constant(value='boolean', kind=None),
                    Constant(value='integer', kind=None),
                    Constant(value='text', kind=None),
                    Constant(value='binary', kind=None),
                    Constant(value='many2one', kind=None),
                    Constant(value='date', kind=None),
                    Constant(value='datetime', kind=None),
                    Constant(value='selection', kind=None),
                ],
                values=[
                    Constant(value='value_text', kind=None),
                    Constant(value='value_float', kind=None),
                    Constant(value='value_integer', kind=None),
                    Constant(value='value_integer', kind=None),
                    Constant(value='value_text', kind=None),
                    Constant(value='value_binary', kind=None),
                    Constant(value='value_reference', kind=None),
                    Constant(value='value_datetime', kind=None),
                    Constant(value='value_datetime', kind=None),
                    Constant(value='value_text', kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TYPE2CLEAN', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='boolean', kind=None),
                    Constant(value='integer', kind=None),
                    Constant(value='float', kind=None),
                    Constant(value='char', kind=None),
                    Constant(value='text', kind=None),
                    Constant(value='selection', kind=None),
                    Constant(value='binary', kind=None),
                    Constant(value='date', kind=None),
                    Constant(value='datetime', kind=None),
                ],
                values=[
                    Name(id='bool', ctx=Load()),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='val', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=BoolOp(
                            op=Or(),
                            values=[
                                Name(id='val', ctx=Load()),
                                Constant(value=False, kind=None),
                            ],
                        ),
                    ),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='val', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=BoolOp(
                            op=Or(),
                            values=[
                                Name(id='val', ctx=Load()),
                                Constant(value=False, kind=None),
                            ],
                        ),
                    ),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='val', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=BoolOp(
                            op=Or(),
                            values=[
                                Name(id='val', ctx=Load()),
                                Constant(value=False, kind=None),
                            ],
                        ),
                    ),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='val', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=BoolOp(
                            op=Or(),
                            values=[
                                Name(id='val', ctx=Load()),
                                Constant(value=False, kind=None),
                            ],
                        ),
                    ),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='val', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=BoolOp(
                            op=Or(),
                            values=[
                                Name(id='val', ctx=Load()),
                                Constant(value=False, kind=None),
                            ],
                        ),
                    ),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='val', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=BoolOp(
                            op=Or(),
                            values=[
                                Name(id='val', ctx=Load()),
                                Constant(value=False, kind=None),
                            ],
                        ),
                    ),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='val', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=IfExp(
                            test=Name(id='val', ctx=Load()),
                            body=Call(
                                func=Attribute(
                                    value=Name(id='val', ctx=Load()),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            orelse=Constant(value=False, kind=None),
                        ),
                    ),
                    Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='val', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=BoolOp(
                            op=Or(),
                            values=[
                                Name(id='val', ctx=Load()),
                                Constant(value=False, kind=None),
                            ],
                        ),
                    ),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='Property',
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
                    value=Constant(value='ir.property', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Company Property', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Resource', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If not set, acts as a default value for new resources', kind=None),
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
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='fields_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.model.fields', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Field', kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
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
                    targets=[Name(id='value_float', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='value_integer', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='value_text', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='value_binary', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Binary',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='attachment',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='value_reference', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='value_datetime', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='type', ctx=Store())],
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
                                            Constant(value='char', kind=None),
                                            Constant(value='Char', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='float', kind=None),
                                            Constant(value='Float', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='boolean', kind=None),
                                            Constant(value='Boolean', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='integer', kind=None),
                                            Constant(value='Integer', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='text', kind=None),
                                            Constant(value='Text', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='binary', kind=None),
                                            Constant(value='Binary', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='many2one', kind=None),
                                            Constant(value='Many2One', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='date', kind=None),
                                            Constant(value='Date', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='datetime', kind=None),
                                            Constant(value='DateTime', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='selection', kind=None),
                                            Constant(value='Selection', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='many2one', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='init',
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
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value="\n            CREATE UNIQUE INDEX IF NOT EXISTS ir_property_unique_index\n            ON %s (fields_id, COALESCE(company_id, 0), COALESCE(res_id, ''))\n        ", kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='query', ctx=Load()),
                                        op=Mod(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_table',
                                            ctx=Load(),
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
                    name='_update_values',
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
                            test=Compare(
                                left=Constant(value='value', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='values', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Name(id='values', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='value', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='prop', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='type_', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='type', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='type_', ctx=Load()),
                            ),
                            body=[
                                If(
                                    test=Name(id='self', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='prop', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='self', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='type_', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='prop', ctx=Load()),
                                                attr='type',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='type_', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='type', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='default',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='self', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='field', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='TYPE2FIELD', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='type_', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='field', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Invalid type', kind=None)],
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
                            test=Compare(
                                left=Name(id='field', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='value_reference', kind=None)],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='value', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='value', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='models', ctx=Load()),
                                                        attr='BaseModel',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='value', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='%s,%d', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='value', ctx=Load()),
                                                                    attr='_name',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='value', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='value', ctx=Load()),
                                                            Name(id='int', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='field_id', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='fields_id', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='field_id', ctx=Load()),
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=UnaryOp(
                                                                        op=Not(),
                                                                        operand=Name(id='prop', ctx=Load()),
                                                                    ),
                                                                    body=[
                                                                        Raise(
                                                                            exc=Call(
                                                                                func=Name(id='ValueError', ctx=Load()),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                            cause=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='field_id', ctx=Store())],
                                                                    value=Attribute(
                                                                        value=Name(id='prop', ctx=Load()),
                                                                        attr='fields_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='field_id', ctx=Store())],
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
                                                                            attr='browse',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='field_id', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='value', ctx=Store())],
                                                            value=BinOp(
                                                                left=Constant(value='%s,%d', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='field_id', ctx=Load()),
                                                                                    attr='sudo',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                            attr='relation',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Name(id='value', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Name(id='field', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='value', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
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
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='default_set', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='SELECT EXISTS (SELECT 1 FROM ir_property WHERE id in %s AND res_id IS NULL)', kind=None),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='default_set', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='rowcount',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Call(
                                                                func=Attribute(
                                                                    value=Name(id='v', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='res_id', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            ops=[Is()],
                                                            comparators=[Constant(value=False, kind=None)],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='v', ctx=Store()),
                                                                iter=Name(id='values', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Property', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_update_values',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='default_set', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='clear_caches',
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
                            value=Name(id='r', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='vals_list', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_update_values',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='vals', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='vals', ctx=Store()),
                                        iter=Name(id='vals_list', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='created_default', ctx=Store())],
                            value=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=UnaryOp(
                                            op=Not(),
                                            operand=Call(
                                                func=Attribute(
                                                    value=Name(id='v', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='res_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='v', ctx=Store()),
                                                iter=Name(id='vals_list', ctx=Load()),
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
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Property', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='created_default', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='clear_caches',
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
                            value=Name(id='r', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
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
                            targets=[Name(id='default_deleted', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_ids',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='SELECT EXISTS (SELECT 1 FROM ir_property WHERE id in %s)', kind=None),
                                            List(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='default_deleted', ctx=Store())],
                                    value=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            attr='rowcount',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='default_deleted', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='clear_caches',
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
                            value=Name(id='r', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_by_record',
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
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='char', kind=None),
                                            Constant(value='text', kind=None),
                                            Constant(value='selection', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='value_text',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='float', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='value_float',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='boolean', kind=None)],
                                            ),
                                            body=[
                                                Return(
                                                    value=Call(
                                                        func=Name(id='bool', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='value_integer',
                                                                ctx=Load(),
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
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='integer', kind=None)],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='value_integer',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='type',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='binary', kind=None)],
                                                            ),
                                                            body=[
                                                                Return(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='value_binary',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='type',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='many2one', kind=None)],
                                                                    ),
                                                                    body=[
                                                                        If(
                                                                            test=UnaryOp(
                                                                                op=Not(),
                                                                                operand=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='value_reference',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            body=[
                                                                                Return(
                                                                                    value=Constant(value=False, kind=None),
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                        Assign(
                                                                            targets=[
                                                                                Tuple(
                                                                                    elts=[
                                                                                        Name(id='model', ctx=Store()),
                                                                                        Name(id='resource_id', ctx=Store()),
                                                                                    ],
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='value_reference',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='split',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value=',', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Return(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Subscript(
                                                                                                value=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='env',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                slice=Name(id='model', ctx=Load()),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='browse',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Call(
                                                                                                func=Name(id='int', ctx=Load()),
                                                                                                args=[Name(id='resource_id', ctx=Load())],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    attr='exists',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='type',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='datetime', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Return(
                                                                                    value=Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='value_datetime',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='type',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='date', kind=None)],
                                                                                    ),
                                                                                    body=[
                                                                                        If(
                                                                                            test=UnaryOp(
                                                                                                op=Not(),
                                                                                                operand=Attribute(
                                                                                                    value=Name(id='self', ctx=Load()),
                                                                                                    attr='value_datetime',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                            body=[
                                                                                                Return(
                                                                                                    value=Constant(value=False, kind=None),
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[],
                                                                                        ),
                                                                                        Return(
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='fields', ctx=Load()),
                                                                                                        attr='Date',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='to_string',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    Call(
                                                                                                        func=Attribute(
                                                                                                            value=Attribute(
                                                                                                                value=Name(id='fields', ctx=Load()),
                                                                                                                attr='Datetime',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='from_string',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[
                                                                                                            Attribute(
                                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                                attr='value_datetime',
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
                                                                                    orelse=[],
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
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_default',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                            arg(arg='company', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Set the given field's generic value for the given company.\n\n        :param name: the field's name\n        :param model: the field's model name\n        :param value: the field's value\n        :param company: the company (record or id)\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field_id', ctx=Store())],
                            value=Attribute(
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
                                        Name(id='model', ctx=Load()),
                                        Name(id='name', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_id', ctx=Store())],
                            value=IfExp(
                                test=Name(id='company', ctx=Load()),
                                body=Call(
                                    func=Name(id='int', ctx=Load()),
                                    args=[Name(id='company', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Constant(value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='prop', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='fields_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='field_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='company_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='prop', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='prop', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='value', kind=None)],
                                                values=[Name(id='value', ctx=Load())],
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
                                            value=Name(id='prop', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='fields_id', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='value', kind=None),
                                                    Constant(value='type', kind=None),
                                                ],
                                                values=[
                                                    Name(id='field_id', ctx=Load()),
                                                    Name(id='company_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Name(id='name', ctx=Load()),
                                                    Name(id='value', ctx=Load()),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Name(id='model', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_fields',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='name', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        attr='type',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
                    name='_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Get the given field\'s generic value for the record.\n\n        :param name: the field\'s name\n        :param model: the field\'s model name\n        :param res_id: optional resource, format: "<id>" (int) or\n                       "<model>,<id>" (str)\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='res_id', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='t', ctx=Store()),
                                                Name(id='v', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_default_property',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='name', ctx=Load()),
                                            Name(id='model', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='v', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Name(id='t', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='many2one', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='v', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Subscript(
                                                    value=Name(id='v', ctx=Load()),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='v', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='p', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_property',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='name', ctx=Load()),
                                    Name(id='model', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='res_id',
                                        value=Name(id='res_id', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='p', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='p', ctx=Load()),
                                            attr='get_by_record',
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
                            value=Constant(value=False, kind=None),
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
                Assign(
                    targets=[Name(id='COMPANY_KEY', ctx=Store())],
                    value=Constant(value='self.env.company.id', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_default_property',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='prop', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_property',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='name', ctx=Load()),
                                    Name(id='model', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='res_id',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='prop', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Constant(value=None, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='v', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='prop', ctx=Load()),
                                    attr='get_by_record',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='prop', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='many2one', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='prop', ctx=Load()),
                                                attr='type',
                                                ctx=Load(),
                                            ),
                                            Name(id='v', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value='many2one', kind=None),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='v', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='v', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='v', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='ormcache', ctx=Load()),
                            args=[
                                Name(id='COMPANY_KEY', ctx=Load()),
                                Constant(value='name', kind=None),
                                Constant(value='model', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_property',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_domain',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='name', ctx=Load()),
                                    Name(id='model', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='domain', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='res_id', ctx=Load()),
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='res_id', ctx=Load()),
                                                    Name(id='int', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='res_id', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%s,%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='model', ctx=Load()),
                                                        Name(id='res_id', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=BinOp(
                                        left=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='res_id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Name(id='res_id', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Name(id='domain', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='order',
                                                value=Constant(value='company_id', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Tuple(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='prop_name', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='field_id', ctx=Store())],
                            value=Attribute(
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
                                        Name(id='model', ctx=Load()),
                                        Name(id='prop_name', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='field_id', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='company_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='company',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='fields_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Name(id='field_id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='company_id', kind=None),
                                            Constant(value='in', kind=None),
                                            List(
                                                elts=[
                                                    Name(id='company_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_multi',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Read the property field `name` for the records of model `model` with\n            the given `ids`, and return a dictionary mapping `ids` to their\n            corresponding value.\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='ids', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='field', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='_fields',
                                    ctx=Load(),
                                ),
                                slice=Name(id='name', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='field_id', ctx=Store())],
                            value=Attribute(
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
                                        Name(id='model', ctx=Load()),
                                        Name(id='name', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='company',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='many2one', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='comodel', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='comodel_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='model_pos', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='model', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Constant(value=2, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='value_pos', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='comodel', ctx=Load()),
                                                    attr='_name',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Constant(value=2, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='query', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value='\n                SELECT substr(p.res_id, %s)::integer, r.id\n                FROM ir_property p\n                LEFT JOIN {} r ON substr(p.value_reference, %s)::integer=r.id\n                WHERE p.fields_id=%s\n                    AND (p.company_id=%s OR p.company_id IS NULL)\n                    AND (p.res_id IN %s OR p.res_id IS NULL)\n                ORDER BY p.company_id NULLS FIRST\n            ', kind=None),
                                            attr='format',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='comodel', ctx=Load()),
                                                attr='_table',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='params', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Name(id='model_pos', ctx=Load()),
                                            Name(id='value_pos', ctx=Load()),
                                            Name(id='field_id', ctx=Load()),
                                            Name(id='company_id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='clean', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='comodel', ctx=Load()),
                                        attr='browse',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='TYPE2FIELD', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='model_pos', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='model', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Constant(value=2, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='query', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Constant(value='\n                SELECT substr(p.res_id, %s)::integer, p.{}\n                FROM ir_property p\n                WHERE p.fields_id=%s\n                    AND (p.company_id=%s OR p.company_id IS NULL)\n                    AND (p.res_id IN %s OR p.res_id IS NULL)\n                ORDER BY p.company_id NULLS FIRST\n            ', kind=None),
                                                    attr='format',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='TYPE2FIELD', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='field', ctx=Load()),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='params', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Name(id='model_pos', ctx=Load()),
                                                    Name(id='field_id', ctx=Load()),
                                                    Name(id='company_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='clean', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='TYPE2CLEAN', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='dict', ctx=Load()),
                                                    attr='fromkeys',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='ids', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='cr', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='cr',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='refs', ctx=Store())],
                            value=SetComp(
                                elt=BinOp(
                                    left=Constant(value='%s,%s', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[
                                            Name(id='model', ctx=Load()),
                                            Name(id='id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='id', ctx=Store()),
                                        iter=Name(id='ids', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='sub_refs', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='split_for_in_conditions',
                                    ctx=Load(),
                                ),
                                args=[Name(id='refs', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cr', ctx=Load()),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='query', ctx=Load()),
                                            BinOp(
                                                left=Name(id='params', ctx=Load()),
                                                op=Add(),
                                                right=List(
                                                    elts=[Name(id='sub_refs', ctx=Load())],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='cr', ctx=Load()),
                                                    attr='fetchall',
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='default', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='result', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=None, kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=DictComp(
                                key=Name(id='id', ctx=Load()),
                                value=Call(
                                    func=Name(id='clean', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='result', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='id', ctx=Load()),
                                                Name(id='default', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='id', ctx=Store()),
                                        iter=Name(id='ids', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
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
                    name='_set_multi',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='default_value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Assign the property field `name` for the records of model `model`\n            with `values` (dictionary mapping record ids to their value).\n            If the value for a given record is the same as the default\n            value, the property entry will not be stored, to avoid bloating\n            the database.\n            If `default_value` is provided, that value will be used instead\n            of the computed default value, to determine whether the value\n            for a record should be stored or not.\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='clean',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='value', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Return(
                                    value=IfExp(
                                        test=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Name(id='value', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='models', ctx=Load()),
                                                    attr='BaseModel',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='value', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        orelse=Name(id='value', ctx=Load()),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='values', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='default_value', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_domain',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='name', ctx=Load()),
                                            Name(id='model', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='domain', ctx=Load()),
                                        ops=[Is()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='default_value', ctx=Store())],
                                    value=Call(
                                        func=Name(id='clean', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='name', ctx=Load()),
                                                    Name(id='model', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='field_id', ctx=Store())],
                            value=Attribute(
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
                                        Name(id='model', ctx=Load()),
                                        Name(id='name', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='company_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                    attr='company',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='refs', ctx=Store())],
                            value=DictComp(
                                key=BinOp(
                                    left=Constant(value='%s,%s', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[
                                            Name(id='model', ctx=Load()),
                                            Name(id='id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                value=Name(id='id', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='id', ctx=Store()),
                                        iter=Name(id='values', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='props', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='fields_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='field_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='company_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='res_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[Name(id='refs', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='prop', ctx=Store()),
                            iter=Name(id='props', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='refs', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='prop', ctx=Load()),
                                                attr='res_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Name(id='clean', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Name(id='id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='value', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(id='default_value', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='DELETE FROM ir_property WHERE id=%s', kind=None),
                                                    List(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='prop', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Call(
                                                        func=Name(id='clean', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='prop', ctx=Load()),
                                                                    attr='get_by_record',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='prop', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='value', kind=None)],
                                                                values=[Name(id='value', ctx=Load())],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
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
                        Assign(
                            targets=[Name(id='vals_list', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='ref', ctx=Store()),
                                    Name(id='id', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='refs', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Call(
                                        func=Name(id='clean', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Name(id='id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='value', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Name(id='default_value', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='vals_list', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='fields_id', kind=None),
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='res_id', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='value', kind=None),
                                                            Constant(value='type', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='field_id', ctx=Load()),
                                                            Name(id='company_id', ctx=Load()),
                                                            Name(id='ref', ctx=Load()),
                                                            Name(id='name', ctx=Load()),
                                                            Name(id='value', ctx=Load()),
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Name(id='model', ctx=Load()),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='_fields',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Name(id='name', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='type',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
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
                    name='search_multi',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return a domain for the records that match the given condition. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='default_matches', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='include_zero', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='field', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='_fields',
                                    ctx=Load(),
                                ),
                                slice=Name(id='name', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='many2one', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='comodel', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='field', ctx=Load()),
                                        attr='comodel_name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                FunctionDef(
                                    name='makeref',
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='value', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=[
                                        Return(
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='value', ctx=Load()),
                                                    BinOp(
                                                        left=Constant(value='%s,%s', kind=None),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Name(id='comodel', ctx=Load()),
                                                                Name(id='value', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='operator', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='=', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Call(
                                                func=Name(id='makeref', ctx=Load()),
                                                args=[Name(id='value', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='default_matches', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='operator', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='!=', kind=None),
                                                            Constant(value='<=', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='>', kind=None),
                                                            Constant(value='>=', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='value', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='makeref', ctx=Load()),
                                                        args=[Name(id='value', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='operator', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='in', kind=None),
                                                                    Constant(value='not in', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='value', ctx=Store())],
                                                            value=ListComp(
                                                                elt=Call(
                                                                    func=Name(id='makeref', ctx=Load()),
                                                                    args=[Name(id='v', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='v', ctx=Store()),
                                                                        iter=Name(id='value', ctx=Load()),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='operator', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='=like', kind=None),
                                                                            Constant(value='=ilike', kind=None),
                                                                            Constant(value='like', kind=None),
                                                                            Constant(value='not like', kind=None),
                                                                            Constant(value='ilike', kind=None),
                                                                            Constant(value='not ilike', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='target', ctx=Store())],
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Name(id='comodel', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='target_names', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='target', ctx=Load()),
                                                                            attr='name_search',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='value', ctx=Load())],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='operator',
                                                                                value=Name(id='operator', ctx=Load()),
                                                                            ),
                                                                            keyword(
                                                                                arg='limit',
                                                                                value=Constant(value=None, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='target_ids', ctx=Store())],
                                                                    value=ListComp(
                                                                        elt=Subscript(
                                                                            value=Name(id='n', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='n', ctx=Store()),
                                                                                iter=Name(id='target_names', ctx=Load()),
                                                                                ifs=[],
                                                                                is_async=0,
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Name(id='operator', ctx=Store()),
                                                                                Name(id='value', ctx=Store()),
                                                                            ],
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Tuple(
                                                                        elts=[
                                                                            Constant(value='in', kind=None),
                                                                            ListComp(
                                                                                elt=Call(
                                                                                    func=Name(id='makeref', ctx=Load()),
                                                                                    args=[Name(id='v', ctx=Load())],
                                                                                    keywords=[],
                                                                                ),
                                                                                generators=[
                                                                                    comprehension(
                                                                                        target=Name(id='v', ctx=Store()),
                                                                                        iter=Name(id='target_ids', ctx=Load()),
                                                                                        ifs=[],
                                                                                        is_async=0,
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
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
                                            value=Name(id='field', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='integer', kind=None),
                                                    Constant(value='float', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='value', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Name(id='operator', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='=', kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='operator', ctx=Store())],
                                                    value=Constant(value='!=', kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='include_zero', ctx=Store())],
                                                    value=Constant(value=True, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='value', ctx=Load()),
                                                                ops=[LtE()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Name(id='operator', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='>=', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='operator', ctx=Store())],
                                                            value=Constant(value='<', kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='include_zero', ctx=Store())],
                                                            value=Constant(value=True, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Name(id='value', ctx=Load()),
                                                                        ops=[Lt()],
                                                                        comparators=[Constant(value=0, kind=None)],
                                                                    ),
                                                                    Compare(
                                                                        left=Name(id='operator', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='>', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='operator', ctx=Store())],
                                                                    value=Constant(value='<=', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='include_zero', ctx=Store())],
                                                                    value=Constant(value=True, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Compare(
                                                                                left=Name(id='value', ctx=Load()),
                                                                                ops=[GtE()],
                                                                                comparators=[Constant(value=0, kind=None)],
                                                                            ),
                                                                            Compare(
                                                                                left=Name(id='operator', ctx=Load()),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='<=', kind=None)],
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='operator', ctx=Store())],
                                                                            value=Constant(value='>', kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='include_zero', ctx=Store())],
                                                                            value=Constant(value=True, kind=None),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Compare(
                                                                                        left=Name(id='value', ctx=Load()),
                                                                                        ops=[Gt()],
                                                                                        comparators=[Constant(value=0, kind=None)],
                                                                                    ),
                                                                                    Compare(
                                                                                        left=Name(id='operator', ctx=Load()),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='<', kind=None)],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='operator', ctx=Store())],
                                                                                    value=Constant(value='>=', kind=None),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='include_zero', ctx=Store())],
                                                                                    value=Constant(value=True, kind=None),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[],
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
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='boolean', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='value', ctx=Load()),
                                                            ),
                                                            Compare(
                                                                left=Name(id='operator', ctx=Load()),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value='=', kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='operator', ctx=Store())],
                                                            value=Constant(value='!=', kind=None),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='include_zero', ctx=Store())],
                                                            value=Constant(value=True, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='value', ctx=Load()),
                                                                    Compare(
                                                                        left=Name(id='operator', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='!=', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='operator', ctx=Store())],
                                                                    value=Constant(value='=', kind=None),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='include_zero', ctx=Store())],
                                                                    value=Constant(value=True, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_domain',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='name', ctx=Load()),
                                    Name(id='model', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='domain', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='Exception', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='props', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='domain', ctx=Load()),
                                        op=Add(),
                                        right=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Subscript(
                                                            value=Name(id='TYPE2FIELD', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='field', ctx=Load()),
                                                                attr='type',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='operator', ctx=Load()),
                                                        Name(id='value', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
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
                        Assign(
                            targets=[Name(id='good_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='prop', ctx=Store()),
                            iter=Name(id='props', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='prop', ctx=Load()),
                                        attr='res_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='res_model', ctx=Store()),
                                                        Name(id='res_id', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='prop', ctx=Load()),
                                                        attr='res_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='split',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=',', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='good_ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[Name(id='res_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='default_matches', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='include_zero', ctx=Load()),
                            body=[
                                Return(
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='not in', kind=None),
                                                    Name(id='good_ids', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='default_matches', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='all_ids', ctx=Store())],
                                            value=List(elts=[], ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='props', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='domain', ctx=Load()),
                                                        op=Add(),
                                                        right=List(
                                                            elts=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='res_id', kind=None),
                                                                        Constant(value='!=', kind=None),
                                                                        Constant(value=False, kind=None),
                                                                    ],
                                                                    ctx=Load(),
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
                                            target=Name(id='prop', ctx=Store()),
                                            iter=Name(id='props', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='res_model', ctx=Store()),
                                                                Name(id='res_id', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='prop', ctx=Load()),
                                                                attr='res_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='split',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=',', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='all_ids', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[Name(id='res_id', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='bad_ids', ctx=Store())],
                                            value=Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='set', ctx=Load()),
                                                            args=[Name(id='all_ids', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Call(
                                                            func=Name(id='set', ctx=Load()),
                                                            args=[Name(id='good_ids', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='not in', kind=None),
                                                            Name(id='bad_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='good_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
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
