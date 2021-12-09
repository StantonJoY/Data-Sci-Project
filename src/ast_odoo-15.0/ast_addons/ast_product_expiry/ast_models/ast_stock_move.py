Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='StockMove',
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
                    value=Constant(value='stock.move', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='use_expiration_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Use Expiration Date', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.use_expiration_date', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_generate_serial_move_line_commands',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='lot_names', annotation=None, type_comment=None),
                            arg(arg='origin_move_line', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Override to add a default `expiration_date` into the move lines values.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='move_lines_commands', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_generate_serial_move_line_commands',
                                    ctx=Load(),
                                ),
                                args=[Name(id='lot_names', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='origin_move_line',
                                        value=Name(id='origin_move_line', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='product_id',
                                    ctx=Load(),
                                ),
                                attr='use_expiration_date',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='date', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='fields', ctx=Load()),
                                                    attr='Datetime',
                                                    ctx=Load(),
                                                ),
                                                attr='today',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='datetime', ctx=Load()),
                                                attr='timedelta',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='expiration_time',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='move_line_command', ctx=Store()),
                                    iter=Name(id='move_lines_commands', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='move_line_vals', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='move_line_command', ctx=Load()),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='move_line_vals', ctx=Load()),
                                                    slice=Constant(value='expiration_date', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='date', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='move_lines_commands', ctx=Load()),
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
