Module(
    body=[
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname='ElementTree')],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='Controller', asname=None),
                alias(name='route', asname=None),
                alias(name='request', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='Board',
            bases=[Name(id='Controller', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='add_to_dashboard',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='action_id', annotation=None, type_comment=None),
                            arg(arg='context_to_save', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='view_mode', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='', kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='board.open_board_my_dash_action', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='action', ctx=Load()),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='res_model', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='board.board', kind=None)],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='action', ctx=Load()),
                                                    slice=Constant(value='views', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='form', kind=None)],
                                    ),
                                    Name(id='action_id', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='view_id', ctx=Store())],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='action', ctx=Load()),
                                                slice=Constant(value='views', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='board', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='board.board', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='fields_view_get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='view_id', ctx=Load()),
                                            Constant(value='form', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='board', ctx=Load()),
                                            Compare(
                                                left=Constant(value='arch', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='board', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='xml', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='ElementTree', ctx=Load()),
                                                    attr='fromstring',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='board', ctx=Load()),
                                                        slice=Constant(value='arch', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='column', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='xml', ctx=Load()),
                                                    attr='find',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='./board/column', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='column', ctx=Load()),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='new_action', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ElementTree', ctx=Load()),
                                                            attr='Element',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='action', kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='string', kind=None),
                                                                    Constant(value='view_mode', kind=None),
                                                                    Constant(value='context', kind=None),
                                                                    Constant(value='domain', kind=None),
                                                                ],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[Name(id='action_id', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    Name(id='name', ctx=Load()),
                                                                    Name(id='view_mode', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[Name(id='context_to_save', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[Name(id='domain', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='column', ctx=Load()),
                                                            attr='insert',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value=0, kind=None),
                                                            Name(id='new_action', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='arch', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ElementTree', ctx=Load()),
                                                            attr='tostring',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='xml', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='encoding',
                                                                value=Constant(value='unicode', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.ui.view.custom', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='create',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='user_id', kind=None),
                                                                    Constant(value='ref_id', kind=None),
                                                                    Constant(value='arch', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='session',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='uid',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='view_id', ctx=Load()),
                                                                    Name(id='arch', ctx=Load()),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Return(
                                                    value=Constant(value=True, kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[Constant(value='/board/add_to_dashboard', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                            ],
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
