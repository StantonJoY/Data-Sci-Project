Module(
    body=[
        Import(
            names=[alias(name='reprlib', asname=None)],
        ),
        Assign(
            targets=[Name(id='shortener', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='reprlib', ctx=Load()),
                    attr='Repr',
                    ctx=Load(),
                ),
                args=[],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='shortener', ctx=Load()),
                    attr='maxstring',
                    ctx=Store(),
                ),
            ],
            value=Constant(value=150, kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='shorten', ctx=Store())],
            value=Attribute(
                value=Name(id='shortener', ctx=Load()),
                attr='repr',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        ClassDef(
            name='Speedscope',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='init_stack_trace', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='Speedscope', kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='init_stack_trace',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='init_stack_trace', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='init_stack_trace_level',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='init_stack_trace',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='caller_frame',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='convert_stack',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='init_stack_trace',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='init_caller_frame',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='init_stack_trace',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='init_caller_frame',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='init_stack_trace',
                                            ctx=Load(),
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='profiles_raw',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='name',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='name', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='frames_indexes',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='frame_count',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='profiles',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                            arg(arg='profile', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='entry', ctx=Store()),
                            iter=Name(id='profile', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='caller_frame',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='init_caller_frame',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='convert_stack',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='entry', ctx=Load()),
                                                        slice=Constant(value='stack', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='query', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='entry', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='query', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='entry', ctx=Load()),
                                                slice=Constant(value='query', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='full_query', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='entry', ctx=Load()),
                                                slice=Constant(value='full_query', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='entry', ctx=Load()),
                                                        slice=Constant(value='stack', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            JoinedStr(
                                                                values=[
                                                                    Constant(value='sql(', kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='shorten', ctx=Load()),
                                                                            args=[Name(id='query', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value=')', kind=None),
                                                                ],
                                                            ),
                                                            Name(id='full_query', ctx=Load()),
                                                            Constant(value=None, kind=None),
                                                        ],
                                                        ctx=Load(),
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
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='profiles_raw',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='key', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='profile', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='convert_stack',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stack', annotation=None, type_comment=None),
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
                                    Name(id='index', ctx=Store()),
                                    Name(id='frame', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='stack', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='method', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='frame', ctx=Load()),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='line', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='number', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='caller_frame',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='caller_frame',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=4, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='line', ctx=Store())],
                                            value=JoinedStr(
                                                values=[
                                                    Constant(value='called at ', kind=None),
                                                    FormattedValue(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='caller_frame',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=' (', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='caller_frame',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=3, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='strip',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=')', kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='number', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='caller_frame',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=1, kind=None),
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
                                            value=Name(id='stack', ctx=Load()),
                                            slice=Name(id='index', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Name(id='method', ctx=Load()),
                                            Name(id='line', ctx=Load()),
                                            Name(id='number', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='caller_frame',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='frame', ctx=Load()),
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
                    name='add_output',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='names', annotation=None, type_comment=None),
                            arg(arg='complete', annotation=None, type_comment=None),
                            arg(arg='display_name', annotation=None, type_comment=None),
                            arg(arg='use_context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='params', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='entries', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='display_name', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='display_name', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Constant(value=',', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='names', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='name', ctx=Store()),
                            iter=Name(id='names', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='entries', ctx=Store()),
                                    op=Add(),
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='profiles_raw',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='entries', ctx=Load()),
                                    attr='sort',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='e', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Subscript(
                                                value=Name(id='e', ctx=Load()),
                                                slice=Constant(value='start', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='process',
                                    ctx=Load(),
                                ),
                                args=[Name(id='entries', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='use_context',
                                        value=Name(id='use_context', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='params', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='result', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='self', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='start', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='at', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='result', ctx=Load()),
                                    slice=UnaryOp(
                                        op=USub(),
                                        operand=Constant(value=1, kind=None),
                                    ),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='at', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='complete', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='start_stack', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='end_stack', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='init_stack_trace_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stack_to_ids',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='init_stack_trace',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='use_context', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='entries', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='exec_context', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='frame_id', ctx=Store()),
                                    iter=Name(id='init_stack_trace_ids', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='start_stack', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='frame', kind=None),
                                                            Constant(value='at', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='O', kind=None),
                                                            Name(id='frame_id', ctx=Load()),
                                                            Name(id='start', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='frame_id', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='reversed', ctx=Load()),
                                        args=[Name(id='init_stack_trace_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='end_stack', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='frame', kind=None),
                                                            Constant(value='at', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='C', kind=None),
                                                            Name(id='frame_id', ctx=Load()),
                                                            Name(id='end', ctx=Load()),
                                                        ],
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
                                    targets=[Name(id='result', ctx=Store())],
                                    value=BinOp(
                                        left=BinOp(
                                            left=Name(id='start_stack', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='result', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='end_stack', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='profiles',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='unit', kind=None),
                                            Constant(value='startValue', kind=None),
                                            Constant(value='endValue', kind=None),
                                            Constant(value='events', kind=None),
                                        ],
                                        values=[
                                            Name(id='display_name', ctx=Load()),
                                            Constant(value='evented', kind=None),
                                            Constant(value='seconds', kind=None),
                                            Constant(value=0, kind=None),
                                            BinOp(
                                                left=Name(id='end', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='start', ctx=Load()),
                                            ),
                                            Name(id='result', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='self', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='add_default',
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
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='profiles_raw',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='add_output',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='profiles_raw',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='display_name',
                                                value=Constant(value='Combined', kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='add_output',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='profiles_raw',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='display_name',
                                                value=Constant(value='Combined no context', kind=None),
                                            ),
                                            keyword(
                                                arg='use_context',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='profile', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='profiles_raw',
                                        ctx=Load(),
                                    ),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sql', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='profile', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='profile', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='query', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='sql', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='add_output',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Name(id='key', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='hide_gaps',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='display_name',
                                                        value=JoinedStr(
                                                            values=[
                                                                FormattedValue(
                                                                    value=Name(id='key', ctx=Load()),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                                Constant(value=' (no gap)', kind=None),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='add_output',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Name(id='key', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='continuous',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='complete',
                                                        value=Constant(value=False, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='display_name',
                                                        value=JoinedStr(
                                                            values=[
                                                                FormattedValue(
                                                                    value=Name(id='key', ctx=Load()),
                                                                    conversion=-1,
                                                                    format_spec=None,
                                                                ),
                                                                Constant(value=' (density)', kind=None),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='add_output',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[Name(id='key', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='display_name',
                                                        value=Name(id='key', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='self', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='make',
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
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='profiles',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='add_default',
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
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='activeProfileIndex', kind=None),
                                    Constant(value='$schema', kind=None),
                                    Constant(value='shared', kind=None),
                                    Constant(value='profiles', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                    Constant(value='https://www.speedscope.app/file-format-schema.json', kind=None),
                                    Dict(
                                        keys=[Constant(value='frames', kind=None)],
                                        values=[
                                            ListComp(
                                                elt=Dict(
                                                    keys=[
                                                        Constant(value='name', kind=None),
                                                        Constant(value='file', kind=None),
                                                        Constant(value='line', kind=None),
                                                    ],
                                                    values=[
                                                        Subscript(
                                                            value=Name(id='frame', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='frame', ctx=Load()),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='frame', ctx=Load()),
                                                            slice=Constant(value=2, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='frame', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='frames_indexes',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='profiles',
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
                    name='get_frame_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='frame', annotation=None, type_comment=None),
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
                                left=Name(id='frame', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='frames_indexes',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frames_indexes',
                                                ctx=Load(),
                                            ),
                                            slice=Name(id='frame', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='frame_count',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='frame_count',
                                        ctx=Store(),
                                    ),
                                    op=Add(),
                                    value=Constant(value=1, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='frames_indexes',
                                    ctx=Load(),
                                ),
                                slice=Name(id='frame', ctx=Load()),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='stack_to_ids',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='stack', annotation=None, type_comment=None),
                            arg(arg='context', annotation=None, type_comment=None),
                            arg(arg='stack_offset', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=0, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n            :param stack: A list of hashable frame\n            :param context: an iterable of (level, value) ordered by level\n            :param stack_offset: offeset level for stack\n\n            Assemble stack and context and return a list of ids representing\n            this stack, adding each corresponding context at the corresponding\n            level.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='stack_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='context_iterator', ctx=Store())],
                            value=Call(
                                func=Name(id='iter', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='context', ctx=Load()),
                                            Tuple(elts=[], ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='context_level', ctx=Store()),
                                        Name(id='context_value', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    Name(id='context_iterator', ctx=Load()),
                                    Tuple(
                                        elts=[
                                            Constant(value=None, kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='context_level', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    Compare(
                                        left=Name(id='context_level', ctx=Load()),
                                        ops=[Lt()],
                                        comparators=[Name(id='stack_offset', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='context_level', ctx=Store()),
                                                Name(id='context_value', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            Name(id='context_iterator', ctx=Load()),
                                            Tuple(
                                                elts=[
                                                    Constant(value=None, kind=None),
                                                    Constant(value=None, kind=None),
                                                ],
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
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='level', ctx=Store()),
                                    Name(id='frame', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[Name(id='stack', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='start',
                                        value=BinOp(
                                            left=Name(id='stack_offset', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                While(
                                    test=Compare(
                                        left=Name(id='context_level', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Name(id='level', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='context_frame', ctx=Store())],
                                            value=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Constant(value=', ', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=JoinedStr(
                                                                    values=[
                                                                        FormattedValue(
                                                                            value=Name(id='k', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                        Constant(value='=', kind=None),
                                                                        FormattedValue(
                                                                            value=Name(id='v', ctx=Load()),
                                                                            conversion=-1,
                                                                            format_spec=None,
                                                                        ),
                                                                    ],
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Tuple(
                                                                            elts=[
                                                                                Name(id='k', ctx=Store()),
                                                                                Name(id='v', ctx=Store()),
                                                                            ],
                                                                            ctx=Store(),
                                                                        ),
                                                                        iter=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='context_value', ctx=Load()),
                                                                                attr='items',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        ifs=[],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='', kind=None),
                                                    Constant(value='', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='stack_ids', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='get_frame_id',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='context_frame', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='context_level', ctx=Store()),
                                                        Name(id='context_value', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='next', ctx=Load()),
                                                args=[
                                                    Name(id='context_iterator', ctx=Load()),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=None, kind=None),
                                                            Constant(value=None, kind=None),
                                                        ],
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='stack_ids', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='get_frame_id',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='frame', ctx=Load())],
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
                        Return(
                            value=Name(id='stack_ids', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='process',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='entries', annotation=None, type_comment=None),
                            arg(arg='continuous', annotation=None, type_comment=None),
                            arg(arg='hide_gaps', annotation=None, type_comment=None),
                            arg(arg='use_context', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Name(id='entry_end', ctx=Store()),
                                Name(id='previous_end', ctx=Store()),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='entries', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=List(elts=[], ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_stack_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='frames_start', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='entries', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='start', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_entry', ctx=Store())],
                            value=Subscript(
                                value=Name(id='entries', ctx=Load()),
                                slice=UnaryOp(
                                    op=USub(),
                                    operand=Constant(value=1, kind=None),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Subscript(
                                value=Name(id='last_entry', ctx=Load()),
                                slice=Constant(value='stack', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='entries', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='stack', kind=None),
                                                    Constant(value='start', kind=None),
                                                ],
                                                values=[
                                                    List(elts=[], ctx=Load()),
                                                    BinOp(
                                                        left=Subscript(
                                                            value=Name(id='last_entry', ctx=Load()),
                                                            slice=Constant(value='start', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='last_entry', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='time', kind=None),
                                                                Constant(value=0, kind=None),
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
                        For(
                            target=Name(id='entry', ctx=Store()),
                            iter=Name(id='entries', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='previous_end', ctx=Store())],
                                    value=Name(id='entry_end', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='hide_gaps', ctx=Load()),
                                            Name(id='previous_end', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='entry_start', ctx=Store())],
                                            value=Name(id='previous_end', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='entry_start', ctx=Store())],
                                            value=BinOp(
                                                left=Subscript(
                                                    value=Name(id='entry', ctx=Load()),
                                                    slice=Constant(value='start', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Name(id='frames_start', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='previous_end', ctx=Load()),
                                            Compare(
                                                left=Name(id='previous_end', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[Name(id='entry_start', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='previous_end', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='close_time', ctx=Store())],
                                            value=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Name(id='entry_start', ctx=Load()),
                                                    Name(id='previous_end', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='close_time', ctx=Store())],
                                            value=Name(id='entry_start', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='entry_time', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='entry', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='time', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='entry_end', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='entry_time', ctx=Load()),
                                            ops=[Is()],
                                            comparators=[Constant(value=None, kind=None)],
                                        ),
                                        body=Constant(value=None, kind=None),
                                        orelse=BinOp(
                                            left=Name(id='entry_start', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='entry_time', ctx=Load()),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='entry_stack_ids', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='stack_to_ids',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='entry', ctx=Load()),
                                                        slice=Constant(value='stack', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='use_context', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='entry', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='exec_context', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='init_stack_trace_level',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='level', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='continuous', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='level', ctx=Store())],
                                            value=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Tuple(
                                                elts=[
                                                    Name(id='level', ctx=Store()),
                                                    Name(id='at_level', ctx=Store()),
                                                ],
                                                ctx=Store(),
                                            ),
                                            iter=Call(
                                                func=Name(id='enumerate', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='zip', ctx=Load()),
                                                        args=[
                                                            Name(id='current_stack_ids', ctx=Load()),
                                                            Name(id='entry_stack_ids', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='current', ctx=Store()),
                                                                Name(id='new', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='at_level', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='current', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='new', ctx=Load())],
                                                    ),
                                                    body=[Break()],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                AugAssign(
                                                    target=Name(id='level', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Name(id='frame', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='reversed', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='current_stack_ids', ctx=Load()),
                                                slice=Slice(
                                                    lower=Name(id='level', ctx=Load()),
                                                    upper=None,
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='events', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='frame', kind=None),
                                                            Constant(value='at', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='C', kind=None),
                                                            Name(id='frame', ctx=Load()),
                                                            Name(id='close_time', ctx=Load()),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='frame', ctx=Store()),
                                    iter=Subscript(
                                        value=Name(id='entry_stack_ids', ctx=Load()),
                                        slice=Slice(
                                            lower=Name(id='level', ctx=Load()),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='events', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='type', kind=None),
                                                            Constant(value='frame', kind=None),
                                                            Constant(value='at', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='O', kind=None),
                                                            Name(id='frame', ctx=Load()),
                                                            Name(id='entry_start', ctx=Load()),
                                                        ],
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
                                    targets=[Name(id='current_stack_ids', ctx=Store())],
                                    value=Name(id='entry_stack_ids', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='events', ctx=Load()),
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
