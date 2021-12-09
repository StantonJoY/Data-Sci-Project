Module(
    body=[
        Expr(
            value=Constant(value=' Test read_group grouping with many2many fields ', kind=None),
        ),
        ImportFrom(
            module='odoo.fields',
            names=[alias(name='Command', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestM2MGrouping',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
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
                                    attr='users',
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
                                        slice=Constant(value='test_read_group.user', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Mario', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Luigi', kind=None)],
                                            ),
                                        ],
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='tasks',
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
                                        slice=Constant(value='test_read_group.task', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='user_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Super Mario Bros.', kind=None),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='set',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='users',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='user_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Paper Mario', kind=None),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='set',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='users',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='user_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value="Luigi's Mansion", kind=None),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='set',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='cls', ctx=Load()),
                                                                                attr='users',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='user_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Donkey Kong', kind=None),
                                                    List(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='Command', ctx=Load()),
                                                                    attr='set',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[List(elts=[], ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
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
                    name='test_base_users',
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
                            targets=[Name(id='user_by_tasks', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='users',
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=List(elts=[], ctx=Load()),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[Constant(value='name:array_agg', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='task_ids', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='user_by_tasks', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='task_ids', kind=None),
                                                    Constant(value='task_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='tasks',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='Super Mario Bros.', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=2, kind=None),
                                                    List(
                                                        elts=[
                                                            Constant(value='Mario', kind=None),
                                                            Constant(value='Luigi', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='task_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='tasks',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='task_ids', kind=None),
                                                    Constant(value='task_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='tasks',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='Paper Mario', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1, kind=None),
                                                    List(
                                                        elts=[Constant(value='Mario', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='task_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='tasks',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=1, kind=None),
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='task_ids', kind=None),
                                                    Constant(value='task_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='tasks',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=2, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value="Luigi's Mansion", kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1, kind=None),
                                                    List(
                                                        elts=[Constant(value='Luigi', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='task_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='tasks',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=2, kind=None),
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
                    name='test_base_tasks',
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
                            targets=[Name(id='task_by_users', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tasks',
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='tasks',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
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
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[Constant(value='name:array_agg', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='user_ids', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='task_by_users', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='user_ids', kind=None),
                                                    Constant(value='user_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='users',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='Mario', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1, kind=None),
                                                    List(
                                                        elts=[Constant(value='Super Mario Bros.', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='&', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='users',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='tasks',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='user_ids', kind=None),
                                                    Constant(value='user_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='users',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='Luigi', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1, kind=None),
                                                    List(
                                                        elts=[Constant(value='Super Mario Bros.', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Constant(value='&', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='users',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='tasks',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
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
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='task_by_users', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tasks',
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=List(elts=[], ctx=Load()),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[Constant(value='name:array_agg', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='user_ids', kind=None)],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='task_by_users', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='user_ids', kind=None),
                                                    Constant(value='user_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='users',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='Mario', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=2, kind=None),
                                                    Call(
                                                        func=Name(id='unordered', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='Super Mario Bros.', kind=None),
                                                                    Constant(value='Paper Mario', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='users',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='user_ids', kind=None),
                                                    Constant(value='user_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='users',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='Luigi', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=2, kind=None),
                                                    Call(
                                                        func=Name(id='unordered', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='Super Mario Bros.', kind=None),
                                                                    Constant(value="Luigi's Mansion", kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='users',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=1, kind=None),
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='user_ids', kind=None),
                                                    Constant(value='user_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Call(
                                                        func=Name(id='unordered', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[Constant(value='Donkey Kong', kind=None)],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
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
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tasks_from_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tasks',
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='task_by_users', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='__domain', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tasks_from_domain', ctx=Load()),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tasks',
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=2, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tasks_from_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tasks',
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='task_by_users', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='__domain', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tasks_from_domain', ctx=Load()),
                                    BinOp(
                                        left=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tasks',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tasks',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tasks_from_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tasks',
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='task_by_users', ctx=Load()),
                                            slice=Constant(value=2, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='__domain', kind=None),
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tasks_from_domain', ctx=Load()),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='tasks',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=3, kind=None),
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
                    name='test_complex_case',
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
                            targets=[Name(id='users_model', ctx=Store())],
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
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='users',
                                            ctx=Load(),
                                        ),
                                        attr='_name',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.rule', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model_id', kind=None),
                                            Constant(value='domain_force', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Only The Lone Wanderer allowed', kind=None),
                                            Attribute(
                                                value=Name(id='users_model', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='users',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value='\n            SELECT\n                min("test_read_group_task".id) AS id,\n                count("test_read_group_task".id) AS "user_ids_count",\n                array_agg("test_read_group_task"."name") AS "name",\n                "test_read_group_task__user_ids"."user_id" AS "user_ids"\n            FROM "test_read_group_task"\n            LEFT JOIN "test_read_group_task_user_rel" AS "test_read_group_task__user_ids"\n                ON ("test_read_group_task"."id" = "test_read_group_task__user_ids"."task_id")\n            GROUP BY "test_read_group_task__user_ids"."user_id"\n            ORDER BY "user_ids"\n        ', kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueries',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Name(id='expected', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='as_admin', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='tasks',
                                                ctx=Load(),
                                            ),
                                            attr='read_group',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='domain',
                                                value=List(elts=[], ctx=Load()),
                                            ),
                                            keyword(
                                                arg='fields',
                                                value=List(
                                                    elts=[Constant(value='name:array_agg', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='groupby',
                                                value=List(
                                                    elts=[Constant(value='user_ids', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
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
                                    Name(id='as_admin', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='user_ids', kind=None),
                                                    Constant(value='user_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='users',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='Mario', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=2, kind=None),
                                                    Call(
                                                        func=Name(id='unordered', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='Super Mario Bros.', kind=None),
                                                                    Constant(value='Paper Mario', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='users',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='user_ids', kind=None),
                                                    Constant(value='user_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='users',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='Luigi', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=2, kind=None),
                                                    Call(
                                                        func=Name(id='unordered', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='Super Mario Bros.', kind=None),
                                                                    Constant(value="Luigi's Mansion", kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='users',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=1, kind=None),
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='user_ids', kind=None),
                                                    Constant(value='user_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Call(
                                                        func=Name(id='unordered', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[Constant(value='Donkey Kong', kind=None)],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
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
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='tasks', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='tasks',
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='browse_ref',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='base.user_demo', kind=None)],
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
                                    value=Name(id='tasks', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='domain',
                                        value=List(elts=[], ctx=Load()),
                                    ),
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[Constant(value='name:array_agg', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='user_ids', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=Constant(value='\n            SELECT\n                min("test_read_group_task".id) AS id,\n                count("test_read_group_task".id) AS "user_ids_count",\n                array_agg("test_read_group_task"."name") AS "name",\n                "test_read_group_task__user_ids"."user_id" AS "user_ids"\n            FROM "test_read_group_task"\n            LEFT JOIN "test_read_group_task_user_rel" AS "test_read_group_task__user_ids"\n                ON (\n                    "test_read_group_task"."id" = "test_read_group_task__user_ids"."task_id"\n                    AND "test_read_group_task__user_ids"."user_id" IN (\n                        SELECT "test_read_group_user".id\n                        FROM "test_read_group_user"\n                        WHERE ("test_read_group_user"."id" = %s)\n                    )\n                )\n            GROUP BY "test_read_group_task__user_ids"."user_id"\n            ORDER BY "user_ids"\n        ', kind=None),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertQueries',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Name(id='expected', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[Name(id='as_demo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='tasks', ctx=Load()),
                                            attr='read_group',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='domain',
                                                value=List(elts=[], ctx=Load()),
                                            ),
                                            keyword(
                                                arg='fields',
                                                value=List(
                                                    elts=[Constant(value='name:array_agg', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='groupby',
                                                value=List(
                                                    elts=[Constant(value='user_ids', kind=None)],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
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
                                    Name(id='as_demo', ctx=Load()),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='user_ids', kind=None),
                                                    Constant(value='user_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='users',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value=0, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='Mario', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=2, kind=None),
                                                    Call(
                                                        func=Name(id='unordered', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='Super Mario Bros.', kind=None),
                                                                    Constant(value='Paper Mario', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Subscript(
                                                                            value=Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='users',
                                                                                ctx=Load(),
                                                                            ),
                                                                            slice=Constant(value=0, kind=None),
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
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='user_ids', kind=None),
                                                    Constant(value='user_ids_count', kind=None),
                                                    Constant(value='name', kind=None),
                                                    Constant(value='__domain', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Call(
                                                        func=Name(id='unordered', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value="Luigi's Mansion", kind=None),
                                                                    Constant(value='Donkey Kong', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='user_ids', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
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
                    func=Attribute(
                        value=Name(id='common', ctx=Load()),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[Constant(value='test_m2m_read_group', kind=None)],
                    keywords=[],
                ),
            ],
        ),
        ClassDef(
            name='unordered',
            bases=[Name(id='list', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' A list where equality is interpreted without ordering. ', kind=None),
                ),
                Assign(
                    targets=[Name(id='__slots__', ctx=Store())],
                    value=Tuple(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                FunctionDef(
                    name='__eq__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Call(
                                    func=Name(id='sorted', ctx=Load()),
                                    args=[Name(id='self', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[Name(id='other', ctx=Load())],
                                        keywords=[],
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
                    name='__ne__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='other', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Compare(
                                left=Call(
                                    func=Name(id='sorted', ctx=Load()),
                                    args=[Name(id='self', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Call(
                                        func=Name(id='sorted', ctx=Load()),
                                        args=[Name(id='other', ctx=Load())],
                                        keywords=[],
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
    ],
    type_ignores=[],
)
