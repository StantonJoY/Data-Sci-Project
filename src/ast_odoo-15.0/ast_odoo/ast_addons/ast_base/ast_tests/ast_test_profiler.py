Module(
    body=[
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='BaseCase', asname=None),
                alias(name='TransactionCase', asname=None),
                alias(name='tagged', asname=None),
                alias(name='new_test_user', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='profiler', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.profiler',
            names=[
                alias(name='Profiler', asname=None),
                alias(name='ExecutionContext', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.speedscope',
            names=[alias(name='Speedscope', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestProfileAccess',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='test_profile',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.profile', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Dict(keys=[], values=[])],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_admin_has_access',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.profile', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='test_profile',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
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
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='test_profile',
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
                                        attr='test_profile',
                                        ctx=Load(),
                                    ),
                                    attr='read',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='name', kind=None)],
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
                    name='test_user_no_access',
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
                            targets=[Name(id='user', ctx=Store())],
                            value=Call(
                                func=Name(id='new_test_user', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='env',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='login',
                                        value=Constant(value='noProfile', kind=None),
                                    ),
                                    keyword(
                                        arg='groups',
                                        value=Constant(value='base.group_user', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='noProfile', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AccessError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.profile', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='AccessError', ctx=Load())],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='test_profile',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='user', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='read',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Constant(value='name', kind=None)],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                        Constant(value='profiling', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestSpeedscope',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='example_profile',
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
                            value=Dict(
                                keys=[
                                    Constant(value='init_stack_trace', kind=None),
                                    Constant(value='result', kind=None),
                                ],
                                values=[
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='/path/to/file_1.py', kind=None),
                                                    Constant(value=135, kind=None),
                                                    Constant(value='__main__', kind=None),
                                                    Constant(value='main()', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2.0, kind=None),
                                                    Tuple(elts=[], ctx=Load()),
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/file_1.py', kind=None),
                                                                    Constant(value=10, kind=None),
                                                                    Constant(value='main', kind=None),
                                                                    Constant(value='do_stuff1(test=do_tests)', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/file_1.py', kind=None),
                                                                    Constant(value=101, kind=None),
                                                                    Constant(value='do_stuff1', kind=None),
                                                                    Constant(value='cr.execute(query, params)', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=3.0, kind=None),
                                                    Tuple(elts=[], ctx=Load()),
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/file_1.py', kind=None),
                                                                    Constant(value=10, kind=None),
                                                                    Constant(value='main', kind=None),
                                                                    Constant(value='do_stuff1(test=do_tests)', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/file_1.py', kind=None),
                                                                    Constant(value=101, kind=None),
                                                                    Constant(value='do_stuff1', kind=None),
                                                                    Constant(value='cr.execute(query, params)', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/sql_db.py', kind=None),
                                                                    Constant(value=650, kind=None),
                                                                    Constant(value='execute', kind=None),
                                                                    Constant(value='res = self._obj.execute(query, params)', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=4.0, kind=None),
                                                    Tuple(elts=[], ctx=Load()),
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/file_1.py', kind=None),
                                                                    Constant(value=10, kind=None),
                                                                    Constant(value='main', kind=None),
                                                                    Constant(value='do_stuff1(test=do_tests)', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/file_1.py', kind=None),
                                                                    Constant(value=101, kind=None),
                                                                    Constant(value='do_stuff1', kind=None),
                                                                    Constant(value='cr.execute(query, params)', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/sql_db.py', kind=None),
                                                                    Constant(value=650, kind=None),
                                                                    Constant(value='execute', kind=None),
                                                                    Constant(value='res = self._obj.execute(query, params)', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=6.0, kind=None),
                                                    Tuple(elts=[], ctx=Load()),
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/file_1.py', kind=None),
                                                                    Constant(value=10, kind=None),
                                                                    Constant(value='main', kind=None),
                                                                    Constant(value='do_stuff1(test=do_tests)', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/file_1.py', kind=None),
                                                                    Constant(value=101, kind=None),
                                                                    Constant(value='do_stuff1', kind=None),
                                                                    Constant(value='check', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/sql_db.py', kind=None),
                                                                    Constant(value=650, kind=None),
                                                                    Constant(value='check', kind=None),
                                                                    Constant(value='assert x = y', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=10.0, kind=None),
                                                    Tuple(elts=[], ctx=Load()),
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/file_1.py', kind=None),
                                                                    Constant(value=10, kind=None),
                                                                    Constant(value='main', kind=None),
                                                                    Constant(value='do_stuff1(test=do_tests)', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Constant(value='/path/to/file_1.py', kind=None),
                                                                    Constant(value=101, kind=None),
                                                                    Constant(value='do_stuff1', kind=None),
                                                                    Constant(value='for i in range(10):', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=10.35, kind=None),
                                                    Tuple(elts=[], ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                            ),
                                        ],
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
                    name='test_convert_empty',
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
                                        func=Name(id='Speedscope', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='make',
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
                    name='test_converts_profile_simple',
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
                            targets=[Name(id='profile', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='example_profile',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sp', ctx=Store())],
                            value=Call(
                                func=Name(id='Speedscope', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='init_stack_trace',
                                        value=Subscript(
                                            value=Name(id='profile', ctx=Load()),
                                            slice=Constant(value='init_stack_trace', kind=None),
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
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='profile', kind=None),
                                    Subscript(
                                        value=Name(id='profile', ctx=Load()),
                                        slice=Constant(value='result', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add_output',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='profile', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='complete',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='make',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='frames', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='shared', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='frames', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='frames', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='profile_combined', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='profiles', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='frame', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='e', ctx=Store()),
                                        iter=Subscript(
                                            value=Name(id='profile_combined', ctx=Load()),
                                            slice=Constant(value='events', kind=None),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='events', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='profile_combined', ctx=Load()),
                                                slice=Constant(value='events', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='at', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=0.0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='profile_combined', ctx=Load()),
                                                slice=Constant(value='events', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='at', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=8.35, kind=None),
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
                    name='test_converts_profile_no_end',
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
                            targets=[Name(id='profile', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='example_profile',
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
                                    value=Subscript(
                                        value=Name(id='profile', ctx=Load()),
                                        slice=Constant(value='result', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sp', ctx=Store())],
                            value=Call(
                                func=Name(id='Speedscope', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='init_stack_trace',
                                        value=Subscript(
                                            value=Name(id='profile', ctx=Load()),
                                            slice=Constant(value='init_stack_trace', kind=None),
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
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='profile', kind=None),
                                    Subscript(
                                        value=Name(id='profile', ctx=Load()),
                                        slice=Constant(value='result', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add_output',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='profile', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='complete',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='make',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='profile_combined', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='profiles', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='frame', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='e', ctx=Store()),
                                        iter=Subscript(
                                            value=Name(id='profile_combined', ctx=Load()),
                                            slice=Constant(value='events', kind=None),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='events', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='profile_combined', ctx=Load()),
                                                slice=Constant(value='events', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='at', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=8, kind=None),
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
                    name='test_converts_init_stack_trace',
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
                            targets=[Name(id='profile', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='example_profile',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sp', ctx=Store())],
                            value=Call(
                                func=Name(id='Speedscope', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='init_stack_trace',
                                        value=Subscript(
                                            value=Name(id='profile', ctx=Load()),
                                            slice=Constant(value='init_stack_trace', kind=None),
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
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='profile', kind=None),
                                    Subscript(
                                        value=Name(id='profile', ctx=Load()),
                                        slice=Constant(value='result', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add_output',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='profile', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='complete',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='make',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='profile_combined', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='profiles', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='frame', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='e', ctx=Store()),
                                        iter=Subscript(
                                            value=Name(id='profile_combined', ctx=Load()),
                                            slice=Constant(value='events', kind=None),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='events', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value=4, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='profile_combined', ctx=Load()),
                                                slice=Constant(value='events', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='at', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=8.35, kind=None),
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
                    name='test_end_priority',
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
                            value=Constant(value='\n        If a sample as a time (usually a query) we expect to keep the complete frame\n        even if another concurent frame tics before the end of the current one:\n        frame duration should always be more reliable.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='async_profile', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='example_profile',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value='result', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sql_profile', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='example_profile',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value='result', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sql_profile', ctx=Store())],
                            value=List(
                                elts=[
                                    Subscript(
                                        value=Name(id='sql_profile', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='sql_profile', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='start', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=2.5, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='sql_profile', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='time', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=3, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='sql_profile', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='query', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='SELECT 1', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Subscript(
                                        value=Name(id='sql_profile', ctx=Load()),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='full_query', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='SELECT 1', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='async_profile', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='start', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=3, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='async_profile', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='start', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=4, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='query', kind=None),
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='async_profile', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stack', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='time', kind=None),
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='async_profile', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stack', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='async_profile', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stack', kind=None),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='async_profile', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stack', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sp', ctx=Store())],
                            value=Call(
                                func=Name(id='Speedscope', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='init_stack_trace',
                                        value=List(elts=[], ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='sql', kind=None),
                                    Name(id='async_profile', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='traces', kind=None),
                                    Name(id='sql_profile', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add_output',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Constant(value='sql', kind=None),
                                            Constant(value='traces', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='complete',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='make',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='profile_combined', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Name(id='res', ctx=Load()),
                                    slice=Constant(value='profiles', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        BinOp(
                                            left=Subscript(
                                                value=Name(id='e', ctx=Load()),
                                                slice=Constant(value='at', kind=None),
                                                ctx=Load(),
                                            ),
                                            op=Add(),
                                            right=Constant(value=2, kind=None),
                                        ),
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='shared', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='frames', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Subscript(
                                                    value=Name(id='e', ctx=Load()),
                                                    slice=Constant(value='frame', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='e', ctx=Store()),
                                        iter=Subscript(
                                            value=Name(id='profile_combined', ctx=Load()),
                                            slice=Constant(value='events', kind=None),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='events', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=2.0, kind=None),
                                                    Constant(value='O', kind=None),
                                                    Constant(value='main', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=2.0, kind=None),
                                                    Constant(value='O', kind=None),
                                                    Constant(value='do_stuff1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=2.5, kind=None),
                                                    Constant(value='O', kind=None),
                                                    Constant(value='execute', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=2.5, kind=None),
                                                    Constant(value='O', kind=None),
                                                    Constant(value="sql('SELECT 1')", kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=5.5, kind=None),
                                                    Constant(value='C', kind=None),
                                                    Constant(value="sql('SELECT 1')", kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=5.5, kind=None),
                                                    Constant(value='C', kind=None),
                                                    Constant(value='execute', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=6.0, kind=None),
                                                    Constant(value='O', kind=None),
                                                    Constant(value='check', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=10.0, kind=None),
                                                    Constant(value='C', kind=None),
                                                    Constant(value='check', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=10.35, kind=None),
                                                    Constant(value='C', kind=None),
                                                    Constant(value='do_stuff1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=10.35, kind=None),
                                                    Constant(value='C', kind=None),
                                                    Constant(value='main', kind=None),
                                                ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_converts_context',
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
                            value=List(
                                elts=[
                                    List(
                                        elts=[
                                            Constant(value='file.py', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value='level1', kind=None),
                                            Constant(value='level1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='file.py', kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value='level2', kind=None),
                                            Constant(value='level2', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='profile', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='init_stack_trace', kind=None),
                                    Constant(value='result', kind=None),
                                ],
                                values=[
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='file.py', kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='level0', kind=None),
                                                    Constant(value='level0)', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2.0, kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=2, kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='a', kind=None)],
                                                                        values=[Constant(value='1', kind=None)],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=3, kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='b', kind=None)],
                                                                        values=[Constant(value='1', kind=None)],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[Name(id='stack', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=3.0, kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=2, kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='a', kind=None)],
                                                                        values=[Constant(value='1', kind=None)],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=3, kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='b', kind=None)],
                                                                        values=[Constant(value='2', kind=None)],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[Name(id='stack', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=10.35, kind=None),
                                                    Tuple(elts=[], ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sp', ctx=Store())],
                            value=Call(
                                func=Name(id='Speedscope', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='init_stack_trace',
                                        value=Subscript(
                                            value=Name(id='profile', ctx=Load()),
                                            slice=Constant(value='init_stack_trace', kind=None),
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
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='profile', kind=None),
                                    Subscript(
                                        value=Name(id='profile', ctx=Load()),
                                        slice=Constant(value='result', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add_output',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='profile', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='complete',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='make',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='shared', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='frames', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Subscript(
                                                    value=Name(id='e', ctx=Load()),
                                                    slice=Constant(value='frame', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='e', ctx=Store()),
                                        iter=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='profiles', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='events', kind=None),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='events', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='level0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='a=1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='level1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='b=1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='level2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='level2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='b=1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='b=2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='level2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='level2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='b=2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='level1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='a=1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='level0', kind=None),
                                                ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_converts_context_nested',
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
                            value=List(
                                elts=[
                                    List(
                                        elts=[
                                            Constant(value='file.py', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value='level1', kind=None),
                                            Constant(value='level1', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='file.py', kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value='level2', kind=None),
                                            Constant(value='level2', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='profile', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='init_stack_trace', kind=None),
                                    Constant(value='result', kind=None),
                                ],
                                values=[
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='file.py', kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='level0', kind=None),
                                                    Constant(value='level0)', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2.0, kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=3, kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='a', kind=None)],
                                                                        values=[Constant(value='1', kind=None)],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=3, kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='b', kind=None)],
                                                                        values=[Constant(value='1', kind=None)],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[Name(id='stack', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=10.35, kind=None),
                                                    Tuple(elts=[], ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sp', ctx=Store())],
                            value=Call(
                                func=Name(id='Speedscope', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='init_stack_trace',
                                        value=Subscript(
                                            value=Name(id='profile', ctx=Load()),
                                            slice=Constant(value='init_stack_trace', kind=None),
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
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='profile', kind=None),
                                    Subscript(
                                        value=Name(id='profile', ctx=Load()),
                                        slice=Constant(value='result', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add_output',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='profile', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='complete',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='make',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='shared', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='frames', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Subscript(
                                                    value=Name(id='e', ctx=Load()),
                                                    slice=Constant(value='frame', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='e', ctx=Store()),
                                        iter=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='profiles', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='events', kind=None),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='events', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='level0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='level1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='a=1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='b=1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='level2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='level2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='b=1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='a=1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='level1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='level0', kind=None),
                                                ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_converts_context_lower',
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
                            value=List(
                                elts=[
                                    List(
                                        elts=[
                                            Constant(value='file.py', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value='level4', kind=None),
                                            Constant(value='level4', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='file.py', kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value='level5', kind=None),
                                            Constant(value='level5', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='profile', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='init_stack_trace', kind=None),
                                    Constant(value='result', kind=None),
                                ],
                                values=[
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='file.py', kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='level0', kind=None),
                                                    Constant(value='level0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='file.py', kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='level1', kind=None),
                                                    Constant(value='level1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='file.py', kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='level2', kind=None),
                                                    Constant(value='level2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='file.py', kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='level3', kind=None),
                                                    Constant(value='level3', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2.0, kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=2, kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='a', kind=None)],
                                                                        values=[Constant(value='1', kind=None)],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=6, kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='b', kind=None)],
                                                                        values=[Constant(value='1', kind=None)],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[Name(id='stack', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=10.35, kind=None),
                                                    Tuple(elts=[], ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sp', ctx=Store())],
                            value=Call(
                                func=Name(id='Speedscope', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='init_stack_trace',
                                        value=Subscript(
                                            value=Name(id='profile', ctx=Load()),
                                            slice=Constant(value='init_stack_trace', kind=None),
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
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='profile', kind=None),
                                    Subscript(
                                        value=Name(id='profile', ctx=Load()),
                                        slice=Constant(value='result', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add_output',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='profile', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='complete',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='make',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='shared', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='frames', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Subscript(
                                                    value=Name(id='e', ctx=Load()),
                                                    slice=Constant(value='frame', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='e', ctx=Store()),
                                        iter=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='profiles', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='events', kind=None),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='events', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='level4', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='b=1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='level5', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='level5', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='b=1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='level4', kind=None),
                                                ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_converts_no_context',
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
                            value=List(
                                elts=[
                                    List(
                                        elts=[
                                            Constant(value='file.py', kind=None),
                                            Constant(value=10, kind=None),
                                            Constant(value='level4', kind=None),
                                            Constant(value='level4', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='file.py', kind=None),
                                            Constant(value=11, kind=None),
                                            Constant(value='level5', kind=None),
                                            Constant(value='level5', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='profile', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='init_stack_trace', kind=None),
                                    Constant(value='result', kind=None),
                                ],
                                values=[
                                    List(
                                        elts=[
                                            List(
                                                elts=[
                                                    Constant(value='file.py', kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='level0', kind=None),
                                                    Constant(value='level0', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='file.py', kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='level1', kind=None),
                                                    Constant(value='level1', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='file.py', kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='level2', kind=None),
                                                    Constant(value='level2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='file.py', kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value='level3', kind=None),
                                                    Constant(value='level3', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2.0, kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=2, kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='a', kind=None)],
                                                                        values=[Constant(value='1', kind=None)],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=6, kind=None),
                                                                    Dict(
                                                                        keys=[Constant(value='b', kind=None)],
                                                                        values=[Constant(value='1', kind=None)],
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[Name(id='stack', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='start', kind=None),
                                                    Constant(value='exec_context', kind=None),
                                                    Constant(value='stack', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=10.35, kind=None),
                                                    Tuple(elts=[], ctx=Load()),
                                                    Constant(value=None, kind=None),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sp', ctx=Store())],
                            value=Call(
                                func=Name(id='Speedscope', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='init_stack_trace',
                                        value=Subscript(
                                            value=Name(id='profile', ctx=Load()),
                                            slice=Constant(value='init_stack_trace', kind=None),
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
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='profile', kind=None),
                                    Subscript(
                                        value=Name(id='profile', ctx=Load()),
                                        slice=Constant(value='result', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='add_output',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Constant(value='profile', kind=None)],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='complete',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='use_context',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='sp', ctx=Load()),
                                    attr='make',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=ListComp(
                                elt=Tuple(
                                    elts=[
                                        Subscript(
                                            value=Name(id='e', ctx=Load()),
                                            slice=Constant(value='type', kind=None),
                                            ctx=Load(),
                                        ),
                                        Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Name(id='res', ctx=Load()),
                                                        slice=Constant(value='shared', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='frames', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Subscript(
                                                    value=Name(id='e', ctx=Load()),
                                                    slice=Constant(value='frame', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='name', kind=None),
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='e', ctx=Store()),
                                        iter=Subscript(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='profiles', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='events', kind=None),
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='events', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='level4', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='O', kind=None),
                                                    Constant(value='level5', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='level5', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='C', kind=None),
                                                    Constant(value='level4', kind=None),
                                                ],
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                        Constant(value='profiling', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='TestProfiling',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_default_values',
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
                            targets=[Name(id='p', ctx=Store())],
                            value=Call(
                                func=Name(id='Profiler', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='p', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='cr',
                                            ctx=Load(),
                                        ),
                                        attr='dbname',
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
                    name='test_env_profiler_database',
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
                            targets=[Name(id='p', ctx=Store())],
                            value=Call(
                                func=Name(id='Profiler', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='collectors',
                                        value=List(elts=[], ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='p', ctx=Load()),
                                        attr='db',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='cr',
                                            ctx=Load(),
                                        ),
                                        attr='dbname',
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
                    name='test_env_profiler_description',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Profiler', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='collectors',
                                                value=List(elts=[], ctx=Load()),
                                            ),
                                            keyword(
                                                arg='db',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='p', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='test_env_profiler_description', kind=None),
                                            Attribute(
                                                value=Name(id='p', ctx=Load()),
                                                attr='description',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_execution_context_save',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Profiler', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='db',
                                                value=Constant(value=None, kind=None),
                                            ),
                                            keyword(
                                                arg='collectors',
                                                value=List(
                                                    elts=[Constant(value='sql', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='p', ctx=Store()),
                                ),
                            ],
                            body=[
                                For(
                                    target=Name(id='letter', ctx=Store()),
                                    iter=Tuple(
                                        elts=[
                                            Constant(value='a', kind=None),
                                            Constant(value='b', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='stack_level', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='profiler', ctx=Load()),
                                                    attr='stack_size',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Name(id='ExecutionContext', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='letter',
                                                                value=Name(id='letter', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    optional_vars=None,
                                                ),
                                            ],
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
                                                        args=[Constant(value='SELECT 1', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='entries', ctx=Store())],
                            value=Attribute(
                                value=Subscript(
                                    value=Attribute(
                                        value=Name(id='p', ctx=Load()),
                                        attr='collectors',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                attr='entries',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='entries', ctx=Load()),
                                                attr='pop',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=0, kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='exec_context', kind=None),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Name(id='stack_level', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='letter', kind=None)],
                                                        values=[Constant(value='a', kind=None)],
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='entries', ctx=Load()),
                                                attr='pop',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=0, kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='exec_context', kind=None),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Name(id='stack_level', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='letter', kind=None)],
                                                        values=[Constant(value='b', kind=None)],
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_execution_context_nested',
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
                            value=Constant(value='\n        This test checks that an execution can be nested at the same level of the stack.\n        ', kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Profiler', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='db',
                                                value=Constant(value=None, kind=None),
                                            ),
                                            keyword(
                                                arg='collectors',
                                                value=List(
                                                    elts=[Constant(value='sql', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='p', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='stack_level', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='profiler', ctx=Load()),
                                            attr='stack_size',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Name(id='ExecutionContext', ctx=Load()),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='letter',
                                                        value=Constant(value='a', kind=None),
                                                    ),
                                                ],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
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
                                                args=[Constant(value='SELECT 1', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Name(id='ExecutionContext', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='letter',
                                                                value=Constant(value='b', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    optional_vars=None,
                                                ),
                                            ],
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
                                                        args=[Constant(value='SELECT 1', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Name(id='ExecutionContext', ctx=Load()),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='letter',
                                                                value=Constant(value='c', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    optional_vars=None,
                                                ),
                                            ],
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
                                                        args=[Constant(value='SELECT 1', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
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
                                                args=[Constant(value='SELECT 1', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='entries', ctx=Store())],
                            value=Attribute(
                                value=Subscript(
                                    value=Attribute(
                                        value=Name(id='p', ctx=Load()),
                                        attr='collectors',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Load(),
                                ),
                                attr='entries',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='entries', ctx=Load()),
                                                attr='pop',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=0, kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='exec_context', kind=None),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Name(id='stack_level', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='letter', kind=None)],
                                                        values=[Constant(value='a', kind=None)],
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='entries', ctx=Load()),
                                                attr='pop',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=0, kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='exec_context', kind=None),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Name(id='stack_level', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='letter', kind=None)],
                                                        values=[Constant(value='a', kind=None)],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='stack_level', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='letter', kind=None)],
                                                        values=[Constant(value='b', kind=None)],
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='entries', ctx=Load()),
                                                attr='pop',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=0, kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='exec_context', kind=None),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Name(id='stack_level', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='letter', kind=None)],
                                                        values=[Constant(value='a', kind=None)],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Name(id='stack_level', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='letter', kind=None)],
                                                        values=[Constant(value='c', kind=None)],
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
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='entries', ctx=Load()),
                                                attr='pop',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=0, kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value='exec_context', kind=None),
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Name(id='stack_level', ctx=Load()),
                                                    Dict(
                                                        keys=[Constant(value='letter', kind=None)],
                                                        values=[Constant(value='a', kind=None)],
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_sync_recorder',
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
                        FunctionDef(
                            name='a',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='b', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='c', ctx=Load()),
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
                            name='b',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[Pass()],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='c',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='d', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Name(id='d', ctx=Load()),
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
                            name='d',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[Pass()],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Profiler', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='description',
                                                value=Constant(value='test', kind=None),
                                            ),
                                            keyword(
                                                arg='collectors',
                                                value=List(
                                                    elts=[Constant(value='traces_sync', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='db',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='p', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='a', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stacks', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='r', ctx=Load()),
                                    slice=Constant(value='stack', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='collectors',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='entries',
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='stacks_methods', ctx=Store())],
                            value=ListComp(
                                elt=ListComp(
                                    elt=Subscript(
                                        value=Name(id='frame', ctx=Load()),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
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
                                generators=[
                                    comprehension(
                                        target=Name(id='stack', ctx=Store()),
                                        iter=Name(id='stacks', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='stacks_methods', ctx=Load()),
                                    List(
                                        elts=[
                                            List(
                                                elts=[Constant(value='a', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='b', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='a', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='c', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='c', kind=None),
                                                    Constant(value='d', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='c', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='c', kind=None),
                                                    Constant(value='d', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='a', kind=None),
                                                    Constant(value='c', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='a', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(elts=[], ctx=Load()),
                                            List(
                                                elts=[Constant(value='__exit__', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='__exit__', kind=None),
                                                    Constant(value='stop', kind=None),
                                                ],
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
                            targets=[Name(id='stacks_lines', ctx=Store())],
                            value=ListComp(
                                elt=ListComp(
                                    elt=Subscript(
                                        value=Name(id='frame', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
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
                                generators=[
                                    comprehension(
                                        target=Name(id='stack', ctx=Store()),
                                        iter=Name(id='stacks', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Subscript(
                                            value=Subscript(
                                                value=Name(id='stacks_lines', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='stacks_lines', ctx=Load()),
                                            slice=Constant(value=3, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='Call of b() in a() should be one line before call of c()', kind=None),
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
                    name='test_qweb_recorder',
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
                            targets=[Name(id='template', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="root">\n                <t t-foreach="{\'a\': 3, \'b\': 2, \'c\': 1}" t-as="item">\n                    [<t t-esc="item_index"/>: <t t-call="base.dummy"/> <t t-esc="item_value"/>]\n                    <b t-esc="add_one_query()"/>\n                </t>\n            </t>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='child_template', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='arch_db', kind=None),
                                        ],
                                        values=[
                                            Constant(value='test', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<t t-name="dummy"><span><t t-esc="item"/> <t t-esc="add_one_query()"/></span></t>', kind=None),
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
                                    Constant(value="INSERT INTO ir_model_data(name, model, res_id, module)VALUES ('dummy', 'ir.ui.view', %s, 'base')", kind=None),
                                    List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='child_template', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='add_one_query', kind=None)],
                                values=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=BoolOp(
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
                                                        attr='execute',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='SELECT id FROM ir_ui_view LIMIT 1', kind=None)],
                                                    keywords=[],
                                                ),
                                                Constant(value='query', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value='\n                    [0: <span>a query</span> 3]\n                    <b>query</b>\n                    [1: <span>b query</span> 2]\n                    <b>query</b>\n                    [2: <span>c query</span> 1]\n                    <b>query</b>\n        ', kind='u'),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rendered', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.qweb', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='template', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='rendered', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='result', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='Without profiling', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Profiler', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='description',
                                                value=Constant(value='test', kind=None),
                                            ),
                                            keyword(
                                                arg='collectors',
                                                value=List(
                                                    elts=[Constant(value='qweb', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='db',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.qweb', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Profiler', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='description',
                                                value=Constant(value='test', kind=None),
                                            ),
                                            keyword(
                                                arg='collectors',
                                                value=List(
                                                    elts=[Constant(value='qweb', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='db',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='p', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='rendered', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.qweb', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='rendered', ctx=Load()),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='result', ctx=Load()),
                                                    attr='strip',
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='p', ctx=Load()),
                                                            attr='collectors',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='entries',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='results', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='archs', kind=None),
                                        ctx=Load(),
                                    ),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='child_template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='arch_db',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='child_template', ctx=Load()),
                                                attr='arch_db',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='data', ctx=Store()),
                            iter=Subscript(
                                value=Subscript(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='collectors',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='entries',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='results', kind=None),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='data', kind=None),
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='delay', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t', kind=None),
                                            Constant(value='t-foreach="{\'a\': 3, \'b\': 2, \'c\': 1}" t-as=\'item\'', kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t/t[1]', kind=None),
                                            Constant(value="t-esc='item_index'", kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t/t[2]', kind=None),
                                            Constant(value="t-call='base.dummy'", kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='child_template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/span/t[1]', kind=None),
                                            Constant(value="t-esc='item'", kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='child_template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/span/t[2]', kind=None),
                                            Constant(value="t-esc='add_one_query()'", kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t/t[3]', kind=None),
                                            Constant(value="t-esc='item_value'", kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t/b', kind=None),
                                            Constant(value="t-esc='add_one_query()'", kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t/t[1]', kind=None),
                                            Constant(value="t-esc='item_index'", kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t/t[2]', kind=None),
                                            Constant(value="t-call='base.dummy'", kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='child_template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/span/t[1]', kind=None),
                                            Constant(value="t-esc='item'", kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='child_template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/span/t[2]', kind=None),
                                            Constant(value="t-esc='add_one_query()'", kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t/t[3]', kind=None),
                                            Constant(value="t-esc='item_value'", kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t/b', kind=None),
                                            Constant(value="t-esc='add_one_query()'", kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t/t[1]', kind=None),
                                            Constant(value="t-esc='item_index'", kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t/t[2]', kind=None),
                                            Constant(value="t-call='base.dummy'", kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='child_template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/span/t[1]', kind=None),
                                            Constant(value="t-esc='item'", kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='child_template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/span/t[2]', kind=None),
                                            Constant(value="t-esc='add_one_query()'", kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t/t[3]', kind=None),
                                            Constant(value="t-esc='item_value'", kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='xpath', kind=None),
                                            Constant(value='directive', kind=None),
                                            Constant(value='query', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/t/t/b', kind=None),
                                            Constant(value="t-esc='add_one_query()'", kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='p', ctx=Load()),
                                                            attr='collectors',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='entries',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='results', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='data', kind=None),
                                        ctx=Load(),
                                    ),
                                    Name(id='expected', ctx=Load()),
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
                    name='test_default_recorders',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Profiler', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='db',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='p', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='queries_start', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='cr',
                                            ctx=Load(),
                                        ),
                                        attr='sql_log_count',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='i', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[Constant(value=10, kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='name', kind=None)],
                                                        values=[
                                                            BinOp(
                                                                left=Constant(value='snail%s', kind=None),
                                                                op=Mod(),
                                                                right=Name(id='i', ctx=Load()),
                                                            ),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='flush',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='total_queries', ctx=Store())],
                                    value=BinOp(
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
                                            attr='sql_log_count',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Name(id='queries_start', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rq', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Name(id='next', ctx=Load()),
                                    args=[
                                        GeneratorExp(
                                            elt=Name(id='r', ctx=Load()),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='r', ctx=Store()),
                                                    iter=Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='collectors',
                                                        ctx=Load(),
                                                    ),
                                                    ifs=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='r', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='sql', kind=None)],
                                                        ),
                                                    ],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                attr='entries',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='p', ctx=Load()),
                                                attr='init_stack_trace',
                                                ctx=Load(),
                                            ),
                                            slice=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='test_default_recorders', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='p', ctx=Load()),
                                                            attr='init_stack_trace',
                                                            ctx=Load(),
                                                        ),
                                                        slice=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='/', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Constant(value='test_profiler.py', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='rq', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='total_queries', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='first_query', ctx=Store())],
                            value=Subscript(
                                value=Name(id='rq', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='first_query', ctx=Load()),
                                                slice=Constant(value='stack', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='create', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGreater',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='first_query', ctx=Load()),
                                        slice=Constant(value='time', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Subscript(
                                                value=Name(id='first_query', ctx=Load()),
                                                slice=Constant(value='stack', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='execute', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='first_query', ctx=Load()),
                                                            slice=Constant(value='stack', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        slice=UnaryOp(
                                                            op=USub(),
                                                            operand=Constant(value=1, kind=None),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='/', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    Constant(value='sql_db.py', kind=None),
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                        Constant(value='profiling', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
        FunctionDef(
            name='deep_call',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='func', annotation=None, type_comment=None),
                    arg(arg='depth', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Call the given function at the given call depth. ', kind=None),
                ),
                If(
                    test=Compare(
                        left=Name(id='depth', ctx=Load()),
                        ops=[Gt()],
                        comparators=[Constant(value=0, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Name(id='deep_call', ctx=Load()),
                                args=[
                                    Name(id='func', ctx=Load()),
                                    BinOp(
                                        left=Name(id='depth', ctx=Load()),
                                        op=Sub(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='func', ctx=Load()),
                                args=[],
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
        ClassDef(
            name='TestPerformance',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_collector_max_frequency',
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
                            value=Constant(value='\n        Check the creation time of an entry\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='collector', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='profiler', ctx=Load()),
                                    attr='Collector',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='p', ctx=Store())],
                            value=Call(
                                func=Name(id='Profiler', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='collectors',
                                        value=List(
                                            elts=[Name(id='collector', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='db',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='collect',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='collector', ctx=Load()),
                                            attr='add',
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
                        With(
                            items=[
                                withitem(
                                    context_expr=Name(id='p', ctx=Load()),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='start', ctx=Store())],
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
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='start', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                        ops=[Gt()],
                                        comparators=[
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
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='deep_call', ctx=Load()),
                                                args=[
                                                    Name(id='collect', ctx=Load()),
                                                    Constant(value=20, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGreater',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
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
                                    Constant(value=20000, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='collector', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='profiler', ctx=Load()),
                                    attr='Collector',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='p', ctx=Store())],
                            value=Call(
                                func=Name(id='Profiler', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='collectors',
                                        value=List(
                                            elts=[Name(id='collector', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='db',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='collect_1_s',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Assign(
                                    targets=[Name(id='start', ctx=Store())],
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
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='start', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                        ops=[Gt()],
                                        comparators=[
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
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='collector', ctx=Load()),
                                                    attr='add',
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
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Name(id='p', ctx=Load()),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='deep_call', ctx=Load()),
                                        args=[
                                            Name(id='collect_1_s', ctx=Load()),
                                            Constant(value=20, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGreater',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
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
                                    Constant(value=50000, kind=None),
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
                    name='test_frequencies_1ms_sleep',
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
                            value=Constant(value='\n        Check the number of entries generated in 1s at 1kHz\n        we need to artificially change the frame as often as possible to avoid\n        triggering the memory optimisation skipping identical frames\n        ', kind=None),
                        ),
                        FunctionDef(
                            name='sleep_1',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='sleep',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0.0001, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='sleep_2',
                            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='sleep',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=0.0001, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Profiler', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='collectors',
                                                value=List(
                                                    elts=[Constant(value='traces_async', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='db',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='res', ctx=Store()),
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='start', ctx=Store())],
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
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='start', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                        ops=[Gt()],
                                        comparators=[
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
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='sleep_1', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Name(id='sleep_2', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='entry_count', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='res', ctx=Load()),
                                                attr='collectors',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='entries',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertGreater',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='entry_count', ctx=Load()),
                                    Constant(value=700, kind=None),
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
                    name='test_traces_async_memory_optimisation',
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
                            value=Constant(value='\n        Identical frames should be saved only once.\n        We should only have a few entries on a 1 second sleep.\n        ', kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Profiler', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='collectors',
                                                value=List(
                                                    elts=[Constant(value='traces_async', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='db',
                                                value=Constant(value=None, kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=Name(id='res', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='time', ctx=Load()),
                                            attr='sleep',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=1, kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='entry_count', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='res', ctx=Load()),
                                                attr='collectors',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='entries',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLess',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='entry_count', ctx=Load()),
                                    Constant(value=5, kind=None),
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
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[
                        Constant(value='-standard', kind=None),
                        Constant(value='profiling_performance', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
