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
            names=[alias(name='ValidationError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='format_date', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='frozendict', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='psycopg2',
            names=[alias(name='sql', asname=None)],
            level=0,
        ),
        ClassDef(
            name='SequenceMixin',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Mechanism used to have an editable sequence number.\n\n    Be careful of how you use this regarding the prefixes. More info in the\n    docstring of _get_last_sequence.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='sequence.mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Automatic sequence', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sequence_field', ctx=Store())],
                    value=Constant(value='name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sequence_date_field', ctx=Store())],
                    value=Constant(value='date', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sequence_index', ctx=Store())],
                    value=Constant(value=False, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sequence_monthly_regex', ctx=Store())],
                    value=Constant(value='^(?P<prefix1>.*?)(?P<year>((?<=\\D)|(?<=^))((19|20|21)\\d{2}|(\\d{2}(?=\\D))))(?P<prefix2>\\D*?)(?P<month>(0[1-9]|1[0-2]))(?P<prefix3>\\D+?)(?P<seq>\\d*)(?P<suffix>\\D*?)$', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sequence_yearly_regex', ctx=Store())],
                    value=Constant(value='^(?P<prefix1>.*?)(?P<year>((?<=\\D)|(?<=^))((19|20|21)?\\d{2}))(?P<prefix2>\\D+?)(?P<seq>\\d*)(?P<suffix>\\D*?)$', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sequence_fixed_regex', ctx=Store())],
                    value=Constant(value='^(?P<prefix1>.*?)(?P<seq>\\d{0,9})(?P<suffix>\\D*?)$', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence_prefix', ctx=Store())],
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
                                value=Constant(value='_compute_split_sequence', kind=None),
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
                    targets=[Name(id='sequence_number', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_split_sequence', kind=None),
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_abstract',
                                            ctx=Load(),
                                        ),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_sequence_index',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='index_name', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_table',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Constant(value='_sequence_index', kind=None),
                                    ),
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
                                            Constant(value='SELECT indexname FROM pg_indexes WHERE indexname = %s', kind=None),
                                            Tuple(
                                                elts=[Name(id='index_name', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
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
                                                attr='fetchone',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
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
                                                    Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='sql', ctx=Load()),
                                                                    attr='SQL',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='\n                    CREATE INDEX {index_name} ON {table} ({sequence_index}, sequence_prefix desc, sequence_number desc, {field});\n                    CREATE INDEX {index2_name} ON {table} ({sequence_index}, id desc, sequence_prefix);\n                ', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='sequence_index',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='sql', ctx=Load()),
                                                                        attr='Identifier',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_sequence_index',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='index_name',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='sql', ctx=Load()),
                                                                        attr='Identifier',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Name(id='index_name', ctx=Load())],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='index2_name',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='sql', ctx=Load()),
                                                                        attr='Identifier',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        BinOp(
                                                                            left=Name(id='index_name', ctx=Load()),
                                                                            op=Add(),
                                                                            right=Constant(value='2', kind=None),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='table',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='sql', ctx=Load()),
                                                                        attr='Identifier',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_table',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='field',
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='sql', ctx=Load()),
                                                                        attr='Identifier',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='_sequence_field',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_constrains_date_sequence',
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
                            targets=[Name(id='constraint_date', ctx=Store())],
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
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
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
                                            Constant(value='sequence.mixin.constraint_start_date', kind=None),
                                            Constant(value='1970-01-01', kind=None),
                                        ],
                                        keywords=[],
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
                                Assign(
                                    targets=[Name(id='date', ctx=Store())],
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
                                        args=[
                                            Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='_sequence_date_field',
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
                                    targets=[Name(id='sequence', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='record', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_sequence_field',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='sequence', ctx=Load()),
                                            Name(id='date', ctx=Load()),
                                            Compare(
                                                left=Name(id='date', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Name(id='constraint_date', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='format_values', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='_get_sequence_format_param',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='sequence', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='format_values', ctx=Load()),
                                                                slice=Constant(value='year', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='format_values', ctx=Load()),
                                                                    slice=Constant(value='year', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Name(id='date', ctx=Load()),
                                                                            attr='year',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Mod(),
                                                                        right=BinOp(
                                                                            left=Constant(value=10, kind=None),
                                                                            op=Pow(),
                                                                            right=Call(
                                                                                func=Name(id='len', ctx=Load()),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Name(id='str', ctx=Load()),
                                                                                        args=[
                                                                                            Subscript(
                                                                                                value=Name(id='format_values', ctx=Load()),
                                                                                                slice=Constant(value='year', kind=None),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='format_values', ctx=Load()),
                                                                slice=Constant(value='month', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='format_values', ctx=Load()),
                                                                    slice=Constant(value='month', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotEq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='date', ctx=Load()),
                                                                        attr='month',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValidationError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value="The %(date_field)s (%(date)s) doesn't match the sequence number of the related %(model)s (%(sequence)s)\nYou will need to clear the %(model)s's %(sequence_field)s to proceed.\nIn doing so, you might want to resequence your entries in order to maintain a continuous date-based sequence.", kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='date',
                                                                        value=Call(
                                                                            func=Name(id='format_date', ctx=Load()),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                Name(id='date', ctx=Load()),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='sequence',
                                                                        value=Name(id='sequence', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='date_field',
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='record', ctx=Load()),
                                                                                        attr='_fields',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Attribute(
                                                                                        value=Name(id='record', ctx=Load()),
                                                                                        attr='_sequence_date_field',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='_description_string',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='sequence_field',
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Subscript(
                                                                                    value=Attribute(
                                                                                        value=Name(id='record', ctx=Load()),
                                                                                        attr='_fields',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    slice=Attribute(
                                                                                        value=Name(id='record', ctx=Load()),
                                                                                        attr='_sequence_field',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='_description_string',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='env',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='model',
                                                                        value=Attribute(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Subscript(
                                                                                        value=Attribute(
                                                                                            value=Name(id='self', ctx=Load()),
                                                                                            attr='env',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        slice=Constant(value='ir.model', kind=None),
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='_get',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='record', ctx=Load()),
                                                                                        attr='_name',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            attr='display_name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
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
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sequence_field',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sequence_date_field',
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
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_split_sequence',
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
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='sequence', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='_sequence_field',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='regex', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\?P<\\w+>', kind=None),
                                            Constant(value='?:', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='_sequence_fixed_regex',
                                                        ctx=Load(),
                                                    ),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='?P<seq>', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='matching', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='regex', ctx=Load()),
                                            Name(id='sequence', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='sequence_prefix',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='sequence', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Call(
                                                func=Attribute(
                                                    value=Name(id='matching', ctx=Load()),
                                                    attr='start',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=1, kind=None)],
                                                keywords=[],
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='sequence_number',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='matching', ctx=Load()),
                                                            attr='group',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value=1, kind=None)],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sequence_field',
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
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_deduce_sequence_number_reset',
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
                        Expr(
                            value=Constant(value='Detect if the used sequence resets yearly, montly or never.\n\n        :param name: the sequence that is used as a reference to detect the resetting\n            periodicity. Typically, it is the last before the one you want to give a\n            sequence.\n        ', kind=None),
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='regex', ctx=Store()),
                                    Name(id='ret_val', ctx=Store()),
                                    Name(id='requirements', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sequence_monthly_regex',
                                                ctx=Load(),
                                            ),
                                            Constant(value='month', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='seq', kind=None),
                                                    Constant(value='month', kind=None),
                                                    Constant(value='year', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sequence_yearly_regex',
                                                ctx=Load(),
                                            ),
                                            Constant(value='year', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='seq', kind=None),
                                                    Constant(value='year', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sequence_fixed_regex',
                                                ctx=Load(),
                                            ),
                                            Constant(value='never', kind=None),
                                            List(
                                                elts=[Constant(value='seq', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='match', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='regex', ctx=Load()),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='name', ctx=Load()),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='match', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='groupdict', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='match', ctx=Load()),
                                                    attr='groupdict',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='all', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Name(id='req', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[Name(id='groupdict', ctx=Load())],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='req', ctx=Store()),
                                                                iter=Name(id='requirements', ctx=Load()),
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
                                                    value=Name(id='ret_val', ctx=Load()),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='ValidationError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='The sequence regex should at least contain the seq grouping keys. For instance:\n^(?P<prefix1>.*?)(?P<seq>\\d*)(?P<suffix>\\D*?)$', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
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
                    name='_get_last_sequence_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='relaxed', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Get the sql domain to retreive the previous sequence number.\n\n        This function should be overriden by models inheriting from this mixin.\n\n        :param relaxed: see _get_last_sequence.\n\n        :returns: tuple(where_string, where_params): with\n            where_string: the entire SQL WHERE clause as a string.\n            where_params: a dictionary containing the parameters to substitute\n                at the execution of the query.\n        ', kind=None),
                        ),
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
                        Return(
                            value=Tuple(
                                elts=[
                                    Constant(value='', kind=None),
                                    Dict(keys=[], values=[]),
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
                    name='_get_starting_sequence',
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
                            value=Constant(value='Get a default sequence number.\n\n        This function should be overriden by models heriting from this mixin\n        This number will be incremented so you probably want to start the sequence at 0.\n\n        :return: string to use as the default sequence to increment\n        ', kind=None),
                        ),
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
                        Return(
                            value=Constant(value='00000000', kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_last_sequence',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='relaxed', annotation=None, type_comment=None),
                            arg(arg='with_prefix', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Retrieve the previous sequence.\n\n        This is done by taking the number with the greatest alphabetical value within\n        the domain of _get_last_sequence_domain. This means that the prefix has a\n        huge importance.\n        For instance, if you have INV/2019/0001 and INV/2019/0002, when you rename the\n        last one to FACT/2019/0001, one might expect the next number to be\n        FACT/2019/0002 but it will be INV/2019/0002 (again) because INV > FACT.\n        Therefore, changing the prefix might not be convenient during a period, and\n        would only work when the numbering makes a new start (domain returns by\n        _get_last_sequence_domain is [], i.e: a new year).\n\n        :param field_name: the field that contains the sequence.\n        :param relaxed: this should be set to True when a previous request didn't find\n            something without. This allows to find a pattern from a previous period, and\n            try to adapt it for the new period.\n        :param with_prefix: The sequence prefix to restrict the search on, if any.\n\n        :return: the string of the previous sequence or None if there wasn't any.\n        ", kind=None),
                        ),
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
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_sequence_field',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_fields',
                                                    ctx=Load(),
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_sequence_field',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='store',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s is not a stored field', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_sequence_field',
                                                        ctx=Load(),
                                                    ),
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
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='where_string', ctx=Store()),
                                        Name(id='param', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_last_sequence_domain',
                                    ctx=Load(),
                                ),
                                args=[Name(id='relaxed', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        attr='origin',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='where_string', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=' AND id != %(id)s ', kind=None),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='param', ctx=Load()),
                                            slice=Constant(value='id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                attr='origin',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='with_prefix', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='where_string', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value=' AND sequence_prefix = %(with_prefix)s ', kind=None),
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='param', ctx=Load()),
                                            slice=Constant(value='with_prefix', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='with_prefix', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='\n            UPDATE {table} SET write_date = write_date WHERE id = (\n                SELECT id FROM {table}\n                {where_string}\n                AND sequence_prefix = (SELECT sequence_prefix FROM {table} {where_string} ORDER BY id DESC LIMIT 1)\n                ORDER BY sequence_number DESC\n                LIMIT 1\n            )\n            RETURNING {field};\n        ', kind=None),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='table',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_table',
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='where_string',
                                        value=Name(id='where_string', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='field',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_sequence_field',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='flush',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sequence_field',
                                                ctx=Load(),
                                            ),
                                            Constant(value='sequence_number', kind=None),
                                            Constant(value='sequence_prefix', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                    Name(id='query', ctx=Load()),
                                    Name(id='param', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Subscript(
                                value=BoolOp(
                                    op=Or(),
                                    values=[
                                        Call(
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
                                                attr='fetchone',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        List(
                                            elts=[Constant(value=None, kind=None)],
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_sequence_format_param',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='previous', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Get the python format and format values for the sequence.\n\n        :param previous: the sequence we want to extract the format from\n        :return tuple(format, format_values):\n            format is the format string on which we should call .format()\n            format_values is the dict of values to format the `format` string\n            ``format.format(**format_values)`` should be equal to ``previous``\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sequence_number_reset', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_deduce_sequence_number_reset',
                                    ctx=Load(),
                                ),
                                args=[Name(id='previous', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='regex', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_sequence_fixed_regex',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='sequence_number_reset', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='year', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='regex', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_sequence_yearly_regex',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='sequence_number_reset', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='month', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='regex', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sequence_monthly_regex',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='format_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='match',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='regex', ctx=Load()),
                                            Name(id='previous', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='groupdict',
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
                                    value=Name(id='format_values', ctx=Load()),
                                    slice=Constant(value='seq_length', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='format_values', ctx=Load()),
                                        slice=Constant(value='seq', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='format_values', ctx=Load()),
                                    slice=Constant(value='year_length', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='format_values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='year', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='format_values', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='seq', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    Compare(
                                        left=Constant(value='prefix1', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='format_values', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Constant(value='suffix', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='format_values', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='format_values', ctx=Load()),
                                            slice=Constant(value='prefix1', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='format_values', ctx=Load()),
                                        slice=Constant(value='suffix', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='format_values', ctx=Load()),
                                            slice=Constant(value='suffix', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='field', ctx=Store()),
                            iter=Tuple(
                                elts=[
                                    Constant(value='seq', kind=None),
                                    Constant(value='year', kind=None),
                                    Constant(value='month', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='format_values', ctx=Load()),
                                            slice=Name(id='field', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='format_values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='field', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
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
                        Assign(
                            targets=[Name(id='placeholders', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='findall',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='(prefix\\d|seq|suffix\\d?|year|month)', kind=None),
                                    Name(id='regex', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='format', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    GeneratorExp(
                                        elt=IfExp(
                                            test=Compare(
                                                left=Name(id='s', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='seq', kind=None)],
                                            ),
                                            body=Constant(value='{seq:0{seq_length}d}', kind=None),
                                            orelse=IfExp(
                                                test=Compare(
                                                    left=Name(id='s', ctx=Load()),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='month', kind=None)],
                                                ),
                                                body=Constant(value='{month:02d}', kind=None),
                                                orelse=IfExp(
                                                    test=Compare(
                                                        left=Name(id='s', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='year', kind=None)],
                                                    ),
                                                    body=Constant(value='{year:0{year_length}d}', kind=None),
                                                    orelse=BinOp(
                                                        left=Constant(value='{%s}', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='s', ctx=Load()),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='s', ctx=Store()),
                                                iter=Name(id='placeholders', ctx=Load()),
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
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='format', ctx=Load()),
                                    Name(id='format_values', ctx=Load()),
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
                    name='_set_next_sequence',
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
                            value=Constant(value='Set the next sequence.\n\n        This method ensures that the field is set both in the ORM and in the database.\n        This is necessary because we use a database query to get the previous sequence,\n        and we need that query to always be executed on the latest data.\n\n        :param field_name: the field that contains the sequence.\n        ', kind=None),
                        ),
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
                        Assign(
                            targets=[Name(id='last_sequence', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_last_sequence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new', ctx=Store())],
                            value=UnaryOp(
                                op=Not(),
                                operand=Name(id='last_sequence', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='new', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='last_sequence', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_last_sequence',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='relaxed',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_starting_sequence',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='format', ctx=Store()),
                                        Name(id='format_values', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_sequence_format_param',
                                    ctx=Load(),
                                ),
                                args=[Name(id='last_sequence', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='new', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='format_values', ctx=Load()),
                                            slice=Constant(value='seq', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='format_values', ctx=Load()),
                                            slice=Constant(value='year', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Subscript(
                                                value=Name(id='self', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_sequence_date_field',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='year',
                                            ctx=Load(),
                                        ),
                                        op=Mod(),
                                        right=BinOp(
                                            left=Constant(value=10, kind=None),
                                            op=Pow(),
                                            right=Subscript(
                                                value=Name(id='format_values', ctx=Load()),
                                                slice=Constant(value='year_length', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='format_values', ctx=Load()),
                                            slice=Constant(value='month', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Name(id='self', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sequence_date_field',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        attr='month',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='format_values', ctx=Load()),
                                    slice=Constant(value='seq', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Subscript(
                                    value=Name(id='format_values', ctx=Load()),
                                    slice=Constant(value='seq', kind=None),
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='self', ctx=Load()),
                                    slice=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_sequence_field',
                                        ctx=Load(),
                                    ),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='format', ctx=Load()),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='format_values', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_split_sequence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_last_from_seq_chain',
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
                            value=Constant(value='Tells whether or not this element is the last one of the sequence chain.\n\n        :return: True if it is the last element of the chain.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='last_sequence', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_last_sequence',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='with_prefix',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sequence_prefix',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='last_sequence', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='seq_format', ctx=Store()),
                                        Name(id='seq_format_values', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_sequence_format_param',
                                    ctx=Load(),
                                ),
                                args=[Name(id='last_sequence', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Subscript(
                                value=Name(id='seq_format_values', ctx=Load()),
                                slice=Constant(value='seq', kind=None),
                                ctx=Store(),
                            ),
                            op=Add(),
                            value=Constant(value=1, kind=None),
                        ),
                        Return(
                            value=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='seq_format', ctx=Load()),
                                        attr='format',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg=None,
                                            value=Name(id='seq_format_values', ctx=Load()),
                                        ),
                                    ],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
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
                    name='_is_end_of_seq_chain',
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
                            value=Constant(value='Tells whether or not these elements are the last ones of the sequence chain.\n\n        :return: True if self are the last elements of the chain.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='batched', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Dict(
                                            keys=[
                                                Constant(value='last_rec', kind=None),
                                                Constant(value='seq_list', kind=None),
                                            ],
                                            values=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                List(elts=[], ctx=Load()),
                                            ],
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
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='format', ctx=Store()),
                                                Name(id='format_values', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_get_sequence_format_param',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='_sequence_field',
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
                                    targets=[Name(id='seq', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='format_values', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='seq', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='batch', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='batched', ctx=Load()),
                                        slice=Tuple(
                                            elts=[
                                                Name(id='format', ctx=Load()),
                                                Call(
                                                    func=Name(id='frozendict', ctx=Load()),
                                                    args=[Name(id='format_values', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='batch', ctx=Load()),
                                                slice=Constant(value='seq_list', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='seq', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Subscript(
                                                value=Name(id='batch', ctx=Load()),
                                                slice=Constant(value='last_rec', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sequence_number',
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='sequence_number',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='batch', ctx=Load()),
                                                    slice=Constant(value='last_rec', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='record', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='values', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='batched', ctx=Load()),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='seq_list', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='seq_list', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=Call(
                                                func=Name(id='max', ctx=Load()),
                                                args=[Name(id='seq_list', ctx=Load())],
                                                keywords=[],
                                            ),
                                            op=Sub(),
                                            right=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[Name(id='seq_list', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='seq_list', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='record', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='last_rec', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='_is_last_from_seq_chain',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value=False, kind=None),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
