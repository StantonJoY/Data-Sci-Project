Module(
    body=[
        ImportFrom(
            module='collections',
            names=[alias(name='deque', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='io', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='http', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='content_disposition', asname=None),
                alias(name='request', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='ustr', asname=None),
                alias(name='osutil', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='xlsxwriter', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TableExporter',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='check_xlsxwriter',
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
                                left=Name(id='xlsxwriter', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web/pivot/check_xlsxwriter', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='none', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='export_xlsx',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='jdata', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[Name(id='data', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='output', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='io', ctx=Load()),
                                    attr='BytesIO',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='workbook', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='xlsxwriter', ctx=Load()),
                                    attr='Workbook',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='output', ctx=Load()),
                                    Dict(
                                        keys=[Constant(value='in_memory', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='worksheet', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='workbook', ctx=Load()),
                                    attr='add_worksheet',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='jdata', ctx=Load()),
                                        slice=Constant(value='title', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='header_bold', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='workbook', ctx=Load()),
                                    attr='add_format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='bold', kind=None),
                                            Constant(value='pattern', kind=None),
                                            Constant(value='bg_color', kind=None),
                                        ],
                                        values=[
                                            Constant(value=True, kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value='#AAAAAA', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='header_plain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='workbook', ctx=Load()),
                                    attr='add_format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='pattern', kind=None),
                                            Constant(value='bg_color', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Constant(value='#AAAAAA', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bold', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='workbook', ctx=Load()),
                                    attr='add_format',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='bold', kind=None)],
                                        values=[Constant(value=True, kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='measure_count', ctx=Store())],
                            value=Subscript(
                                value=Name(id='jdata', ctx=Load()),
                                slice=Constant(value='measure_count', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='origin_count', ctx=Store())],
                            value=Subscript(
                                value=Name(id='jdata', ctx=Load()),
                                slice=Constant(value='origin_count', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='col_group_headers', ctx=Store())],
                            value=Subscript(
                                value=Name(id='jdata', ctx=Load()),
                                slice=Constant(value='col_group_headers', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='x', ctx=Store()),
                                        Name(id='y', ctx=Store()),
                                        Name(id='carry', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Constant(value=1, kind=None),
                                    Constant(value=0, kind=None),
                                    Call(
                                        func=Name(id='deque', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='i', ctx=Store()),
                                    Name(id='header_row', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='col_group_headers', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='worksheet', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='i', ctx=Load()),
                                            Constant(value=0, kind=None),
                                            Constant(value='', kind=None),
                                            Name(id='header_plain', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='header', ctx=Store()),
                                    iter=Name(id='header_row', ctx=Load()),
                                    body=[
                                        While(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='carry', ctx=Load()),
                                                    Compare(
                                                        left=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='carry', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='x', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='x', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='cell', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='carry', ctx=Load()),
                                                            attr='popleft',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='j', ctx=Store()),
                                                    iter=Call(
                                                        func=Name(id='range', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Name(id='measure_count', ctx=Load()),
                                                                op=Mult(),
                                                                right=BinOp(
                                                                    left=BinOp(
                                                                        left=Constant(value=2, kind=None),
                                                                        op=Mult(),
                                                                        right=Name(id='origin_count', ctx=Load()),
                                                                    ),
                                                                    op=Sub(),
                                                                    right=Constant(value=1, kind=None),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='worksheet', ctx=Load()),
                                                                    attr='write',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='y', ctx=Load()),
                                                                    BinOp(
                                                                        left=Name(id='x', ctx=Load()),
                                                                        op=Add(),
                                                                        right=Name(id='j', ctx=Load()),
                                                                    ),
                                                                    Constant(value='', kind=None),
                                                                    Name(id='header_plain', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Subscript(
                                                            value=Name(id='cell', ctx=Load()),
                                                            slice=Constant(value='height', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=1, kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='carry', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='x', kind=None),
                                                                            Constant(value='height', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Name(id='x', ctx=Load()),
                                                                            BinOp(
                                                                                left=Subscript(
                                                                                    value=Name(id='cell', ctx=Load()),
                                                                                    slice=Constant(value='height', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                                op=Sub(),
                                                                                right=Constant(value=1, kind=None),
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
                                                Assign(
                                                    targets=[Name(id='x', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='x', ctx=Load()),
                                                        op=Add(),
                                                        right=BinOp(
                                                            left=Name(id='measure_count', ctx=Load()),
                                                            op=Mult(),
                                                            right=BinOp(
                                                                left=BinOp(
                                                                    left=Constant(value=2, kind=None),
                                                                    op=Mult(),
                                                                    right=Name(id='origin_count', ctx=Load()),
                                                                ),
                                                                op=Sub(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        For(
                                            target=Name(id='j', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='range', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='header', ctx=Load()),
                                                        slice=Constant(value='width', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='worksheet', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='y', ctx=Load()),
                                                            BinOp(
                                                                left=Name(id='x', ctx=Load()),
                                                                op=Add(),
                                                                right=Name(id='j', ctx=Load()),
                                                            ),
                                                            IfExp(
                                                                test=Compare(
                                                                    left=Name(id='j', ctx=Load()),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value=0, kind=None)],
                                                                ),
                                                                body=Subscript(
                                                                    value=Name(id='header', ctx=Load()),
                                                                    slice=Constant(value='title', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                orelse=Constant(value='', kind=None),
                                                            ),
                                                            Name(id='header_plain', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='header', ctx=Load()),
                                                    slice=Constant(value='height', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='carry', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='x', kind=None),
                                                                    Constant(value='height', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='x', ctx=Load()),
                                                                    BinOp(
                                                                        left=Subscript(
                                                                            value=Name(id='header', ctx=Load()),
                                                                            slice=Constant(value='height', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Sub(),
                                                                        right=Constant(value=1, kind=None),
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
                                        Assign(
                                            targets=[Name(id='x', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='x', ctx=Load()),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='header', ctx=Load()),
                                                    slice=Constant(value='width', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                While(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='carry', ctx=Load()),
                                            Compare(
                                                left=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='carry', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='x', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='x', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='cell', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='carry', ctx=Load()),
                                                    attr='popleft',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='j', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='range', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Name(id='measure_count', ctx=Load()),
                                                        op=Mult(),
                                                        right=BinOp(
                                                            left=BinOp(
                                                                left=Constant(value=2, kind=None),
                                                                op=Mult(),
                                                                right=Name(id='origin_count', ctx=Load()),
                                                            ),
                                                            op=Sub(),
                                                            right=Constant(value=1, kind=None),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='worksheet', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='y', ctx=Load()),
                                                            BinOp(
                                                                left=Name(id='x', ctx=Load()),
                                                                op=Add(),
                                                                right=Name(id='j', ctx=Load()),
                                                            ),
                                                            Constant(value='', kind=None),
                                                            Name(id='header_plain', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Subscript(
                                                    value=Name(id='cell', ctx=Load()),
                                                    slice=Constant(value='height', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='carry', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='x', kind=None),
                                                                    Constant(value='height', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='x', ctx=Load()),
                                                                    BinOp(
                                                                        left=Subscript(
                                                                            value=Name(id='cell', ctx=Load()),
                                                                            slice=Constant(value='height', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Sub(),
                                                                        right=Constant(value=1, kind=None),
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
                                        Assign(
                                            targets=[Name(id='x', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='x', ctx=Load()),
                                                op=Add(),
                                                right=BinOp(
                                                    left=Name(id='measure_count', ctx=Load()),
                                                    op=Mult(),
                                                    right=BinOp(
                                                        left=BinOp(
                                                            left=Constant(value=2, kind=None),
                                                            op=Mult(),
                                                            right=Name(id='origin_count', ctx=Load()),
                                                        ),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                ),
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
                                                Name(id='x', ctx=Store()),
                                                Name(id='y', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            BinOp(
                                                left=Name(id='y', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='measure_headers', ctx=Store())],
                            value=Subscript(
                                value=Name(id='jdata', ctx=Load()),
                                slice=Constant(value='measure_headers', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='measure_headers', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='worksheet', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='y', ctx=Load()),
                                            Constant(value=0, kind=None),
                                            Constant(value='', kind=None),
                                            Name(id='header_plain', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='measure', ctx=Store()),
                                    iter=Name(id='measure_headers', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='style', ctx=Store())],
                                            value=IfExp(
                                                test=Subscript(
                                                    value=Name(id='measure', ctx=Load()),
                                                    slice=Constant(value='is_bold', kind=None),
                                                    ctx=Load(),
                                                ),
                                                body=Name(id='header_bold', ctx=Load()),
                                                orelse=Name(id='header_plain', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='worksheet', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='y', ctx=Load()),
                                                    Name(id='x', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='measure', ctx=Load()),
                                                        slice=Constant(value='title', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='style', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        For(
                                            target=Name(id='i', ctx=Store()),
                                            iter=Call(
                                                func=Name(id='range', ctx=Load()),
                                                args=[
                                                    Constant(value=1, kind=None),
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Constant(value=2, kind=None),
                                                            op=Mult(),
                                                            right=Name(id='origin_count', ctx=Load()),
                                                        ),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='worksheet', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='y', ctx=Load()),
                                                            BinOp(
                                                                left=Name(id='x', ctx=Load()),
                                                                op=Add(),
                                                                right=Name(id='i', ctx=Load()),
                                                            ),
                                                            Constant(value='', kind=None),
                                                            Name(id='header_plain', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='x', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='x', ctx=Load()),
                                                op=Add(),
                                                right=BinOp(
                                                    left=BinOp(
                                                        left=Constant(value=2, kind=None),
                                                        op=Mult(),
                                                        right=Name(id='origin_count', ctx=Load()),
                                                    ),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='x', ctx=Store()),
                                                Name(id='y', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            BinOp(
                                                left=Name(id='y', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='worksheet', ctx=Load()),
                                            attr='set_column',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=0, kind=None),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='measure_headers', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value=16, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='origin_headers', ctx=Store())],
                            value=Subscript(
                                value=Name(id='jdata', ctx=Load()),
                                slice=Constant(value='origin_headers', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='origin_headers', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='worksheet', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='y', ctx=Load()),
                                            Constant(value=0, kind=None),
                                            Constant(value='', kind=None),
                                            Name(id='header_plain', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='origin', ctx=Store()),
                                    iter=Name(id='origin_headers', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='style', ctx=Store())],
                                            value=IfExp(
                                                test=Subscript(
                                                    value=Name(id='origin', ctx=Load()),
                                                    slice=Constant(value='is_bold', kind=None),
                                                    ctx=Load(),
                                                ),
                                                body=Name(id='header_bold', ctx=Load()),
                                                orelse=Name(id='header_plain', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='worksheet', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='y', ctx=Load()),
                                                    Name(id='x', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='origin', ctx=Load()),
                                                        slice=Constant(value='title', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='style', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='x', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='x', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='y', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='y', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='x', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Subscript(
                                value=Name(id='jdata', ctx=Load()),
                                slice=Constant(value='rows', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='worksheet', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='y', ctx=Load()),
                                            Name(id='x', ctx=Load()),
                                            BinOp(
                                                left=BinOp(
                                                    left=Subscript(
                                                        value=Name(id='row', ctx=Load()),
                                                        slice=Constant(value='indent', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    op=Mult(),
                                                    right=Constant(value='     ', kind=None),
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='ustr', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='row', ctx=Load()),
                                                            slice=Constant(value='title', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            Name(id='header_plain', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='cell', ctx=Store()),
                                    iter=Subscript(
                                        value=Name(id='row', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='x', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='x', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='cell', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='is_bold', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='worksheet', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='y', ctx=Load()),
                                                            Name(id='x', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='cell', ctx=Load()),
                                                                slice=Constant(value='value', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='bold', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='worksheet', ctx=Load()),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='y', ctx=Load()),
                                                            Name(id='x', ctx=Load()),
                                                            Subscript(
                                                                value=Name(id='cell', ctx=Load()),
                                                                slice=Constant(value='value', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='x', ctx=Store()),
                                                Name(id='y', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Constant(value=0, kind=None),
                                            BinOp(
                                                left=Name(id='y', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='workbook', ctx=Load()),
                                    attr='close',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='xlsx_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='output', ctx=Load()),
                                    attr='getvalue',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='filename', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='osutil', ctx=Load()),
                                    attr='clean_filename',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Pivot %(title)s (%(model_name)s)', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='title',
                                                value=Subscript(
                                                    value=Name(id='jdata', ctx=Load()),
                                                    slice=Constant(value='title', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='model_name',
                                                value=Subscript(
                                                    value=Name(id='jdata', ctx=Load()),
                                                    slice=Constant(value='model', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[Name(id='xlsx_data', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='headers',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='Content-Type', kind=None),
                                                        Constant(value='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                Tuple(
                                                    elts=[
                                                        Constant(value='Content-Disposition', kind=None),
                                                        Call(
                                                            func=Name(id='content_disposition', ctx=Load()),
                                                            args=[
                                                                BinOp(
                                                                    left=Name(id='filename', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Constant(value='.xlsx', kind=None),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/web/pivot/export_xlsx', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
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
