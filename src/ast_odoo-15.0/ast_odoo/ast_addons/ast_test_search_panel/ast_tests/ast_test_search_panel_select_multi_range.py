Module(
    body=[
        Import(
            names=[alias(name='odoo.tests', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Assign(
            targets=[Name(id='SEARCH_PANEL_ERROR', ctx=Store())],
            value=Dict(
                keys=[Constant(value='error_msg', kind=None)],
                values=[Constant(value='Too many items to display.', kind=None)],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='TestSelectRangeMulti',
            bases=[
                Attribute(
                    value=Attribute(
                        value=Name(id='odoo', ctx=Load()),
                        attr='tests',
                        ctx=Load(),
                    ),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                                    attr='setUp',
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
                                    attr='SourceModel',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_search_panel.source_model', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='TargetModel',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_search_panel.filter_target_model', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='GroupByModel',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_search_panel.category_target_model', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_many2one_empty',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                    name='test_many2one',
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
                            targets=[Name(id='folders', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='GroupByModel',
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
                                                values=[Constant(value='Folder 1', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Folder 2', kind=None)],
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
                                Tuple(
                                    elts=[
                                        Name(id='f1_id', ctx=Store()),
                                        Name(id='f2_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='folders', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='TargetModel',
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
                                                    Constant(value='folder_id', kind=None),
                                                    Constant(value='color', kind=None),
                                                    Constant(value='status', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value='Red', kind=None),
                                                    Constant(value='cool', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='folder_id', kind=None),
                                                    Constant(value='status', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value='cool', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='color', kind=None),
                                                    Constant(value='status', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 3', kind=None),
                                                    Constant(value='Green', kind=None),
                                                    Constant(value='cool', kind=None),
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
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='t1_id', ctx=Store()),
                                        Name(id='t2_id', ctx=Store()),
                                        Name(id='t3_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='tags', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
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
                                                    Constant(value='tag_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='tag_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 2', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='tag_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 3', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Rec 4', kind=None)],
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
                                Tuple(
                                    elts=[
                                        Name(id='r1_id', ctx=Store()),
                                        Name(id='r2_id', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='records', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='folder_id', kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value='Folder 2', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value='Folder 1', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Constant(value='Not Set', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='status', kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Constant(value='cool', kind=None),
                                                    Constant(value='Cool', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                    Constant(value='cool', kind=None),
                                                    Constant(value='Cool', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
                                                    Constant(value='cool', kind=None),
                                                    Constant(value='Cool', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='color', kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Constant(value='Red', kind=None),
                                                    Constant(value='Red', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Constant(value='Not Set', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
                                                    Constant(value='Green', kind=None),
                                                    Constant(value='Green', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        List(
                                                            elts=[
                                                                Name(id='r1_id', ctx=Load()),
                                                                Name(id='r2_id', ctx=Load()),
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=2, kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='SEARCH_PANEL_ERROR', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='folder_id', kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value='Folder 2', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value='Folder 1', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Constant(value='Not Set', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        List(
                                                            elts=[
                                                                Name(id='r1_id', ctx=Load()),
                                                                Name(id='r2_id', ctx=Load()),
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='folder_id', kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value='Folder 2', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value='Folder 1', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        List(
                                                            elts=[
                                                                Name(id='r1_id', ctx=Load()),
                                                                Name(id='r2_id', ctx=Load()),
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=2, kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='SEARCH_PANEL_ERROR', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='folder_id', kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value='Folder 2', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value='Folder 1', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        List(
                                                            elts=[
                                                                Name(id='r1_id', ctx=Load()),
                                                                Name(id='r2_id', ctx=Load()),
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='comodel_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        List(
                                                            elts=[
                                                                Name(id='t2_id', ctx=Load()),
                                                                Name(id='t3_id', ctx=Load()),
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
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
                    name='test_many2many_empty',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(elts=[], ctx=Load()),
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
                    name='test_many2many',
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
                            targets=[Name(id='folders', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='GroupByModel',
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
                                                values=[Constant(value='Folder 1', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Folder 2', kind=None)],
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
                                Tuple(
                                    elts=[
                                        Name(id='f1_id', ctx=Store()),
                                        Name(id='f2_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='folders', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='TargetModel',
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
                                                    Constant(value='folder_id', kind=None),
                                                    Constant(value='color', kind=None),
                                                    Constant(value='status', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value='Red', kind=None),
                                                    Constant(value='cool', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='folder_id', kind=None),
                                                    Constant(value='status', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value='cool', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='color', kind=None),
                                                    Constant(value='status', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 3', kind=None),
                                                    Constant(value='Green', kind=None),
                                                    Constant(value='cool', kind=None),
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
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='t1_id', ctx=Store()),
                                        Name(id='t2_id', ctx=Store()),
                                        Name(id='t3_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='tags', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
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
                                                    Constant(value='tag_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 1', kind=None),
                                                    List(
                                                        elts=[
                                                            Name(id='t1_id', ctx=Load()),
                                                            Name(id='t2_id', ctx=Load()),
                                                            Name(id='t3_id', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='tag_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 2', kind=None),
                                                    List(
                                                        elts=[Name(id='t1_id', ctx=Load())],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='tag_ids', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 3', kind=None),
                                                    List(
                                                        elts=[
                                                            Name(id='t2_id', ctx=Load()),
                                                            Name(id='t3_id', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Rec 4', kind=None)],
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
                                Tuple(
                                    elts=[
                                        Name(id='r1_id', ctx=Store()),
                                        Name(id='r2_id', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='records', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='folder_id', kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value='Folder 2', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value='Folder 1', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Constant(value='Not Set', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='status', kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Constant(value='cool', kind=None),
                                                    Constant(value='Cool', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                    Constant(value='cool', kind=None),
                                                    Constant(value='Cool', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
                                                    Constant(value='cool', kind=None),
                                                    Constant(value='Cool', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='color', kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Constant(value='Red', kind=None),
                                                    Constant(value='Red', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Constant(value='Not Set', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
                                                    Constant(value='Green', kind=None),
                                                    Constant(value='Green', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='folder_id', kind=None),
                                    ),
                                    keyword(
                                        arg='group_domain',
                                        value=Dict(
                                            keys=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='json', ctx=Load()),
                                                        attr='dumps',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='f1_id', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='json', ctx=Load()),
                                                        attr='dumps',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='f2_id', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='json', ctx=Load()),
                                                        attr='dumps',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=False, kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            values=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='tag_ids', kind=None),
                                                                Constant(value='in', kind=None),
                                                                List(
                                                                    elts=[Name(id='t1_id', ctx=Load())],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='tag_ids', kind=None),
                                                                Constant(value='in', kind=None),
                                                                List(
                                                                    elts=[Name(id='t2_id', ctx=Load())],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='tag_ids', kind=None),
                                                                Constant(value='in', kind=None),
                                                                List(
                                                                    elts=[Name(id='t1_id', ctx=Load())],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='tag_ids', kind=None),
                                                                Constant(value='in', kind=None),
                                                                List(
                                                                    elts=[Name(id='t2_id', ctx=Load())],
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value='Folder 2', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value='Folder 1', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Constant(value='Not Set', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='color', kind=None),
                                    ),
                                    keyword(
                                        arg='group_domain',
                                        value=Dict(
                                            keys=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='json', ctx=Load()),
                                                        attr='dumps',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value=False, kind=None)],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='json', ctx=Load()),
                                                        attr='dumps',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='Green', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            values=[
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='tag_ids', kind=None),
                                                                Constant(value='in', kind=None),
                                                                List(
                                                                    elts=[Name(id='t1_id', ctx=Load())],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                                List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='tag_ids', kind=None),
                                                                Constant(value='in', kind=None),
                                                                List(
                                                                    elts=[Name(id='t1_id', ctx=Load())],
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Constant(value='Red', kind=None),
                                                    Constant(value='Red', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Constant(value='Not Set', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
                                                    Constant(value='Green', kind=None),
                                                    Constant(value='Green', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        List(
                                                            elts=[
                                                                Name(id='r1_id', ctx=Load()),
                                                                Name(id='r2_id', ctx=Load()),
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='folder_id', kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value='Folder 2', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value='Folder 1', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Constant(value='Not Set', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        List(
                                                            elts=[
                                                                Name(id='r1_id', ctx=Load()),
                                                                Name(id='r2_id', ctx=Load()),
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='folder_id', kind=None),
                                    ),
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Name(id='r2_id', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value='Folder 2', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Name(id='r2_id', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='category_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Name(id='r2_id', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Tag 2', kind=None),
                                                    Name(id='t2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Tag 3', kind=None),
                                                    Name(id='t3_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='folder_id', kind=None),
                                    ),
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Name(id='r2_id', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value='group_name', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value='Folder 2', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Name(id='r2_id', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Tag 1', kind=None),
                                                    Name(id='t1_id', ctx=Load()),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tag_ids', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=2, kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Name(id='SEARCH_PANEL_ERROR', ctx=Load()),
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
                    name='test_selection_empty',
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='state', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='A', kind=None),
                                                    Constant(value='a', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='B', kind=None),
                                                    Constant(value='b', kind=None),
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
                    name='test_selection',
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
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
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
                                                    Constant(value='state', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 1', kind=None),
                                                    Constant(value='a', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='state', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 2', kind=None),
                                                    Constant(value='a', kind=None),
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
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='r1_id', ctx=Store()),
                                        Name(id='_', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='records', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='state', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='group_by',
                                        value=Constant(value='not_possible_to_group', kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='__count', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='A', kind=None),
                                                    Constant(value='a', kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='__count', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='B', kind=None),
                                                    Constant(value='b', kind=None),
                                                    Constant(value=0, kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='state', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='__count', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='A', kind=None),
                                                    Constant(value='a', kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='__count', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='B', kind=None),
                                                    Constant(value='b', kind=None),
                                                    Constant(value=0, kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='state', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Name(id='r1_id', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='__count', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='A', kind=None),
                                                    Constant(value='a', kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='__count', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='B', kind=None),
                                                    Constant(value='b', kind=None),
                                                    Constant(value=0, kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='state', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='A', kind=None),
                                                    Constant(value='a', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='B', kind=None),
                                                    Constant(value='b', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='state', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='=', kind=None),
                                                        Name(id='r1_id', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='A', kind=None),
                                                    Constant(value='a', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='B', kind=None),
                                                    Constant(value='b', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='state', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='A', kind=None),
                                                    Constant(value='a', kind=None),
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_multi_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='state', kind=None)],
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
                                    Subscript(
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='A', kind=None),
                                                    Constant(value='a', kind=None),
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
                        value=Attribute(
                            value=Name(id='odoo', ctx=Load()),
                            attr='tests',
                            ctx=Load(),
                        ),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
