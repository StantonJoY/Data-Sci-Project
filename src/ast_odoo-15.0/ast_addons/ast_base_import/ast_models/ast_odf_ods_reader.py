Module(
    body=[
        ImportFrom(
            module='odf',
            names=[alias(name='opendocument', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odf.table',
            names=[
                alias(name='Table', asname=None),
                alias(name='TableRow', asname=None),
                alias(name='TableCell', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odf.text',
            names=[alias(name='P', asname=None)],
            level=0,
        ),
        ClassDef(
            name='ODSReader',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='file', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='clonespannedcolumns', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='content', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='clonespannedcolumns',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='clonespannedcolumns', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='doc',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='opendocument', ctx=Load()),
                                            attr='load',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='file', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='clonespannedcolumns',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='clonespannedcolumns', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='doc',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='content', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='SHEETS',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='sheet', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='doc',
                                            ctx=Load(),
                                        ),
                                        attr='spreadsheet',
                                        ctx=Load(),
                                    ),
                                    attr='getElementsByType',
                                    ctx=Load(),
                                ),
                                args=[Name(id='Table', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='readSheet',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='sheet', ctx=Load())],
                                        keywords=[],
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
                FunctionDef(
                    name='readSheet',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='sheet', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sheet', ctx=Load()),
                                    attr='getAttribute',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='name', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rows', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sheet', ctx=Load()),
                                    attr='getElementsByType',
                                    ctx=Load(),
                                ),
                                args=[Name(id='TableRow', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='arrRows', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='row', ctx=Store()),
                            iter=Name(id='rows', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='arrCells', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='cells', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='row', ctx=Load()),
                                            attr='getElementsByType',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='TableCell', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='count', ctx=Store()),
                                            Name(id='cell', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Name(id='enumerate', ctx=Load()),
                                        args=[Name(id='cells', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='start',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='repeat', ctx=Store())],
                                            value=Constant(value=0, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='count', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='cells', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='repeat', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='cell', ctx=Load()),
                                                            attr='getAttribute',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='numbercolumnsrepeated', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='repeat', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='repeat', ctx=Store())],
                                                    value=Constant(value=1, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='spanned', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='cell', ctx=Load()),
                                                                            attr='getAttribute',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='numbercolumnsspanned', kind=None)],
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
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='clonespannedcolumns',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[IsNot()],
                                                                comparators=[Constant(value=None, kind=None)],
                                                            ),
                                                            Compare(
                                                                left=Name(id='spanned', ctx=Load()),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='repeat', ctx=Store())],
                                                            value=Name(id='spanned', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='ps', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='cell', ctx=Load()),
                                                    attr='getElementsByType',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='P', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='textContent', ctx=Store())],
                                            value=Constant(value='', kind='u'),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='p', ctx=Store()),
                                            iter=Name(id='ps', ctx=Load()),
                                            body=[
                                                For(
                                                    target=Name(id='n', ctx=Store()),
                                                    iter=Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='childNodes',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='n', ctx=Load()),
                                                                            attr='nodeType',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value=1, kind=None)],
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='n', ctx=Load()),
                                                                            attr='tagName',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='text:span', kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                For(
                                                                    target=Name(id='c', ctx=Store()),
                                                                    iter=Attribute(
                                                                        value=Name(id='n', ctx=Load()),
                                                                        attr='childNodes',
                                                                        ctx=Load(),
                                                                    ),
                                                                    body=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='c', ctx=Load()),
                                                                                    attr='nodeType',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value=3, kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='textContent', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Constant(value='{}{}', kind='u'),
                                                                                            attr='format',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Name(id='textContent', ctx=Load()),
                                                                                            Attribute(
                                                                                                value=Name(id='n', ctx=Load()),
                                                                                                attr='data',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
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
                                                            orelse=[],
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='n', ctx=Load()),
                                                                    attr='nodeType',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value=3, kind=None)],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='textContent', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Constant(value='{}{}', kind='u'),
                                                                            attr='format',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='textContent', ctx=Load()),
                                                                            Attribute(
                                                                                value=Name(id='n', ctx=Load()),
                                                                                attr='data',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
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
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='textContent', ctx=Load()),
                                            body=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='textContent', ctx=Load()),
                                                                attr='startswith',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='#', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    body=[
                                                        For(
                                                            target=Name(id='rr', ctx=Store()),
                                                            iter=Call(
                                                                func=Name(id='range', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='int', ctx=Load()),
                                                                        args=[Name(id='repeat', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='arrCells', ctx=Load()),
                                                                            attr='append',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='textContent', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                For(
                                                    target=Name(id='rr', ctx=Store()),
                                                    iter=Call(
                                                        func=Name(id='range', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[Name(id='repeat', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='arrCells', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='arrCells', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='arrRows', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='arrCells', ctx=Load())],
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
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SHEETS',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='name', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='arrRows', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='getSheet',
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
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='SHEETS',
                                    ctx=Load(),
                                ),
                                slice=Name(id='name', ctx=Load()),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='getFirstSheet',
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
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='iter', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='SHEETS',
                                                        ctx=Load(),
                                                    ),
                                                    attr='values',
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
