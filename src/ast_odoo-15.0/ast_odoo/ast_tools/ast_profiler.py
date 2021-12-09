Module(
    body=[
        Import(
            names=[alias(name='datetime', asname=None)],
        ),
        Import(
            names=[alias(name='gc', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='sys', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='functools', asname=None)],
        ),
        ImportFrom(
            module='psycopg2',
            names=[alias(name='sql', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tools', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='_format_frame',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='frame', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='code', ctx=Store())],
                    value=Attribute(
                        value=Name(id='frame', ctx=Load()),
                        attr='f_code',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Tuple(
                        elts=[
                            Attribute(
                                value=Name(id='code', ctx=Load()),
                                attr='co_filename',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='frame', ctx=Load()),
                                attr='f_lineno',
                                ctx=Load(),
                            ),
                            Attribute(
                                value=Name(id='code', ctx=Load()),
                                attr='co_name',
                                ctx=Load(),
                            ),
                            Constant(value='', kind=None),
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
            name='_format_stack',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='stack', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=ListComp(
                        elt=Call(
                            func=Name(id='list', ctx=Load()),
                            args=[Name(id='frame', ctx=Load())],
                            keywords=[],
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='frame', ctx=Store()),
                                iter=Name(id='stack', ctx=Load()),
                                ifs=[],
                                is_async=0,
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
            name='get_current_frame',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='thread', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                If(
                    test=Name(id='thread', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='frame', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='sys', ctx=Load()),
                                        attr='_current_frames',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Attribute(
                                    value=Name(id='thread', ctx=Load()),
                                    attr='ident',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='frame', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='_getframe',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                ),
                While(
                    test=Compare(
                        left=Attribute(
                            value=Attribute(
                                value=Name(id='frame', ctx=Load()),
                                attr='f_code',
                                ctx=Load(),
                            ),
                            attr='co_filename',
                            ctx=Load(),
                        ),
                        ops=[Eq()],
                        comparators=[Name(id='__file__', ctx=Load())],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='frame', ctx=Store())],
                            value=Attribute(
                                value=Name(id='frame', ctx=Load()),
                                attr='f_back',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='frame', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_get_stack_trace',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='frame', annotation=None, type_comment=None),
                    arg(arg='limit_frame', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=None, kind=None)],
            ),
            body=[
                Assign(
                    targets=[Name(id='stack', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                While(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Name(id='frame', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            Compare(
                                left=Name(id='frame', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Name(id='limit_frame', ctx=Load())],
                            ),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='stack', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='_format_frame', ctx=Load()),
                                        args=[Name(id='frame', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='frame', ctx=Store())],
                            value=Attribute(
                                value=Name(id='frame', ctx=Load()),
                                attr='f_back',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Name(id='frame', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            Name(id='limit_frame', ctx=Load()),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='error',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Limit frame was not found', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Call(
                        func=Name(id='list', ctx=Load()),
                        args=[
                            Call(
                                func=Name(id='reversed', ctx=Load()),
                                args=[Name(id='stack', ctx=Load())],
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
        FunctionDef(
            name='stack_size',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Name(id='frame', ctx=Store())],
                    value=Call(
                        func=Name(id='get_current_frame', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='size', ctx=Store())],
                    value=Constant(value=0, kind=None),
                    type_comment=None,
                ),
                While(
                    test=Name(id='frame', ctx=Load()),
                    body=[
                        AugAssign(
                            target=Name(id='size', ctx=Store()),
                            op=Add(),
                            value=Constant(value=1, kind=None),
                        ),
                        Assign(
                            targets=[Name(id='frame', ctx=Store())],
                            value=Attribute(
                                value=Name(id='frame', ctx=Load()),
                                attr='f_back',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='size', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='make_session',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='name', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='', kind=None)],
            ),
            body=[
                Return(
                    value=JoinedStr(
                        values=[
                            FormattedValue(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='datetime', ctx=Load()),
                                            attr='datetime',
                                            ctx=Load(),
                                        ),
                                        attr='now',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                conversion=-1,
                                format_spec=JoinedStr(
                                    values=[Constant(value='%Y-%m-%d %H:%M:%S', kind=None)],
                                ),
                            ),
                            Constant(value=' ', kind=None),
                            FormattedValue(
                                value=Name(id='name', ctx=Load()),
                                conversion=-1,
                                format_spec=None,
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
            name='force_hook',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value='\n    Force periodic profiling collectors to generate some stack trace.  This is\n    useful before long calls that do not release the GIL, so that the time\n    spent in those calls is attributed to a specific stack trace, instead of\n    some arbitrary former frame.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='thread', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='threading', ctx=Load()),
                            attr='current_thread',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='func', ctx=Store()),
                    iter=Call(
                        func=Name(id='getattr', ctx=Load()),
                        args=[
                            Name(id='thread', ctx=Load()),
                            Constant(value='profile_hooks', kind=None),
                            Tuple(elts=[], ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='func', ctx=Load()),
                                args=[],
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
        ClassDef(
            name='Collector',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Base class for objects that collect profiling data.\n\n    A collector object is used by a profiler to collect profiling data, most\n    likely a list of stack traces with time and some context information added\n    by ExecutionContext decorator on current thread.\n\n    This is a generic implementation of a basic collector, to be inherited.\n    It defines default behaviors for creating an entry in the collector.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Constant(value=None, kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_registry', ctx=Store())],
                    value=Dict(keys=[], values=[]),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init_subclass__',
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
                        If(
                            test=Attribute(
                                value=Name(id='cls', ctx=Load()),
                                attr='name',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='_registry',
                                                ctx=Load(),
                                            ),
                                            slice=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='cls', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='_registry',
                                                ctx=Load(),
                                            ),
                                            slice=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='__name__',
                                                ctx=Load(),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='cls', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='make',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                        ],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Instantiate a collector corresponding to the given name. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Subscript(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='_registry',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='name', ctx=Load()),
                                    ctx=Load(),
                                ),
                                args=[
                                    Starred(
                                        value=Name(id='args', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_processed',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_entries',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='profiler',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='start',
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
                            value=Constant(value=' Start the collector. ', kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='stop',
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
                            value=Constant(value=' Stop the collector. ', kind=None),
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
                            arg(arg='entry', annotation=None, type_comment=None),
                            arg(arg='frame', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Add an entry (dict) to this collector. ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_entries',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='stack', kind=None),
                                            Constant(value='exec_context', kind=None),
                                            Constant(value='start', kind=None),
                                            None,
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_get_stack_trace',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='frame', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='profiler',
                                                            ctx=Load(),
                                                        ),
                                                        attr='init_thread',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='exec_context', kind=None),
                                                    Tuple(elts=[], ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='time',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='entry', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
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
                FunctionDef(
                    name='_get_stack_trace',
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
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Return the stack trace to be included in a given entry. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='frame', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='frame', ctx=Load()),
                                    Call(
                                        func=Name(id='get_current_frame', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='profiler',
                                                    ctx=Load(),
                                                ),
                                                attr='init_thread',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='_get_stack_trace', ctx=Load()),
                                args=[
                                    Name(id='frame', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='profiler',
                                            ctx=Load(),
                                        ),
                                        attr='init_frame',
                                        ctx=Load(),
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
                    name='post_process',
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
                            target=Name(id='entry', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_entries',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='stack', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='entry', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='stack', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='profiler',
                                                ctx=Load(),
                                            ),
                                            attr='_add_file_lines',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='stack', ctx=Load())],
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
                    name='entries',
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
                            value=Constant(value=' Return the entries of the collector after postprocessing. ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_processed',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='post_process',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_processed',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_entries',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='property', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='SQLCollector',
            bases=[Name(id='Collector', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Saves all executed queries in the current thread with the call stack.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Constant(value='sql', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='start',
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
                            targets=[Name(id='init_thread', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='profiler',
                                    ctx=Load(),
                                ),
                                attr='init_thread',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='hasattr', ctx=Load()),
                                    args=[
                                        Name(id='init_thread', ctx=Load()),
                                        Constant(value='query_hooks', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='init_thread', ctx=Load()),
                                            attr='query_hooks',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='init_thread', ctx=Load()),
                                        attr='query_hooks',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hook',
                                        ctx=Load(),
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
                    name='stop',
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='profiler',
                                                ctx=Load(),
                                            ),
                                            attr='init_thread',
                                            ctx=Load(),
                                        ),
                                        attr='query_hooks',
                                        ctx=Load(),
                                    ),
                                    attr='remove',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hook',
                                        ctx=Load(),
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
                    name='hook',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                            arg(arg='query', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                            arg(arg='query_start', annotation=None, type_comment=None),
                            arg(arg='query_time', annotation=None, type_comment=None),
                        ],
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
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='query', kind=None),
                                            Constant(value='full_query', kind=None),
                                            Constant(value='start', kind=None),
                                            Constant(value='time', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='query', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='cr', ctx=Load()),
                                                            attr='_format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='query', ctx=Load()),
                                                            Name(id='params', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='query_start', ctx=Load()),
                                            Name(id='query_time', ctx=Load()),
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
        ClassDef(
            name='PeriodicCollector',
            bases=[Name(id='Collector', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Record execution frames asynchronously at most every `interval` seconds.\n\n    :param interval (float): time to wait in seconds between two samples.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Constant(value='traces_async', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='interval', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=0.01, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='active',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='frame_interval',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='interval', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='thread',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='Thread',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='target',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='run',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='last_frame',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='run',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='active',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_time', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='time',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='active',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='duration', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='time', ctx=Load()),
                                                attr='time',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Name(id='last_time', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='duration', ctx=Load()),
                                                ops=[Gt()],
                                                comparators=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='frame_interval',
                                                            ctx=Load(),
                                                        ),
                                                        op=Mult(),
                                                        right=Constant(value=10, kind=None),
                                                    ),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='last_frame',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_entries',
                                                                ctx=Load(),
                                                            ),
                                                            slice=UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=1, kind=None),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='stack', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='profiling', kind=None),
                                                            Constant(value=0, kind=None),
                                                            BinOp(
                                                                left=Constant(value='⚠ Profiler freezed for %s s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='duration', ctx=Load()),
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
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
                                                    attr='last_frame',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='last_time', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='time',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='sleep',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='frame_interval',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_entries',
                                        ctx=Load(),
                                    ),
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
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='time', ctx=Load()),
                                                    attr='time',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
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
                FunctionDef(
                    name='start',
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
                            targets=[Name(id='interval', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='profiler',
                                            ctx=Load(),
                                        ),
                                        attr='params',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='traces_async_interval', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='interval', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='frame_interval',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='min', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='max', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='float', ctx=Load()),
                                                        args=[Name(id='interval', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=0.001, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='init_thread', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='profiler',
                                    ctx=Load(),
                                ),
                                attr='init_thread',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='hasattr', ctx=Load()),
                                    args=[
                                        Name(id='init_thread', ctx=Load()),
                                        Constant(value='profile_hooks', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='init_thread', ctx=Load()),
                                            attr='profile_hooks',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='init_thread', ctx=Load()),
                                        attr='profile_hooks',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='add',
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
                                        value=Name(id='self', ctx=Load()),
                                        attr='thread',
                                        ctx=Load(),
                                    ),
                                    attr='start',
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
                    name='stop',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='active',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='thread',
                                        ctx=Load(),
                                    ),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='profiler',
                                                ctx=Load(),
                                            ),
                                            attr='init_thread',
                                            ctx=Load(),
                                        ),
                                        attr='profile_hooks',
                                        ctx=Load(),
                                    ),
                                    attr='remove',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='add',
                                        ctx=Load(),
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
                    name='add',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='entry', annotation=None, type_comment=None),
                            arg(arg='frame', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Add an entry (dict) to this collector. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='frame', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='frame', ctx=Load()),
                                    Call(
                                        func=Name(id='get_current_frame', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='profiler',
                                                    ctx=Load(),
                                                ),
                                                attr='init_thread',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='frame', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='last_frame',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='last_frame',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='frame', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='entry',
                                        value=Name(id='entry', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='frame',
                                        value=Name(id='frame', ctx=Load()),
                                    ),
                                ],
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
        ClassDef(
            name='SyncCollector',
            bases=[Name(id='Collector', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Record complete execution synchronously.\n    Note that --limit-memory-hard may need to be increased when launching Odoo.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Constant(value='traces_sync', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='start',
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
                        Assert(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_processed',
                                    ctx=Load(),
                                ),
                            ),
                            msg=Constant(value='You cannot start SyncCollector after accessing entries.', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sys', ctx=Load()),
                                    attr='settrace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hook',
                                        ctx=Load(),
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
                    name='stop',
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
                                    value=Name(id='sys', ctx=Load()),
                                    attr='settrace',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=None, kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='hook',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='_frame', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='_arg', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='event', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='line', kind=None)],
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='entry', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='event', kind=None),
                                    Constant(value='frame', kind=None),
                                ],
                                values=[
                                    Name(id='event', ctx=Load()),
                                    Call(
                                        func=Name(id='_format_frame', ctx=Load()),
                                        args=[Name(id='_frame', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='event', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='call', kind=None)],
                                    ),
                                    Attribute(
                                        value=Name(id='_frame', ctx=Load()),
                                        attr='f_back',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='entry', ctx=Load()),
                                            slice=Constant(value='parent_frame', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='_format_frame', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='_frame', ctx=Load()),
                                                attr='f_back',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[Name(id='entry', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='frame',
                                        value=Name(id='_frame', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='hook',
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_stack_trace',
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
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Return(
                            value=Constant(value=None, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='post_process',
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
                            targets=[Name(id='stack', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='entry', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='_entries',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='frame', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='entry', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='frame', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='event', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='entry', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='event', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='event', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='call', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Name(id='stack', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='stack', ctx=Load()),
                                                            slice=UnaryOp(
                                                                op=USub(),
                                                                operand=Constant(value=1, kind=None),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='entry', ctx=Load()),
                                                            attr='pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='parent_frame', kind=None)],
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
                                                    value=Name(id='stack', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='frame', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='event', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='return', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='stack', ctx=Load()),
                                                            attr='pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='entry', ctx=Load()),
                                            slice=Constant(value='stack', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='stack', ctx=Load()),
                                        slice=Slice(lower=None, upper=None, step=None),
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='post_process',
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='QwebTracker',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='wrap_render',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='method_render', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='_tracked_method_render',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='self', annotation=None, type_comment=None),
                                    arg(arg='template', annotation=None, type_comment=None),
                                    arg(arg='values', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='options', annotation=None, type_comment=None),
                                defaults=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='current_thread', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='current_thread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='execution_context_enabled', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Name(id='current_thread', ctx=Load()),
                                                    Constant(value='profiler_params', kind=None),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='execution_context_qweb', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='qweb_hooks', ctx=Store())],
                                    value=Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='current_thread', ctx=Load()),
                                            Constant(value='qweb_hooks', kind=None),
                                            Tuple(elts=[], ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='execution_context_enabled', ctx=Load()),
                                            Name(id='qweb_hooks', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='options', ctx=Load()),
                                                    slice=Constant(value='profile', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Name(id='method_render', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Name(id='template', ctx=Load()),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='options', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            decorator_list=[
                                Call(
                                    func=Attribute(
                                        value=Name(id='functools', ctx=Load()),
                                        attr='wraps',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='method_render', ctx=Load())],
                                    keywords=[],
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='_tracked_method_render', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='wrap_compile',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='method_compile', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='_tracked_compile',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='self', annotation=None, type_comment=None),
                                    arg(arg='template', annotation=None, type_comment=None),
                                    arg(arg='options', annotation=None, type_comment=None),
                                ],
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
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='options', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='profile', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='method_compile', ctx=Load()),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='template', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='render_template', ctx=Store())],
                                    value=Call(
                                        func=Name(id='method_compile', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Name(id='template', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                FunctionDef(
                                    name='profiled_method_compile',
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
                                            targets=[Name(id='ref', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='ref', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='ref_xml', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='ref_xml', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='qweb_tracker', ctx=Store())],
                                            value=Call(
                                                func=Name(id='QwebTracker', ctx=Load()),
                                                args=[
                                                    Name(id='ref', ctx=Load()),
                                                    Name(id='ref_xml', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='self', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='qweb_tracker',
                                                        value=Name(id='qweb_tracker', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='qweb_tracker', ctx=Load()),
                                                attr='execution_context_enabled',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                With(
                                                    items=[
                                                        withitem(
                                                            context_expr=Call(
                                                                func=Name(id='ExecutionContext', ctx=Load()),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='template',
                                                                        value=Name(id='ref', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                            optional_vars=None,
                                                        ),
                                                    ],
                                                    body=[
                                                        Return(
                                                            value=Call(
                                                                func=Name(id='render_template', ctx=Load()),
                                                                args=[
                                                                    Name(id='self', ctx=Load()),
                                                                    Name(id='values', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Return(
                                            value=Call(
                                                func=Name(id='render_template', ctx=Load()),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='values', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='profiled_method_compile', ctx=Load()),
                                ),
                            ],
                            decorator_list=[
                                Call(
                                    func=Attribute(
                                        value=Name(id='functools', ctx=Load()),
                                        attr='wraps',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='method_compile', ctx=Load())],
                                    keywords=[],
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='_tracked_compile', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='wrap_compile_directive',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='method_compile_directive', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        FunctionDef(
                            name='_tracked_compile_directive',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='self', annotation=None, type_comment=None),
                                    arg(arg='el', annotation=None, type_comment=None),
                                    arg(arg='options', annotation=None, type_comment=None),
                                    arg(arg='directive', annotation=None, type_comment=None),
                                    arg(arg='indent', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='options', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='profile', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Compare(
                                                left=Name(id='directive', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='content', kind=None),
                                                            Constant(value='tag', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='method_compile_directive', ctx=Load()),
                                                args=[
                                                    Name(id='self', ctx=Load()),
                                                    Name(id='el', ctx=Load()),
                                                    Name(id='options', ctx=Load()),
                                                    Name(id='directive', ctx=Load()),
                                                    Name(id='indent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='enter', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            JoinedStr(
                                                values=[
                                                    Constant(value="self.env.context['qweb_tracker'].enter_directive(", kind=None),
                                                    FormattedValue(
                                                        value=Name(id='directive', ctx=Load()),
                                                        conversion=114,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=', ', kind=None),
                                                    FormattedValue(
                                                        value=Attribute(
                                                            value=Name(id='el', ctx=Load()),
                                                            attr='attrib',
                                                            ctx=Load(),
                                                        ),
                                                        conversion=114,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=', ', kind=None),
                                                    FormattedValue(
                                                        value=Subscript(
                                                            value=Name(id='options', ctx=Load()),
                                                            slice=Constant(value='last_path_node', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        conversion=114,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=')', kind=None),
                                                ],
                                            ),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='leave', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_indent',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value="self.env.context['qweb_tracker'].leave_directive()", kind=None),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='code_directive', ctx=Store())],
                                    value=Call(
                                        func=Name(id='method_compile_directive', ctx=Load()),
                                        args=[
                                            Name(id='self', ctx=Load()),
                                            Name(id='el', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                            Name(id='directive', ctx=Load()),
                                            Name(id='indent', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=IfExp(
                                        test=Name(id='code_directive', ctx=Load()),
                                        body=List(
                                            elts=[
                                                Name(id='enter', ctx=Load()),
                                                Starred(
                                                    value=Name(id='code_directive', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                Name(id='leave', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        orelse=List(elts=[], ctx=Load()),
                                    ),
                                ),
                            ],
                            decorator_list=[
                                Call(
                                    func=Attribute(
                                        value=Name(id='functools', ctx=Load()),
                                        attr='wraps',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='method_compile_directive', ctx=Load())],
                                    keywords=[],
                                ),
                            ],
                            returns=None,
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='_tracked_compile_directive', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='view_id', annotation=None, type_comment=None),
                            arg(arg='arch', annotation=None, type_comment=None),
                            arg(arg='cr', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='current_thread', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='current_thread',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='execution_context_enabled',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='current_thread', ctx=Load()),
                                            Constant(value='profiler_params', kind=None),
                                            Dict(keys=[], values=[]),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='execution_context_qweb', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='qweb_hooks',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='current_thread', ctx=Load()),
                                    Constant(value='qweb_hooks', kind=None),
                                    Tuple(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='context_stack',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='cr',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='cr', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='view_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='view_id', ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='hook', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='qweb_hooks',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='hook', ctx=Load()),
                                        args=[
                                            Constant(value='render', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='sql_log_count',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='view_id',
                                                value=Name(id='view_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='arch',
                                                value=Name(id='arch', ctx=Load()),
                                            ),
                                        ],
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
                    name='enter_directive',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='directive', annotation=None, type_comment=None),
                            arg(arg='attrib', annotation=None, type_comment=None),
                            arg(arg='xpath', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='execution_context', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='execution_context_enabled',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='execution_context', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='tools', ctx=Load()),
                                                attr='profiler',
                                                ctx=Load(),
                                            ),
                                            attr='ExecutionContext',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='directive',
                                                value=Name(id='directive', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='xpath',
                                                value=Name(id='xpath', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='execution_context', ctx=Load()),
                                            attr='__enter__',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='context_stack',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='execution_context', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='hook', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='qweb_hooks',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='hook', ctx=Load()),
                                        args=[
                                            Constant(value='enter', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='sql_log_count',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='view_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='view_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='xpath',
                                                value=Name(id='xpath', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='directive',
                                                value=Name(id='directive', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='attrib',
                                                value=Name(id='attrib', ctx=Load()),
                                            ),
                                        ],
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
                    name='leave_directive',
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
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='execution_context_enabled',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='context_stack',
                                                        ctx=Load(),
                                                    ),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='__exit__',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='hook', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='qweb_hooks',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='hook', ctx=Load()),
                                        args=[
                                            Constant(value='leave', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='cr',
                                                    ctx=Load(),
                                                ),
                                                attr='sql_log_count',
                                                ctx=Load(),
                                            ),
                                        ],
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='QwebCollector',
            bases=[Name(id='Collector', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Record qweb execution with directive trace.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Constant(value='qweb', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__init__',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='__init__',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='events',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='hook',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='event', annotation=None, type_comment=None),
                                    arg(arg='sql_log_count', annotation=None, type_comment=None),
                                ],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='events',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Name(id='event', ctx=Load()),
                                                    Name(id='kwargs', ctx=Load()),
                                                    Name(id='sql_log_count', ctx=Load()),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='time', ctx=Load()),
                                                            attr='time',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='hook',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='hook', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_directive_profiling_name',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='directive', annotation=None, type_comment=None),
                            arg(arg='attrib', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='expr', ctx=Store())],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='directive', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='set', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='expr', ctx=Store())],
                                    value=JoinedStr(
                                        values=[
                                            Constant(value='t-set=', kind=None),
                                            FormattedValue(
                                                value=Call(
                                                    func=Name(id='repr', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='attrib', ctx=Load()),
                                                            slice=Constant(value='t-set', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='t-value', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='attrib', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='expr', ctx=Store())],
                                            value=JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='expr', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=' t-value=', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='attrib', ctx=Load()),
                                                                    slice=Constant(value='t-value', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='t-valuef', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='attrib', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='expr', ctx=Store())],
                                            value=JoinedStr(
                                                values=[
                                                    FormattedValue(
                                                        value=Name(id='expr', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=' t-valuef=', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='attrib', ctx=Load()),
                                                                    slice=Constant(value='t-valuef', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='directive', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='foreach', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='expr', ctx=Store())],
                                            value=JoinedStr(
                                                values=[
                                                    Constant(value='t-foreach=', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='attrib', ctx=Load()),
                                                                    slice=Constant(value='t-foreach', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value=' t-as=', kind=None),
                                                    FormattedValue(
                                                        value=Call(
                                                            func=Name(id='repr', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='attrib', ctx=Load()),
                                                                    slice=Constant(value='t-as', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='directive', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='options', kind=None)],
                                            ),
                                            body=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='attrib', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='t-options', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='expr', ctx=Store())],
                                                            value=JoinedStr(
                                                                values=[
                                                                    Constant(value='t-options=', kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='repr', ctx=Load()),
                                                                            args=[
                                                                                Subscript(
                                                                                    value=Name(id='attrib', ctx=Load()),
                                                                                    slice=Constant(value='t-options', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                For(
                                                    target=Name(id='key', ctx=Store()),
                                                    iter=Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[Name(id='attrib', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Call(
                                                                func=Attribute(
                                                                    value=Name(id='key', ctx=Load()),
                                                                    attr='startswith',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='t-options-', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='expr', ctx=Store())],
                                                                    value=JoinedStr(
                                                                        values=[
                                                                            FormattedValue(
                                                                                value=Name(id='expr', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value='  ', kind=None),
                                                                            FormattedValue(
                                                                                value=Name(id='key', ctx=Load()),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                            Constant(value='=', kind=None),
                                                                            FormattedValue(
                                                                                value=Call(
                                                                                    func=Name(id='repr', ctx=Load()),
                                                                                    args=[
                                                                                        Subscript(
                                                                                            value=Name(id='attrib', ctx=Load()),
                                                                                            slice=Name(id='key', ctx=Load()),
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                                conversion=-1,
                                                                                format_spec=None,
                                                                            ),
                                                                        ],
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
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='directive', ctx=Load()),
                                                            Compare(
                                                                left=BinOp(
                                                                    left=Constant(value='t-', kind=None),
                                                                    op=Add(),
                                                                    right=Name(id='directive', ctx=Load()),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[Name(id='attrib', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='expr', ctx=Store())],
                                                            value=JoinedStr(
                                                                values=[
                                                                    Constant(value='t-', kind=None),
                                                                    FormattedValue(
                                                                        value=Name(id='directive', ctx=Load()),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                    Constant(value='=', kind=None),
                                                                    FormattedValue(
                                                                        value=Call(
                                                                            func=Name(id='repr', ctx=Load()),
                                                                            args=[
                                                                                Subscript(
                                                                                    value=Name(id='attrib', ctx=Load()),
                                                                                    slice=BinOp(
                                                                                        left=Constant(value='t-', kind=None),
                                                                                        op=Add(),
                                                                                        right=Name(id='directive', ctx=Load()),
                                                                                    ),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        conversion=-1,
                                                                        format_spec=None,
                                                                    ),
                                                                ],
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
                        Return(
                            value=Name(id='expr', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='start',
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
                            targets=[Name(id='init_thread', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='profiler',
                                    ctx=Load(),
                                ),
                                attr='init_thread',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='hasattr', ctx=Load()),
                                    args=[
                                        Name(id='init_thread', ctx=Load()),
                                        Constant(value='qweb_hooks', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='init_thread', ctx=Load()),
                                            attr='qweb_hooks',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='init_thread', ctx=Load()),
                                        attr='qweb_hooks',
                                        ctx=Load(),
                                    ),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hook',
                                        ctx=Load(),
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
                    name='stop',
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='profiler',
                                                ctx=Load(),
                                            ),
                                            attr='init_thread',
                                            ctx=Load(),
                                        ),
                                        attr='qweb_hooks',
                                        ctx=Load(),
                                    ),
                                    attr='remove',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hook',
                                        ctx=Load(),
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
                    name='post_process',
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
                            targets=[Name(id='last_event_query', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_event_time', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stack', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='results', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='archs', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='event', ctx=Store()),
                                    Name(id='kwargs', ctx=Store()),
                                    Name(id='sql_count', ctx=Store()),
                                    Name(id='time', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='events',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='event', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='render', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='archs', ctx=Load()),
                                                    slice=Subscript(
                                                        value=Name(id='kwargs', ctx=Load()),
                                                        slice=Constant(value='view_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='kwargs', ctx=Load()),
                                                slice=Constant(value='arch', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Continue(),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='stack', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='top', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='stack', ctx=Load()),
                                                slice=UnaryOp(
                                                    op=USub(),
                                                    operand=Constant(value=1, kind=None),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='top', ctx=Load()),
                                                slice=Constant(value='delay', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=BinOp(
                                                left=Name(id='time', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='last_event_time', ctx=Load()),
                                            ),
                                        ),
                                        AugAssign(
                                            target=Subscript(
                                                value=Name(id='top', ctx=Load()),
                                                slice=Constant(value='query', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=BinOp(
                                                left=Name(id='sql_count', ctx=Load()),
                                                op=Sub(),
                                                right=Name(id='last_event_query', ctx=Load()),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='last_event_time', ctx=Store())],
                                    value=Name(id='time', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='last_event_query', ctx=Store())],
                                    value=Name(id='sql_count', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='event', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='enter', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='data', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='view_id', kind=None),
                                                    Constant(value='xpath', kind=None),
                                                    Constant(value='directive', kind=None),
                                                    Constant(value='delay', kind=None),
                                                    Constant(value='query', kind=None),
                                                ],
                                                values=[
                                                    Subscript(
                                                        value=Name(id='kwargs', ctx=Load()),
                                                        slice=Constant(value='view_id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='kwargs', ctx=Load()),
                                                        slice=Constant(value='xpath', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_get_directive_profiling_name',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='kwargs', ctx=Load()),
                                                                slice=Constant(value='directive', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='kwargs', ctx=Load()),
                                                                slice=Constant(value='attrib', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='results', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='data', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='stack', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='data', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assert(
                                            test=Compare(
                                                left=Name(id='event', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='leave', kind=None)],
                                            ),
                                            msg=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='data', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='stack', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='results', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='archs', kind=None),
                                                    Constant(value='data', kind=None),
                                                ],
                                                values=[
                                                    Name(id='archs', ctx=Load()),
                                                    Name(id='results', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='post_process',
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
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ExecutionContext',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Add some context on thread at current call stack level.\n    This context stored by collector beside stack and is used by Speedscope\n    to add a level to the stack with this information.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='context', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='context',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='context', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='previous_context',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__enter__',
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
                            targets=[Name(id='current_thread', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='current_thread',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='previous_context',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='current_thread', ctx=Load()),
                                    Constant(value='exec_context', kind=None),
                                    Tuple(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='current_thread', ctx=Load()),
                                    attr='exec_context',
                                    ctx=Store(),
                                ),
                            ],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='previous_context',
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Tuple(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='stack_size', ctx=Load()),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='context',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__exit__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='_args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='current_thread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='exec_context',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='previous_context',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Profiler',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Context manager to use to start the recording of some execution.\n    Will save sql and async stack trace by default.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='collectors', annotation=None, type_comment=None),
                            arg(arg='db', annotation=None, type_comment=None),
                            arg(arg='profile_session', annotation=None, type_comment=None),
                            arg(arg='description', annotation=None, type_comment=None),
                            arg(arg='disable_gc', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=Ellipsis, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        :param db: database name to use to save results.\n            Will try to define database automatically by default.\n            Use value ``None`` to not save results in a database.\n        :param collectors: list of string and Collector object Ex: ['sql', PeriodicCollector(interval=0.2)]. Use `None` for default collectors\n        :param profile_session: session description to use to reproup multiple profile. use make_session(name) for default format.\n        :param description: description of the current profiler Suggestion: (route name/test method/loading module, ...)\n        :param disable_gc: flag to disable gc durring profiling (usefull to avoid gc while profiling, especially during sql execution)\n        :param params: parameters usable by collectors (like frame interval)\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_time',
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
                                    attr='duration',
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
                                    attr='profile_session',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='profile_session', ctx=Load()),
                                    Call(
                                        func=Name(id='make_session', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='description',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='description', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='init_frame',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='init_stack_trace',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='init_thread',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='disable_gc',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='disable_gc', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filecache',
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
                                    attr='params',
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='params', ctx=Load()),
                                    Dict(keys=[], values=[]),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='db', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=Ellipsis, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='db', ctx=Store())],
                                    value=Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='threading', ctx=Load()),
                                                    attr='current_thread',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Constant(value='dbname', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='db', ctx=Load()),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='Exception', ctx=Load()),
                                                args=[Constant(value='Database name cannot be defined automaticaly. \n Please provide a valid/falsy dbname or path parameter', kind=None)],
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='db',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='db', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='collectors', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='collectors', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Constant(value='sql', kind=None),
                                            Constant(value='traces_async', kind=None),
                                        ],
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
                                    attr='collectors',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='collector', ctx=Store()),
                            iter=Name(id='collectors', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='collector', ctx=Load()),
                                            Name(id='str', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='collector', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Collector', ctx=Load()),
                                                            attr='make',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='collector', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='Exception', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='error',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='Could not create collector with name %r', kind=None),
                                                                    Name(id='collector', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Continue(),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='collector', ctx=Load()),
                                            attr='profiler',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='self', ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='collectors',
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='collector', ctx=Load())],
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
                    name='__enter__',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='init_thread',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='threading', ctx=Load()),
                                    attr='current_thread',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='init_frame',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='get_current_frame', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='init_thread',
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
                                    attr='init_stack_trace',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='_get_stack_trace', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='init_frame',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='description',
                                    ctx=Load(),
                                ),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='frame', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='init_frame',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='code', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='frame', ctx=Load()),
                                        attr='f_code',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='description',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=JoinedStr(
                                        values=[
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='frame', ctx=Load()),
                                                        attr='f_code',
                                                        ctx=Load(),
                                                    ),
                                                    attr='co_name',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=' (', kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Name(id='code', ctx=Load()),
                                                    attr='co_filename',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=':', kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Name(id='frame', ctx=Load()),
                                                    attr='f_lineno',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value=')', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='params',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='init_thread',
                                                ctx=Load(),
                                            ),
                                            attr='profiler_params',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='params',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='disable_gc',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='gc', ctx=Load()),
                                            attr='isenabled',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='gc', ctx=Load()),
                                            attr='disable',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='start_time',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='time',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='collector', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='collectors',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='collector', ctx=Load()),
                                            attr='start',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
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
                    name='__exit__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                For(
                                    target=Name(id='collector', ctx=Store()),
                                    iter=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='collectors',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='collector', ctx=Load()),
                                                    attr='stop',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='duration',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='time', ctx=Load()),
                                                attr='time',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='start_time',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_add_file_lines',
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
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        ImportFrom(
                                            module='odoo.sql_db',
                                            names=[alias(name='db_connect', asname=None)],
                                            level=0,
                                        ),
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Name(id='db_connect', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='db',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='cursor',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='cr', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                Assign(
                                                    targets=[Name(id='values', ctx=Store())],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='name', kind=None),
                                                            Constant(value='session', kind=None),
                                                            Constant(value='create_date', kind=None),
                                                            Constant(value='init_stack_trace', kind=None),
                                                            Constant(value='duration', kind=None),
                                                            Constant(value='entry_count', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='description',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='profile_session',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='datetime', ctx=Load()),
                                                                        attr='datetime',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='now',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='json', ctx=Load()),
                                                                    attr='dumps',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_format_stack', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='init_stack_trace',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='duration',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='entry_count',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='collector', ctx=Store()),
                                                    iter=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='collectors',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        If(
                                                            test=Attribute(
                                                                value=Name(id='collector', ctx=Load()),
                                                                attr='entries',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            slice=Attribute(
                                                                                value=Name(id='collector', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='json', ctx=Load()),
                                                                            attr='dumps',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='collector', ctx=Load()),
                                                                                attr='entries',
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
                                                Assign(
                                                    targets=[Name(id='query', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='sql', ctx=Load()),
                                                                    attr='SQL',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='INSERT INTO {}({}) VALUES %s RETURNING id', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            attr='format',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='sql', ctx=Load()),
                                                                    attr='Identifier',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='ir_profile', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='sql', ctx=Load()),
                                                                            attr='SQL',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value=',', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='map', ctx=Load()),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='sql', ctx=Load()),
                                                                                attr='Identifier',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='values', ctx=Load()),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='cr', ctx=Load()),
                                                            attr='execute',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='query', ctx=Load()),
                                                            List(
                                                                elts=[
                                                                    Call(
                                                                        func=Name(id='tuple', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='values', ctx=Load()),
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
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Assign(
                                                    targets=[Name(id='profile_id', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='cr', ctx=Load()),
                                                                attr='fetchone',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='info',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='ir_profile %s (%s) created', kind=None),
                                                            Name(id='profile_id', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='profile_session',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='disable_gc',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='gc', ctx=Load()),
                                                    attr='enable',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='params',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Delete(
                                            targets=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='init_thread',
                                                        ctx=Load(),
                                                    ),
                                                    attr='profiler_params',
                                                    ctx=Del(),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_file_lines',
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
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='filename', ctx=Store()),
                                                Name(id='lineno', ctx=Store()),
                                                Name(id='name', ctx=Store()),
                                                Name(id='line', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='frame', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='line', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='', kind=None)],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='filelines', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='filecache',
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='filename', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='KeyError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Try(
                                                    body=[
                                                        With(
                                                            items=[
                                                                withitem(
                                                                    context_expr=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='tools', ctx=Load()),
                                                                            attr='file_open',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='filename', ctx=Load())],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='filter_ext',
                                                                                value=Tuple(
                                                                                    elts=[Constant(value='.py', kind=None)],
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    optional_vars=Name(id='f', ctx=Store()),
                                                                ),
                                                            ],
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='filelines', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='f', ctx=Load()),
                                                                            attr='readlines',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Tuple(
                                                                elts=[
                                                                    Name(id='ValueError', ctx=Load()),
                                                                    Name(id='FileNotFoundError', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            name=None,
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='filelines', ctx=Store())],
                                                                    value=Constant(value=None, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    finalbody=[],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='filecache',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Name(id='filename', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='filelines', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='filelines', ctx=Load()),
                                        ops=[IsNot()],
                                        comparators=[Constant(value=None, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='line', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='filelines', ctx=Load()),
                                                slice=BinOp(
                                                    left=Name(id='lineno', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
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
                                                    Name(id='filename', ctx=Load()),
                                                    Name(id='lineno', ctx=Load()),
                                                    Name(id='name', ctx=Load()),
                                                    Name(id='line', ctx=Load()),
                                                ],
                                                ctx=Load(),
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='entry_count',
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
                            value=Constant(value=' Return the total number of entries collected in this profiler. ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='collector', ctx=Load()),
                                                    attr='entries',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='collector', ctx=Store()),
                                                iter=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='collectors',
                                                    ctx=Load(),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
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
                FunctionDef(
                    name='format_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='path', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Utility function to format a path for this profiler.\n        This is mainly useful to uniquify a path between executions.\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='path', ctx=Load()),
                                    attr='format',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='time',
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='datetime', ctx=Load()),
                                                            attr='datetime',
                                                            ctx=Load(),
                                                        ),
                                                        attr='now',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='strftime',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='%Y%m%d-%H%M%S', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='len',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='entry_count',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='desc',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='re', ctx=Load()),
                                                attr='sub',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='[^0-9a-zA-Z-]+', kind=None),
                                                Constant(value='_', kind=None),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='description',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
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
                FunctionDef(
                    name='json',
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
                            value=Constant(value="\n        Utility function to generate a json version of this profiler.\n        This is useful to write profiling entries into a file, such as::\n\n            with Profiler(db=None) as profiler:\n                do_stuff()\n\n            filename = p.format_path('/home/foo/{desc}_{len}.json')\n            with open(filename, 'w') as f:\n                f.write(profiler.json())\n        ", kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='dumps',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='session', kind=None),
                                            Constant(value='create_date', kind=None),
                                            Constant(value='init_stack_trace', kind=None),
                                            Constant(value='duration', kind=None),
                                            Constant(value='collectors', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='description',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='profile_session',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='datetime', ctx=Load()),
                                                                attr='datetime',
                                                                ctx=Load(),
                                                            ),
                                                            attr='now',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='strftime',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='%Y%m%d-%H%M%S', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='_format_stack', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='init_stack_trace',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='duration',
                                                ctx=Load(),
                                            ),
                                            DictComp(
                                                key=Attribute(
                                                    value=Name(id='collector', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                value=Attribute(
                                                    value=Name(id='collector', ctx=Load()),
                                                    attr='entries',
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='collector', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='collectors',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='indent',
                                        value=Constant(value=4, kind=None),
                                    ),
                                ],
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
        ClassDef(
            name='Nested',
            bases=[],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Utility to nest another context manager inside a profiler.\n\n    The profiler should only be called directly in the "with" without nesting it\n    with ExitStack. If not, the retrieval of the \'init_frame\' may be incorrect\n    and lead to an error "Limit frame was not found" when profiling. Since the\n    stack will ignore all stack frames inside this file, the nested frames will\n    be ignored, too. This is also why Nested() does not use\n    contextlib.contextmanager.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='profiler', annotation=None, type_comment=None),
                            arg(arg='context_manager', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='profiler',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='profiler', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='context_manager',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='context_manager', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='__enter__',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='profiler',
                                        ctx=Load(),
                                    ),
                                    attr='__enter__',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='context_manager',
                                        ctx=Load(),
                                    ),
                                    attr='__enter__',
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
                    name='__exit__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='exc_type', annotation=None, type_comment=None),
                            arg(arg='exc_value', annotation=None, type_comment=None),
                            arg(arg='traceback', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Try(
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='context_manager',
                                                ctx=Load(),
                                            ),
                                            attr='__exit__',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='exc_type', ctx=Load()),
                                            Name(id='exc_value', ctx=Load()),
                                            Name(id='traceback', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='profiler',
                                                ctx=Load(),
                                            ),
                                            attr='__exit__',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='exc_type', ctx=Load()),
                                            Name(id='exc_value', ctx=Load()),
                                            Name(id='traceback', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
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
