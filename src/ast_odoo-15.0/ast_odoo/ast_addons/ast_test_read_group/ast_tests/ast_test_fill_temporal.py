Module(
    body=[
        Expr(
            value=Constant(value='Test for fill temporal.', kind=None),
        ),
        ImportFrom(
            module='odoo.tests',
            names=[alias(name='common', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestFillTemporal',
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
                    value=Constant(value="Test for fill temporal.\n\n    This feature is mainly used in graph view. For more informations, read the\n    documentation of models's '_read_group_fill_temporal' method.\n    ", kind=None),
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
                                            Name(id='TestFillTemporal', ctx=Load()),
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
                                slice=Constant(value='test_read_group.fill_temporal', kind=None),
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
                    name='test_date_range_and_flag',
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
                            value=Constant(value="Simple date range test, the flag is also tested.\n\n        One of the most simple test. It must verify that dates 'holes' are filled\n        only when the fill_temporal flag is set.\n        ", kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-08-18', kind=None),
                                            Constant(value=2, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-10-19', kind=None),
                                            Constant(value=3, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-12-19', kind=None),
                                            Constant(value=5, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-08-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-08-01', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='August 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-10-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-09-01', kind=None),
                                                            Constant(value='1916-10-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='September 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-10-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-11-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-10-01', kind=None),
                                                            Constant(value='1916-11-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='October 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-11-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-12-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-11-01', kind=None),
                                                            Constant(value='1916-12-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='November 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-12-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1917-01-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-12-01', kind=None),
                                                            Constant(value='1917-01-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='December 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=5, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Model',
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
                                    ListComp(
                                        elt=Name(id='group', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='group', ctx=Store()),
                                                iter=Name(id='expected', ctx=Load()),
                                                ifs=[
                                                    Subscript(
                                                        value=Name(id='group', ctx=Load()),
                                                        slice=Constant(value='date_count', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fill_temporal',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_date_range_with_context_timezone',
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
                            value=Constant(value='Test if date are date_trunced correctly by pgres.\n\n        This test was added in attempt to fix a bug appearing with babel that\n        we use to translate the dates. Typically after a daylight saving, A\n        whole year was displayed in a graph like this (APR missing and OCT\n        appearing twice) :\n\n            JAN   FEB   MAR   MAY   JUN   JUL   AUG   SEP   OCT   OCT   NOV\n                           ^^^                                    ^^^\n        ', kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1915-01-01', kind=None),
                                            Constant(value=3, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-01-01', kind=None),
                                            Constant(value=5, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-01-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1915-02-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-01-01', kind=None),
                                                            Constant(value='1915-02-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='January 1915', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-02-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1915-03-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-02-01', kind=None),
                                                            Constant(value='1915-03-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='February 1915', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-03-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1915-04-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-03-01', kind=None),
                                                            Constant(value='1915-04-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='March 1915', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-04-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1915-05-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-04-01', kind=None),
                                                            Constant(value='1915-05-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='April 1915', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-05-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1915-06-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-05-01', kind=None),
                                                            Constant(value='1915-06-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='May 1915', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-06-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1915-07-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-06-01', kind=None),
                                                            Constant(value='1915-07-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='June 1915', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-07-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1915-08-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-07-01', kind=None),
                                                            Constant(value='1915-08-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='July 1915', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-08-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1915-09-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-08-01', kind=None),
                                                            Constant(value='1915-09-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='August 1915', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-09-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1915-10-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-09-01', kind=None),
                                                            Constant(value='1915-10-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='September 1915', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-10-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1915-11-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-10-01', kind=None),
                                                            Constant(value='1915-11-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='October 1915', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-11-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1915-12-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-11-01', kind=None),
                                                            Constant(value='1915-12-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='November 1915', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-12-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-12-01', kind=None),
                                                            Constant(value='1916-01-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='December 1915', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-02-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01', kind=None),
                                                            Constant(value='1916-02-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='January 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=5, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tzs', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='America/Anchorage', kind=None),
                                    Constant(value='Europe/Brussels', kind=None),
                                    Constant(value='Pacific/Kwajalein', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='tz', ctx=Store()),
                            iter=Name(id='tzs', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='model_fill', ctx=Store())],
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
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='tz',
                                                value=Name(id='tz', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='fill_temporal',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='groups', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='model_fill', ctx=Load()),
                                            attr='read_group',
                                            ctx=Load(),
                                        ),
                                        args=[List(elts=[], ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='fields',
                                                value=List(
                                                    elts=[
                                                        Constant(value='date', kind=None),
                                                        Constant(value='value', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='groupby',
                                                value=List(
                                                    elts=[Constant(value='date', kind=None)],
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
                                            Name(id='groups', ctx=Load()),
                                            Name(id='expected', ctx=Load()),
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
                FunctionDef(
                    name='test_only_with_only_null_date',
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
                            value=Constant(value='We should have the same result when fill_temporal is set or not.', kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=13, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=11, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=17, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                            Constant(value='date', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[Constant(value=False, kind=None)],
                                            ),
                                            Constant(value=3, kind=None),
                                            Constant(value=41, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Model',
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
                                    Name(id='expected', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fill_temporal',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_date_range_and_null_date',
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
                            value=Constant(value='Test data with null and non-null dates.', kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-08-19', kind=None),
                                            Constant(value=4, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=13, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-10-18', kind=None),
                                            Constant(value=5, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-08-18', kind=None),
                                            Constant(value=3, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-10-19', kind=None),
                                            Constant(value=4, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=11, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-08-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-08-01', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='August 1916', kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=7, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-10-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-09-01', kind=None),
                                                            Constant(value='1916-10-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='September 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-10-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-11-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-10-01', kind=None),
                                                            Constant(value='1916-11-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='October 1916', kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=9, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[Constant(value=False, kind=None)],
                                            ),
                                            Constant(value=False, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=24, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Model',
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
                                    ListComp(
                                        elt=Name(id='group', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='group', ctx=Store()),
                                                iter=Name(id='expected', ctx=Load()),
                                                ifs=[
                                                    Subscript(
                                                        value=Name(id='group', ctx=Load()),
                                                        slice=Constant(value='date_count', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fill_temporal',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_order_date_desc',
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
                            value=Constant(value='Test if changing Model._order has influence on the result.', kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-08-18', kind=None),
                                            Constant(value=3, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-08-19', kind=None),
                                            Constant(value=4, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-10-18', kind=None),
                                            Constant(value=5, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-10-19', kind=None),
                                            Constant(value=4, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='patch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='type', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='Model',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='_order', kind=None),
                                    Constant(value='date desc', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-08-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-08-01', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='August 1916', kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=7, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-10-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-09-01', kind=None),
                                                            Constant(value='1916-10-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='September 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-10-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-11-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-10-01', kind=None),
                                                            Constant(value='1916-11-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='October 1916', kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=9, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Model',
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
                                    ListComp(
                                        elt=Name(id='group', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='group', ctx=Store()),
                                                iter=Name(id='expected', ctx=Load()),
                                                ifs=[
                                                    Subscript(
                                                        value=Name(id='group', ctx=Load()),
                                                        slice=Constant(value='date_count', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fill_temporal',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_timestamp_without_timezone',
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
                            value=Constant(value='Test datetimes.\n\n        Date stored with an hour inside the Odoo model are processed as timestamp\n        without timezone by postgres.\n        ', kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-08-19 01:30:00', kind=None),
                                            Constant(value=7, kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=13, kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-10-18 02:30:00', kind=None),
                                            Constant(value=5, kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-08-18 01:50:00', kind=None),
                                            Constant(value=3, kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=11, kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-10-19 23:59:59', kind=None),
                                            Constant(value=2, kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-10-19', kind=None),
                                            Constant(value=19, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-08-01 00:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-09-01 00:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-08-01 00:00:00', kind=None),
                                                            Constant(value='1916-09-01 00:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='August 1916', kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-09-01 00:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-10-01 00:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-09-01 00:00:00', kind=None),
                                                            Constant(value='1916-10-01 00:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='September 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-10-01 00:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-11-01 00:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-10-01 00:00:00', kind=None),
                                                            Constant(value='1916-11-01 00:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='October 1916', kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=26, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[Constant(value=False, kind=None)],
                                            ),
                                            Constant(value=False, kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=24, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='Model',
                                        ctx=Load(),
                                    ),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='datetime', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='datetime', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
                                    ListComp(
                                        elt=Name(id='group', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='group', ctx=Store()),
                                                iter=Name(id='expected', ctx=Load()),
                                                ifs=[
                                                    Subscript(
                                                        value=Name(id='group', ctx=Load()),
                                                        slice=Constant(value='datetime_count', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fill_temporal',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='datetime', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='datetime', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_with_datetimes_and_groupby_per_hour',
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
                            value=Constant(value='Test with datetimes and groupby per hour.\n\n        Test if datetimes are filled correctly when grouping by hours instead of\n        months.\n        ', kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-01-01 01:30:00', kind=None),
                                            Constant(value=2, kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-01-01 01:50:00', kind=None),
                                            Constant(value=8, kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-01-01 02:30:00', kind=None),
                                            Constant(value=3, kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-01-01 13:50:00', kind=None),
                                            Constant(value=5, kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-01-01 23:50:00', kind=None),
                                            Constant(value=7, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 01:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 02:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 01:00:00', kind=None),
                                                            Constant(value='1916-01-01 02:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='01:00 01 Jan', kind=None),
                                            Constant(value=2, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 02:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 03:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 02:00:00', kind=None),
                                                            Constant(value='1916-01-01 03:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='02:00 01 Jan', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 03:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 04:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 03:00:00', kind=None),
                                                            Constant(value='1916-01-01 04:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='03:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 04:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 05:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 04:00:00', kind=None),
                                                            Constant(value='1916-01-01 05:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='04:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 05:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 06:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 05:00:00', kind=None),
                                                            Constant(value='1916-01-01 06:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='05:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 06:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 07:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 06:00:00', kind=None),
                                                            Constant(value='1916-01-01 07:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='06:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 07:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 08:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 07:00:00', kind=None),
                                                            Constant(value='1916-01-01 08:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='07:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 08:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 09:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 08:00:00', kind=None),
                                                            Constant(value='1916-01-01 09:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='08:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 09:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 10:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 09:00:00', kind=None),
                                                            Constant(value='1916-01-01 10:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='09:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 10:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 11:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 10:00:00', kind=None),
                                                            Constant(value='1916-01-01 11:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='10:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 11:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 12:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 11:00:00', kind=None),
                                                            Constant(value='1916-01-01 12:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='11:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 12:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 13:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 12:00:00', kind=None),
                                                            Constant(value='1916-01-01 13:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='12:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 13:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 14:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 13:00:00', kind=None),
                                                            Constant(value='1916-01-01 14:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='01:00 01 Jan', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=5, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 14:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 15:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 14:00:00', kind=None),
                                                            Constant(value='1916-01-01 15:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='02:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 15:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 16:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 15:00:00', kind=None),
                                                            Constant(value='1916-01-01 16:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='03:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 16:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 17:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 16:00:00', kind=None),
                                                            Constant(value='1916-01-01 17:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='04:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 17:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 18:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 17:00:00', kind=None),
                                                            Constant(value='1916-01-01 18:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='05:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 18:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 19:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 18:00:00', kind=None),
                                                            Constant(value='1916-01-01 19:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='06:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 19:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 20:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 19:00:00', kind=None),
                                                            Constant(value='1916-01-01 20:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='07:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 20:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 21:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 20:00:00', kind=None),
                                                            Constant(value='1916-01-01 21:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='08:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 21:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 22:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 21:00:00', kind=None),
                                                            Constant(value='1916-01-01 22:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='09:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 22:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 23:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 22:00:00', kind=None),
                                                            Constant(value='1916-01-01 23:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='10:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 23:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-02 00:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 23:00:00', kind=None),
                                                            Constant(value='1916-01-02 00:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='11:00 01 Jan', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=7, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fill_temporal',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='datetime', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='datetime:hour', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_hour_with_timezones',
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
                            value=Constant(value='Test hour with timezones.\n\n        What we do here is similar to test_with_datetimes_and_groupby_per_hour\n        but with a timezone in the user context.\n        ', kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1915-12-31 22:30:00', kind=None),
                                            Constant(value=2, kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-01-01 03:30:00', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-12-31 22:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1915-12-31 23:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-12-31 22:00:00', kind=None),
                                                            Constant(value='1915-12-31 23:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='04:00 01 Jan', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1915-12-31 23:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 00:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1915-12-31 23:00:00', kind=None),
                                                            Constant(value='1916-01-01 00:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='05:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 00:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 01:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 00:00:00', kind=None),
                                                            Constant(value='1916-01-01 01:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='06:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 01:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 02:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 01:00:00', kind=None),
                                                            Constant(value='1916-01-01 02:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='07:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 02:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 03:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 02:00:00', kind=None),
                                                            Constant(value='1916-01-01 03:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='08:00 01 Jan', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:hour', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-01-01 03:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-01-01 04:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-01-01 03:00:00', kind=None),
                                                            Constant(value='1916-01-01 04:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='09:00 01 Jan', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tz',
                                        value=Constant(value='Asia/Hovd', kind=None),
                                    ),
                                    keyword(
                                        arg='fill_temporal',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='datetime', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='datetime:hour', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_quarter_with_timezones',
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
                            value=Constant(value='Test quarter with timezones.\n\n        We group year by quarter and check that it is consistent with timezone.\n        ', kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2016-01-01 03:30:00', kind=None),
                                            Constant(value=2, kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2016-12-30 22:30:00', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:quarter', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='2015-12-31 17:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='2016-03-31 16:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2015-12-31 17:00:00', kind=None),
                                                            Constant(value='2016-03-31 16:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='Q1 2016', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:quarter', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='2016-03-31 16:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='2016-06-30 16:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2016-03-31 16:00:00', kind=None),
                                                            Constant(value='2016-06-30 16:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='Q2 2016', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:quarter', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='2016-06-30 16:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='2016-09-30 17:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2016-06-30 16:00:00', kind=None),
                                                            Constant(value='2016-09-30 17:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='Q3 2016', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime:quarter', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='2016-09-30 17:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='2016-12-31 17:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2016-09-30 17:00:00', kind=None),
                                                            Constant(value='2016-12-31 17:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='Q4 2016', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tz',
                                        value=Constant(value='Asia/Hovd', kind=None),
                                    ),
                                    keyword(
                                        arg='fill_temporal',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='datetime', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='datetime:quarter', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_edge_fx_tz',
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
                            value=Constant(value="We test if different edge effect by using a different timezone from the user context\n\n        Suppose a user resident near Hovd, a city in Mongolia. he sells a product\n        at exacltly 4:00 AM on 1st January 2018. Using its context, that datetime\n        is previously converted to UTC time by the ORM so as being stored properly\n        inside the datebase. We are in winter time so 'Asia/Hovd' is UTC+7 :\n\n                 '2018-01-01 04:00:00'   -->  '2017-12-31 21:00:00'\n\n        If that same user groups by datetime, we must ensure that the last\n        displayed date is in January and not in December.\n        ", kind=None),
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
                                            Constant(value='datetime', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2017-12-31 21:00:00', kind=None),
                                            Constant(value=42, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='datetime', kind=None),
                                            Constant(value='datetime_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='2017-12-31 17:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='datetime', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='2018-01-31 17:00:00', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='datetime', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='2017-12-31 17:00:00', kind=None),
                                                            Constant(value='2018-01-31 17:00:00', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='January 2018', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=42, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tz',
                                        value=Constant(value='Asia/Hovd', kind=None),
                                    ),
                                    keyword(
                                        arg='fill_temporal',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='datetime', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='datetime', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_with_bounds',
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
                            value=Constant(value='Test the alternative dictionary format for the fill_temporal context key (fill_from, fill_to).\n\n        We apply the fill_temporal logic only to a cibled portion of the result of a read_group.\n        [fill_from, fill_to] are the inclusive bounds of this portion.\n        Data outside those bounds will not be filtered out\n        Bounds will be converted to the start of the period which they belong to (depending\n        on the granularity of the groupby). This means that we can put any date of the period as the bound\n        and it will still work.\n        ', kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-02-15', kind=None),
                                            Constant(value=1, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-06-15', kind=None),
                                            Constant(value=2, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-11-15', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-02-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-02-01', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='February 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-05-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-06-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-05-01', kind=None),
                                                            Constant(value='1916-06-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='May 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-06-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-07-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-06-01', kind=None),
                                                            Constant(value='1916-07-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='June 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-07-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-08-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-07-01', kind=None),
                                                            Constant(value='1916-08-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='July 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-08-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-08-01', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='August 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-11-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-12-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-11-01', kind=None),
                                                            Constant(value='1916-12-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='November 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fill_temporal',
                                        value=Dict(
                                            keys=[
                                                Constant(value='fill_from', kind=None),
                                                Constant(value='fill_to', kind=None),
                                            ],
                                            values=[
                                                Constant(value='1916-05-15', kind=None),
                                                Constant(value='1916-08-15', kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_upper_bound',
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
                            value=Constant(value='Test the alternative dictionary format for the fill_temporal context key (fill_to).\n\n        Same as with both bounds, but this time the first bound is the earliest group with data\n        (since only fill_to is set)\n        ', kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-02-15', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-02-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-02-01', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='February 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-04-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-03-01', kind=None),
                                                            Constant(value='1916-04-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='March 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-04-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-05-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-04-01', kind=None),
                                                            Constant(value='1916-05-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='April 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fill_temporal',
                                        value=Dict(
                                            keys=[Constant(value='fill_to', kind=None)],
                                            values=[Constant(value='1916-04-15', kind=None)],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_lower_bound',
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
                            value=Constant(value='Test the alternative dictionary format for the fill_temporal context key (fill_from).\n\n        Same as with both bounds, but this time the second bound is the lastest group with data\n        (since only fill_from is set)\n        ', kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-04-15', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-02-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-02-01', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='February 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-04-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-03-01', kind=None),
                                                            Constant(value='1916-04-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='March 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-04-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-05-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-04-01', kind=None),
                                                            Constant(value='1916-05-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='April 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fill_temporal',
                                        value=Dict(
                                            keys=[Constant(value='fill_from', kind=None)],
                                            values=[Constant(value='1916-02-15', kind=None)],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_empty_context_key',
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
                            value=Constant(value='Test the alternative dictionary format for the fill_temporal context key.\n\n        When fill_temporal context key is set to an empty dictionary, it must be equivalent to being True\n        ', kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-02-15', kind=None),
                                            Constant(value=1, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-04-15', kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-02-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-02-01', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='February 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-04-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-03-01', kind=None),
                                                            Constant(value='1916-04-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='March 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-04-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-05-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-04-01', kind=None),
                                                            Constant(value='1916-05-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='April 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fill_temporal',
                                        value=Dict(keys=[], values=[]),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_min_groups',
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
                            value=Constant(value='Test the alternative dictionary format for the fill_temporal context key (min_groups).\n\n        We guarantee that at least a certain amount of contiguous groups is returned, from the\n        earliest group with data.\n        ', kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-02-15', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-02-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-02-01', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='February 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-04-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-03-01', kind=None),
                                                            Constant(value='1916-04-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='March 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fill_temporal',
                                        value=Dict(
                                            keys=[Constant(value='min_groups', kind=None)],
                                            values=[Constant(value=2, kind=None)],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
                    name='test_with_bounds_and_min_groups',
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
                            value=Constant(value='Test the alternative dictionary format for the fill_temporal context key (fill_from, fill_to, min_groups).\n\n        We guarantee that at least a certain amount of contiguous groups is returned, from the\n        fill_from bound. The fill_from bound has precedence over the first group with data regarding min_groups\n        (min_groups will first try to anchor itself on fill_from, or, if not specified, on the first group with data).\n        This amount is not restricted by the fill_to bound, so, if necessary, the fill_temporal\n        logic will be applied until min_groups is guaranteed, even for groups later than fill_to\n        Groups outside the specifed bounds are not counted as part of min_groups, unless added specifically\n        to guarantee min_groups.\n        ', kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-02-15', kind=None),
                                            Constant(value=1, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-06-15', kind=None),
                                            Constant(value=2, kind=None),
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
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1916-11-15', kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='expected', ctx=Store())],
                            value=List(
                                elts=[
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-02-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-02-01', kind=None),
                                                            Constant(value='1916-03-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='February 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-05-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-06-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-05-01', kind=None),
                                                            Constant(value='1916-06-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='May 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-06-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-07-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-06-01', kind=None),
                                                            Constant(value='1916-07-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='June 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=2, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-07-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-08-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-07-01', kind=None),
                                                            Constant(value='1916-08-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='July 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-08-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-08-01', kind=None),
                                                            Constant(value='1916-09-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='August 1916', kind=None),
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    Dict(
                                        keys=[
                                            Constant(value='__domain', kind=None),
                                            Constant(value='__range', kind=None),
                                            Constant(value='date', kind=None),
                                            Constant(value='date_count', kind=None),
                                            Constant(value='value', kind=None),
                                        ],
                                        values=[
                                            List(
                                                elts=[
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='>=', kind=None),
                                                            Constant(value='1916-11-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='<', kind=None),
                                                            Constant(value='1916-12-01', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[Constant(value='date', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='from', kind=None),
                                                            Constant(value='to', kind=None),
                                                        ],
                                                        values=[
                                                            Constant(value='1916-11-01', kind=None),
                                                            Constant(value='1916-12-01', kind=None),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            Constant(value='November 1916', kind=None),
                                            Constant(value=1, kind=None),
                                            Constant(value=3, kind=None),
                                        ],
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_fill', ctx=Store())],
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
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='fill_temporal',
                                        value=Dict(
                                            keys=[
                                                Constant(value='fill_from', kind=None),
                                                Constant(value='fill_to', kind=None),
                                                Constant(value='min_groups', kind=None),
                                            ],
                                            values=[
                                                Constant(value='1916-05-15', kind=None),
                                                Constant(value='1916-07-15', kind=None),
                                                Constant(value=4, kind=None),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='model_fill', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='fields',
                                        value=List(
                                            elts=[
                                                Constant(value='date', kind=None),
                                                Constant(value='value', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='groupby',
                                        value=List(
                                            elts=[Constant(value='date', kind=None)],
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
                                    Name(id='groups', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
