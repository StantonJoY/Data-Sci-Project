Module(
    body=[
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestReadProgressBar',
            bases=[
                Attribute(
                    value=Name(id='common', ctx=Load()),
                    attr='TransactionCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Test for read_progress_bar', kind=None),
                ),
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
                                        args=[
                                            Name(id='TestReadProgressBar', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
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
                                    attr='Model',
                                    ctx=Store(),
                                ),
                            ],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
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
                    name='test_read_progress_bar_m2m',
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
                            value=Constant(value=' Test that read_progress_bar works with m2m field grouping ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='progressbar', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='field', kind=None),
                                    Constant(value='colors', kind=None),
                                ],
                                values=[
                                    Constant(value='type', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='contact', kind=None),
                                            Constant(value='private', kind=None),
                                            Constant(value='other', kind=None),
                                        ],
                                        values=[
                                            Constant(value='success', kind=None),
                                            Constant(value='danger', kind=None),
                                            Constant(value='muted', kind=None),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
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
                                    attr='read_progress_bar',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(elts=[], ctx=Load()),
                                    Constant(value='category_id', kind=None),
                                    Name(id='progressbar', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[Name(id='result', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='False', kind=None),
                                    Name(id='result', ctx=Load()),
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
                    name='test_week_grouping',
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
                            value=Constant(value='The labels associated to each record in read_progress_bar should match\n        the ones from read_group, even in edge cases like en_US locale on sundays\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='lang', kind=None)],
                                values=[Constant(value='en_US', kind=None)],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groupby', ctx=Store())],
                            value=Constant(value='date:week', kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Model',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='date', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2021-05-02', kind=None),
                                            Constant(value='testWeekGrouping_first', kind=None),
                                        ],
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
                                        attr='Model',
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='date', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2021-05-09', kind=None),
                                            Constant(value='testWeekGrouping_second', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='progress_bar', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='field', kind=None),
                                    Constant(value='colors', kind=None),
                                ],
                                values=[
                                    Constant(value='name', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='testWeekGrouping_first', kind=None),
                                            Constant(value='testWeekGrouping_second', kind=None),
                                        ],
                                        values=[
                                            Constant(value='success', kind=None),
                                            Constant(value='danger', kind=None),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='Model',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='testWeekGrouping%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='name', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Name(id='groupby', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='progressbars', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='Model',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='context', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='read_progress_bar',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='like', kind=None),
                                                    Constant(value='testWeekGrouping%', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='group_by',
                                        value=Name(id='groupby', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='progress_bar',
                                        value=Name(id='progress_bar', ctx=Load()),
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='groups', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
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
                                        args=[Name(id='progressbars', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='pg_groups', ctx=Store())],
                            value=DictComp(
                                key=Call(
                                    func=Name(id='next', ctx=Load()),
                                    args=[
                                        GeneratorExp(
                                            elt=Name(id='record_name', ctx=Load()),
                                            generators=[
                                                comprehension(
                                                    target=Tuple(
                                                        elts=[
                                                            Name(id='record_name', ctx=Store()),
                                                            Name(id='count', ctx=Store()),
                                                        ],
                                                        ctx=Store(),
                                                    ),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='data', ctx=Load()),
                                                            attr='items',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    ifs=[Name(id='count', ctx=Load())],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                value=Name(id='group_name', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='group_name', ctx=Store()),
                                                Name(id='data', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='progressbars', ctx=Load()),
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
                                            value=Name(id='groups', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='groupby', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='pg_groups', ctx=Load()),
                                        slice=Constant(value='testWeekGrouping_first', kind=None),
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
                                            value=Name(id='groups', ctx=Load()),
                                            slice=Constant(value=1, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='groupby', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Name(id='pg_groups', ctx=Load()),
                                        slice=Constant(value='testWeekGrouping_second', kind=None),
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
                    name='test_simple',
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
                            targets=[Name(id='model', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='model', kind=None),
                                            Constant(value='name', kind=None),
                                            Constant(value='field_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='x_progressbar', kind=None),
                                            Constant(value='progress_bar', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='field_description', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='ttype', kind=None),
                                                                    Constant(value='relation', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Country', kind=None),
                                                                    Constant(value='x_country_id', kind=None),
                                                                    Constant(value='many2one', kind=None),
                                                                    Constant(value='res.country', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='field_description', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='ttype', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Date', kind=None),
                                                                    Constant(value='x_date', kind=None),
                                                                    Constant(value='date', kind=None),
                                                                ],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='field_description', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='ttype', kind=None),
                                                                    Constant(value='selection', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='State', kind=None),
                                                                    Constant(value='x_state', kind=None),
                                                                    Constant(value='selection', kind=None),
                                                                    Constant(value="[('foo', 'Foo'), ('bar', 'Bar'), ('baz', 'Baz')]", kind=None),
                                                                ],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='c1', ctx=Store()),
                                        Name(id='c2', ctx=Store()),
                                        Name(id='c3', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='res.country', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=3, kind=None),
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='x_progressbar', kind=None),
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
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-05-20', kind=None),
                                                    Constant(value='foo', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-05-21', kind=None),
                                                    Constant(value='foo', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-05-22', kind=None),
                                                    Constant(value='foo', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-05-23', kind=None),
                                                    Constant(value='bar', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c1', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-05-24', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c2', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-05-25', kind=None),
                                                    Constant(value='foo', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c2', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-05-26', kind=None),
                                                    Constant(value='bar', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c2', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-05-27', kind=None),
                                                    Constant(value='bar', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c2', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-05-28', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c2', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-05-29', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c3', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-05-30', kind=None),
                                                    Constant(value='foo', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c3', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-05-31', kind=None),
                                                    Constant(value='foo', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c3', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-06-01', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c3', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-06-02', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='x_country_id', kind=None),
                                                    Constant(value='x_date', kind=None),
                                                    Constant(value='x_state', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='c3', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='2021-06-03', kind=None),
                                                    Constant(value='baz', kind=None),
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
                            targets=[Name(id='progress_bar', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='field', kind=None),
                                    Constant(value='colors', kind=None),
                                ],
                                values=[
                                    Constant(value='x_state', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='foo', kind=None),
                                            Constant(value='bar', kind=None),
                                            Constant(value='baz', kind=None),
                                        ],
                                        values=[
                                            Constant(value='success', kind=None),
                                            Constant(value='warning', kind=None),
                                            Constant(value='danger', kind=None),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='x_progressbar', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_progress_bar',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(elts=[], ctx=Load()),
                                    Constant(value='x_country_id', kind=None),
                                    Name(id='progress_bar', ctx=Load()),
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
                                    Name(id='result', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='c1', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='c2', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='c3', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='x_progressbar', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_progress_bar',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(elts=[], ctx=Load()),
                                    Constant(value='x_date:week', kind=None),
                                    Name(id='progress_bar', ctx=Load()),
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
                                    Name(id='result', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='W21 2021', kind=None),
                                            Constant(value='W22 2021', kind=None),
                                            Constant(value='W23 2021', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=3, kind=None),
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
                                    value=Name(id='model', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='field_id', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='field_description', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='ttype', kind=None),
                                                                    Constant(value='selection', kind=None),
                                                                    Constant(value='compute', kind=None),
                                                                    Constant(value='depends', kind=None),
                                                                    Constant(value='readonly', kind=None),
                                                                    Constant(value='store', kind=None),
                                                                ],
                                                                values=[
                                                                    Constant(value='Related State', kind=None),
                                                                    Constant(value='x_state_computed', kind=None),
                                                                    Constant(value='selection', kind=None),
                                                                    Constant(value="[('foo', 'Foo'), ('bar', 'Bar'), ('baz', 'Baz')]", kind=None),
                                                                    Constant(value="for rec in self: rec['x_state_computed'] = rec.x_state", kind=None),
                                                                    Constant(value='x_state', kind=None),
                                                                    Constant(value=True, kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
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
                            targets=[Name(id='progress_bar', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='field', kind=None),
                                    Constant(value='colors', kind=None),
                                ],
                                values=[
                                    Constant(value='x_state_computed', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='foo', kind=None),
                                            Constant(value='bar', kind=None),
                                            Constant(value='baz', kind=None),
                                        ],
                                        values=[
                                            Constant(value='success', kind=None),
                                            Constant(value='warning', kind=None),
                                            Constant(value='danger', kind=None),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='x_progressbar', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_progress_bar',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(elts=[], ctx=Load()),
                                    Constant(value='x_country_id', kind=None),
                                    Name(id='progress_bar', ctx=Load()),
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
                                    Name(id='result', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Attribute(
                                                value=Name(id='c1', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='c2', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='c3', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=1, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=2, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='x_progressbar', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='read_progress_bar',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(elts=[], ctx=Load()),
                                    Constant(value='x_date:week', kind=None),
                                    Name(id='progress_bar', ctx=Load()),
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
                                    Name(id='result', ctx=Load()),
                                    Dict(
                                        keys=[
                                            Constant(value='W21 2021', kind=None),
                                            Constant(value='W22 2021', kind=None),
                                            Constant(value='W23 2021', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=3, kind=None),
                                                    Constant(value=1, kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=2, kind=None),
                                                    Constant(value=2, kind=None),
                                                    Constant(value=3, kind=None),
                                                ],
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='foo', kind=None),
                                                    Constant(value='bar', kind=None),
                                                    Constant(value='baz', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=1, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Constant(value=3, kind=None),
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
            ],
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Name(id='common', ctx=Load()),
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
