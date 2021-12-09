Module(
    body=[
        Import(
            names=[alias(name='odoo.tests', asname=None)],
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
            name='TestSelectRange',
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
                                slice=Constant(value='test_search_panel.category_target_model', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='TargetModelNoParentName',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='test_search_panel.category_target_model_no_parent_name', kind=None),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
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
                                    Name(id='result', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='parent_field', kind=None),
                                            Constant(value='values', kind=None),
                                        ],
                                        values=[
                                            Constant(value='parent_name_id', kind=None),
                                            List(elts=[], ctx=Load()),
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
                            targets=[Name(id='parent_folders', ctx=Store())],
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
                                value=Name(id='parent_folders', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='children_folders', ctx=Store())],
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
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
                                        Name(id='f3_id', ctx=Store()),
                                        Name(id='f4_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='children_folders', ctx=Load()),
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
                                                    Constant(value='folder_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='folder_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 2', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='folder_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 3', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
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
                                        Name(id='_', ctx=Store()),
                                        Name(id='r3_id', ctx=Store()),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Folder 2', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
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
                                                                Name(id='r3_id', ctx=Load()),
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Folder 2', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
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
                                        value=Constant(value=200, kind=None),
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
                                    Dict(
                                        keys=[
                                            Constant(value='parent_field', kind=None),
                                            Constant(value='values', kind=None),
                                        ],
                                        values=[
                                            Constant(value='parent_name_id', kind=None),
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='__count', kind=None),
                                                            Constant(value='display_name', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='parent_name_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=2, kind=None),
                                                            Constant(value='Folder 1', kind=None),
                                                            Name(id='f1_id', ctx=Load()),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='__count', kind=None),
                                                            Constant(value='display_name', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='parent_name_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=1, kind=None),
                                                            Constant(value='Folder 2', kind=None),
                                                            Name(id='f2_id', ctx=Load()),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='__count', kind=None),
                                                            Constant(value='display_name', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='parent_name_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=1, kind=None),
                                                            Constant(value='Folder 3', kind=None),
                                                            Name(id='f3_id', ctx=Load()),
                                                            Name(id='f1_id', ctx=Load()),
                                                        ],
                                                    ),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='__count', kind=None),
                                                            Constant(value='display_name', kind=None),
                                                            Constant(value='id', kind=None),
                                                            Constant(value='parent_name_id', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value=1, kind=None),
                                                            Constant(value='Folder 4', kind=None),
                                                            Name(id='f4_id', ctx=Load()),
                                                            Name(id='f2_id', ctx=Load()),
                                                        ],
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='SourceModel',
                                        ctx=Load(),
                                    ),
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
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
                                        arg='hierarchize',
                                        value=Constant(value=False, kind=None),
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
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
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
                                                    Constant(value='Folder 2', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
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
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
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
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                ],
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='parent_field', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 2', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
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
                                                                Name(id='r3_id', ctx=Load()),
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 2', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='expand',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='hierarchize',
                                        value=Constant(value=False, kind=None),
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
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 2', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Folder 2', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                ],
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='parent_field', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='parent_name_id', kind=None),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='hierarchize',
                                        value=Constant(value=False, kind=None),
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
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
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
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
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
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                ],
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='parent_field', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='hierarchize',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='category_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        List(
                                                            elts=[
                                                                Name(id='r1_id', ctx=Load()),
                                                                Name(id='r3_id', ctx=Load()),
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
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
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
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
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
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                ],
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='parent_field', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='enable_counters',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='hierarchize',
                                        value=Constant(value=False, kind=None),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='hierarchize',
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 2', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                ],
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='parent_field', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='parent_name_id', kind=None),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='search_domain',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value=0, kind=None),
                                                        Constant(value='=', kind=None),
                                                        Constant(value=1, kind=None),
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
                                    Name(id='result', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='parent_field', kind=None),
                                            Constant(value='values', kind=None),
                                        ],
                                        values=[
                                            Constant(value='parent_name_id', kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='hierarchize',
                                        value=Constant(value=False, kind=None),
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
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                ],
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='parent_field', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='hierarchize',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='category_domain',
                                        value=List(
                                            elts=[
                                                List(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='in', kind=None),
                                                        List(
                                                            elts=[
                                                                Name(id='r1_id', ctx=Load()),
                                                                Name(id='r3_id', ctx=Load()),
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
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                ],
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='parent_field', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='hierarchize',
                                        value=Constant(value=False, kind=None),
                                    ),
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
                                                                Name(id='f1_id', ctx=Load()),
                                                                Name(id='f4_id', ctx=Load()),
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
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                ],
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='parent_field', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                    name='test_many2one_deep_hierarchy',
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
                            targets=[Name(id='folders_level_0', ctx=Store())],
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
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Folder 1', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Folder 2', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Folder 3', kind=None)],
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
                                        Name(id='f3_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='folders_level_0', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='folders_level_1', ctx=Store())],
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 5', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 6', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
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
                                        Name(id='f4_id', ctx=Store()),
                                        Name(id='f5_id', ctx=Store()),
                                        Name(id='f6_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='folders_level_1', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='folders_level_2', ctx=Store())],
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 7', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 8', kind=None),
                                                    Name(id='f6_id', ctx=Load()),
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
                                        Name(id='f7_id', ctx=Store()),
                                        Name(id='f8_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='folders_level_2', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='folders_level_3', ctx=Store())],
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 9', kind=None),
                                                    Name(id='f8_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 10', kind=None),
                                                    Name(id='f8_id', ctx=Load()),
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
                                        Name(id='f9_id', ctx=Store()),
                                        Name(id='f10_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='folders_level_3', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
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
                                                    Constant(value='folder_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='folder_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 2', kind=None),
                                                    Name(id='f6_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='folder_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 3', kind=None),
                                                    Name(id='f7_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='folder_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 4', kind=None),
                                                    Name(id='f7_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='folder_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 5', kind=None),
                                                    Name(id='f9_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='folder_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 6', kind=None),
                                                    Name(id='f10_id', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Constant(value='\n        The folder tree is like this (the numbers are the local counts)\n\n                f1_id (1)       f2_id (0)           f3_id (0)\n                    |          /                         f4_id (0)  f5_id (0)  f6_id (1)\n                    |                     |\n                f7_id (2)             f8_id (0)\n                                     /                                         f9_id (1)  f10_id (1)\n        ', kind=None),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Folder 10', kind=None),
                                                    Name(id='f10_id', ctx=Load()),
                                                    Name(id='f8_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value='Folder 2', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Folder 3', kind=None),
                                                    Name(id='f3_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Folder 5', kind=None),
                                                    Name(id='f5_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value='Folder 6', kind=None),
                                                    Name(id='f6_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Folder 7', kind=None),
                                                    Name(id='f7_id', ctx=Load()),
                                                    Name(id='f4_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value='Folder 8', kind=None),
                                                    Name(id='f8_id', ctx=Load()),
                                                    Name(id='f6_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='__count', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value='Folder 9', kind=None),
                                                    Name(id='f9_id', ctx=Load()),
                                                    Name(id='f8_id', ctx=Load()),
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
                            targets=[Name(id='extra_folder_level_0', ctx=Store())],
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 11', kind=None),
                                                    Constant(value=False, kind=None),
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
                            targets=[Name(id='f11_id', ctx=Store())],
                            value=Attribute(
                                value=Name(id='extra_folder_level_0', ctx=Load()),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
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
                                                    Constant(value='folder_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 7', kind=None),
                                                    Name(id='f11_id', ctx=Load()),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='folder_id', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='comodel_domain',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='id', kind=None),
                                                        Constant(value='not in', kind=None),
                                                        List(
                                                            elts=[
                                                                Name(id='f8_id', ctx=Load()),
                                                                Name(id='f11_id', ctx=Load()),
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
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 1', kind=None),
                                                    Name(id='f1_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 2', kind=None),
                                                    Name(id='f2_id', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 4', kind=None),
                                                    Name(id='f4_id', ctx=Load()),
                                                    Name(id='f1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 6', kind=None),
                                                    Name(id='f6_id', ctx=Load()),
                                                    Name(id='f2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_name_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Folder 7', kind=None),
                                                    Name(id='f7_id', ctx=Load()),
                                                    Name(id='f4_id', ctx=Load()),
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
                    name='test_many2one_empty_no_parent_name',
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='categ_id', kind=None)],
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
                                    Name(id='result', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='parent_field', kind=None),
                                            Constant(value='values', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            List(elts=[], ctx=Load()),
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
                    name='test_many2one_no_parent_name',
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
                            targets=[Name(id='categories', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='TargetModelNoParentName',
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
                                                values=[Constant(value='Cat 1', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Cat 2', kind=None)],
                                            ),
                                            Dict(
                                                keys=[Constant(value='name', kind=None)],
                                                values=[Constant(value='Cat 3', kind=None)],
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
                                        Name(id='c1_id', ctx=Store()),
                                        Name(id='c2_id', ctx=Store()),
                                        Name(id='c3_id', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='categories', ctx=Load()),
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
                                                    Constant(value='categ_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 1', kind=None),
                                                    Name(id='c1_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='categ_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 2', kind=None),
                                                    Name(id='c2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='categ_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Rec 3', kind=None),
                                                    Name(id='c2_id', ctx=Load()),
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
                                        Name(id='_', ctx=Store()),
                                        Name(id='r3_id', ctx=Store()),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='categ_id', kind=None)],
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
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Cat 3', kind=None),
                                                    Name(id='c3_id', ctx=Load()),
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
                                                    Constant(value='Cat 2', kind=None),
                                                    Name(id='c2_id', ctx=Load()),
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
                                                    Constant(value='Cat 1', kind=None),
                                                    Name(id='c1_id', ctx=Load()),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='categ_id', kind=None)],
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
                                                                Name(id='r3_id', ctx=Load()),
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
                                                    Constant(value=0, kind=None),
                                                    Constant(value='Cat 3', kind=None),
                                                    Name(id='c3_id', ctx=Load()),
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
                                                    Constant(value='Cat 2', kind=None),
                                                    Name(id='c2_id', ctx=Load()),
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
                                                    Constant(value='Cat 1', kind=None),
                                                    Name(id='c1_id', ctx=Load()),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='categ_id', kind=None)],
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
                                                    Constant(value='Cat 3', kind=None),
                                                    Name(id='c3_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Cat 2', kind=None),
                                                    Name(id='c2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Cat 1', kind=None),
                                                    Name(id='c1_id', ctx=Load()),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='categ_id', kind=None)],
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
                                                                Name(id='r3_id', ctx=Load()),
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
                                                    Constant(value='Cat 3', kind=None),
                                                    Name(id='c3_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Cat 2', kind=None),
                                                    Name(id='c2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Cat 1', kind=None),
                                                    Name(id='c1_id', ctx=Load()),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='categ_id', kind=None)],
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
                                                    Constant(value='Cat 2', kind=None),
                                                    Name(id='c2_id', ctx=Load()),
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
                                                    Constant(value='Cat 1', kind=None),
                                                    Name(id='c1_id', ctx=Load()),
                                                ],
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='parent_field', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                                    attr='search_panel_select_range',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='categ_id', kind=None)],
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
                                                    Constant(value='Cat 2', kind=None),
                                                    Name(id='c2_id', ctx=Load()),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='display_name', kind=None),
                                                    Constant(value='id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Cat 1', kind=None),
                                                    Name(id='c1_id', ctx=Load()),
                                                ],
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
                                        value=Name(id='result', ctx=Load()),
                                        slice=Constant(value='parent_field', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
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
                                    attr='search_panel_select_range',
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
                                    Name(id='result', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='parent_field', kind=None),
                                            Constant(value='values', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
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
                                    attr='search_panel_select_range',
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
                                    attr='search_panel_select_range',
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
                                    attr='search_panel_select_range',
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
                                    attr='search_panel_select_range',
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
                                    attr='search_panel_select_range',
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
                                    attr='search_panel_select_range',
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
